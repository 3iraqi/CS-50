# \[SQLite ~~ database\]

- [\[SQLite ~~ database\]](#sqlite--database)
  - [SQL Keywords](#sql-keywords)

|Name|Description|
|-|-|
|SQL "Structured Query Language"|A language via which you can create, read,update, and delete data in a database.|
<!-- |Querying|-| -->

[Our Database](SQLite_CS50_\longlist.db) --- [\[The Booker Prizes\]](https://thebookerprizes.com/the-booker-library/features/booker-prize-winners)

## SQL Keywords

<details>
<Summary>SQL Keywords Table</Summary>

>> SQL keywords are case insensitive  but we should follow the conventions.

|KeyWord|Usage|
|-|-|
|**SELECT**|to select n rows|
|**Comments**|-|
|**--** one line comment|Double '-' for comments.|
|/\*multiline Comment\*/|for multiline comments.|
|*|All|
|"columns Name"|convention|
|'String names'|convention|
|LIMIT|to choose how many rows should be selected|

</details>

```SQL
-- SQLite CS50 Course
SELECT * FROM "books" ; 
-- Each line must end with semicolons
-- select all from books table
SELECT "title" FROM "books" ;
-- select title column from books table
SELECT "title" FROM "books" LIMIT 10;
-- select title column from books table limit first 10 rows

```


\[  \]