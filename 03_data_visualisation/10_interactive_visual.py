from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.sampledata.iris import flowers

# Prepare some data
x = flowers["petal_length"]
y = flowers["sepal_length"]
source = ColumnDataSource(data=dict(x=x, y=y))

# Output to an HTML file
output_file("interactive_visual.html")

# Create a new plot with a title and axis labels
p = figure(
    title="Simple Line Chart Example",
    x_axis_label="Petal Length",
    y_axis_label="Sepal Length",
    sizing_mode="stretch_width",
    height=250,
)

# Add a line renderer with legend and line thickness
p.line("x", "y", source=source, legend_label="Length", line_width=2)

# Add a hover tool
hover = HoverTool()
hover.tooltips = [
    ("Petal Length", "@x"),
    ("Sepal Length", "@y"),
]
hover.mode = "vline"
p.add_tools(hover)

# Show the results in the browser
show(p)
