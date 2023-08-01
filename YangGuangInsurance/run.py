from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'toutiao','-a','keyword=小米10'])
execute(['scrapy', 'crawl', 'yangGuangInsurance'])#yangGuangInsurance是spider文件中的name = 'yangGuangInsurance'指定的。

