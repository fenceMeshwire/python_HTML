#!/usr/bin/env python3

# Purpose: Make updates to a current HTML document

# Change working directory for the actual OS:

class ChangePWD:
    def changePath(self):
        from pathlib import Path
        import os, platform

        if os.name == 'posix' or platform.system() == 'Darwin': 
            p = '/Users/...'
        if os.name == 'nt' or platform.system() == 'Windows': 
            p = 'C:\\...'

        os.chdir(p) # Change the current working directory.
        Path.cwd() # Check current working directory.

class MakeFiles:
    def __init__(self):
        self.title = "This is a document"

    def startHTML(self):
        docType = '<!DOCTYPE html>' 
        htmlStart = '<html lang="de">' 
        # HTML head:
        headHTML = '<head>'
        headHTML += '\n\t' + '<meta charset="UTF-8">'
        headHTML += '\n\t' + '<link href="style.css" rel="stylesheet"></link>'
        headHTML += '\n\t' + '<title>' + self.title + '</title>' 
        headHTML += '\n' + '</head>' + '\n'
        start = docType 
        start += '\n' + htmlStart
        start += '\n' + headHTML
        return start

    def makeBody(self):
        # HTML code for divisions:
        division1 = '<div>This is the placeholder for DIVISION 1</div>'
        division2 = '<div>This is the placeholder for DIVISION 2</div>'
        division3 = '<div>This is the placeholder for DIVISION 3</div>'
        # Structure for HTML body:
        htmlBody = '<body>'
        htmlBody += '\n\t' + '<script src="code.js"></script>'
        htmlBody += '\n\t' + '<details>'
        htmlBody += '\n\t' + '<summary>Further information</summary>'
        htmlBody += '\n\t' + '<br>'
        htmlBody += '\n\t' + division1
        htmlBody += '\n\t' + division2
        htmlBody += '\n\t' + division3
        htmlBody += '\n\t' + '</details>'
        htmlBody += '\n' + '</body>'
        return htmlBody

    def makeScript(self):
        # Structure for date and time function:
        jsScript = ''
        jsScript += "var myDate = new Date();"
        jsScript += "\n" + "var myDay = myDate.getDay();"
        jsScript += "\n" + "var day = myDate.getDate();"
        jsScript += "\n" + "var month = myDate.getMonth() + 1;"
        jsScript += "\n" + "var year = myDate.getFullYear();"
        jsScript += "\n" + "var hours = myDate.getHours();"
        jsScript += "\n" + "var minutes = myDate.getMinutes();"
        jsScript += "\n" + "var seconds = myDate.getSeconds();"
        jsScript += "\n" + 'month = month < 10 ? "0" + month : month;'
        jsScript += "\n" + 'day = day < 10 ? "0" + day : day;'
        jsScript += "\n" + 'minutes = minutes < 10 ? "0" + minutes : minutes;'
        jsScript += "\n" + 'seconds = seconds < 10 ? "0" + seconds : seconds;'
        jsScript += "\n" + 'var myTime = hours + ":" + minutes + ":" + seconds;'
        jsScript += "\n" + "var weekday = [\n\t\t\t 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' \n\t\t\t];"
        jsScript += "\n" + 'document.write("Current date (ISO 8601): " + year + "/" + month + "/" + day);'
        jsScript += "\n" + 'document.write("<br/>");'
        jsScript += "\n" + 'document.write("Current time: " + myTime);'
        jsScript += "\n" + 'document.write("<br/>");'
        jsScript += "\n" + 'document.write("Weekday: " + weekday[myDay]);'
        jsScript += "\n" + 'document.write("<br/><br/>");'
        with open('code.js', 'wt', encoding='utf-8') as outFile:
            outFile.write(jsScript)
        outFile.close()

    def makeStylesheet(self):
        # Structure for date and time function:
        style = """
        body {
        background-color:#33D4FF;
        }"""
        with open('style.css', 'wt', encoding='utf-8') as outFile:
            outFile.write(style)
        outFile.close()

    def makeEnd(self):
        # Closing HTML tag:
        end = '\n' + '</html>'
        return end

oChangePWD = ChangePWD()
oChangePWD.changePath()

oMakeFiles = MakeFiles()

start = oMakeFiles.startHTML()
body = oMakeFiles.makeBody() # Integration into the HTML body.
end = oMakeFiles.makeEnd()

oMakeFiles.makeScript() # JavaScript date and time function.
oMakeFiles.makeStylesheet() # Make CSS style sheet

basicHTML = start + body + end

# Output of the HTML document:
with open('basicHTML.html', 'wt', encoding='utf-8') as outFile:
    outFile.write(basicHTML)
outFile.close()
