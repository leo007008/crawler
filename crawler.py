#!/usr/bin/env python
# -*- coding: utf-8 -*-


#################
#all the imports
#################
from flask import Flask, request, session, g, redirect, url_for,\
  abort, render_template, flash

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