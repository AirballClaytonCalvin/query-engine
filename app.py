import dash
import dash_design_kit as ddk
from dash import dcc, html, Input, Output, State, callback, no_update
import plotly.express as px
import dash_mantine_components as dmc
from datetime import datetime
import time

from constants import app
# import utils
from dash_iconify import DashIconify


server = app.server

df = px.data.stocks()

print(dash.page_registry.values())
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
                        ddk.Menu(
                            children=[
                                html.Div(
                                    dmc.Menu(
                                        children=[
                                            dmc.MenuTarget(
                                                dmc.Button(
                                                    DashIconify(
                                                        icon="material-symbols:menu"
                                                    ),
                                                    style={
                                                        "border-radius": "4px",
                                                    },
                                                ),
                                            ),
                                            dmc.MenuDropdown(
                                                [
                                                    html.Div(
                                                        dmc.MenuItem(
                                                            [
                                                                f"{page['name']} - {page['path']}",
                                                                DashIconify(
                                                                    icon="tabler:external-link"
                                                                ),
                                                            ],
                                                            href=page["relative_path"],
                                                            target="_blank",
                                                            icon=DashIconify(
                                                                icon="material-symbols:add"
                                                            ),
                                                        ),
                                                    )
                                                    for page in dash.page_registry.values()
                                                ]
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        )
                    ]
                ),
                dash.page_container,
            ],
            show_editor=True,
        )
    )
)



if __name__ == "__main__":
    app.run_server(debug=True)
