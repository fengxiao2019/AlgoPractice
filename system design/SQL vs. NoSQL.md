SQL vs. NoSQL

In the world of databases, there are two main types of solutions: SQL and NoSQL - or relational databases and non-relational databases. Both of them differ in the way they were built, the kind of information they store, and how they store it.

Relational databases are structured and have predefined schemas, like phone books that store phone numbers and addresses. Non-relational databases are unstructured, distributed and have a dynamic schema, like file folders that hold everything from a person’s address and phone number to their Facebook ‘likes’ and online shopping preferences.

## **SQL**
Relational databases store data in rows and columns. Each row contains all the information about one entity, and columns are all the separate data points. Some of the most popular relational databases are MySQL, Oracle, MS SQL Server, SQLite, Postgres, MariaDB, etc.

## **NoSQL**
Following are most common types of NoSQL:
**Key-Value Stores**: Data is stored in an array of key-value pairs. The ‘key’ is an attribute name, which is linked to a ‘value’. Well-known key value stores include Redis, Voldemort and Dynamo.
**Document Databases**: In these databases data is stored in documents, instead of rows and columns in a table, and these documents are grouped together in collections. Each document can have an entirely different structure. Document databases include the CouchDB and MongoDB.
**Wide-Column Databases**: Instead of ‘tables,’ in columnar databases we have column families, which are containers for rows. Unlike relational databases, we don’t need to know all the columns up front, and each row doesn’t have to have the same number of columns. Columnar databases are best suited for analyzing large datasets - big names include Cassandra and HBase.
**Graph Databases**: These databases are used to store data whose relations are best represented in a graph. Data is saved in graph structures with nodes (entities), properties (information about the entities) and lines (connections between the entities). Examples of graph database include Neo4J and InfiniteGraph.

## High level differences between SQL and NoSQL
**Storage**: SQL stores data in **tables**, where each row represents an entity, and each column represents a data point about that entity; for example, if we are storing a car entity in a table, different columns could be ‘Color’, ‘Make’, ‘Model’, and so on.
NoSQL databases have different data storage models. The main ones are key-value, document, graph and columnar. We will discuss differences between these databases below.
**Schema**: In SQL, each record conforms to a fixed schema, meaning the columns must be decided and chosen before data entry and each row must have data for each column. The schema can be altered later, but it involves modifying the whole database and going offline.
Whereas in NoSQL, schemas are dynamic. Columns can be added on the fly, and each ‘row’ (or equivalent) doesn’t have to contain data for each ‘column.’
**Querying**: SQL databases uses SQL (structured query language) for defining and manipulating the data, which is very powerful. In NoSQL database, queries are focused on a collection of documents. Sometimes it is also called UnQL (Unstructured Query Language). Different databases have different syntax for using UnQL.
**Scalability**: In most common situations, SQL databases are vertically scalable, i.e., by increasing the horsepower (higher Memory, CPU, etc.) of the hardware, which can get very expensive. It is possible to scale a relational database across multiple servers, but this is a challenging and time-consuming process.
On the other hand, **NoSQL databases are horizontally scalable,** meaning we can add more servers easily in our NoSQL database infrastructure to handle large traffic. Any cheap commodity hardware or cloud instances can host NoSQL databases, thus making it a lot more cost-effective than vertical scaling. A lot of NoSQL technologies also distribute data across servers automatically.
Reliability or ACID Compliancy (Atomicity, Consistency, Isolation, Durability): The vast majority of relational databases are ACID compliant. So, when it comes to data reliability and safe guarantee of performing transactions, SQL databases are still the better bet.

Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

## SQL VS. NoSQL - Which one to use?
When it comes to database technology, there’s no one-size-fits-all solution. That’s why many businesses rely on both relational and non-relational databases for different needs. Even as NoSQL databases are gaining popularity for their speed and scalability, there are still situations where a highly structured SQL database may perform better; choosing the right technology hinges on the use case.

### Reasons to use SQL database
Here are a few reasons to choose a SQL database:
1. We need to ensure **ACID compliance**. ACID compliance reduces anomalies and protects the integrity of your database by prescribing exactly how transactions interact with the database.
2. Generally, NoSQL databases sacrifice ACID compliance for scalability and processing speed, but for many e-commerce and financial applications, an ACID-compliant database remains the preferred option.
3. Your data is **structured and unchanging**. If your business is not experiencing massive growth that would require more servers and if you’re only working with data that’s consistent, then there may be no reason to use a system designed to support a variety of data types and high traffic volume.

### 选择NoSQL数据库的理由
几个流行的NoSQL数据库的例子是MongoDB、CouchDB、Cassandra和HBase。
1. 海量数据存储，数据没有固定的Schema。
> NoSQL数据库对我们可以一起存储的数据类型没有设置任何限制，并允许我们根据需求的变化增加不同的新类型。通过基于文档的数据库，你可以将数据存储在一个地方，而不必事先定义那些数据的 "类型"。
2. 充分发挥云计算和存储的作用。基于云的存储是一个很好的节约成本的解决方案，但需要将数据轻松地分散到多个服务器上，以扩大规模。在现场或云中使用商品（负担得起的、较小的）硬件，可以节省额外软件的麻烦，而且像Cassandra这样的NoSQL数据库被设计成可以在多个数据中心之间进行扩展，开箱即用，不会有太多的麻烦。
3. 快速开发。NoSQL对于快速开发非常有用，因为它不需要提前准备。如果你正在进行系统的快速迭代，需要对数据结构进行频繁的更新，而在两个版本之间没有大量的停机时间，那么关系型数据库会拖累你。