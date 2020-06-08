import datetime
import time
import html_downloader,url_manager,commodity_crawed,html_outputer,html_parser,properties_read,str_conver

class SpiderMain(object):
    def __init__(self,comm_type):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser  =  html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.crawed = commodity_crawed.CommodityCrawed(comm_type)

    def craw(self,craw_comms,max_Count):
        for craw_comm in craw_comms:
            #清空缓存区，爬取另一种商品
            self.outputer.pages_commodity = []
            #字符转16进制
            strhex = str_conver.str2hex(craw_comm)
            #爬取页数
            count = 1
            while True:
                    #前30
                    top_30_url = "https://search.jd.com/Search?keyword={}&qrst=1&wq={}&zx=1&page={}&s={}&click=0".format(strhex,strhex,(count*2)-1,((count*2)-2)*30)
                    #后30
                    last_30_url = "https://search.jd.com/s_new.php?keyword={}&qrst=1&wq={}&zx=1&page={}&s={}&scrolling=y&log_id={}&tpl=3_M&isList=0".format(strhex,strhex,count*2,(count*2)-1,time.time())
                    print('----------------------------爬取%s的第%s页----------------------------' %(craw_comm,count))
                    try:
                        #得到当前页前30条的数据
                        html_cont = self.downloader.download(top_30_url)
                        #取得当前页前30条的商品
                        commoditys = self.parser.parse(top_30_url,html_cont)
                        #将当前页的前30条商品存储到list中
                        self.outputer.collect_data(commoditys)
                        # 得到当前页后30条的数据
                        html_cont = self.downloader.download(last_30_url)
                        # 取得当前页后30条的商品
                        commoditys = self.parser.parse(last_30_url, html_cont)
                        # 将当前页的后30条商品存储到list中
                        self.outputer.collect_data(commoditys)
                        #爬取总页数
                        if count == max_Count:
                            break
                    except:
                       print('----------------------------第%s页爬取失败----------------------------' %count)
                    finally:
                        count += 1

            #输出本次爬取的所有结果
            self.outputer.output_html(craw_comm,self.crawed.crawled_list)
            print("----------------------------爬取%s完成：" %craw_comm,end='')
            print("共爬取%s页----------------------------" %(str(count-1)))

#启动程序
if __name__ == "__main__":
    while True:
        start = datetime.datetime.now()
        p = properties_read.Properties('config.properties')
        try:
            # 想要爬取的关键字，从配置文件中取得
            craw_comms = p.getProperties('craw_comms').split(",")
            # 爬取总页数，从配置文件中取得
            MaxCount = int(p.getProperties('MaxCount'))
        except:
            print("config文件不正确---退出----")
        obj_spider = SpiderMain(craw_comms)
        obj_spider.craw(craw_comms, MaxCount)
        end = datetime.datetime.now()
        print('----------------------------总用时%s----------------------------' % str(end - start))
        # 到达设定时间,跳出内循环,执行任务
        while True:
            # 取得当前时间
            now = datetime.datetime.now()
            #跳出内循环,重新爬取数据
            if now.hour == 0 and now.minute == 0:
                break
            else:
                #间隔10分钟爬取一次数据
                for i in range(600, -1, -1):
                    mystr = "----------------------------倒计时" + str(i) + "秒----------------------------"
                    print(mystr, end="")
                    # 删除上一行打印内容
                    print("\b" * (len(mystr) * 2), end="", flush=True)
                    time.sleep(1)
                print('\n')
                start = datetime.datetime.now()
                #循环爬取
                obj_spider.craw(craw_comms, MaxCount)
                end = datetime.datetime.now()
                print('----------------------------总用时%s----------------------------' % str(end - start))




