icon = True

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

    if icon==True:
        logoHtml='''
        <a herf="https://github.com/itsdaniyalm/pysparrow" title="pySparrow" target="_blank" rel="noopener"><img src="https://raw.githubusercontent.com/itsdaniyalm/pysparrow/master/images/icon.png" width="25" height="25"></a>
        </head>
        <body>
        '''
        file = open(filen,'a')
        file.write(logoHtml)
    else:
        logoHtml='''
        </head>
        <body>
        '''
        file = open(filen,'a')
        file.write(logoHtml)

def h1(txt):
    h1 = f'''
    <h1>{txt}</h1>
    '''
    return h1

def h2(txt):
    h2 = f'''
    <h2>{txt}</h2>
    '''
    return h2

def h3(txt):
    h3 = f'''
    <h3>{txt}</h3>
    '''
    return h3

def h4(txt):
    h4 = f'''
    <h4>{txt}</h4>
    '''
    return h4

def p(txt):
    p = f'''
    <p>{txt}</p>
    '''
    return p

def bar(title, labels, dtLabel, dt):
    chart = f'''
    <div><canvas id='{title}'></canvas></div>
    <script>
        const ctx = document.getElementById('{title}');
      
        new Chart(ctx, {{
          type: 'bar',
          data: {{
            labels: {labels},
            datasets: [{{
              label: '{dtLabel}',
              data: {dt},
              borderWidth: 1,
              backgroundColor: [
          "#F72585",
          "#720987",
          "#3A0CA3",
          "#4361EE",
          "#4CC9F0"
          ]
            }}]
          }},
          options: {{
            scales: {{
              y: {{
                beginAtZero: true
              }}
            }}
          }}
        }});
      </script>
    '''
    return chart

def row(col1='False',col2='False',col3='False',col4='False',col5='False'):
    start = '''
    <div class = "container">
    <div class = "row">
    '''
    if col1!='False':
        cc1 = f'''<div class="column">{col1}</div>'''
    else:
        cc1 = ''
    if col2!='False':
        cc2 = f'''<div class="column">{col2}</div>'''
    else:
        cc2 = ''
    if col3!='False':
        cc3 = f'''<div class="column">{col3}</div>'''
    else:
        cc3 = ''
    if col4!='False':
        cc4 = f'''<div class="column">{col4}</div>'''
    else:
        cc4 = ''
    if col5!='False':
        cc5 = f'''<div class="column">{col5}</div>'''
    else:
        cc5 = ''
    end = '''
    </div>
    </div>
    '''
    html = start+cc1+cc2+cc3+cc4+cc5+end 
    file.write(html)