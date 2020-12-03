from random import randint

from model.product import Product
from model.cook import Cook
from model.food import Food
from model.ingredient import Ingredient
from model.product import Product
from model.shop import Shop
from model.stock import Stock

# 料理名から食材のリストを取得
def getIngredientsFromFoodName(foodName):
    food = Food.getFoodByName(foodName)
    ingIds = Cook.getIngredientIdsFromFoodId(food.id)
    if ingIds is None:
        return None
    ingredients = []
    for id in ingIds:
        ingredients.append(Ingredient.getIngredientFromId(id))
    return ingredients

def initialize():
    Food.setFood("カレー")
    Food.setFood("肉じゃが")
    Food.setFood("ハンバーグ")
    ingredients = ["牛肉","あいびき肉","カレールウ","玉ねぎ","にんじん","じゃがいも","糸こんにゃく","絹さや","醤油","みりん","酒","砂糖","パン粉"
            ,"牛乳","にんにく","こしょう","ケチャップ","ウスターソース"]
    for i in ingredients:
        Ingredient.setIngredient(i)
    cooks = [[1,3,4,5,6],[1,4,6,7,8,9,10,11,12],[2,4,13,14,15,16,17,18]]
    for n in range(1,4):
        for m in cooks[n-1]:
            Cook.setCook(n,m)
    products = [["和牛","豪州産牛","米国産牛"],["あいびき肉"],["A社甘口とろ～り","A社辛口ぴりっと","B社甘口まったり","B社辛口30倍"],["玉ねぎ","新玉ねぎ"]
                  ,["にんじん","金時にんじん"],["男爵","新じゃが","メークイン"],["A社いとこん","B社いとこん"],["絹さや"]
                  ,["A社濃口醤油","B社濃口醤油"],["本みりん","みりん風調味料"],["A社料理酒","B社料理酒"],["上白糖","三温糖"],["パン粉"]
                  ,["A社牛乳","B社牛乳"],["にんにく"],["A社こしょう","B社こしょう"],["ケチャップ"],["A社ウスターソース","B社ウスターソース"]]
    for n in range(1,19):
        for m in products[n-1]:
            Product.setProduct(m,n)
    Shop.setShop("わいわいマーケット")
    Shop.setShop("併設コンビニ")
    Shop.setShop("地下食料品コーナー")
    stocks=[[[1,500],[2,300],[3,200],[4,100],[5,200],[6,200],[7,230],[8,230],[9,60],[10,65],[11,70],[13,40],[15,30],[16,120],[17,110]
                ,[18,98],[19,250],[20,350],[21,300],[22,200],[23,178],[24,160],[25,150],[26,150],[27,98],[28,220],[29,190]
                ,[30,200],[31,120],[33,180],[34,170],[35,250]]
        ,[[5,250],[25,190],[32,170],[33,210]]
         ,[[1,650],[2,340],[4,100],[5,210],[6,210],[9,50],[11,75],[13,50],[14,50],[16,130],[17,120]
           ,[19,210],[20,360],[21,320],[22,200],[23,180],[25,170],[26,170],[28,230]
                ,[30,220],[31,120],[32,140],[33,190],[34,170],[35,240]]
    ]
    for n in range(1,4):
        for m in stocks[n-1]:
            Stock.setStock(m[0],n,m[1],randint(1,30))

