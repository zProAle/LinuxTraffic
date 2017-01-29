import os

print("                     Created for Linux Server by zProAle t.me/zProAle\n")

print("Digitare cosa visualizzare: Nginx Log, Apache2 Log, TCP/UDP Log\nPer visualizzare i Log di Nginx, digitare 'Nginx'\nPer Apache 'Apache'\ne invece per i log UDP/TCP 'dos'\n")
log = raw_input("Digitare cosa visualizzare: ")


if log==("apache"):
    os.system("tail -f /var/log/apache2/access.log")

if log==("Apache"):
    os.system("tail -f /var/log/apache2/access.log")

if log==("dos"):
    os.system("netstat -nat | awk '{ print $5}' | cut -d: -f1 | sed -e '/^$/d' | uniq | wc -l")
    os.system("netstat -anp |grep 'tcp\|udp' | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")
if log==("nginx"):
    os.system("tail -f /var/log/nginx/access.log")

if log==("DoS"):
    os.system("netstat -nat | awk '{ print $5}' | cut -d: -f1 | sed -e '/^$/d' | uniq | wc -l")
    os.system("netstat -anp |grep 'tcp\|udp' | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")

if log==("Dos"):
    os.system("netstat -nat | awk '{ print $5}' | cut -d: -f1 | sed -e '/^$/d' | uniq | wc -l")
    os.system("netstat -anp |grep 'tcp\|udp' | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")

if log==("Nginx"):
    os.system("tail -f /var/log/nginx/access.log")
