import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[2, 3, 1])],
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Displayed with fig.show()")
    )
)

fig.show()

# Through Dictionary
fig2 = go.Figure({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
})

fig2.show()