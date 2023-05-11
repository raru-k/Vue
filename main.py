from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/')
def index():
    df = pd.read_csv('static/csv/todo.csv', header=None, encoding='utf-8')
    
    df.columns = ['todo','check','important','visible']
    
    ToDoList = []
    
    for i in range(len(df)):
        ToDoList.append({
            "todo" : df['todo'][i],
            "check" : df['check'][i],
            "important" : df['important'][i],
            "visible" : df['visible'][i]
        })
    
    return render_template('index.html',
                        ToDoList=ToDoList)



if __name__ == '__main__':
    app.run(debug=True)