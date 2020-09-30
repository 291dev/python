f = open('text.txt', 'w')
f.write('Test \n')
print('my', 'name', 'is', 'fukui', sep='#', file=f)
f.close()

with open('text2.txt', 'w') as f:
  f.write('Test\n')


with open('text.txt', 'r') as f:
  while True:
    chunk = 2
    line = f.readline()
    chunkedstr = f.read(chunk)
    print('line: ',line)
    print('chunked: ', chunkedstr)
    if not chunkedstr:
      break



s = """\
XXXXXX
YYYYYY
ZZZZZZ
"""
with open('test.txt', 'w+') as f:
  f.write(s)
  f.seek(0)
  print(f.read())

import string

s = """\

Hi $name.

$contents

Have a good day
"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents='How do you do')
print(contents)

import csv

with open('test.csv' , 'w') as csv_file:
  fieldnames = ['Name', 'Count']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'Name': 'Fukui', 'Count':1})
  writer.writerow({'Name': 'Fukuda', 'Count':2})


with open('test.csv', 'r') as csv_file:
  reader = csv.DictReader(csv_file)
  print(reader)
  for row in reader:
    print(row['Name'], row['Count'])


import subprocess

r = subprocess.run('ls -al', shell=True)
print(r.returncode)

import datetime
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y'))