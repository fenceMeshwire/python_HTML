#!/usr/bin/env python3

# Python 3.9.5

# webSiteAutomation.py

# Purpose: Make updates to a current HTML document

# Change working directory for the actual OS:
def changePath():
    from pathlib import Path
    import os, platform

    if os.name == 'posix' or platform.system() == 'Darwin': 
        p = '/Users/...'
    if os.name == 'nt' or platform.system() == 'Windows': 
        p = 'C:\\...'

    os.chdir(p) # Change the current working directory.
    Path.cwd() # Check current working directory.

changePath()

def startHTML(title):
    docType = '<!DOCTYPE html>' 
    htmlStart = '<html lang="en">' 
    # HTML head:
    headHTML = '<head>'
    headHTML += '\n\t' + '<meta charset="UTF-8">'
    headHTML += '\n\t' + '<title>' + title + '</title>' 
    headHTML += '\n' + '</head>' + '\n'
    start = docType 
    start += '\n' + htmlStart
    start += '\n' + headHTML
    return start

def makeBody(timeDate):
    # HTML code for divisions:
    division1 = '<div>This is the placeholder for DIVISION 1</div>'
    division2 = '<div>This is the placeholder for DIVISION 2</div>'
    division3 = '<div>This is the placeholder for DIVISION 3</div>'
    # Structure for HTML body:
    htmlBody = '<body>'
    htmlBody += '\n\t' + timeDate
    htmlBody += '\n\t' + division1
    htmlBody += '\n\t' + division2
    htmlBody += '\n\t' + division3
    htmlBody += '\n' + '</body>'
    return htmlBody

def makeTimeDate():
    # Structure for date and time function:
    jsScript = ''
    jsScript += "<script type='text/javascript'>"
    jsScript += "\n\t\t" + "var myDate = new Date();"
    jsScript += "\n\t\t" + "var myDay = myDate.getDay();"
    jsScript += "\n\t\t" + "var day = myDate.getUTCDay();"
    jsScript += "\n\t\t" + "var month = myDate.getUTCMonth();"
    jsScript += "\n\t\t" + "var year = myDate.getUTCFullYear();"
    jsScript += "\n\t\t" + "var hours = myDate.getHours();"
    jsScript += "\n\t\t" + "var minutes = myDate.getMinutes();"
    jsScript += "\n\t\t" + "var seconds = myDate.getSeconds();"
    jsScript += "\n\t\t" + 'day = day < 10 ? "0" + day : day;'
    jsScript += "\n\t\t" + 'minutes = minutes < 10 ? "0" + minutes : minutes;'
    jsScript += "\n\t\t" + 'seconds = seconds < 10 ? "0" + seconds : seconds;'
    jsScript += "\n\t\t" + 'var myTime = hours + ":" + minutes + ":" + seconds;'
    jsScript += "\n\t\t" + "var weekday = [\n\t\t\t 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' \n\t\t\t];"
    jsScript += "\n\t\t" + 'document.write("Current date: " + weekday[myDay] + "," + " " + day + "/" + month + "/" + year);'
    jsScript += "\n\t\t" + 'document.write("<br/>");'
    jsScript += "\n\t\t" + 'document.write("Current time: " + myTime);'
    jsScript += "\n\t\t" + 'document.write("<br/>");'
    jsScript += "\n\t\t" + 'document.write("<br/>");'
    jsScript += '\n\t' + '</script>'
    return jsScript

def makeEnd():
    # Closing HTML tag:
    end = '\n' + '</html>'
    return end

title = "This is a document"

start = startHTML(title)
timeDate = makeTimeDate() # JavaScript date and time function.
body = makeBody(timeDate) # Integration into the HTML body.
end = makeEnd()

print(body)

basicHTML = start + body + end

# Output of the HTML document:
with open('basicHTML.html', 'wt', encoding='utf-8') as outFile:
    outFile.write(basicHTML)
outFile.close()
