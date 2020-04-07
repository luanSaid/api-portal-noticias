# coding: utf-8
""" Esse módulo codifica a query e analisa os parametros enviados."""
from urllib.parse import parse_qs

def parse_query_params(query_string):
    """
        Função para analisar a sequência de parâmetros da consulta.
    """
    # Análise da sequencia de parametros da consulta.
    query_params = dict(parse_qs(query_string))
    # Pega o valor da lista
    query_params = {k: v[0] for k, v in query_params.items()}
    return query_params