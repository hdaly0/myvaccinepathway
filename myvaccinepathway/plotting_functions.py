import plotly.express as px
from constants import COLUMNS


def get_plotly_figure(df):
    fig = px.line(df/100.0,
                  x=df.index,
                  y=COLUMNS,
                  # labels={IMMUNITY: "Date", "immunity_level": "Immunity Level"},
                  title="Immunity from Symptomatic infection")
    fig.update_xaxes(showspikes=True, spikecolor="white", spikethickness=0.5, spikesnap="cursor", spikemode="across", fixedrange=True)
    fig.update_yaxes(tickformat=".1%", range=[0, 1], fixedrange=True)
    fig.update_layout(spikedistance=1000, hovermode="x")
    fig.update_traces(mode="lines", hovertemplate=None)

    return fig


def get_plotly_timeline(df, start_date, end_date):
    fig = px.scatter(df,
                     x="dates",
                     y="values",
                     text="text",
                     height=250,
                     title="My vaccine timeline")
    fig.update_xaxes(range=[start_date, end_date], showgrid=False, title="", fixedrange=True)
    fig.update_yaxes(range=[-0.2, 1], showgrid=False, title="", showticklabels=False, fixedrange=True)
    fig.update_traces(marker={"symbol": "triangle-down"}, marker_size=20, textposition="top center")
    fig.update_layout(hovermode=False, plot_bgcolor="rgba(0,0,0,0)")
    return fig
