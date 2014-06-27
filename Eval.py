#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def get_size(start_path = 'path'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print get_size()

measure = get_size()

size = int(measure)

GBs = size / 1073741824


if size > 1503238553600:
         
        import smtplib
        import string
        SUBJECT = "Archive too full!"
        TO = "recipient@example.com"
        FROM = "sender@example.com"
        text = "Size is %d Gigabytes" % (GBs)
        BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            text
            ), "\r\n")
        server = smtplib.SMTP('smtp.example.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sender@example.com", "AccountPassword")
        server.sendmail(FROM, [TO], BODY)
 
        from time import gmtime, strftime       
        f = open("sizelog", 'a')
        f.write("Size is %d Gigabytes" % (GBs) + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) +'\n')
        f.close()
        exit()
         
elif size > 1395864371200:
         
        import smtplib
        import string
        SUBJECT = "Archive getting close!"
        TO = "recipient@example.com"
        FROM = "sender@example.com"
        text = "Size is %d Gigabytes" % (GBs)
        BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            text
            ), "\r\n")
        server = smtplib.SMTP('smtp.example.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sender@example.com", "AccountPassword")
        server.sendmail(FROM, [TO], BODY)
 
        from time import gmtime, strftime       
        f = open("sizelog", 'a')
        f.write("Size is %d Gigabytes" % (GBs) + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) +'\n')
        f.close()
        exit()


elif size <= 1395864371200:
         
        from time import gmtime, strftime       
        f = open("sizelog", 'a')
        f.write("Size is %d Gigabytes" % (GBs) + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) +'\n')
        f.close()
        exit()
