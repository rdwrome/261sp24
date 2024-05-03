# SQL

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

          - sqlite3 nycto261.db //creates database
          - CREATE TABLE 'nycto' ('id' integer, 'name' text, 'dark' text);
          - .tables //names table
          - .schema // shows structure of table named
          - INSERT INTO nycto (id, name, dark) VALUES(6, 'raymond', 'no');
          - SELECT name FROM nycto;
          - SELECT name, dark FROM nycto;
          - SELECT * FROM nycto;
          - SELECT * FROM nycto WHERE dark = 'no';
          - SELECT DISTINCT name FROM nycto;
          - ALTER TABLE nycto ADD COLUMN 'muchness' integer;
          - UPDATE nycto SET dark = 'yes' WHERE id = 2;
          - UPDATE nycto SET muchness = 9 WHERE id = 2;

**Operators**

          - SELECT * FROM nycto WHERE name LIKE 'ra_hel';
          - SELECT * FROM nycto WHERE name LIKE 'r%';
          - SELECT * FROM nycto WHERE name LIKE '%o%';
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

          - DELETE FROM nycto WHERE muchness IS NULL;


**Database Problems**
  - Race Condition
    - The timing of two actions or events cause unexpected behavior
  - Injection Attack
    - Why you can't have certain characters in usernames and passwords
    ![](img/injection.png)

**[DB Browser for SQLite](https://sqlitebrowser.org/dl/)**

**[SQLite in Python...](https://docs.python.org/3/library/sqlite3.html)**

# AI & ML

## Singularity & Cyborgs
- [Ray Kurzweil](https://www.goodreads.com/book/show/83518.The_Singularity_is_Near)
- [Donna Haraway](https://en.wikipedia.org/wiki/A_Cyborg_Manifesto)

## Uncanny Valley
- Robots: OK, Humans: OK. Can't tell? Not OK
- [Cats (2019)](https://www.youtube.com/watch?v=FtSd844cI7U)
- [AIVA](https://www.youtube.com/watch?v=6I3aKYyKl68)
- [Turing Test](http://web.cse.ohio-state.edu/~stiff.4/cse3521/turing-test.html)
- Bots
- [Google Translate](https://translate.google.com/)
- Much is made of them, but the Singularity, the Uncanny Valley and the concept of "Smart" are **socially-constructed**

## "AI" vs "Machine Learning" according to AI folks
- "Science of Making Machines Smart" - Demis Hassabis (Google DeepMind)
- Make a machine do something 'smart,' automatically adapt to users, provide them unique experience
- Early methods include **Logic or Expert Systems**
  - Creator 'solves' problem
  - [DeepBlue](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer))
  - Can't deal with the unexpected, can't learn anything new
- Machine Learning
  - Machine can learn new things
  - [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo)
  - [BINA48](https://www.hansonrobotics.com/bina48-9/)
  - [chatGPT-3](https://www.nytimes.com/2022/04/15/magazine/ai-language.html?searchResultPosition=2)
  - but can it learn **beyond its training data**?

### Types of Machine Learning
  - Supervised (training data has all the answers)
  - Unsupervised (anomaly detection)
  - Semisupervised (partially labelled, looking for patterns)
  - Reinforcement learning (getting towards AI...like training a dog with positive and negative rewards)

### Modes
  - Batch learning (you get all the training data at once)
  - "Online" learning (system can accept new training data on the go)
  - Instance-based (commits training data to memory, then compares new data to training data)
  - Model-based (generalizes from a set of examples then uses that model to make predictions)

### Problems
  - Insufficient quantity of training data
  - Poor quality of training data
  - Non-representative training data

### AI
- Neural Networks
  - identifies + reproduces patterns in the same way a human brain does
  - used to be called "deep learning"
- *what can it learn beyond it's training data?*
  - [Google Neural Network](https://www.wired.co.uk/article/google-ai-language-create)

**Ethics**
- [Bias in AI](https://www.nytimes.com/2021/03/15/technology/artificial-intelligence-google-bias.html)

**Art**
- [Stephanie Dinkins: Conversations with BINA48](https://www.stephaniedinkins.com/conversations-with-bina48.html)
- [Daniel Ek, Spotify and AI](https://www.vice.com/en/article/epxxkn/musicians-are-dragging-spotifys-ceo-for-funding-a-military-ai-company)
- [My Favorite Deep Fake](https://moondisaster.org/film)
- ["Your" Favorite Deep Fake](https://www.youtube.com/watch?v=VWrhRBb-1Ig)
