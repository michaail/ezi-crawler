from scrapy.cmdline import execute

try:
  execute(
    [
      'scrapy',
      'crawl',
      'basic_crawler',
      '-o',
      'out.json',
    ]
  )
except SystemExit:
  pass