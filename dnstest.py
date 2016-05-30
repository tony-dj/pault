#!/usr/bin/env python
#
import dns.resolver


def mx(domain):
    MX = dns.resolver.query(domain,'MX')
    for i in MX:
        print 'MX preference:%s' % i.preference,'mail exchanger:%s' % i.exchange
    
def a(domain):
        A = dns.resolver.query(domain,'A')
        for i in A.response.answer:
            for j in i.items:
                try:
                    print j.address
                except AttributeError,e:
                    print e

def c(domain):
        cname = dns.resolver.query(domain,'CNAME')
        for i in cname.response.answer:
            for j in i.items:
                print j.to_text()

def ns(domain):
    NS = dns.resolver.query(domain,'NS')
    for i in NS.response.answer:
            for j in i.items:
                print j.to_text()


if __name__ == '__main__':
    domain = raw_input('\033[32mPlease input an domain: \033[m')
    
    a(domain)
    c(domain)
    mx(domain)
    ns(domain)


