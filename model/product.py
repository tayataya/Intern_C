from database import db
from model.ingredient import Ingredient

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 商品id,主キー
    name = db.Column(db.String(128), nullable=False)  # 商品名
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id))   # 食材id, 外部キー

    def __init__(self, name, ingredientId):
        self.name = name
        self.ingredient_id = ingredientId

    # 全ての商品を取得
    @staticmethod
    def getAllProducts():
        products = db.session.query(Product).all()
        return products

    # 商品を追加
    @staticmethod
    def setProduct(name, ingredientId):
        record = Product(name=name, ingredientId=ingredientId)
        db.session.add(record)
        db.session.commit()

    # 食材idから商品を取得
    @staticmethod
    def getProductFromIngredientId(ingredientId):
        products = db.session.query(Product).filter_by(ingredient_id=ingredientId).all()
        return products

   # idから商品名を取得
    @staticmethod
    def getProductNameFromId(id):
        product_name = db.session.query(Product).get(id)
        return product_name