# SQLite Week 0 Lec 1 Querying

- [SQLite Week 0 Lec 1 Querying](#sqlite-week-0-lec-1-querying)
  - [SQL Keywords](#sql-keywords)

|Name|Description|
|-|-|
|SQL "Structured Query Language"|A language via which you can create, read,update, and delete data in a database.|
<!-- |Querying|-| -->

[Our Database](SQLite_CS50_\longlist.db) --- [\[The Booker Prizes\]](https://thebookerprizes.com/the-booker-library/features/booker-prize-winners)

## SQL Keywords

<details open>
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
|NULL| it is not in our data base.|
|IS NULL|-|
|IS NOT NULL|-|
|LIKE|to check if there is any word like or contain some of these string  |
|LIKE operator| % , _ |
|%: combine some word|_: combine some char|
|word%,%word%,%word  |if word in first,middle or any where,end|
|t__|the replaced chars with _|
|< > <= >=|range operator|
|BETWEEN .. AND ..|range operator|
|ORDER BY .. ASC|order data ascending. |
|ORDER BY .. DESC|order data descending. |
|COUNT() <br> AVG()<br> MIN() <br> MAX()<br> SUM() |<h3>aggregate functions.</h3>|
|ROUND(object,decimal)| round the fraction to n places|
|AS|to show output in specific name|
|DISTINCT| to remove duplicated value in any column |

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
SELECT "title" FROM "books" WHERE "title" LIKE '%love%';
-- find sentence contain love
SELECT "title" , "pages" FROM "books" ORDER BY "pages" DESC LIMIT 10;
-- order by descending
SELECT ROUND(AVG("pages"),2) AS "Average Pages" FROM "books";
-- to change column name that contain the average of pages .
SELECT DISTINCT "publisher" FROM "books";
-- that will filter duplicates

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
