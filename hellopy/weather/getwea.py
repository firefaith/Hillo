# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
 
def main():
    query = "sunshine"
    dlist = []
    for i in range(18,32,1):
      dlist.append("201801{}".format(i))
    dlist.append("20180201")
    for d in dlist:
      getweather(d)
 
def getweather(date):
    #search_type: Web, Image, News, Video
    key= 'YOUR_API_KEY'
    #query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'http://api.k780.com:88/?app=weather.history&weaid=37&date='+date+'&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    #print json_result
    result_list = json_result['result']
    res = []
    for one in result_list:
      arr = []
      t = one['uptime']
      tem = one['temperature'].split(u"℃")[0]
      hum = one['humidity'].split("%")[0]
      arr=[t,tem,hum]
      #print t,tem,hum
      print ",".join(arr)
      res.append(arr)
    return res
    #return result_list
 
if __name__ == "__main__":
    main()
