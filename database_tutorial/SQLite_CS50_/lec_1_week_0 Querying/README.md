# SQLite Week 0 Lec 1 Querying

- [SQLite Week 0 Lec 1 Querying](#sqlite-week-0-lec-1-querying)
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
|<> , !=|not equal|
|NOT|negation the condition|
|AND|AND conditional operator|
|OR|OR conditional operator|
|(Condition)|to combine conditions as one condition|
|||

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

┌────┬───────────────────────────────────────┐
│ id │                 title                 │
├────┼───────────────────────────────────────┤
│ 1  │ Boulder                               │
│ 2  │ Whale                                 │
│ 3  │ The Gospel According to the New World │
│ 4  │ Standing Heavy                        │
└────┴───────────────────────────────────────┘

```

</details>
