## FAQ

### Does this work in iPython and the Jupyter notebook?
It can if you bring in the Ipython display.

```python
from IPython.display import SVG, display

# Let's say you have an SVG string stored in the variable `svg_data`
# make the SVG here ...
svg_data = str(canvas)
display(SVG(svg_data))
```

### Does this work with Latex?
It can if you bring in the latex `SVG` package. 
Latex the SVG package can do this automatically for you if inkscape in in the path.
You can also work thru Inkscape to do a conversion for you.

### How do I convert SVGs to a different format?

With Inkscape you can do something from the command line like `inkscape -D -z --file=myimage.svg --export-pdf=myimage.pdf`, or do it manually by opening the file and picking "save a copy" from the file menu.

With google chrome you can do something like `google-chrome --headless --disable-gpu --no-sandbox --screenshot=example.png --window-size=1280,720 file:///path/to/your/document.html`

### Does this work with web pages?

Yes! Most browers will nativly render svg images. So upload them and include them as normal with an img tag
```html
<img src="path/to/your/image.svg" alt="Description of SVG" />
```
or directly inline as
```html
<body>
  <!-- Inline SVG code -->
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
    <circle cx="100" cy="100" r="50" />
  </svg>
</body>
```

### Does this really need to be a library? 
Oh, absolutely not. Why write repetitive, error-prone XML manually when you can have a neat, Pythonic interface do it for you? But hey, if you enjoy typing `<svg>` and `</svg>` by hand all day, be my guest.  

### Isn't this too simple?
Yes! That's the entire point. If you want to suffer through boilerplate just to draw a circle, go ahead and use an overcomplicated graphics library. Otherwise, enjoy the simplicity.  

### Why not just use an existing SVG library?  
Good question! You totally can. But if you like minimalism and don't want to install yet another dependency just to generate a few shapes, this is for you. Plus, writing your own tools is way more fun.  

### Can I use this to make complex SVG graphics?  
Sure! You just have to put in some effort. ~~If you're expecting AI-powered, automatic art generation, you're in the wrong place. This is a lightweight interface, not a magic wand.~~ If you do feed this and the examples into an AI coding engine then you can get some working outputs fast. 

### How do I install this? 
You don’t. It’s literally one Python file. Copy it, use it, and move on with your life.  

### Why does this use function calls to nest elements?
Because it the simpleist way to do nesting.  

### Does this support animations?
Technically, yes. SVG supports animations so in theory this does too. But if you're asking this question, you're probably better off using JavaScript.  

### Can I contribute?
Of course! If you have an idea for improvement, open a pull request. If you just want to complain, feel free to scream into the void.  

