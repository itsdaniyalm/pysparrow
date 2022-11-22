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

def bar(title, dataframe, xlabel, ydata, ylabel, titledisplay = 'true', legenddisplay = 'true', color=default, height = '100', width = '100'):
    df = f'pd.{dataframe}'
    x_label = dataframe[xlabel].tolist()
    y_data = dataframe[ydata].tolist()
    chart = f'''
    <div><canvas id='{title}' width='{width}' height='{height}'></canvas></div>
    <script>
        const ctx = document.getElementById('{title}');
        new Chart(ctx, {{
          type: 'bar',
          data: {{
            labels: {x_label},
            datasets: [{{
              label: '{ylabel}',
              data: {y_data},
              borderWidth: 0,
              backgroundColor: {color} 
            }}]
          }},
          options: {{
            scales: {{
              y: {{
                beginAtZero: true
              }}
            }},
            plugins: {{
                title: {{
                    align: 'start',
                    display: {titledisplay},
                    text: '{title}'
                }},
                legend: {{
                    display: {legenddisplay}
                }}
            }}
          }}
        }});
      </script>
    '''
    return chart

def line(title, dataframe, xlabel, ylabel1, ydata1, ylabel2='null', ydata2='null', ylabel3='null', ydata3='null', ylabel4='null', ydata4='null', ylabel5='null', ydata5='null', titledisplay = 'true', legenddisplay = 'true', color=default, height = '100', width = '100'):
    df = f'pd.{dataframe}'
    x_label = dataframe[xlabel].tolist()
    y_data1 = dataframe[ydata1].tolist()
    try:
        y_data2 = dataframe[ydata2].tolist()
    except:
        y_data2 = 'null'
    try:
        y_data3 = dataframe[ydata3].tolist()
    except:
        y_data3 = 'null'
    try:
        y_data4 = dataframe[ydata4].tolist()
    except:
        y_data4 = 'null'
    try:
        y_data5 = dataframe[ydata5].tolist()
    except:
        y_data5 = 'null'
    chart = f'''
    <div><canvas id='{title}' width='{width}' height='{height}'></canvas></div>
    <script>
        const ctxLine = document.getElementById('{title}');
        new Chart(ctxLine, {{
            type: 'line',
            data: {{
                labels: {x_label},
                datasets: [
                {{
                label: ['{ylabel1}'],
                data: {y_data1},
                borderColor: '{color[0]}' 
                }},
                {{
                label: ['{ylabel2}'],
                data: {y_data2},
                borderColor: '{color[1]}'
                }},
                {{
                label: ['{ylabel3}'],
                data: {y_data3},
                borderColor: '{color[2]}'
                }},
                {{
                label: ['{ylabel4}'],
                data: {y_data4},
                borderColor: '{color[3]}'
                }},
                {{
                label: ['{ylabel5}'],
                data: {y_data5},
                borderColor: '{color[4]}'
                }}
                ]
            }},
            options: {{
                scales: {{
                y: {{
                    beginAtZero: true
                }}
                }},
                plugins: {{
                    title: {{
                        align: 'start',
                        display: {titledisplay},
                        text: '{title}'
                    }},
                    legend: {{
                        display: {legenddisplay}
                    }}
                }}
            }}
            }});
    </script>
    '''
    return chart



def row(col1='False',col2='False',col3='False',col4='False',col5='False', col1w = 100, col2w = 100, col3w = 100, col4w = 100, col5w = 100):
    start = f'''
    <div class = "container">
    <div class = "row">
    '''
    if col1!='False':
        cc1 = f'''<div class="column column-{col1w}">{col1}</div>'''
    else:
        cc1 = ''
    if col2!='False':
        cc2 = f'''<div class="column column-{col2w}">{col2}</div>'''
    else:
        cc2 = ''
    if col3!='False':
        cc3 = f'''<div class="column column-{col3w}">{col3}</div>'''
    else:
        cc3 = ''
    if col4!='False':
        cc4 = f'''<div class="column column-{col4w}">{col4}</div>'''
    else:
        cc4 = ''
    if col5!='False':
        cc5 = f'''<div class="column column-{col5w}">{col5}</div>'''
    else:
        cc5 = ''
    end = '''
    </div>
    </div>
    '''
    html = start+cc1+cc2+cc3+cc4+cc5+end 
    file.write(html)