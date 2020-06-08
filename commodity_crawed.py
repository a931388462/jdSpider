class CommodityCrawed:
    # 避免重复爬取，维护此列表
    crawled_list = {}

    def __init__(self,comm_type):
        self.crawled_list = {}
        for type in comm_type:
            self.crawled_list[type] = set()

