# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:33:04 2025

Please do not use this as a plotting code. Below is just a trivial example of how one could be made.

@author: MatthewSarsby
"""

import random
from xmlish import Node  # Assuming the class is in svg_generator.py

# Generate random (x, y) data points
num_points = 50
data_x = [ random.uniform(0, 100) for _ in range(num_points)]
data_y = [random.uniform(0, 100) for _ in range(num_points)]

# Define SVG canvas size and margins
svg_width, svg_height = 500, 500
margin = 50  # Space for labels and axes

# Determine data ranges
data_x_min, data_x_max = 0,100 #min(data_x), max(data_x)
data_y_min, data_y_max = 0,100 #min(data_y), max(data_y)

# Function to map data coordinates to SVG pixel space
def data_to_svg(x, y):
    x_svg = margin + ((x - data_x_min) / (data_x_max - data_x_min)) * (svg_width - 2 * margin)
    y_svg = svg_height - margin - ((y - data_y_min) / (data_y_max - data_y_min)) * (svg_height - 2 * margin)  # Invert y-axis for SVG
    x_svg = round(x_svg,2) # round off floats to only 100th of a pixel. 
    y_svg = round(y_svg,2) 
    return x_svg, y_svg

# Create SVG canvas
canvas = Node('svg', width=f'{svg_width}px', height=f'{svg_height}px')

# Draw axis lines
canvas('line', x1=margin, y1=svg_height-margin, x2=svg_width-margin, y2=svg_height-margin, stroke='black', stroke_width="2")  # X-axis
canvas('line', x1=margin, y1=margin, x2=margin, y2=svg_height-margin, stroke='black', stroke_width="2")  # Y-axis

# Add axis labels
canvas('text', x=svg_width/2, y=svg_height-10, text_anchor="middle").text("X Axis")
canvas('text', x=10, y=svg_height/2, text_anchor="middle", transform=f"rotate(-90,10,{svg_height/2})").text("Y Axis")

# Add tick marks and labels
num_ticks = 5
for i in range(num_ticks + 1):
    # X-axis ticks
    tick_x = margin + (i / num_ticks) * (svg_width - 2 * margin)
    value_x = data_x_min + (i / num_ticks) * (data_x_max - data_x_min)
    canvas('line', x1=tick_x, y1=svg_height-margin, x2=tick_x, y2=svg_height-margin+5, stroke='black')
    canvas('text', x=tick_x, y=svg_height-margin+20, text_anchor="middle").text(f"{value_x:.1f}")

    # Y-axis ticks
    tick_y = svg_height - margin - (i / num_ticks) * (svg_height - 2 * margin)
    value_y = data_y_min + (i / num_ticks) * (data_y_max - data_y_min)
    canvas('line', x1=margin-5, y1=tick_y, x2=margin, y2=tick_y, stroke='black')
    canvas('text', x=margin-10, y=tick_y+5, text_anchor="end").text(f"{value_y:.1f}")

# Plot each point
for x, y in zip(data_x, data_y):
    x_svg, y_svg = data_to_svg(x, y)
    canvas('circle', cx=x_svg, cy=y_svg, r=5, fill='blue', stroke='black', stroke_width="1")

# Save the SVG file
canvas.save('SVG_scatter_plot_with_axes.svg')
