# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:22:52 2025

@author: MatthewSarsby
"""

from xmlish import Node

# Create an SVG canvas
canvas = Node('svg', width='400px', height='400px')

# Define CSS styles
css = """
text {
  font-family: sans-serif;
  font-size: 12px;
  fill: black;
}
@keyframes move {
  0% { transform: translateX(0px); }
  50% { transform: translateX(50px); }
  100% { transform: translateX(0px); }
}
.animated {
  animation: move 2s infinite;
}
"""
canvas('style').text(css)

# Define a gradient
defs = canvas('defs')
linear_gradient = defs('linearGradient', id="grad1", x1="0%", y1="0%", x2="100%", y2="0%")
linear_gradient('stop', offset="0%", style="stop-color:blue;stop-opacity:1")
linear_gradient('stop', offset="100%", style="stop-color:purple;stop-opacity:1")

# Use gradient in a rectangle
canvas('rect', x=50, y=50, width=300, height=100, fill="url(#grad1)")

# Add a transformed group with a rotated rectangle
group = canvas('g', transform="rotate(30,200,200)")
group('rect', x=150, y=150, width=100, height=50, fill="red", stroke="black", stroke_width="2")

# Add a path (curved line)
canvas('path', d="M 50 250 Q 200 100 350 250", stroke="green", fill="none", stroke_width="3")

# Add an animated circle
canvas('circle', cx=200, cy=300, r=20, fill="orange", **{"class":"animated"})

# Add text elements
canvas('text', x=50, y=350).text("SVG Demo with Transformations, Animations, and Gradients")

# Save the SVG file
canvas.save('SVG_advanced_demo.svg')
