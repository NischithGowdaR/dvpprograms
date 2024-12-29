import numpy as np
from bokeh.plotting import figure, show

# Generate data
x = np.linspace(0, 15, 100)
y = np.sin(x)

# Create a figure
p = figure(title="Nischith Gouda R - 1K23CS122", width=500, height=500)

# Bar plot
p.vbar(x=x, top=y, width=0.5, legend_label="Bar Chart")

# Line plot
p.line(x, y, line_width=2, color="red", legend_label="Line Plot")

# Scatter plot
p.circle(x, y, size=4, color="blue", legend_label="Scatter Plot")

# Add axis labels
p.xaxis.axis_label = "x-axis"
p.yaxis.axis_label = "y-axis"

# Show the plot
show(p)