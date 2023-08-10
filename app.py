import dash
import dash_design_kit as ddk
from dash import dcc, html, Input, Output, State, callback, no_update
import plotly.express as px
import dash_mantine_components as dmc
from datetime import datetime
import time

from constants import app
import utils
from dash_iconify import DashIconify


server = app.server

df = px.data.stocks()

app.layout = dmc.MantineProvider(
    dmc.NotificationsProvider(
        ddk.App(
            [
                ddk.Header(
                    [
                        ddk.Logo(src=app.get_asset_url("bofa_logo.png")),
                        ddk.Title("Bank of America Query Engine"),
                        html.Div(
                            dmc.Badge(
                                "latest deployment: "
                                + datetime.today().strftime("%Y-%m-%d"),
                                size="sm",
                                fullWidth=False,
                            ),
                            style={"width": "50px"},
                        ),
                        ddk.Menu(utils.menu_utils.default_menu()),
                    ]
                ),
                dmc.LoadingOverlay(
                    ddk.Row(
                        children=[
                            html.Div(id="overlay-placeholder"),
                            html.Div(id="notification-provider"),
                            ddk.Card(
                                width=40,
                                children=[
                                    html.Div(
                                        "Construct You Query",
                                        style={"textAlign": "center"},
                                    ),
                                    dmc.Space(h=15),
                                    dmc.Divider(
                                        label="Team Name", labelPosition="center"
                                    ),
                                    dmc.Space(h=15),
                                    ddk.Block(
                                        children=dmc.TextInput(
                                            id="team_text",
                                            placeholder="Team Alpha",
                                            error=True,
                                        ),
                                    ),
                                    dmc.Space(h=15),
                                    dmc.Divider(
                                        label="Project/Use Case",
                                        labelPosition="center",
                                    ),
                                    dmc.Space(h=15),
                                    ddk.Block(
                                        children=dmc.Textarea(
                                            id="project_text",
                                            placeholder="",
                                            description="Please describe your usecase in detail",
                                        ),
                                    ),
                                    dmc.Space(h=15),
                                    dmc.Divider(
                                        label="Select a Project Manager",
                                        labelPosition="center",
                                    ),
                                    dmc.Space(h=15),
                                    dcc.Dropdown(
                                        id="manager_dropdown",
                                        options=[
                                            "Manager1",
                                            "Manager2",
                                            "Manager3",
                                        ],
                                        value="Manager1",
                                        multi=True,
                                        searchable=True,
                                    ),
                                    dmc.Space(h=15),
                                    dmc.Divider(
                                        label="Storage Capacity Required",
                                        labelPosition="center",
                                    ),
                                    dmc.Space(h=15),
                                    dmc.NumberInput(
                                        id="storage_int",
                                        description="From 0 to 10",
                                        value=0,
                                        min=0,
                                        max=10,
                                        step=1,
                                        # style={"width": 250},
                                    ),
                                    dmc.Space(h=15),
                                    dmc.Divider(
                                        label="Select your required tools",
                                        labelPosition="center",
                                    ),
                                    dmc.Space(h=15),
                                    dcc.Checklist(
                                        id="tools_checkbox",
                                        options=["Tool 1", "Tool 2", "Tool 3"],
                                        inline=True,
                                        style={
                                            "display": "flex",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                        },
                                    ),
                                    dmc.Space(h=30),
                                    html.Div(
                                        children=[
                                            dmc.Button(
                                                "Send Query",
                                                id="query_button",
                                                leftIcon=DashIconify(
                                                    icon="fluent:database-plug-connected-20-filled"
                                                ),
                                            ),
                                        ],
                                        style={
                                            "display": "flex",
                                            "justifyContent": "center",
                                            "alignItems": "center",
                                        },
                                    ),
                                ],
                            ),
                            ddk.Card(
                                width=60,
                                children=[
                                    html.Div("Results", style={"textAlign": "center"}),
                                    dmc.Space(h=15),
                                    dmc.Divider(),
                                    dmc.Space(h=15),
                                    ddk.Block(
                                        id="table_div",
                                        children=utils.chart_utils.generate_table(df),
                                    ),
                                ],
                            ),
                        ]
                    ),
                ),
            ],
            show_editor=True,
        )
    )
)


@callback(
    Output("table_div", "children"),
    Output("notification-provider", "children"),
    Output("overlay-placeholder", "children"),
    State("team_text", "value"),
    State("project_text", "value"),
    State("manager_dropdown", "value"),
    State("storage_int", "value"),
    State("tools_checkbox", "value"),
    Input("query_button", "n_clicks"),
    prevent_initial_call=True,
)
def run_query(team, project, manager, storage, tools, _):

    ### This is where we want to execute the query ###
    # We will also want to condier caching and state saving depending on the use case
    # Most Dash components support a property called persistance=True which will save the users selections
    # https://dash.plotly.com/persistence

    # you can also use the snapshot engine to save queries and built reports from them
    time.sleep(2)
    return (
        utils.chart_utils.generate_table(df),
        dmc.Notification(
            title="Query Submitted!",
            id="simple-notify",
            action="show",
            message="Notifications in Dash, Awesome!",
            icon=DashIconify(icon="ic:round-celebration"),
        ),
        no_update,
    )


if __name__ == "__main__":
    app.run_server(debug=True)
