import piesparrow as ps

ps.init(filename='01-typography', title='Typograpy Example')

ps.row(
        ps.colxs(align='left', type='card', content=
            ps.h1('This is H1 text')
        +   ps.h2('This is H2 text')
        +   ps.h3('This is H2 text')
        )
)