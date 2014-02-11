# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20131215 Firefox/24.0 Iceweasel/24.2.0'

ITEM_PIPELINES = ['crawler.pipelines.SqlitePipeline']
RETRY_TIMES = 100
