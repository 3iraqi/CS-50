# SQLite  database

- [SQLite  database](#sqlite--database)
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
|WHERE|select cell or row by condition|

</details>

<details>

<Summary>CODE Examples</Summary>

```SQL
-- SQLite CS50 Course
SELECT * FROM "books" ; 
-- Each line must end with semicolons
-- select all from books table
SELECT "title" FROM "books" ;
-- select title column from books table
SELECT "title" FROM "books" LIMIT 10;
-- select title column from books table limit first 10 rows
SELECT "id" FROM "books" WHERE "title"="Whale";
-- WHERE to select cell when another cell equal  something
SELECT "title" FROM "books" WHERE "id"<10;
-- select title rows from books when the id is lower than 10


```

</details>

<details>

<Summary>SQL Commands</Summary>

```sql

.mode box
-- to show displayed data in a table
┌────┬────────────────────────────────────────┬────┐
│ id │                 title                  │ id │
├────┼────────────────────────────────────────┼────┤
│ 1  │ Boulder                                │ 1  │
│ 2  │ Whale                                  │ 2  │
│ 3  │ The Gospel According to the New World  │ 3  │
│ 4  │ Standing Heavy                         │ 4  │
│ 5  │ Time Shelter                           │ 5  │
│ 6  │ Is Mother Dead                         │ 6  │
│ 7  │ Jimi Hendrix Live in Lviv              │ 7  │
│ 8  │ The Birthday Party                     │ 8  │
│ 9  │ While We Were Dreaming                 │ 9  │
│ 10 │ Pyre                                   │ 10 │
│ 11 │ Still Born                             │ 11 │
│ 12 │ A System So Magnificent It Is Blinding │ 12 │
│ 13 │ Ninth Building                         │ 13 │
└────┴────────────────────────────────────────┴────┘

```

</details>
