## Topics

**Database**
- Set of data
- Usually organized and managed by software
- Comma Separated Value (CSV) files (only numbers and letters)

**Intro to Structured Query Language (SQL)**
- Manages data stored in relational databases
- Simple, declarative statements
- Used for all kinds of database systems, helps you understand all database systems
- Made in the 70s by IBM
- Different dialects of SQL (MySQL, SQLite)

**[SQLite](https://www.sqlite.org/index.html)**

**Relational Databases**
- Organizes information into one or more tables
- Store and provide access to data points that are related to one another

  ***Parts of a Relational Database***

    - Table: collection of data organized into rows and columns (sometimes called “relations.”)
    - Column: set of data values of a particular type.
    - Row: a single record in a table.

**SQLite Data Types**
- Integer: + or - whole number
- Real: decimal
- Text: string
- Numeric: boolean, date (YYYY-MM-DD)
- BLOB: Binary Large OBject, can store any kind of data

**SQLite is cAsE-sEnSiTiVe**

**[Let's create a table for demo data here (you must be signed into your Berklee Google account to access)](https://docs.google.com/spreadsheets/d/1X-W0rR9GqpL1ljVHCzU1cX9qhdfiUnC2dHHLQYLQiw4/edit#gid=0)**

**Statements CODE ALONG**

          - sqlite3 nyctosptwentythree.db //creates database
          - CREATE TABLE 'nycto' ('id' integer, 'name' text, 'dark' text);
          - .tables //names table
          - .schema // shows structure of table named
          - INSERT INTO nycto (id, name, dark) VALUES(2, 'rachel', 'no');
          - SELECT name FROM nycto;
          - SELECT name, dark FROM nycto;
          - SELECT * FROM nycto;
          - SELECT * FROM nycto WHERE dark = 'yes';
          - SELECT DISTINCT dark FROM nycto;
          - ALTER TABLE nycto ADD COLUMN 'muchness' integer;
          - UPDATE nycto SET dark = 'yes' WHERE id = 2;
          - UPDATE nycto SET muchness = 9 WHERE id = 2;

**Operators**

          - SELECT * FROM nycto WHERE name LIKE 'ra_hel';
          - SELECT * FROM nycto WHERE name LIKE 'r%';
          - SELECT * FROM nycto WHERE name LIKE '%ch%';
          - SELECT * FROM nycto WHERE id BETWEEN 1 AND 3;
          - SELECT * FROM nycto WHERE id > 3 OR dark = 'yes';

**Order By**

          - SELECT * FROM nycto ORDER BY id;

**Limit**

          - SELECT * FROM nycto WHERE muchness > 7 ORDER BY id DESC;

**Case**

          - SELECT name,
              CASE
              WHEN dark = 'no' THEN 'brave'
              ELSE 'scaredycat'
            END
            FROM nycto;

**Constraints/Renaming**

          - SELECT muchness AS 'scaredness' FROM nycto;
          - DELETE FROM nycto WHERE muchness IS NULL;


**Database Problems**
  - Race Condition
    - The timing of two actions or events cause unexpected behavior
  - Injection Attack
    - Why you can't have certain characters in usernames and passwords
    ![](img/injection.png)

**[DB Browser for SQLite](https://sqlitebrowser.org/dl/)**

**[SQLite in Python...](https://docs.python.org/3/library/sqlite3.html)**
