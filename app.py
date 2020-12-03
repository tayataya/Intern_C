from flask import Flask, send_from_directory,render_template
import os
from database import db, db_init
from model.product import Product
from model.cook import Cook
from model.food import Food
from model.ingredient import Ingredient
from model.product import Product
from model.shop import Shop
from model.stock import Stock


app = Flask(__name__)

app.config.from_object('dbConfig.DbConfig')
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


@app.route('/init')
def initdatabase():
    # Food.setFood("カレー")
    # Food.setFood("肉じゃが")
    # Food.setFood("ハンバーグ")
    return "done"

if __name__ == '__main__':
    app.run(debug=True)
