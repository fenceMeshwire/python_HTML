#!/usr/bin/env python3

# Python 3.9.5

# changeInlineCSSpropertiesTable.py

# PURPOSE: Change the width and height of a table cell with inline CSS. 
# This is e.g. needed to show the seamless transition of an image <img>.
# Condition: The <img> tag has to be in the same line as the <td> tag in the HTML document.
# Make sure you have the file index.html in your working directory.
# It should contain at least one table <table> with rows <tr> and standard data cells <td>.
# 
# EXAMPLE: Structure see below and index.html
# ...
# <table>
#     <tr>
#         <td colspan=3><img src="" width=10 height="20" alt=""></td>
#     </tr>
# </table>
# ...
# CONCLUSION: It is strongly recommended to reference an external CSS stylesheet.

import os
from pathlib import Path

class DirMgmt:

    def __init__(self):
        pass

    def checkDir(self):
        dirName = '...' # Current working directory goes here
        os.chdir(dirName)
        return Path.cwd()

oCreateDirectories = DirMgmt()
oCreateDirectories.checkDir()

lines = []
strippedLines = []

tdArgument = ''
tdStyle = 'style="padding:0px;margin:0px;border-collapse:collapse;box-sizing:content-box;border-spacing:0px;vertical-align:middle;line-height:0px;'

with open('index.html', 'rt', encoding='utf-8') as html:
    for line in html:
        lines.append(line)

for line in lines:
    line = line.strip('\n')
    line = line.strip('\t')
    strippedLines.append(line)

output_file = 'newHTML.html'

if os.path.exists(os.path.join(Path.cwd(), output_file)):
    os.remove(os.path.join(Path.cwd(), output_file))

def addCSSproperties():
    widthStart = line.find('width')
    heightStart = line.find('height')
    findAltStart = line.find('alt')
    widthEnd = heightStart - 1
    heightEnd = findAltStart - 1
    widthArgument = line[widthStart:widthEnd]
    widthArgument = widthArgument.replace('"', '')
    widthArgument = widthArgument.replace('=', ':')
    heightArgument = line[heightStart:heightEnd]
    heightArgument = heightArgument.replace('"', '')
    heightArgument = heightArgument.replace('=', ':')
    tdArgumentLeft = line.find('><img') - 1
    tdNewArgument = line[0:tdArgumentLeft + 1] + ' ' +  tdStyle + widthArgument + ';' + heightArgument + '"' + line[tdArgumentLeft+1:]
    return tdNewArgument

with open(output_file, 'wt') as fout:
    fout.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Document</title>\n</head>\n<body>\n')
    for line in strippedLines:
        if 'rowspan' in line or 'colspan' in line:
            fout.write(addCSSproperties() + '\n')
        elif '<td>' in line and not 'rowspan' in line or '<td>' in line and not 'colspan' in line:
            fout.write(addCSSproperties() + '\n')
        else:
            fout.write(line + '\n')
    fout.write('</body>\n</html>')
fout.close()
