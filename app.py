from flask import Flask, jsonify, redirect, url_for, request, abort, session
import handle_db

app = Flask(__name__)
endpoint = "/api/v1"


@app.route('/')
def hello_world():
    return "<h2>Rest-api endpoint: "+endpoint + " </h2>"


@app.route(endpoint+'/tasks', methods=['GET'])
def get_all():
    tasks = handle_db.retrieve_all()
    return jsonify(tasks)


@app.route(endpoint+'/tasks', methods=['POST'])
def add_one_task():
    new_task = request.json
    print(new_task)
    handle_db.insert(new_task['todo'], new_task['urgency'])


@app.route(endpoint+'/tasks/<id>', methods=['GET'])
def get_one_task(id):
    task = handle_db.retrieve_one(id=id)
    return jsonify(task)


@app.route(endpoint+'/tasks/<id>', methods=['DELETE'])
def remove_one(id):
    handle_db.remove(id=id)


@app.route(endpoint+'/tasks/<id>', methods=['PUT'])
def update_one(id):
    news = request.json
    todo =  news.get('todo', "")
    urgency = news.get('urgency', "")
    if todo != "":
        handle_db.update_todo(id=id, todo=todo)
    if urgency != "":
        handle_db.update_urgency(id=id, urgency=urgency)

    return ""


