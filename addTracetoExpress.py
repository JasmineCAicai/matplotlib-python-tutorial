import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=True
    )
)

fig.show()