#!/usr/bin/env python
#
from IPy import IP

ip_s = raw_input('\033[32mPlease input IP or net-range:\033[m')
ips = IP(ip_s)

if ips.len() > 1:
    print "net is %s" % ips.net()
    print "netmask is %s" % ips.netmask()
    print "broadcast is %s" % ips.broadcast()
    print "reverseName is %s" % ips.reverseNames()[0]
    print "subnet is %s" % ips.len()
else:
    print "reverseName is %s" % ips.reverseNames()[0]

print "hexadecimal is %s" % ips.strHex()
print "binary is %s" % ips.strBin()
print "net type is %s" % ips.iptype()


