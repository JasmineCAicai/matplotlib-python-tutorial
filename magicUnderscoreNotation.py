import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line_color="crimson")],
    layout_title_text="A Chart"
)

fig.update_layout(title_font_size=30)

fig.show()

