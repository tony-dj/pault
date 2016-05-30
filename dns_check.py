#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import httplib
import dns.resolver

ip_list = []
appdomain = 'xx'

def get_iplist(domain=''):
    A = dns.resolver.query(domain,'A')
    for i in A.response.answer:
        for j in i.items:
            try:
                ip_list.append(j.address)
            except AttributeError,e:
                print j.to_text()
    return True

def check_ip(ip):
    checkurl = ip + ':80'
    directory = '/'
    getcontent = ''
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)
    
    try:
    	conn.request('GET',directory,headers={'HOST':'www.xueshandai.com'})
    	r = conn.getresponse()
    finally:
        print ip+directory,r.status,r.reason    



if __name__ == '__main__':
    if get_iplist(appdomain) and len(ip_list)>0:
        for ip in ip_list:
            check_ip(ip)
    else:
	print 'dns resolver error'

