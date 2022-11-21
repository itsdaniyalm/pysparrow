#Sandboxing the pySparrow library
from yattag import Doc
title = 'Enter your title by declaring psp.title'
message = 'Enter your message by declaring psp.message'
txt = 'Text'

doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')
with tag('html', 'lang="en"'):
    with tag('head'):
        doc.asis('<meta charset="UTF-8">')
        doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        doc.asis('<meta http-equiv="X-UA-Compatible" content="ie=edge">')
        doc.asis('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">')
        doc.asis('<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>')
        with tag('title'):
            text(title)



def h1(txt):
    with tag(h1):
        text(txt)

def compose(filename):
    fileExtension = filename + '.html'
    file = open(fileExtension,'w')
    file.write(doc.getvalue())
    file.close()
