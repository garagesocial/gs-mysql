#!/usr/bin/python

################################################################################
### Garagesocial, Inc. - https://www.garagesocial.com
################################################################################
###
### Filename:  gs_mysql.py
###
### About:     Is a basic start of a python shell class to help managing the
###            connection with an sql database and performing common operations
### Usage:
###            Method 1:
###               my_instance = gs_mysql("host", "username", "password", "port")
###               my_instance.create("database")
###               del db_instance
###            Method 2:
###               with gs_mysql("host", "username", "password", "port") as
###               instance:
###                instance.create("database")
###
### Dependencies:
###            MySQL-python
###               linux:   sudo apt-get install python-mysqldb
###               windows: http://www.codegood.com/archives/129
###
### Documentation Reference: https://docs.python.org/devguide/documenting.html
###
################################################################################
###
### The MIT License (MIT)
###
### Copyright (c) 2014 Garagesocial, Inc.
###
### Permission is hereby granted, free of charge, to any person obtaining a
### copy of this software and associated documentation files (the "Software"),
### to deal in the Software without restriction, including without limitation
### the rights to use, copy, modify, merge, publish, distribute, sublicense,
### and/or sell copies of the Software, and to permit persons to whom the
### Software is furnished to do so, subject to the following conditions:
###
### The above copyright notice and this permission notice shall be included in
### all copies or substantial portions of the Software.
###
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
### IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
### FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
### THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
### LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
### FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
### DEALINGS IN THE SOFTWARE.
###
################################################################################

import MySQLdb
import subprocess, shlex

class gs_mysql:
   ### connection information
   host = None
   username = None
   password = None
   port = None
   ### connection handles
   db_handle = None
   db_cursor = None

   #############################################################################

   def __init__(self, host, username, password, port = 3306):
      self.host = host
      self.username = username
      self.password = password
      self.port = port

   def __enter__(self):
      self.setup()
      return self

   def __exit__(self, type, value, traceback):
      self.db_cursor.close()
      self.db_cursor = None
      self.db_handle.close()
      self.db_handle = None

   def __del__(self):
      if self.db_cursor is not None: self.db_cursor.close()
      if self.db_handle is not None: self.db_handle.close()

   #############################################################################

   def setup(self):
      """Initialize the db handle and cursor"""
      if self.db_handle is None:
         self.db_handle = MySQLdb.connect(host=self.host, user=self.username,
                                          passwd=self.password, port=self.port)
         self.db_cursor = self.cursor()

   def handle(self):
      """Initialize the db handle"""
      if self.db_handle is None: setup()
      return self.db_handle

   def cursor(self):
      """Initialize the db cursor"""
      if self.db_handle is None or self.db_cursor is None:
         self.setup()
         self.db_cursor = self.db_handle.cursor()
      return self.db_cursor

   #############################################################################

   def create(self, database, drop_first = False):
      """Create specified database"""
      if drop_first: self.drop(database)
      self.cursor().execute("CREATE DATABASE %s;" % database)
      self.handle().commit()

   def drop(self, database):
      """Drop specified database"""
      self.cursor().execute("DROP DATABASE IF EXISTS %s;" % database)
      self.handle().commit()

   def dump(self, database, output_file_path):
      """Dump specified database to file"""
      command_text = """
                        mysqldump
                        --user=%(user)s
                        --password=%(password)s
                        --host=%(host)s
                        --port=%(port)i
                        %(database)s
                        --result-file=%(file)s
                     """
      command_data = {
                        "user": self.username,
                        "password": self.password,
                        "host": self.host,
                        "port": self.port,
                        "database": database,
                        "file": output_file_path
                     }
      subprocess.call(shlex.split(command_text % command_data ))

   def raw(self, raw):
      """Execute raw sql commands"""
      self.cursor().execute(raw)
      self.handle().commit()
