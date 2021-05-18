# SQL, Django Models and Migrations

## SQL

SQL lets you talk to a DB (could be relational like MySQl, PostgreSQL; or lightweight like SQLite)

Each db column has a type, just like python

E.g. SQLite:

* Text
* Numeric (number-ish data that's not a number, like a date)
* Integer
* Real
* Blob (binary, large object)

MySQL has Char(size) and Varchar(size) to save space, plus multiple types of int (Smallint, int, bigint)

### Command to create a table

`CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);`

Other constraints:

* Check (for a range)
* Default
* Not null
* Primary key
* Unique (can't have dupes)

### Command to insert data

`INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);`

### Command to get data

`SELECT * FROM flights;` (gets all rows and all columns)
`SELECT origin, destination FROM flights;` (select all rows, but only some columns)
`SELECT * FROM flights WHERE id = 3;` (select all columns, but only row(s) that match WHERE)
`SELECT * FROM flights WHERE duration > 500;` (other comparisons)
`SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";` (join multiple expressions together with AND or OR)
`...WHERE origin IN ("New York", "Lima")` (shortcut for multiple "origin" checks)
`...WHERE origin LIKE "%a%"` (flights where there's an "a" in the origin. % = wildcard)
`SELECT AVERAGE|COUNT|MAX|MIN|SUM` (other calculations)

### Setting this up on the command line

`$ touch flights.sql
$ sqlite3 flights.sql
sqlite> .mode columns
sqlite> .headers yes`

### Updating data

`UPDATE flights
    SET duration = 430
    WHERE origin = "New York"
    AND destination = "London";`

### Removing rows

`DELETE FROM FLIGHTS WHERE ...`

### Other clauses

* LIMIT
* ORDER BY
* GROUP BY
* HAVING (constraint on GROUP BY)

### Relational data & Foreign keys

`CREATE TABLE airports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_code,
    city_name,
);`

Change `flights` table to have `origin_id`, and `destination_id`

### Relationships

* One to many
* Many to many

Join table `passengers` just has `person_id` and `flight_id`

### Joins

Inner join:

`SELECT first, origin, destination
FROM flights JOIN passengers
ON passengers.flight_id = flights.id;`

### Create index to make queries more efficient

`CREATE INDEX name_index ON passengers (last);`

### Preventing SQL Injection by using Django models

`SELECT * FROM users WHERE user = user AND password = pass;`

## Models

Django's abstraction layer atop the database. Allows you to write code to handle persistance, and represent the data

Create a class in `models.py` then run migrations

`$ python manage.py makemigrations`
`$ python manage.py migrate`

Use django shell to run commands

`$ python manage.py shell`

In [1]: from flights.models import Flight
In [2]: f = Flight(origin="New York", destination="London", duration=415)
In [3]: f.save()
In [4]: Flight.objects.all()
Out[4]: QuerySet [<Flight: 1: New York to London>]
In [5]: flights = _
In [6]: flight = flights.first()
In [7]: flight
Out[7]: <Flight: 1: New York to London>
In [8]: flight.id
Out[8]: 1
In [9]: flight.origin
Out[9]: 'New York'
In [10]: flight.destination
Out[10]: 'London'
In [11]: flight.delete()
Out[11]: (1, {'flights.Flight': 1})

## Migrations

How you make changes to the database, as models change


In [1]: from flights.models import *
In [2]: jfk = Airport(code="JFK", city="New York")
In [3]: jfk.save()
In [4]: lhr = Airport(code="LHR", city="London")
In [5]: lhr.save()
In [6]: cdg = Airport(code="CDG", city="Paris")
In [7]: cdg.save()
In [8]: f = Flight(origin=jfk, destination=lhr, duration=415)
In [9]: f.save()
In [10]: f
Out[10]: <Flight: 1: New York (JFK) to London (LHR)>
In [11]: f.origin
Out[11]: <Airport: New York (JFK)>
In [12]: f.origin.city
Out[12]: 'New York'
In [13]: f.origin.code
Out[13]: 'JFK'
In [14]: lhr.arrivals.all()
Out[14]: QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]
In [15]: lhr.departures.all()
Out[15]: QuerySet []
In [16]: Airport.objects.all()
Out[16]: QuerySet [<Airport: New York (JFK)>, <Airport: London (LHR)>, <Airport: Paris (CDG)>]
In [17]: Airport.objects.filter(city="New York")
Out[17]: QuerySet [<Airport: New York (JFK)>]
In [18]: Airport.objects.filter(city="New York").first()
Out[18]: <Airport: New York (JFK)>
In [19]: Airport.objects.get(city="New York")
Out[19]: <Airport: New York (JFK)>
In [20]: jfk = Airport.objects.get(city="New York")
In [21]: cdg
Out[21]: <Airport: Paris (CDG)>
In [22]: f = Flight(origin=jfk, destination=cdg, duration=435)
In [23]: f.save()

## Adding data with a buit-in Web UI

Django already built an app for CRUD
Django Admin app

Need to create an admin account
`python manage.py createsuperuser`

then register the models in `admin.py`
then visit the `/admin` url and login
