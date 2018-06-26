# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from scrapy import signals
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaPipeline(object):
    def process_item(self, item, spider):
        head = item['head']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = head
        filename += ".txt"

        with open(item['subFilename']+'/'+filename, 'w') as fp:
        	fp.write(item['content'])
        return item