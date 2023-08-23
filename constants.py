import os
import dash


app = dash.Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

app.title = "Bank of America"
