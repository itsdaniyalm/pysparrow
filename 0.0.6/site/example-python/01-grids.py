import piesparrow as ps

ps.init(filename='01-grids', title='Grids Example')

ps.row(
        ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colmd(align='left', type='card', content=ps.h2('MD Column'))
)
ps.row(
        ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
    +   ps.colxs(align='left', type='card', content=ps.h2('XS Column'))
)
ps.row(
        ps.colmd(align='left', type='card', content=ps.h2('MD Column'))
    +   ps.colmd(align='left', type='card', content=ps.h2('MD Column'))
)
ps.row(
    ps.colxl(type='card', content=ps.h2('XL Column'))
)