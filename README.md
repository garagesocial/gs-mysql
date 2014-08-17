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
The MIT License

Copyright (c) 2013-2014 Garagesocial, Inc. http://garagesocial.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
