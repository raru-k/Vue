# @app.route('/todo')
# def todo():
#     df = pd.read_csv('../static/todo.csv', header=None, encoding='utf-8')
#     df.columns = ['todo','check','class','important']
    
#     for i in range(len(df['todo'])):
#         if df['check'][i] == 'on':
#             df['class'][i] = 'checked'
#         else:
#             df['class'][i] = ''

#     return render_template('index.html', df=df)

# @app.route('\create')
# def create():
#     return render_template('create.html')