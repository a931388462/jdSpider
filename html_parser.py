from bs4 import BeautifulSoup
import re
from commodity import Commodity

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        #此方法暂时不用
        return ""


    def _get_new_data(self ,soup):
        commoditys = []
        #爬取的前30件商品
        commo_nodes = soup.findAll('li',class_ = re.compile(r'.*gl-item.*'))
        for commo_node in commo_nodes:
            commID = commo_node['data-sku']
            commName = commo_node.find('div',class_ = re.compile(r'.*p-name p-name-type-2.*'))\
                .find('em').get_text()
            price = commo_node.find('div', class_=re.compile(r'.*p-price.*'))\
                .find('i').get_text()
            evaluate = commo_node.find('div', class_=re.compile(r'.*p-commit.*'))\
                .find('strong').find('a').get_text()
            #推荐指数有可能不存在
            try:
                purchasingIndex = commo_node.find('div', class_=re.compile(r'.*p-commit.*'))\
                    .find('span').find('em').get_text()
            except:
                purchasingIndex="-"
            # 店铺有可能不存在
            try:
                shopName = commo_node.find('div', class_=re.compile(r'.*p-shop.*'))\
                    .find('a').get_text()
            except:
                shopName = "-"
            #是否为京东自营
            if self.isJdOwn(commo_node):
                print("\t商品id:"+commID+"\t商品名:"+commName+"\t价格:"+price)
                commodity = Commodity(commID, commName, price, evaluate, purchasingIndex, shopName)
                commoditys.append(commodity)

        # 爬取的内容
        return commoditys


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf—8')
        commoditys = self._get_new_data(soup)
        return commoditys


    def isJdOwn(self,commo_node):
        try:
            ss = commo_node.find('div', class_=re.compile(r'.*p-icons.*')).find('i').get_text()
        except:
            ss = ''
        if ss == '自营':
            return True
        else:
            return False





