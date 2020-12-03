from database import db
from model.food import Food

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 食材id, 主キー
    name = db.Column(db.String(128), nullable=False)                    # 食材名

    def __init__(self, name):
        self.name = name

    # 全ての食材を取得
    @staticmethod
    def getAllIngredients():
        ingredients = db.session.query(Ingredient).all()
        return ingredients

    # 食材を追加
    @staticmethod
    def setIngredient(name):
        record = Ingredient(name=name)
        db.session.add(record)
        db.session.commit()

    # idから食材を取得
    @staticmethod
    def getIngredientFromId(id):
        ingredient = db.session.query(Ingredient).get(id)
        return ingredient

