# GenVoice API Backend

## Table of Contents
1. [How to Run](#how-to-run)
2. [Salient Features](#salient-features)
3. [Directory Structure](#directory-structure)
4. [Components](#components)
    4.1. [app.py](#apppy)
    4.2. [Routes](#routes)
    4.3. [Utils/security](#security)
5. [Extras](#extras)
6. [References](#references)

## How to Run
Postman Collection: 
   Open Postman --> import the [collection](/extras/genvoice.postman_collection.json).
   Logging In generates an ***Authorization Token***, which is needed by some other requests to function.
![Clinician Login API Testing in Postman](/extras/clinician_login_postman.png)

The following Requests require the Authorization Token to be pasted in the headers section.
  - Fetching All Available Cases.
  - Adding a New Case.
  - Logging Out.
![Auth Token in Postman Header](/extras/postman_auth_token_header.png)

---

## Salient Features
- [x] Modular
- [x] Scalable
- [x] Inline Comments for Easy Comprehension
- [x] Extensive Documentation

---

## Directory Structure
```
GenVoice
|
|-- /decorators
|    |-- auth.py
|
|-- /extras
|    |-- database.sql
|    |-- postman-collection.json
|    |-- screenshots
|    |-- sql_queries.sql
|
|-- /routes
|    |-- __init__.py
|    |-- cases.py
|    |-- clinicians.py
|
|-- /utils
|    |-- security.py
|
|-- .gitignore
|-- app.py
|-- config.py
|-- README.md
|-- requirements.txt
```

---

## Components
### [app.py](app.py)
This is the starting point of the API Program. This program ensures systematic and consolidates execution of the available processes as required.

This is also where the connection for MySQL has been intialised. So all processes and functions requiring a connection with the database import it from this directory using the following code:
```py
from app import mysql
```
This avoids multiple instances of the Database being accessed.

### Routes
#### [\_\_init__.py](/routes/__init__.py)
This is responsible for consolidating all the available routes.
This helps **Modularise** the code and keep it clean.
It also makes the code more **scalable**.

#### [cases](./routes/cases.py)
This is responsible for Adding New Cases to the database, and fetching all of them whenever required.

It ensures that Case data is not freely accessible by anyone, and confirms that a Clinician is logged in using the `@login_required` [decorator](/decorators/auth.py). 

#### [clinicians](./routes/clinicians.py)
This is responsible for **Registering** New Clinicians, and **Logging In** to already registered ones.

It is also ensured that if data is deleted, then the new auto_increment ID Integer is the one next to the largest available ID in the table.
For example, if there are 10 entries, and we delete entry no. 3, 5, 8, 9 and 10, so when we register a New user (or [Add a New Case](#cases)) the ID would be 8, as we already have ID up to 7 present in the table.
```py
cur.execute("ALTER TABLE cases AUTO_INCREMENT=1")
```

This file also provides the option to ***Promote*** a clinician to Senior Role, or ***Demote*** a clinician to Junior Role.

### [Security](./utils/security.py)
This is a Crucial part of the program.
It contains functions which are responsible for ***Hashing** the password* before storing it in the database.

the `check_password()` function compares the stored hash, and hash of the submitted password for *Verification* and *Authentication*.

At the Heart of the functioning of the API is the `generate_token()` function, which generates a JSON Web Token (JWT) to verify the validity of an ongoing session.

The generated token is used by multiple services and requests to confirm that user has access to what they are looking for.


The `Secret_Key` for the same has been generated using the following code:
```py
import secrets
print(secrets.token_hex(32))
```
This generates a secure 32-byte hex token, which has been stored in a private `.env` file.

> [!IMPORTANT]
> Sensitive information like SECRET_KEY is stored in an environment variable file, which is added to .gitignore. This ensures that it is not shared or visible publicly. 

---

## Extras
- [requirements.txt](/requirements.txt): Required Packages.
- [SQL_Queries.sql](/SQL_Queries.sql): This contains all the SQL Queries used to create the database, tables and fill dummy data into it.
- [hashed_pwd.py](extras/hashed_pwd.py): This is a file which uses the security functions to hash and verify the  passwords in the dummy data. It justifies what has been inserted in the database instead of the provided passwords.
- [config.py](/config.py): Configurations for MySQL Connection.
- [Logout](/routes/clinicians.py): added a Logout and Token Expire function.
- [Postman Collection](/extras/genvoice.postman_collection.json).
- [MySQL Database](/extras/genvoice.sql).

---

## References
- [py-bcrypt](http://www.mindrot.org/projects/py-bcrypt/)
- JWT
  - [Basic Usage](https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html)
  - [Easy Tutorial](https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/)
- [Flask-MySQL](https://flask-mysql.readthedocs.io/en/stable/)
- [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/)