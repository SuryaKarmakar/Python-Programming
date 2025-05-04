import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
fig.show()

# Simple Bubble Chart
fig = go.Figure(
    data=[
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[10, 11, 12, 13],
            mode="markers",
            marker_size=[40, 60, 80, 100],
        )
    ]
)
fig.show()

# Setting Marker Size and Color
fig = go.Figure(
    data=[
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[10, 11, 12, 13],
            mode="markers",
            marker=dict(
                color=[
                    "rgb(93, 164, 214)",
                    "rgb(255, 144, 14)",
                    "rgb(44, 160, 101)",
                    "rgb(255, 65, 54)",
                ],
                opacity=[1, 0.8, 0.6, 0.4],
                size=[40, 60, 80, 100],
            ),
        )
    ]
)
fig.show()

# Bubble Charts with Colorscale
fig = go.Figure(
    data=[
        go.Scatter(
            x=[1, 3.2, 5.4, 7.6, 9.8, 12.5],
            y=[1, 3.2, 5.4, 7.6, 9.8, 12.5],
            mode="markers",
            marker=dict(
                color=[120, 125, 130, 135, 140, 145],
                size=[15, 30, 55, 70, 90, 110],
                showscale=True,
            ),
        )
    ]
)
fig.show()
