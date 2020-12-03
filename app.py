from flask import Flask, send_from_directory,render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from database import db
from models import Food, Ingredient
app = Flask(__name__)

app.config.from_object('dbConfig.DbConfig')
db.init_app(app)


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
    for v in range(1,10):
        Ingredient.setIngredient("Ingredient" + str(v))
    return "done"

if __name__ == '__main__':
    app.run(debug=True)
