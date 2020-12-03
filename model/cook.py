from database import db
from model.food import Food
from model.ingredient import Ingredient

class Cook(db.Model):
    __tablename__ = "cook"
    __table_args__ = (db.UniqueConstraint("food_id", "ingredient_id"),{})  # id組み合わせのユニーク制約
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 料理と食材の組み合わせid, 主キー
    food_id = db.Column(db.Integer, db.ForeignKey(Food.id))    # 料理id, 外部キー
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id))   # 食材id, 外部キー

    def __init__(self, foodId, ingredientId):
        self.food_id = foodId
        self.ingredient_id = ingredientId

    # 全ての料理と食材の組み合わせを取得
    @staticmethod
    def getAllCooks():
        cooks = db.session.query(Cook).all()
        return cooks

    # 料理idから食材idリストを取得
    @staticmethod
    def getIngredientIdsFromFoodId(foodId):
        ings = db.session.query(Cook).filter_by(food_id=foodId).all()
        if ings is None:
            return None
        ids = []
        for ing in ings:
            ids.append(ing.ingredient_id)
        return ids

    # 料理に必要な食材を追加
    @staticmethod
    def setCook(foodId, ingredientId):
        record = Cook(foodId=foodId, ingredientId=ingredientId)
        db.session.add(record)
        db.session.commit()


