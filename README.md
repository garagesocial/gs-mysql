gs_mysql
===============

## Requirements

  * MySQL-python
    *   linux:  ``sudo apt-get install python-mysqldb``
    *   windows: http://www.codegood.com/archives/129

## Usage
* [Instantiate](#instantiate)
* [Create a database](#create-database)
* [Drop a database](#drop-database)
* [Dump a database](#dump-database)
* [Inject a database](#inject-database)
* [Execute raw command](#raw-command)


<a name="instantiate"></a>
## Instantiate

```
  my_instance = gs_mysql("host", "username", "password", "port")
```

<a name="create-database"></a>
### Create database

```php
my_instance.create("database")
```

<a name="drop-database"></a>
### Drop database

```php
my_instance.drop("database")
```

<a name="dump-database"></a>
### Dump database to file

```php
my_instance.dump("database", "/home/user/my_dump.sql")
```

<a name="raw-command"></a>
### Execute raw command

```php
my_instance.raw("database", "DELETE FROM groups WHERE ID = 2")
```

<a name="inject-database"></a>
### Inject a database from an sql dump 
note: make sure the sql dump does not contain ``create database`` statements or `use` statements

```php
my_instance.inject("database", "/home/user/my_dump.sql")
```


### License
gs_mysql is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT)

