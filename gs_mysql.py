#!/usr/bin/python

###############################################################################
### Garagesocial, Inc. - https://www.garagesocial.com
###############################################################################
###
### Filename:  gs_mysql.py
###
### About:     Python shell class to facilitate and manage common MySQL
###            operations through MySQL-python driver
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
###############################################################################
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
###############################################################################

import MySQLdb
import subprocess, shlex
import warnings

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

   # Instantiate the mysql handle and cursor and store them
   # Connection information passed into constructor are used
   def setup(self):
      """Initialize the db handle and cursor"""
      if self.db_handle is None:
         self.db_handle = MySQLdb.connect(host=self.host, user=self.username,
                                          passwd=self.password, port=self.port)
         self.db_cursor = self.cursor()

   # Instantiate db handle if necessary and update local variable
   def handle(self):
      """Initialize the db handle"""
      if self.db_handle is None: setup()
      return self.db_handle

   # Instantiate db cursor if necessary and update local variable
   def cursor(self):
      """Initialize the db cursor"""
      if self.db_handle is None or self.db_cursor is None:
         self.setup()
         self.db_cursor = self.db_handle.cursor()
      return self.db_cursor

   #############################################################################

   # Create a database
   #
   # @param  string   database    Name of database
   # @param  bool     drop_first  Whether to attempt to drop the database first
   # @return void
   def create(self, database, drop_first = False):
      """Create specified database"""
      if drop_first: self.drop(database)
      self.cursor().execute("CREATE DATABASE %s;" % database)
      self.handle().commit()

   # Drop a database
   #
   # @param  string   database    Name of database
   # @return void
   def drop(self, database):
      """Drop specified database"""
      # the IF EXISTS is not respected and a warning is still thrown
      # this ignores it
      warnings.filterwarnings("ignore")
      self.cursor().execute("DROP DATABASE IF EXISTS %s;" % database)
      self.handle().commit()
      warnings.resetwarnings()

   # Dump a database to a file
   #
   # @param  string   database            Name of database
   # @param  string   output_file_path    File path to dump database to
   # @return void
   def dump(self, database, output_file_path):
      """Dump specified database to file"""
      command_text = """
                        mysqldump
                        --user=%(user)s
                        --password=%(password)s
                        --host=%(host)s
                        --port=%(port)i
                        %(database)s
                        --result-file="%(file)s"
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

   # Inject a database dump
   #
   # @param  string   database            Name of database
   # @param  string   input_file_path     Path to SQL dump
   # @return void
   def inject(self, database, input_file_path):
      """Inject a dump sql file into database"""
      command_text = """
                        mysql
                        --user=%(user)s
                        --password=%(password)s
                        --host=%(host)s
                        --port=%(port)i
                        %(database)s
                     """
      command_data = {
                        "user": self.username,
                        "password": self.password,
                        "host": self.host,
                        "port": self.port,
                        "database": database
                     }

      proc = subprocess.Popen(shlex.split(command_text % command_data), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      out, err = proc.communicate(file(input_file_path).read())

   # Execute a raw command
   #
   # @param  string   raw  (ex: DELETE FROM groups WHERE ID = 2)
   # @return void
   def raw(self, raw):
      """Execute raw sql commands"""
      self.cursor().execute(raw)
      self.handle().commit()

# End of gs_mysql.py
