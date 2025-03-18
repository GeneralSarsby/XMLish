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

### Methods and Usage

#### Creating an SVG Element
To start, create an SVG root node:
```python
canvas = Node('svg', width='500px', height='500px')
```
This initializes an SVG element with a width and height. 

#### Adding Child Elements
You can add elements dynamically using function calls:
```python
circle = canvas('circle', cx=100, cy=100, r=50, fill='red')
```
This adds a red circle at (100,100) with a radius of 50.

#### Nesting Elements
Elements can be nested by calling a node instance:
```python
group = canvas('g', transform="translate(50,50)")
group('rect', x=0, y=0, width=100, height=100, fill="blue")
```
This creates a `<g>` group with a translated blue rectangle inside.

#### Adding Text
Text content can be added using the `.text()` method:
```python
canvas('text', x=10, y=20).text("Hello, SVG!")
```
This adds a text element at coordinates (10,20).

#### Updating Attributes
You can update an element's attributes dynamically:
```python
circle.update(fill="green", stroke="black")
```
This changes the fill color to green and adds a black stroke.

#### Saving to File
To save the generated SVG:
```python
canvas.save('output.svg')
```
This writes the full SVG structure to a file.


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

### How it works

The code provides a single class `Node`, this makes an XML element with the same properties. All the code does is covert python syntax for function calls, into XML elements have params (key-value set), and children (ordered list).

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
generated for you.

To add text into an element, call `text()` on the node. `canavs('text', x=10, y=20).text("world")` to get `<text x="60" y="20">world</text>`.

All nodes can create new nodes that are nested. The native `__call__` on any node also returns a node that is nested to the partent.
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

