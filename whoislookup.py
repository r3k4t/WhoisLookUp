import os
import sys
os.system("clear")
os.system("figlet -f standard Whois LookUp")
print "Author : Rahat Khan Tusar (RKT)"
print
print "Github : https://github.com/r3k4t"
print 
print "Information : This python program can help to get ip and ipv6 and website information."
print
ip = raw_input("Enter any website IP/Url : ")
os.system("whois {} " .format(ip))

