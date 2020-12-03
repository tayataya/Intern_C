from database import db
from model.product import Product
from model.shop import Shop

class Stock(db.Model):
    __tablename__ = "stock"
    __table_args__ = (db.UniqueConstraint("product_id", "shop_id"),{})  # id組み合わせのユニーク制約
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 在庫id, 主キー
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))  # 商品id, 外部キー
    shop_id = db.Column(db.Integer, db.ForeignKey(Shop.id))   # 店舗id, 外部キー
    price = db.Column(db.Integer, nullable=False)  # 価格
    amount = db.Column(db.Integer, nullable=False)          # 在庫数量

    def __init__(self, productId, shopId, amount):
        self.product_id = productId
        self.shop_id = shopId
        self.amount = amount

    # 全ての在庫を取得
    @staticmethod
    def getAllStocks():
        stocks = db.session.query(Stock).all()
        return stocks

    # 在庫を追加
    @staticmethod
    def setStock(productId, shopId, amount):
        record = Stock(productId=productId, shopId=shopId, amount=amount)
        db.session.add(record)
        db.session.commit()