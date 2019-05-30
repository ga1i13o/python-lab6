from flask import Flask, jsonify, redirect, url_for, request, abort, session, Response
import handle_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app, methods=["GET","POST","PUT","DELETE"])
endpoint = "/api/v1"


@app.route('/')
def hello_world():
    return "<h2>Rest-api endpoint: "+endpoint + " </h2>"


@app.route(endpoint+'/tasks', methods=['GET'])
def get_all():
    tasks = handle_db.retrieve_all()
    print(tasks)

    return jsonify({'tasks': tasks})


@app.route(endpoint+'/tasks', methods=['POST'])
def add_one_task():
    new_task = request.json

    if( new_task is not None) and ('todo' in new_task) and ('urgency' in new_task):
        print(new_task)
        handle_db.insert(new_task['todo'], new_task['urgency'])

        return Response(status=201)
    abort(403)


@app.route(endpoint+'/tasks/<id>', methods=['GET'])
def get_one_task(id):
    task = handle_db.retrieve_one(id=id)
    return jsonify({'task': task})


@app.route(endpoint+'/tasks/<id>', methods=['DELETE'])
def remove_one(id):
    handle_db.remove(id=id)

    return Response(status=200)


@app.route(endpoint+'/tasks/<id>', methods=['PUT'])
def update_one(id):
    news = request.json

    if( news is not None) and ('todo' in news) and ('urgency' in news):
        todo =  news['todo']
        urgency = news['urgency']
        handle_db.update_todo(id=id, todo=todo)
        handle_db.update_urgency(id=id, urgency=urgency)

        return Response(status=200)

    abort(403)


