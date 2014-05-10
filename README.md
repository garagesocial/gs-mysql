# gs_mysql

**gs_mysql** is the start of a python class wrapper around MySQL-python to manage manage the connection and perform common operations

## Requirements

  * MySQLdb Driver
    *   linux:  ``sudo apt-get install python-mysqldb``
    *   windows: http://www.codegood.com/archives/129

## Usage
* [Instantiate](#instantiate)
* [Create a database](#create-database)
* [Drop a database](#drop-database)
* [Dump a database](#dump-database)
* [Execute raw command](#raw-command)


<a name="instantiate"></a>
## Instantiate

```
  my_instance = gs_mysql("host", "username", "password", "port")
```

<a name="create-database"></a>
### Create database

```php
my_instance.drop("database")
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

gs_sql is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT)
(See LICENSE file for details).

