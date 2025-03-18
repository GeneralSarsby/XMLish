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

### Usage

The code provides a single class `Node`, this makes an XML element with the same properties.

For example in python 
```python
canvas('circle', cx=30, cy=40, r=10, stroke='#600', fill='none', stroke_width='1.5px')
```
becomes
```xml
<circle cx="30" cy="40" r="10" stroke="#600" fill="none" stroke-width="1.5px"/>
```
Note that the underscore in `stroke_width` automatically becomes a dash in `stroke-width`.

There is one special element, `svg`, which when made updates the parameters with 
` {"xmlns":'http://www.w3.org/2000/svg', "version":'1.1', "xmlns:xlink":'http://www.w3.org/1999/xlink'}` for convenience.

This means that to start a new SVG document, you only need to write
```python
canvas = Node('svg', width='200px', height='200px')
```
to get 
```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="200px" height="200px">
```

To add text into an element, call `text()` on the node. `canavs('text', x=10, y=20).text("world")` to get `<text x="60" y="20">world</text>`.

All nodes can create new nodes that are nested.
starting with the `svg` element.
```python
canvas = Node('svg', width='200px', height='200px')
```
one can add directly to that calling from the new `canvas` object to :
```python
g = canvas('g')
```
then into the group make new elements with
```python
g('text', x=10, y=20).text("world")
```

#### Catches
The simple mapping of names means that if there are python keyword collisions or spaces in the key then a slightly different invocation is required.
For example in the case to add a `class` to an element, for example when styling, one can not use class as a keyword argument, instead use python's dictionary expansion to keywords:
```python
canvas('text', *{"class":"myclass"}) 
```

### Example 
The `Node` class acts as a flexible interface for constructing SVGs. Below is an example of how to use it. This script generates an SVG file (`SVG_nesting_test.svg`) containing a circle, a horizontal line, and two groups of text elements.



```python
from XMLish import Node

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

The base class is considered nearly feature complete in simplisity.
Feel free to contribute by improving the code or adding new features.
Examples are most welcome.

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

