from flask import Blueprint, jsonify, request

wordcount = Blueprint(name='wordcount', import_name='__name__')

@wordcount.route('/test', methods=['GET'])
def home():
    output = {"msg": "You've reached the test endpoint from wordcount"}
    return jsonify(output)
