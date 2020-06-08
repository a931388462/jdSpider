#用作定义商品
class Commodity(object):
    # 初始化中给对象属性赋值
    def __init__(self,commID, commName, price, evaluate,purchasingIndex,shopName):
        # 商品id
        self.commID = commID
        #商品名
        self.commName = commName
        #价格
        self.price = price
        #评价
        self.evaluate = evaluate
        #选购指数
        self.purchasingIndex = purchasingIndex
        #店铺名
        self.shopName = shopName
