

#coding=utf-8
import urllib
import urllib.request
import re

def getHtml(url):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {'name' : 'WHY',
	          'location' : 'SDU',
	          'language' : 'Python' }
	headers = { 'User-Agent' : user_agent }
	data = urllib.parse.urlencode(values)
	proxy_handler = urllib.request.ProxyHandler({'http': 'proxy.zte.com.cn'})
	#opener = urllib.request.build_opener(proxy_handler,data,headers)
	opener = urllib.request.build_opener(proxy_handler)
	r = opener.open(url)
	html = r.read()
	return html

html = getHtml("http://it.zte.com.cn/its/login/ssoLogin.action?rand=1498037115649")
def getImg(html):
    reg =  'src="(.*?\.js)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
print ("%s " % html )

print ("%s " % getImg(html.decode("utf-8")))
imglist = getImg(html.decode("utf-8"))
x=0
for imgurl in imglist:
        if imgurl.find("http") == -1 :
            imgurl = 'http://it.zte.com.cn' + imgurl

        print("%s " %  imgurl)
        urllib.request.urlretrieve(imgurl,'%s' % imgurl[imgurl.rfind("/")+1:])
        x+=1


















