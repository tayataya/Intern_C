from database import db


class Food(db.Model):
    __tablename__ = "foods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name.title()

    @staticmethod
    def getFoodList():
        list = db.session.query(Food).all()
        return list

    @staticmethod
    def setFood(name):
        record = Food(name = name)
        db.session.add(record)
        db.session.commit()



class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name.title()

    @staticmethod
    def getIngredientList():
        list = db.session.query(Ingredient).all()
        return list

    @staticmethod
    def setIngredient(name):
        record = Ingredient(name=name)
        db.session.add(record)
        db.session.commit()
