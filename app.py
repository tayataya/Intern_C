from random import randint

from flask import Flask, send_from_directory,render_template, request
import os
from database import db, db_init

import pymysql
import service
from model.ingredient import Ingredient
from model.product import Product
from model.shop import Shop
from model.stock import Stock

app = Flask(__name__)

db_init(app)

@app.route('/')
def form():
   return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
      result = request.form
      return render_template("confirm.html",result = result)


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
        stock_dict.append(list([str(service.getProductNameFromId(i[1])),str(service.getShopNameFromId(i[2])),str(i[3]),str(i[4])]))

    return render_template('outputs.html',message=stock_dict)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'), 'favicon.ico', )

# 料理名から食材名のリストを取得するサンプルです。
@app.route('/test')
def test():
    output = ""
    # ingredients = service.getIngredientsFromFoodName("ハンバーグ")
    # for ing in ingredients:
    #     output += (str(ing.name) + "<br>")

    ingAndPrs = service.getIngredientsAndProductsFromFoodName("カレー")
    for ingandpr in ingAndPrs:
        output+=str(ingandpr[0].name) + "<br>"
        for pro in ingandpr[1]:
            output +=(str(str(pro.name)))
        output+="<br>"
    return output


# データベースに初期値を入れます。 最初の1回のみ実行できます。
@app.route('/init')
def initdatabase():
    service.initialize()
    return "done"

@app.route("/show") #アプリケーション/showにアクセスがあった場合
def show():
    #データベース接続
    connection=pymysql.connect(
        host="localhost",
        db="jse_intern",
        user='jseintern',
        password= 'jseintern+',

    )
    cursor=connection.cursor()
    food_name="カレー"
    product_name_list=[]
    coming_list= service.getIngredientsAndProductsFromFoodName(food_name)
    for ing in coming_list:
        for pro in ing[1]:
            product_name_list.append(pro.name)
            
    #stock情報を取得
    cursor.execute("SELECT * FROM stock")
    materials = cursor.fetchall()


    stock_dict=[]
    for i in materials:
        #stock内のidを名前に変換してHTMLに送る
        #product_name_listに格納済みの選択された料理の商品のみ表示
        if str(service.getProductNameFromId(i[1])) in product_name_list:
            stock_dict.append(list([str(Ingredient.getIngredientFromId(Product.getProductNameFromId(i[1]).id).name),str(service.getProductNameFromId(i[1])),str(service.getShopNameFromId(i[2])),str(i[3]),str(i[4])]))

    return render_template('show.html',food=food_name,message=stock_dict)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
