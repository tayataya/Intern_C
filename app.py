from random import randint

from flask import Flask, send_from_directory,render_template
import os
from database import db, db_init
import repository


app = Flask(__name__)

db_init(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():

    materials = {}
    materials['name'] = "jinja"
    materials['shop_name']=list(["shop1","shop2","shop3"])
    materials['value']=list([100,200,300])
    materials['stock_num'] = list([10,20,30])
    return render_template('outputs.html',message=materials)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'), 'favicon.ico', )

# 料理名から食材名のリストを取得するサンプルです。
@app.route('/test')
def test():
    ingredients = repository.getIngredientsFromFoodName("ハンバーグ")
    output = ""
    for ing in ingredients:
        output += (str(ing.name) + "<br>")
    return output


# データベースに初期値を入れます。 最初の1回のみ実行できます。
@app.route('/init')
def initdatabase():
    repository.initialize()
    return "done"

if __name__ == '__main__':
    app.run(debug=True)
