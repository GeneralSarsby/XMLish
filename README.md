# XMLish | an SVG Generator in Python
Make XML elements for SVG images natively in python 

This repository contains a simple Python interface for generating SVG documents using an intuitive tree-like structure. The `Node` class allows you to create SVG elements dynamically, add attributes, and structure them hierarchically.

## Features
- Create and define SVG elements with a simple Python API.
- Nest elements dynamically using function calls.
- Add attributes and update them easily.
- Save the generated SVG to a file.
- Support for inline CSS styling.

## Getting Started

### Prerequisites
This script runs on Python 3 and does not require external dependencies.

### Example Usage
The `Node` class acts as a flexible interface for constructing SVGs. Below is an example of how to use it. This script generates an SVG file (`SVG_nesting_test.svg`) containing a circle, a horizontal line, and two groups of text elements.



```python
from svg_generator import Node

# Create an SVG canvas
canvas = Node('svg', width='200px', height='200px') # 'svg' is the only special node. 

# Add CSS styles
css = """
text {
  font-family: sans-serif;
  font-size: 9px;
}
path {
   stroke-linejoin : round;
}
"""
canvas('style').text(css)

# Add SVG elements
canvas('circle', cx=30, cy=40, r=10, stroke='#600', fill='none', stroke_width='1.5px')
canvas('path', d="M 10 90 H 50", stroke='#066', fill='none', stroke_width='1px', **{'class': 'def'})

# Add grouped text elements
group1 = canvas('g')
group1('text', x=10, y=10).text("hello")
group1('text', x=10, y=20).text("world")

group2 = canvas('g')
group2('text', x=60, y=10).text("hello")
group2('text', x=60, y=20).text("world")

# Save the SVG file
canvas.save('SVG_nesting_test.svg')
```

### Example SVG Output
```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="200px" height="200px">
    <style>
    text {
      font-family: sans-serif;
      font-size: 9px;
    }
    path {
       stroke-linejoin : round;
    }
    </style>
    
    <circle cx="30" cy="40" r="10" stroke="#600" fill="none" stroke-width="1.5px"/>
    <path d="M 10 90 H 50" stroke="#066" fill="none" stroke-width="1px" class="def"/>
    
    <g>
        <text x="10" y="10">hello</text>
        <text x="10" y="20">world</text>
    </g>
    
    <g>
        <text x="60" y="10">hello</text>
        <text x="60" y="20">world</text>
    </g>
</svg>
```

## Contributing
Feel free to contribute by improving the code or adding new features.
The base class is considered nearly feature complete in simplisity

## Source
The full source code is just this

```python
class Node(object):
    def __init__(self, el, **params):
        self.params = params
        if el == 'svg':  self.params.update( {"xmlns":'http://www.w3.org/2000/svg', "version":'1.1', "xmlns:xlink":'http://www.w3.org/1999/xlink'})
        self.children = []
        self.el = el
    def __call__(self,el, **params):
        a = Node(el, **params)
        self.children.append(a)
        return a
    def text(self, text):
        self.children.append(str(text))
    def update(self, **params):
        self.params.update(params)
    def __str__(self):
        p = ' '.join([str(k).replace('_','-')+'="'+str(self.params[k])+'"' for k in self.params])
        if len(self.children) == 1:
            c = f'<{self.el} {p}>{str(self.children[0])}</{self.el}>\n'
        elif len(self.children) != 0:
            c = "".join(str(el) for el in self.children)
            c = f"<{self.el} {p}>\n{c}</{self.el}>\n"
        else:
            c = f"<{self.el} {p}/>\n"
        return c
    def __repr__(self): return str(self)
    def save(self, path):
        with  open(path, "w+") as f:
            f.write(str(self))
```

## License
This project is licensed under the MIT License.

## Author
Matthew Sarsby

