Query Writing
--------------------

[![de](https://img.shields.io/badge/lang-de-blue.svg)](QUERIES.de.md)

This document describes techniques for creating, understanding, and revising SQL queries.

**Contents**

1\. [SQL Style](#1-SQL-Style) 
1.2\. [Spacing and indentation](#12-spacing-and-indentation) 
1.3\. [Keywords](#13-Keywords) 
1.4\. [Blank lines](#14-Blank-lines) 
1.5\. [Type conversion](#15-Type-conversion) 
1.6\. [Comments](#16-Comments) 
1.7\. [File name](#17-File name) 
2\. [Structuring a query](#2-Structuring-a-query) 
3\. [Specific strategies](#3-Specific-strategies) 
4\. [Accommodating Redshift](#4-Accommodating-Redshift) 


1\. SQL Style
--------------------


1.2\. Spacing and indentation
--------------------

4 spaces are used for indents.

```
SELECT 
    column
FROM
    table
```

* Each element is placed on a new line.

```
SELECT 
    sp.name AS service_point_name,
    m.name AS material_type,
    i.barcode AS item_barcode,
    ...
```

* If there are parallel expressions, equal spacing can be used to align similar elements.

```
    loan_date BETWEEN (SELECT start_date FROM parameters) AND
                      (SELECT end_date FROM parameters) 
```


1.3\. Keywords
--------------------

Keywords should be written in capital letters, e.g.:

* `SELECT`
* `'2019-01-01' :: DATE`
* Always use `AS` for aliasing (columns, subqueries, tables, etc.)


1.4\. Blank lines
--------------------

No blank lines are used.


1.5\. Type conversion
--------------------

If a type conversion is necessary, `‘ :: ’` followed by the data type in uppercase letters is always used, e.g., `VARCHAR` or `DATE`.


1.6\. Comments
--------------------

* `/* ... */` for multi-line comments
* `--` for single line comments


1.7\. File name
--------------------

Underscores are used for delimitation, not dashes.


2\. Structuring a query
--------------------

1. header 

Please add the following header to each query and adjust the following points.

* File name
* Author
* Description

If a query is modified and reused, `Modification` is added below `Author` with your own personal details.

```
/*
-------------------------------------------------------------------------------
File name

Author:         John Doe <jd@example.org>
Description:    Brief description of the purpose.
-------------------------------------------------------------------------------
Copyright 2026 The Open Library Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
*/
```

2. Performance warnings

Write a warning in `Description` if the query could return more than 1 million rows (Excel) or if processing requires a lot of resources.

3. Parameter

* Parameters are defined within a CTE (using `WITH` statements).
* Place parameters at the beginning of the file to make it easier for others to change them.
* Set default parameter values to ensure that the query returns results. If necessary, use default values or a logical OR (e.g., with 1=1).

4. Subqueries are created as additional `WITH` statements.

5. Primary query


3\. Specific strategies
--------------------

* Intercepting empty strings and null values
    * If **only one column** is selected that could have a NULL value, no special action is required. 
    * If the column is converted in any way, e.g., in a mathematical calculation or if part of the value is extracted, it must be tested for a NULL value or an empty string. One option is to use `COALESCE`, which can be used to specify a default value if the result is NULL.
* Picking which table to select from first.
    * When writing a query, it's important to think through which table you list first in the `SELECT` statement because of the joins that will build on it.
    * Start with the table that best represents what you want on each line of the results table. This improves performance.
* `LEFT JOIN` vs. `INNER JOIN`
    * In general, using `LEFT JOIN` makes sure you don't accidentally lose the items you're most interested.
        * For example, if you're interested in loans and also want to see the demographics of the users making the loan, you can use `LEFT JOIN` to keep all loans even if you don't know the user's demographics.
    * If you are filtering a table based on a field in a secondary table, you may instead want to use INNER JOIN to make sure to exclude records that don't have the required value.
* `BETWEEN`
    * Note that using `BETWEEN` for dates is risky because it only includes records up to midnight of the end date (essentially, the end of the day before, but it will include items exactly at midnight of the end date).
    * If you do use `BETWEEN`, try to educate people about its behavior in comments and set default values that make sense for the behavior (e.g., the first day of one year and the first day of the following year, instead of the last day of the year).
    * If you do not want to risk including values from midnight of the end date, you can use `>= start_date` and `< end_date` instead of `BETWEEN`. This is like using `BETWEEN` except that you use `<` instead of `<=`. You still have to use an end date that will not be included in the date range (i.e., the day after the last day you want included).
* DRY - Don't Repeat Yourself
    * As with any programming, the more repetition you have in your query, the more likely you are to forget to update something or make a mistake the second time around.
    * Try to find a way to reuse parts of your query creatively, either with parameters or `WITH` statements.


4\. Accommodating Redshift
--------------------

* General notes
    * FOLIO Reporting supports queries on both PostgreSQL and Redshift, so the queries must also run on both.
    * Redshift's dialect of SQL is largely based on an old version of PostgreSQL, but there are differences that mean that not everything that runs on PostgreSQL can run on Redshift (and vice versa).
* JSON functions
    * PostgreSQL has much better JSON support than Redshift. Redshift can pretty much only use `json_extract_path_text()` .
    * [Redshift JSON functions](https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html)
* Explicit casting
    * For anything in a query that doesn't come from a database table, you will need to explicitly state (or "cast") the value to a data type.