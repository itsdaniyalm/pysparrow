import pandas as pd
import piesparrow as ps

ps.init(filename='webtest', title='web test')

ps.row(
        ps.h1('H1 Text')
    +   ps.h2('H2 Text')
    +   ps.h3('H3 Text')
    +   ps.h4('H4 Text')
    +   ps.p('Paragraph text')
    +   ps.bold('Strong Text')
    +   ps.link(target='#',label='link')
)