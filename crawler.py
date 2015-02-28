#!/usr/bin/env python
# -*- coding: utf-8 -*-


#################
#all the imports
#################
import sqlite3
import time
from handler import index_handler, login_handler, register_handler,\
  logout_handler, add_entry_handler, manage_handler
from flask import Flask, request, session, g, redirect, url_for,\
  abort, render_template, flash
from contextlib import closing

#configuration


#################
#create the server
#################
app = Flask(__name__)
app.config.from_object(__name__)

#################
#database initialization
#################


#################
#router function
#################


#################
#run the server
#################    
if __name__ == '__main__':
  app.run(host='0.0.0.0')