# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:28:04 2025

@author: MatthewSarsby
"""

from xmlish import Node  # Assuming the class is in svg_generator.py
import random

# Create an SVG canvas
canvas = Node('svg', width='400px', height='400px')

# Define bright Pop Art colors
colors = ["#ff0000", "#00ff00", "#0000ff", "#ffcc00", "#ff00ff", "#00ffff"]

# Generate a grid of colorful squares with circles inside them
rows, cols = 5, 5
cell_size = 80

for i in range(rows):
    for j in range(cols):
        x, y = j * cell_size, i * cell_size
        fill_color = random.choice(colors)
        stroke_color = random.choice(colors)

        # Add square background
        canvas('rect', x=x, y=y, width=cell_size, height=cell_size, fill=fill_color, stroke="black", stroke_width="2")

        # Add circle in the center of each square
        canvas('circle', cx=x + cell_size / 2, cy=y + cell_size / 2, r=cell_size / 4, fill=stroke_color, stroke="black", stroke_width="2")

# Save the SVG file
canvas.save('SVG_pop_art_demo.svg')
