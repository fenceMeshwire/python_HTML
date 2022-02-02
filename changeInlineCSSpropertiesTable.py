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
# CONCLUSION: It is strongly recommended to reference to an external CSS style sheet.

import os
from pathlib import Path

class DirMgmt:
    def __init__(self):
        pass

    def checkDir(self):
        dirName = 'C:\\...' # Current working directory goes here
        os.chdir(dirName)
        return Path.cwd()

class AddInternalCSS:
    def __init__(self):
        self.lines = []
        self.strippedLines = []
        self.tdArgument = ''
        self.tdStyle = 'style="padding:0px;margin:0px;border-collapse:collapse;box-sizing:content-box;border-spacing:0px;vertical-align:middle;line-height:0px;'
        self.output_file = 'newHTML.html'

    def readHTML(self):
        with open('index.html', 'rt', encoding='utf-8') as html:
            for line in html:
                self.lines.append(line)
        # Remove newline and tabulator:
        for line in self.lines:
            line = line.strip('\n')
            line = line.strip('\t')
            self.strippedLines.append(line)
        # Remove the output file, if it exists:
        if os.path.exists(os.path.join(Path.cwd(), self.output_file)):
            os.remove(os.path.join(Path.cwd(), self.output_file))

    def addCSSproperties(self, line):
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
        tdNewArgument = line[0:tdArgumentLeft + 1] + ' ' +  self.tdStyle + widthArgument + ';' + heightArgument + ';"' + line[tdArgumentLeft+1:]
        return tdNewArgument
    
    def writeCSS(self):
        with open(self.output_file, 'wt') as fout:
            for line in self.strippedLines:
                if 'rowspan' in line or 'colspan' in line:
                    fout.write(self.addCSSproperties(line) + '\n')
                elif '<td>' in line and not 'rowspan' in line or '<td>' in line and not 'colspan' in line:
                    fout.write(self.addCSSproperties(line) + '\n')
                else:
                    fout.write(line + '\n')
        fout.close()

# Change working directory:
oCreateDirectories = DirMgmt()
oCreateDirectories.checkDir()
# Perform internal CSS adaptation:
oAddInternalCSS = AddInternalCSS()
oAddInternalCSS.readHTML()
oAddInternalCSS.writeCSS()
