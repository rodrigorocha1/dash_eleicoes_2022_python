
import dash
from dash import html
app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1('Teste Nisso aquiaaasss444545454ssss')
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
