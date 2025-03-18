# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:47:47 2023

make an XML-like element that can next other XML elements and text nodes.
XML elements have params (key-value set), and children (ordered list).

@author: MatthewSarsby
"""

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
