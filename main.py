import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Iframe(
    src=f'https://gva-nowcast-complete-data-dot-dcms-statistics.nw.r.appspot.com/',
    height=700, width=1200, style={'backgroundColor': '#494949', }
)])


#if __name__ == '__main__':
#    app.run_server(debug=True)
