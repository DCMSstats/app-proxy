import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Iframe(
        src=f'https://gva-nowcast-complete-data-dot-dcms-statistics.nw.r.appspot.com/',
        height=460,
        width=1450, style={
            'backgroundColor': '#494949',
            'border': 'none',
            'frameBorder': 'none',
            'frameborder': 'none'
        }
)])



if __name__ == '__main__':

    #Uncomment this to host locally useful for testing
    app.run_server()#debug=True)

    #app.run_server(host='0.0.0.0', port=8080, use_reloader=True)
