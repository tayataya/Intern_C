from database import db

class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    # 料理id,主キー
    name = db.Column(db.String(128), nullable=False)                    # 料理名

    def __init__(self, name):
        self.name = name

    # 全ての料理を取得
    @staticmethod
    def getAllFoods():
        foods = db.session.query(Food).all()
        return foods

    # 料理を追加
    @staticmethod
    def setFood(name):
        record = Food(name = name)
        db.session.add(record)
        db.session.commit()