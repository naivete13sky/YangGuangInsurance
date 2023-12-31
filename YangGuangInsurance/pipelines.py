# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import time

import pandas as pd

class YangGuangInsurancePipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        pass
        self.conn = sqlite3.connect("my_scrapy_yangGuangInsurance.db")


    def close_spider(self, spider):
        pass
        self.conn.close()

    def process_item(self, item, spider):
        pass
        # 创建一条记录，通过pandas保存到数据库
        name = item['name']
        bdh = item['bdh']
        sfzh = item['sfzh']
        br_mobile = item['br_mobile']
        pe_name = item['pe_name']
        pe_mobile = item['pe_mobile']
        xd_name = item['xd_name']
        xd_mobile = item['xd_mobile']
        fq_name = item['fq_name']
        fq_mobile = item['fq_mobile']
        mq_name = item['mq_name']
        mq_mobile = item['mq_mobile']
        ts_name = item['ts_name']
        ts_mobile = item['ts_mobile']
        qt_name = item['qt_name']
        qt_mobile = item['qt_mobile']
        new = pd.DataFrame({'姓名': name,
                            '保单号': bdh,
                            '身体证号码': sfzh,
                            '本人手机号': br_mobile,
                            '配偶': pe_name,
                            '配偶手机号': pe_mobile,
                            '兄弟': xd_name,
                            '兄弟手机号': xd_mobile,
                            '父亲': fq_name,
                            '父亲手机号': fq_mobile,
                            '母亲': mq_name,
                            '母亲手机号': mq_mobile,
                            '同事': ts_name,
                            '同事手机号': ts_mobile,
                            '其他': qt_name,
                            '其他手机号': qt_mobile,
                            },
                           index=[1]
                           )  # 自定义索引为：1 ，这里也可以不设置index

        new.to_sql("cc", self.conn, if_exists='append', index=False)


        # 保存网页到临时文件夹
        with open(r'temp\{}.html'.format(str(int(round(time.time() * 1000)))+'_'+name), 'w', encoding='utf8') as f:
            f.write(item['responseText'])


    def create_table(self):
        pass





