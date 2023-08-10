from dash import (
    html,
    Input,
    Output,
    State,
    MATCH,
    ctx,
    no_update,
    callback,
    dcc,
)
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import flask

import dash_design_kit as ddk

# import dash_snapshots
# import dash_enterprise_auth as dae

from constants import app


# def default_archive_table():
# """
# The out-of-the-box archive table is okay, but not great. Here, we construct our own and
# distinguish between app views and reports, which is convienent.
# Anyways, if you ever want to modify it yourself, this should make that process quicker.
# """
# keys = dash_snapshots.constants.KEYS
# # Get a list of all snapshots
# snapshot_ids = snap.snapshot_list()

# # declare the names of our columns
# columns = [
#     {"id": keys["snapshot_id"], "name": "Live"},
#     {
#         "id": keys["pdf"],
#         "name": "PDF",
#     },
#     {"id": "report_type", "name": "Type"},
#     {"id": keys["username"], "name": "Created By"},
#     {"id": keys["created_time"], "name": "Created On"},
# ]

# # initialize an empty data dictionary where we append each row of the table to
# data = []

# # loop though each snapshot for the list and build our data set to be used in the datatable
# for idx, snapshot_id in enumerate(snapshot_ids):
#     row = {}
#     for col in columns:
#         cell = snap.meta_get(snapshot_id, col["id"], "")
#         # magic that formats the cells
#         if col["id"] == dash_snapshots.constants.KEYS["snapshot_id"]:
#             cell = "[{}]({})".format(
#                 "View", app.get_relative_path("/{}".format(snapshot_id))
#             )
#             col["presentation"] = "markdown"
#         elif col["id"] == dash_snapshots.constants.KEYS["pdf"]:
#             exists = snap.meta_get(snapshot_id, col["id"], "")
#             if exists:
#                 cell = "[{}]({})".format(
#                     "Download",
#                     app.get_relative_path("/{}.pdf".format(snapshot_id)),
#                 )
#                 col["presentation"] = "markdown"
#             elif not exists:
#                 cell = "Pending"
#                 col["presentation"] = "markdown"
#         elif col["id"] == "id":
#             cell = idx
#             col["presentation"] = "markdown"

#         row[col["id"]] = cell

#     data.append(row)

# for row in data:
#     if row["report_type"] == "View":
#         row["pdf"] = "N/A"

# return ddk.DataTable(
#     columns=columns,
#     data=data,
#     page_current=0,
#     page_size=15,
#     filter_action="native",
#     page_action="native",
#     cell_selectable=False,
#     style_as_list_view=True,
#     style_cell={"textAlign": "left"},
#     style_header={"fontWeight": "bold", "textAlign": "left"},
#     css=[
#         dict(selector=".cell-markdown p", rule="margin: 0;"),
#         dict(selector=".dash-filter input", rule="text-align: left;"),
#     ],
# )


def archive_table_modal():
    return [
        # default_archive_table(),
        dmc.Space(h=20),
        dmc.Group(
            [
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id={"type": "modal-close", "contents": "views"},
                ),
            ],
            position="right",
        ),
    ]


def report_modal():
    return [
        dmc.TextInput(label="Report title", value=app.title, id="report-title"),
        dmc.Space(h=20),
        dmc.Textarea(
            label="Report description",
            description="Notes to add the report. Supports Markdown syntax.",
            id="report-description",
        ),
        dmc.Space(h=20),
        dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ["vertical", "horizontal"]],
            id="report-orientation",
            value="vertical",
            label="Report orientation",
            description="Set the orientation of the report.",
            size="sm",
            mt=10,
        ),
        dmc.Space(h=20),
        dmc.Group(
            [
                dmc.Button(id="generate-report", children="Submit", variant="outline"),
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id={"type": "modal-close", "contents": "report"},
                ),
            ],
            position="right",
        ),
    ]


def default_menu():
    """
    Some DMC components representing a menu of common actions in an application.
    """

    host = flask.request.host_url if flask.has_request_context() else ""
    return html.Div(
        [
            dmc.Menu(
                [
                    dmc.MenuTarget(
                        dmc.Button(
                            DashIconify(icon="material-symbols:menu"),
                            style={
                                "border-radius": "4px",
                            },
                        ),
                    ),
                    dmc.MenuDropdown(
                        [
                            dmc.MenuLabel("Application"),
                            dmc.MenuItem(
                                "Save this query",
                                icon=DashIconify(icon="material-symbols:save"),
                                id="save-query",
                            ),
                            dmc.MenuItem(
                                "Generate report",
                                icon=DashIconify(icon="ic:twotone-save-alt"),
                                id={
                                    "type": "modal-open",
                                    "contents": "report",
                                },
                            ),
                            dmc.MenuItem(
                                "Show saved views and queries",
                                icon=DashIconify(
                                    icon="material-symbols:calendar-view-week"
                                ),
                                id={
                                    "type": "modal-open",
                                    "contents": "views",
                                },
                            ),
                        ],
                    ),
                ],
                position="bottom-end",
                style={"margin-right": "10px"},
            ),
            dmc.Menu(
                [
                    dmc.MenuTarget(
                        dmc.Avatar(
                            id="menu-avatar",
                            radius="xl",
                            style={"cursor": "pointer"},
                        ),
                    ),
                    dmc.MenuDropdown(
                        [
                            dmc.MenuLabel("Get help", id="menu-label"),
                            dmc.MenuItem(
                                [
                                    "Contact Plotly support",
                                    DashIconify(icon="tabler:external-link"),
                                ],
                                href="mailto:onpremise.support@plot.ly",
                                icon=DashIconify(icon="material-symbols:help-center"),
                            ),
                            # dmc.MenuItem(
                            #     [
                            #         "Create a new Dash app",
                            #         DashIconify(icon="tabler:external-link"),
                            #     ],
                            #     href=f"{host}/apps",
                            #     target="_blank",
                            #     icon=DashIconify(icon="material-symbols:add"),
                            # ),
                            # dmc.MenuItem(
                            #     [
                            #         "View all Dash apps",
                            #         DashIconify(icon="tabler:external-link"),
                            #     ],
                            #     href=f"{host}/portal",
                            #     target="_blank",
                            #     icon=DashIconify(icon="ic:round-remove-red-eye"),
                            # ),
                            # dmc.MenuItem(
                            #     [
                            #         "Contact Plotly support",
                            #         DashIconify(icon="tabler:external-link"),
                            #     ],
                            #     href="mailto:onpremise.support@plot.ly",
                            #     icon=DashIconify(icon="material-symbols:help-center"),
                            # ),
                        ]
                    ),
                ],
                position="bottom-end",
            ),
            dmc.Modal(
                title="Saved views",
                id={"type": "modal", "contents": "views"},
                size="lg",
                children=archive_table_modal(),
            ),
            dmc.Modal(
                id={"type": "modal", "contents": "report"},
                children=report_modal(),
                size="lg",
            ),
            html.Div(id="snapshot-generator-dummy-output", style={"display": "none"}),
        ],
        style={
            "display": "flex",
            "align-items": "center",
            "margin": "0px 10px 0px 10px",
        },
    )


@callback(
    Output("menu-avatar", "children"),
    Output("menu-label", "children"),
    Input("url", "pathname"),
)
def populate_avatar(pathname):
    user = dae.get_username()
    if user:
        return user[0], f"Hi, {user}!"
    return no_update, no_update


@callback(
    Output({"type": "modal", "contents": MATCH}, "opened"),
    Output({"type": "modal", "contents": MATCH}, "children"),
    Input({"type": "modal-open", "contents": MATCH}, "n_clicks"),
    Input({"type": "modal-close", "contents": MATCH}, "n_clicks"),
    State({"type": "modal", "contents": MATCH}, "opened"),
    prevent_initial_call=True,
)
def modal_manager(nc1, nc2, opened):
    """
    Open and close our modals
    """
    # We need a special handler for the archive table because it won't refresh on its own.
    if ctx.triggered_id["contents"] == "views":
        return not opened, archive_table_modal()
    return not opened, no_update
