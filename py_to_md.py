#!/usr/bin/python
import pdfkit
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="Input python File")
#parser.add_argument('-o', '--output', help="Output PDF File")
args = parser.parse_args()

fileName = args.input
output_pdf = fileName.replace('.py','.pdf')
lineList = [line.rstrip('\n') for line in open(fileName)]
# print lineList

def style(string):
    text_style = string.startswith('#')
    code_style = not string.startswith('#')
    start = string.startswith('# start')
    end = string.startswith('# end')
    if text_style:
        if start:
            return """```python"""
        elif end:
            return """```"""
        return string[1:]
    else:
        return '    ' + string

L = []
for i in lineList:
    L.append(style(i))

# print L

msg = '\n'.join(L)
# print msg
md_file = 'out.md'
f = open(md_file,'w')
f.write(msg)
f.close()
print 'MD FILE HAS BEEN GENERATED'
print 'OPENING MD FILE WITH GRIP'
grip = 'grip out.md localhost:8971 &'
os.system(grip)
time.sleep(10)
cmd2 = 'wkhtmltopdf http://localhost:8971 '+output_pdf
print 'GENERATING PDF FILE'
os.system(cmd2)
time.sleep(5)
os.system('killall grip')
print 'PDF FILE IS SAVED AS '+output_pdf
kill = """kill $(ps -eo pid,command | grep grip | grep -v grep | awk '{print $1}'"""


