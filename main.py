from flask import Flask, render_template,request

def updateTxt(text):
    if(text is None):
        return
    with open("static/txt/todo.txt","w",encoding="utf-8") as f:
        f.write(text)

def readTxt():
    with open("static/txt/todo.txt","r",encoding="utf-8") as f:
        text = f.read()
    if text == "":
        text = '[]'
    return text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def updateToDo():
    
    if request.method == 'POST': # POSTの場合はtxtファイルの中身を更新する
        
        print(request.form.get("tasks"))
        
        updateTxt(request.form.get("tasks"))
    
    list= readTxt()
    
    return render_template('index.html',
                            list=list)


if __name__ == '__main__':
    app.run(debug=True)