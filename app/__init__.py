# coding: utf-8
""" Módulo init. """

from flask import Flask

# Place where app is defined
app = Flask(__name__)

from app import operations
