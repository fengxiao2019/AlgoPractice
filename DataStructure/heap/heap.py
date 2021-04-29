# heap

# topic1: heap attribute
# topic2: min_heap insert / remove
# topic3: max_heap insert / remove
# topic4: min_heap -> max_heap
# topic5: heap_sort, small-> large: min_heap
#       : heap_sort, large-> small: max_heap


from numpy import random
# complete binary tree 
# --> binary + all leaves, except possibly the last level are
# --> completed filled with node
# --> last level has all its nodes to the left side

# heap
# --> complete binary tree 
# --> + the value in every node x is the smallest value in the subtree rooted at node x
# insert: append the value to the array, then adjust the position of the value


class Heap(object):
    def __init__(self):
        self.values = [None]

    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        self.filterUp(index)

    def filterUp(self, index):
        pn = index // 2
        while pn > 0:
            if self.values[pn] > self.values[index]:
                self.values[pn], self.values[index] = self.values[index], self.values[pn]
                index = pn
                pn = index // 2
                print(index, pn)
            else:
                break

    def check_valid(self):
        index = len(self.values) - 1
        while index > 0 and index // 2 > 0:
            pn = self.values[index // 2]
            print(index, pn)
            if pn > self.values[index]:
                print(f"invalid heap: {self.values}")
                break
            index -= 1
        return True

    def min_index(self, index, length):
        left = 2 * index
        right = left + 1
        min_value = self.values[index]
        min_index = index
        if left < length and self.values[left] < min_value:
            min_value = self.values[left]
            min_index = left
        if right < length and self.values[right] < min_value:
            min_value = self.values[right]
            min_index = right
        return min_index

    def filterDown(self, index):
        length = len(self.values)
        while index < length:
            min_index = self.min_index(index, length)
            if min_index == index:
                break
            self.values[min_index], self.values[index] = self.values[index], self.values[min_index]
            index = min_index

    @property
    def length(self):
        return len(self.values)

    def remove(self, index):
        if index >= self.length or index <= 0:
            return
        # check the value of the node
        # if this is the root node or
        # the value of this node is the biggest value of its subnodes
        # filter down
        parent_node = index // 2
        self.values[index] = self.values[self.length - 1]
        self.values.pop(self.length - 1)
        if index == 1 or self.values[parent_node] < self.values[index]:
            self.filterDown(index)
        elif self.values[parent_node] > self.values[index]:
            self.filterUp(index)


hp = Heap()
for item in random.randint(1000, size=10):
    hp.insert(item)
print(hp.values)
sorted_values = []
for i in range(1, hp.length, 1):
    sorted_values.append(hp.values[1])
    hp.remove(1)
print(sorted_values)
print(hp.values)
print(hp.check_valid())
