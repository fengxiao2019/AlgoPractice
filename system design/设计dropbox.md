# 功能需求
- 上传/下载/分享文件
- 修改自动同步，设备间数据同步
- 事务，离线编辑
# 非功能需求
可用性 / 可靠性 / 可持久性 
# 设计考量
读写比例基本一致 / 增量上传 / 如何避免无效流量 / 去重
# 容量评估
用户量 - 
DAU -\> QPS -\> 年存储量 -\> 5年存储量 
peek QPS
eg： DAU 100M
假设没人每天上传10个文件 QPS：380 /s      peek: qps * 5*
磁盘存储：PB级别数据

# [ API设计][1] （可以参考dropbox的api设计）
## 上传文件
/files/upload
```python
# /files/upload
{
    "path": "/Homework/math/Matrices.txt",
    "mode": "add",
    "autorename": true,
    "mute": false,
    "strict_conflict": false
}

```
返回值
```python
name / id client_modified / server_modified
rev String(min_length=9, pattern="[0-9a-f]+") A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.
size UInt64 The file size in bytes.
path_lower String? The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted. This field is optional.
content_hash
```
## 下载文件
```python
files/download
{
    "path": "/Homework/math/Prime_Numbers.txt"
}
{
    "path": "id:a4ayc_80_OEAAAAAAAAAYa"
}
{
    "path": "rev:a1c10ce0dd78"
}
```
## 搜索
```python
files/search_v2
参数
{
    "query": "cat",
    "options": {
        "path": "/Folder",
        "max_results": 20,
        "file_status": "active",
        "filename_only": false
    },
    "match_field_options": {
        "include_highlights": false
    }
}
```
可以通过分页显示，返回结果中会返回cursor标志，用于在下一次请求中使用。
# high level design
# component design
## client
### 如何高效的上传文件？
### client 如何感知其它设备的变化？
### 如何去重
SHA256 加密-去重
切割文件，4M，每4M计算一个hash值
然后合并hash值，再进行sha256进行计算，最后得出的hash值作为整个文件hash值

[https://www.dropbox.com/developers/reference/content-hash][2]



[1]:	https://www.dropbox.com/developers/documentation/http/documentation#files-upload
[2]:	https://www.dropbox.com/developers/reference/content-hash