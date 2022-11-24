import piesparrow as ps

ps.init(filename='hello_world', title='Hello World')

ps.row(
    col1w=50,
    col1=(ps.h3("Column 1 - 50% width")),
    col2w=50,
    col2=(ps.h3("Column 2 - 50% width")),
)
ps.row(
    col1w=25,
    col1=(ps.h3("Column 1 - 25% width")),
    col2w=25,
    col2=(ps.h3("Column 2 - 25% width")),
    col3w=25,
    col3=(ps.h3("Column 3 - 25% width")),
    col4w=25,
    col4=(ps.h3("Column 4 - 25% width"))
)
ps.row(
    col1w=25,
    col1=(ps.h3("Column 1 - 25% width")),
    col2w=25,
    col2=(""),
    col3w=50,
    col3=(ps.h3("Column 3 - 50% width"))
)