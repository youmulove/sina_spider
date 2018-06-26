# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaItem(scrapy.Item):
    # 大类的标题 和 url
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    # 小类的标题 和 子url
    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    # 小类目录存储路径
    subFilename = scrapy.Field()

    # 小类下的子链接
    sonUrls = scrapy.Field()
    sonTitle = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
