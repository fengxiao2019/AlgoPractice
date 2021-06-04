import redis
from datetime import datetime
import time, datetime

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
client = redis.Redis(connection_pool=pool)

"""
算法：固定窗口限流算法
优点：实现简单
缺点：窗口结束时的突发请求会导致服务器处理的请求超过限制，因为这种算法将允许在短时间内对当前和下一个窗口的请求进行处理。例如，对于100个req/min，如果用户在55到60秒窗口提出100个请求，然后在下一个窗口从0到5秒提出100个请求，这个算法会处理所有的请求。因此，最终在10秒内为这个用户处理了200个请求，这超过了100 req/min的限制。
"""
def get_cur_time_in_seconds() -> int:
    return time.mktime(datetime.datetime.today().timetuple())


def RateLimitUsingFixedWindow(user_id: str, intervals: int, maximum_request: int) -> bool:
    seconds = get_cur_time_in_seconds()
    # 计算当前窗口
    current_window = seconds // intervals
    key = f"{user_id}:{current_window}"
    # 获取当前value
    request_count = client.get(key)

    if request_count and int(request_count) > maximum_request:
        return False
    client.incr(key, 1)
    return True


"""
Sliding Logs
在这个算法中，我们将用户的每个请求记录在一个排序的列表中（以时间排序）。
对于用户提出的每个请求:
1. 通过获取排序集中最后一个窗口的所有日志计数，检查用户是否在当前窗口中超过了限制。如果当前时间是10:00:27，速率是100 req/min，获取从上一个窗口（10:00:27-60= 09:59:28）到当前时间（10:00:27）的日志。
2. 如果用户已经超过了限制，请求就会被放弃。
3. 否则，我们将唯一的请求ID（你可以从请求中得到，或者你可以用用户ID和时间生成一个唯一的哈希值）添加到排序的集合中（按时间排序）。
删除方式：ZRemRangeByScore 删除
优点： 克服了固定窗口的缺点，不强加固定的窗口限制，因此不受窗口结束时的突发请求的影响。
缺点: 1. 由于我们为每一个请求存储一个新的条目，所以它的内存效率不高。
     2. 因为我们在每个请求中计算用户的最后一个窗口请求，这在大量攻击发生时不能很好地扩展。
"""
def RateLimitUsingSlidingLogs(user_id: str, unique_req_id: str, interval_in_secs: int, max_reqs: int) -> bool:
    cur_time = get_cur_time_in_seconds()
    last_window_time = cur_time - interval_in_secs

    # 获取当前窗口内的请求数
    req_count = client.zcount(user_id, last_window_time, cur_time)
    if req_count > max_reqs:
        return False

    # 将当前请求添加到窗口中
    client.zadd(user_id, {unique_req_id: cur_time})
    return True

import uuid
def test():
    for i in range(13):
        res = RateLimitUsingSlidingLogs("shaoyongzhe", uuid.uuid4().hex, 60, 10)
        print(res)

"""
Leaky Bucket
在这个算法中，我们使用有限大小的队列，并以先入先出的方式从队列中以恒定的速度处理请求。
对于用户发起的每个请求, 
1. 检查是否超过了队列的限制。
2. 如果超过了队列的限制，请求就会被放弃。
3. 否则，我们将请求添加到队列末端并处理传入的请求。

优点
    1. 克服了固定窗口的缺点，因为它不强加一个固定的窗口限制，因此不受窗口结束时的突发请求的影响。
    2. 克服了滑动日志的缺点，不存储所有的请求（只存储受队列大小限制的请求），因此内存效率高。
缺点
    1. 突发的请求会使队列中充满旧的请求，而最近的请求会被延缓处理，因此不能保证请求在固定的时间内被处理。
    2. 无法应对突发流量。
"""
def RateLimitUsingLeakyBucket(user_id: str, unique_req_id: str, max_req_count: int) -> int:
    req_count = client.llen(user_id)
    if req_count and int(req_count) > max_req_count:
        return False

    client.rpush(user_id, unique_req_id)
    return True
"""
请求以恒定的速度从队列中以先进先出的方式进行处理（从队列的开始位置移除并处理），
由一个后台进程进行。
你可以在Redis中使用LPOP命令，以恒定的速度，
例如，对于60个req/min，你可以每秒移除1个元素，并处理被移除的请求）。
"""

"""
滑动窗口  Sliding Window
滑动窗口
在这个算法中，我们结合了固定窗口和滑动日志算法。我们为每个固定窗口维护一个计数器，并将前一个窗口的请求数与当前窗口的请求数加权后的计数器值计算在内。
对于用户发起的每个请求
1. 检查用户是否在当前窗口中没有超过限制。
2. 如果用户超过了，则放弃该请求。
3. 否则，我们计算前一个窗口的加权计数，例如，如果当前窗口的时间已经过了30%，那么我们将前一个窗口的计数加权为70%。
4. 检查前一个窗口的加权计数和当前窗口的计数是否已经超过了限制。
5. 如果用户已经超过了，则请求被放弃。
6. 否则，我们在当前窗口中把计数器增加1，并处理进入的请求。

每隔一段时间，例如每10分钟或每小时，删除所有过期的窗口钥匙。
优点
    1. 克服了固定窗口的缺点，因为它不强加一个固定的窗口限制，因此不受窗口结束时请求的爆发的影响。
    2. 克服了滑动日志的缺点，因为它不存储所有的请求，避免对每个请求进行计数，因此在内存和性能上都很高效。
    3. 通过不放慢请求，不进行流量整形，克服了漏桶饥饿问题的弊端。
缺点
    不是缺点，但你需要删除过期的窗口键，这是Redis上的一个额外命令/负载，你可以在下一个算法中克服。
"""

def RateLimitUsingSlidingWindow(user_id: str, unique_id: str, interval_seconds: int, max_reqs: int) -> bool:
    cur_time = get_cur_time_in_seconds()
    cur_window = cur_time // interval_seconds
    key = f"{user_id}:{cur_window}"
    # 获取当前窗口的值
    cur_count = client.get(key)
    cur_count = int(cur_count) if cur_count else 0
    # 如果当前请求已经大于最大限制，返回
    if cur_count > max_reqs:
        return False

    # 获取上一个窗口的值
    last_window = (cur_time - interval_seconds) // interval_seconds
    last_window_key = f"{user_id}:{last_window}"
    # 获取上一个窗口请求的大小
    last_count = client.get(last_window_key)
    last_count = int(last_count) if last_count else 0
    elapsed_time_percentage = (cur_time % interval_seconds) / interval_seconds
    # last window weighted count + current window count
    if last_count * (1 - elapsed_time_percentage) + cur_count > max_reqs:
        # drop request
        return False

    # 增加当前窗口的请求量
    client.incrby(key)
    return True

"""
令牌桶算法 Token Bucket
在这个算法中，我们维护一个计数器，它显示一个用户留下了多少个请求以及计数器被重置的时间。
对于用户发起的每个请求:
    1. 检查自上次重置计数器以来是否已经过了窗口时间。对于速率100 req/min，当前时间10:00:27，最后一次重置时间9:59:00未过，9:59:25（10:00:27-9:59:25 > 60秒）已过。
    2. 如果窗口时间未过，检查用户是否有足够的请求来处理进入的请求。
    3. 如果用户没有剩余的请求，则放弃该请求。
    4. 否则，我们将计数器递减1并处理传入的请求。
    5. 如果窗口时间已过，即上次计数器被重置和当前时间之间的差异大于允许的窗口时间（60s），我们将允许的请求数重置为允许的限制（100）。
在这种算法中，不需要后台代码来检查和删除过期的钥匙。
优点
    1. 克服了上述所有算法的缺点，没有固定的窗口限制，内存和性能高效，没有流量整形。
    2. 不需要后台代码来检查和删除过期的密钥。
"""
def RateLimitUsingTokenBucket(user_id: str, interval_seconds: int, max_reqs: int) -> bool:
    # 获取上次重置的时间
    last_reset_key = f"{user_id}_last_reset_time"
    last_reset_time = client.get(last_reset_key)
    # 如果是第一次获取，last_reset_time 设置成0
    last_reset_time = int(last_reset_time) if last_reset_time else 0
    # 检查自上次重置到现在是否过了时间窗口
    cur_time = get_cur_time_in_seconds()
    key = f'{user_id}_counter'
    if cur_time - last_reset_time >= interval_seconds:
        # 如果过了时间窗口，直接重置
        client.set(key, max_reqs)
    else:
        # 如果还没过期，获取当前窗口下还剩余多少个请求
        left_reqs = client.get(key)
        left_reqs = left_reqs if left_reqs else 0
        if left_reqs <= 0:
            # 已经没有剩余了，丢掉请求
            return False

    # 如果还有剩余，将请求数减1
    client.decr(key)
    return True


if __name__ == '__main__':
    test()