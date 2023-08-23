import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("This is our Archive page"),
        html.Div(
            [
                "Select a city: ",
                dcc.RadioItems(
                    options=["New York City", "Montreal", "San Francisco"],
                    value="Montreal",
                    id="archive-input",
                ),
            ]
        ),
        html.Br(),
        html.Div(id="archive-output"),
    ]
)


@callback(Output("archive-output", "children"), Input("archive-input", "value"))
def update_city_selected(input_value):
    return f"You selected: {input_value}"
