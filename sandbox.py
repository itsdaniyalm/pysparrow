import piesparrow as psp



psp.init(filename='columns', title='Columns Test')

psp.row(
    col1 = psp.h3('1st Column') + psp.p('One column example')
)

psp.row(
    col1 = psp.h3('1st Column') + psp.p('Two columns example'),
    col2 = psp.h3('2nd Column') + psp.p('Two columns example')
)
psp.row(
    col1 = psp.h3('1st Column') + psp.p('Three columns example'),
    col2 = psp.h3('2nd Column') + psp.p('Three columns example'),
    col3 = psp.h3('3rd Column') + psp.p('Three columns example')
)