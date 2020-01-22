#爬取网页的通用代码框架－时间

import requests
import time

def getHTML(url):
      try:
            r = requests.get(url)
            r.raise_for_status()  #如果不是200，引发HTTP返回异常
            return r
      except:
            return "异常产生"

if __name__=="__main__":
      start_time=time.perf_counter()
      url=input("网站是：")
      for i in range(100):
            getHTML(url)
      end_time=time.perf_counter()
      print("爬100次{}的时间是{}秒".format(url, end_time-start_time))
