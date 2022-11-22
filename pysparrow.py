import pandas as pd

#pySparrow Icon
icon = True

# color pallets
default = ["#ff3399","#cc33ff","#6600cc","#3333cc","#330099","#003399","#3366ff","3399ff","33ccff"]
beach = ["#99ccff","#99ffff","#009999","#66cccc","#99cccc","#cc9966","#ffcc99","#ffcccc","#ffffcc"]
forest = ["#333366","#336666","#cc6633","#993300","#99cc66","#999966","#ff6633","#ff9966","#ffcc66"]
dusktilldawn = ["#9999ff","#6666cc","#666699","#333366","#333333","#663300","#996633","#cc9900","#ffcc00"]
rainbow = ["#666699","#3399cc","#66cc99","#99cc99","#ffff99","#ffcc99","#ff9966","#ff6633","#cc3366"]

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
    '''
    global filen
    filen = filename + '.html'
    global file
    file = open(filen,'w')
    file.write(head)
    if icon==True:
        logoHtml='''
        <a herf="https://itsdaniyalm.com" title="Made with pySparrow" target="_blank" rel="noopener"><img src="https://raw.githubusercontent.com/itsdaniyalm/pysparrow/master/images/pysparrow_icon.png" height="30" align="right"></a>
        </head>
        <body>
        '''
        file = open(filen,'a')
        file.write(logoHtml)
    else:
        logoHtml='''
        </head>
        <body>
        <style>
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

def bar(title, dataframe, xlabel, xdata, ylabel, color=default):
    df = f'pd.{dataframe}'
    x_label = dataframe[xlabel].tolist()
    x_data = dataframe[xdata].tolist()
    chart = f'''
    <div><canvas id='{title}'></canvas></div>
    <script>
        const ctx = document.getElementById('{title}');
      
        new Chart(ctx, {{
          type: 'bar',
          data: {{
            labels: {x_label},
            datasets: [{{
              label: '{ylabel}',
              data: {x_data},
              borderWidth: 1,
              backgroundColor: {color} 
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