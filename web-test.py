import piesparrow as ps

ps.init(filename='hello_world', title='Hello World')


ps.row(
    ps.h1("H1 - Text")+
    ps.h2("H2 - Text")+
    ps.h3("H3 - Text")+
    ps.h4("H4 - Text")+
    ps.p("Paragraph - Text")+
    ps.bold("Bold - Text")
)
