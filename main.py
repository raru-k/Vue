from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def todo():
    df = pd.read_csv('../static/todo.csv', header=None, encoding='CP932')
