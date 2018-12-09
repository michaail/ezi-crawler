from scrapy.cmdline import execute

try:
  execute(
    [
      'scrapy',
      'crawl',
      'test_crawler',
      '-o',
      'out.json',
    ]
  )
except SystemExit:
  pass