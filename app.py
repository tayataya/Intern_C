from random import randint

from flask import Flask, send_from_directory,render_template
import os
from database import db, db_init
import repository
import pymysql

app = Flask(__name__)

db_init(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():
    #データベース接続
    connection=pymysql.connect(
        host="localhost",
        db="jse_intern",
        user='jseintern',
        password= 'jseintern+',

    )
    cursor=connection.cursor()
    #stock情報を取得
    cursor.execute("SELECT * FROM stock")
    materials = cursor.fetchall()

    stock_dict=[]
    for i in materials:
        #stock内のidを名前に変換してHTMLに送る
        stock_dict.append(list([str(repository.getProductNameFromId(i[1])),str(repository.getShopNameFromId(i[2])),str(i[3]),str(i[4])]))

    return render_template('outputs.html',message=stock_dict)

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
