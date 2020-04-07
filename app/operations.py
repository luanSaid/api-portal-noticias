# coding: utf-8
""" Essa página atende as requisições. """

from config import client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
from importlib.machinery import SourceFileLoader
from bson.objectid import ObjectId

# Importa  o módulo facilitador
helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

# Selecão da database
db = client.portal_noticias
# Seleção da collection
collection = db.noticias

@app.route("/")
def get_initial_response():
    """ Mensagem de boas vindas da API. """
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Bem vind@ a API do Portal de Notícias da Code 7'
    }
    # Formatando a mensagem:
    resp = jsonify(message)
    # Retorno do json
    return resp

@app.route("/api/v1/news", methods=['POST'])
def create_news():
    """
       Função para cadastrar notícias
    """
    try:
        # Criar nova notícia
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request caso os dados estejam incorretos
            # Adiciona mensagem para debuggar
            return "Dados ausentes e/ou formato incorreto.", 400

        record_created = collection.insert(body)

        # Prepara a response
        if isinstance(record_created, list):
            # Retorna uma lista de ID do novo obj criado
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/api/v1/news/<search>", methods=['GET'])
def fetch_news(search):
    """
       Função para carregar as notícias baseadas na busca do usuário.
    """
    try:
        records_fetched = collection.find({ "$text" : {"$search" : search }})
        if records_fetched.count() > 0:
            # Prepara a response
            return dumps(records_fetched)
        else:
            return "Nenhum registro foi encontrado!", 404
    except:
        return "Erro na busca dos dados!", 500

@app.route("/api/v1/news/<news_id>", methods=['POST'])
def update_news(news_id):
    """
       Função para atualizar a notícia.
    """
    try:
        # Captura o valor para ser atualizado
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "O 'ID' e/ou formato inserido é inválido.", 400

        # Atualizando a notícia
        records_updated = collection.update_one({"_id": ObjectId(news_id)}, body)

        # Verifica se atualizou
        if records_updated.modified_count > 0:
            # successfully
            return "Notícia atualizada com sucesso!", 200
        else:
            # Not found
            return "Não foram encontrado(s) registro(s) com esse identificador (id) ", 404
    except:
        return "Erro ao atualizar os dados!", 500

@app.route("/api/v1/news/<news_id>", methods=['DELETE'])
def remove_news(news_id):
    """
       Função para apagar uma notícia
    """
    try:
        # Deletar notícia pelo id automático
        delete_news = collection.delete_one({'_id': ObjectId(news_id)})
        
        print(delete_news.deleted_count)
        if delete_news.deleted_count > 0 :
            return "Notícia deletada com sucesso!", 204
        else:
            return "Nenhum registro foi encontrado com esse id!", 404
    except:
        return "Erro durante a tentativa de deletar os dados!", 500

@app.errorhandler(404)
def page_not_found(e):
    # Mensagem pro usuário
    message = {
        "err":
            {
                "msg": "A rota digitada é inválida. Por favor, dirija-se a documentação da API para mais informações."
            }
    }
    # Formatação visual 
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    return resp


#db.noticias.find( { $and : [ { $or : [ { titulo : '' } },{ $or : [ { texto : '' }, { id_autor : '' } ] }]} )