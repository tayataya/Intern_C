from database import db


class Shop(db.Model):
    __tablename__ = "shop"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 店舗id,主キー
    name = db.Column(db.String(128), nullable=False)                    # 店舗名

    def __init__(self, name):
        self.name = name

    # 全ての店舗を取得
    @staticmethod
    def getAllShops():
        shops = db.session.query(Shop).all()
        return shops

    # 店舗を追加
    @staticmethod
    def setShop(name):
        record = Shop(name = name)
        db.session.add(record)
        db.session.commit()

    # idから店舗名を取得
    @staticmethod
    def getShopNameFromId(id):
        shop_name = db.session.query(Shop).get(id)
        return shop_name