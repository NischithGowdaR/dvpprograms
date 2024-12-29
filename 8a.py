import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show

# Generate data
x = np.linspace(0, 15, 100)
y = np.sin(x)

# Define tools for interaction
tools = "pan, wheel_zoom, box_zoom, reset, save, box_select"

# Create a figure
p = figure(
    title="Nischith Gouda R - 1K23CS122 in Bokeh Line Plot",
    tools=tools
)

# Add a line to the plot
p.line(x, y, line_width=2, color="red", legend_label="sin(x)")
p.line(x, 2 * y, line_width=2, color="green", legend_label="2*sin(x)")
p.line(x, 3 * y, line_width=2, color="blue", legend_label="3*sin(x)")

# Show the plot
show(p)