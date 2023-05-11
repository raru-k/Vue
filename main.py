from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/')
def index():
    ToDoList=[
        {
        "todo" : "aaa",
        "check" : "false",
        "class" : "NotCom",
        "important": "false"
    }]
    return render_template('index.html',
                        ToDoList=ToDoList)

@app.route('/todolist')
def get_todolist():
    ToDoList=[
        {
        "todo" : "aaa",
        "check" : False,
        "class" : "NotComp",
        "important": False
    }]
    return jsonify(ToDoList)


if __name__ == '__main__':
    app.run(debug=True)