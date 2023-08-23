import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("This is our home page"),
        html.Div(
            [
                "Select a city: ",
                dcc.RadioItems(
                    options=["New York City", "Montreal", "San Francisco"],
                    value="Montreal",
                    id="home-input",
                ),
            ]
        ),
        html.Br(),
        html.Div(id="home-output"),
    ]
)


@callback(Output("home-output", "children"), Input("home-input", "value"))
def update_city_selected(input_value):
    return f"You selected: {input_value}"
