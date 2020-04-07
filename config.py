# coding: utf-8
"""Configuração do app para conectar com a database."""

from pymongo import MongoClient

DATABASE = MongoClient()['portal_noticias'] # DB_NAME
DEBUG = True
client = MongoClient('localhost', 27017)
