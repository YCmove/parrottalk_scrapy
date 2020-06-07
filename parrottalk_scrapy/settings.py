# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'parrottalk_scrapy'

SPIDER_MODULES = ['parrottalk_scrapy.spiders']
NEWSPIDER_MODULE = 'parrottalk_scrapy.spiders'

INDEX_URL = 'https://www.parrottalks.com/'
LOGIN_URL = 'https://www.parrottalks.com/#/main/login'
LOGIN_API = 'https://www.parrottalks.com/api/login'

CATELOG_API = 'https://www.parrottalks.com/api/catalogs?__rnd=1562310364589&note_only=1'
BOOK_URL = 'https://www.parrottalks.com/#/note/book'

COOKIES = {'__utma': '173579682.1846711591.1551106388.1551106388.1551106388.1', '__utmz': '173579682.1551106388.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 'fbm_399939833405464': 'base_domain=.parrottalks.com', 'amplitude_id_03f1549bb309566c3700c5277b015081parrottalks.com': 'eyJkZXZpY2VJZCI6IjNjNDAxYmZjLWJiOTEtNGMyNy1hZTgzLWRiZWYwYTRiMDMwNVIiLCJ1c2VySWQiOiIxMTA3ODkiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1NTExMDYzODg5ODYsImxhc3RFdmVudFRpbWUiOjE1NTExMTAzODkxNDYsImV2ZW50SWQiOjI1LCJpZGVudGlmeUlkIjo1NSwic2VxdWVuY2VOdW1iZXIiOjgwfQ==', 'parrottalks': '18e51eed9548f97c2ca57ca5f55e46874558de0b%2BUcop18uCr5tEReKGyl9Qq7wRMstuRoHHIJEhYSdM', 'session_payload': 'b66a8192e04425f8e5fb6f9dce5c8ae678de3e55%2B%2BvFs%2BRc%2BOrMiedd5l45CFuxRmiaQPJY3ZngFeo%2FayT9ymXLxpPtFoVUszAABkyV%2FsEWIhf7HcqzKR73Yyb1RXxHIP%2B0v%2Bh8uANpYZum8KyHU7cmfRTP5Y4QyUVVI9K64r1hI2XR5Bct7DyMTmVqYgsk8eu1cSrTjh5NIlHtiEHcBk7l812rOWBHFxFNUMwA9PeHsKzgcmPpZcjMUpeftMN3Lrsnb8MxtCSKkX8h7t%2FxxdxhhJ2HxaV%2Fj0ybO2gXMHKLIjHZM9arNwrU00I%2B2o81J1tO8uvaUnv80B2H9vCf4TMkwmOPsd4432%2BzxgR%2FqbMfIgYyOoxAlPc5Xkl6hCg%3D%3D', 'ajs_user_id': 'null', 'ajs_anonymous_id': '%2282505b30-5b0c-491f-9c38-56c4cb39a37b%22', 'fbsr_399939833405464': 'hNxvaDz8PnhqjqBq4ue1Yw_kuXN8tIh008sB2hPJ4QU.eyJ1c2VyX2lkIjoiMjI2NzE1NTI4NjYzMzA1MyIsImNvZGUiOiJBUURGR2VVelFDRzZvWl9NX2ZUdkt4NkJWS2hDM2ltUWExVlJXRUxBVVJjUjBXZTZVQzJwWnNFM3ZVLUtlRUcybG9vWVE2SkUtQmg4WDBObDV6c0dtTmF5X3R2WnhfTm9wQTdDS3pDRTRwRTB3d0otN2dUV0Iyc0dxdHJwbF9VMVFqNGJlNnNtVEdZSFBSWmkxU1UwdGwyMVk4QVhEZ0dOeDFnVDNLXzBFbkZhU2ZFQ0VrRVNJR0FtOFlTUXFwUjR3MFJPM3E3SlE2Rk9MSUhtTkQ3RHBjWTJIMGlSbDFVT0g4Z2RVa1N5S2ZXTW5ab3ZjSDRMajgwNmZJN3BneUtZU0RaS3loQnpKU0hsaFNGTDJCa1RRZEZNQVpIaUVubGR6a0ZYeHNZRnF4SlVrZE1qTWpERlVWZTJMWWxRUkc4MjBXZFZ1REQxb3BiN2FQYTJwQTcxbE1QSCIsIm9hdXRoX3Rva2VuIjoiRUFBRnJ2alpCem9CZ0JBSk9sQVFDZnFraVZ1UHZiVGJaQjhqRWNoNmloYjAzSFh0dXBOWFpBZTlIa2F4T1Z0ck5mclUxRFIxWXlDcE1GRTRlN0xLTmVUUVY1WUFYMk9vdjlaQ0tPREx1dndtQUJvalNiOGlPV3hGWWZXUUx2MlpBR0hiMDRLdjNaQkRrTFpCb0VjUnRTWkE5cEoxYlpBWTE0Tm1Md0NDeGpMU0Qya0NOSlUzNUlJVXhHTHZiSzFPSmVQbE5aQ3BQdTNzWkE5NktBWkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTYyMzA3MTA3fQ'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
