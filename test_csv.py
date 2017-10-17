#-*-coding:utf8-*-


import csv

with open('test.csv' , 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['a' , 'b' , 'c'])
    writer.writerows([['真是最棒的',1,3],[1,2,3],[2,3,4]])
