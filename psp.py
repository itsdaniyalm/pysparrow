
def init(filename, title):
    head = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body>
    '''
    global filen
    filen = filename + '.html'
    global file
    file = open(filen,'w')
    file.write(head)

def h1(txt):
    h1 = f'''
    <h1>{txt}</h1>
    '''
    file.write(h1)


def row(cont1,cont2,cont3,cont4,cont5,col1=False,col2=False,col3=False,col4=False,col5=False):
    if col1==True:
        cc1 = f'''{cont1}'''
    else
        cc1 = ''
