'''# -*- coding: utf-8 -*-
import fitz

# the document to annotate
doc = fitz.open("sample.pdf")

# the text to be marked
#t = input("please enter selected string")
t ="Virtual Mechanics"

# work with first page only
page = doc[0]

# get list of text locations
# we use "quads", not rectangles because text may be tilted!
rl = page.search_for(t, quads = True)

# mark all found quads with one annotation
#page.add_squiggly_annot(rl)
page.add_highlight_annot(rl)

# save to a new PDF
doc.save("a-squiggly.pdf")
'''

# -*- coding: utf-8 -*-
import fitz

# the document to annotate
doc = fitz.open("sample.pdf")

# the text to be marked
#t = input("please enter selected string")
t ="pdf"

# work with first page only
page = doc[0]

# get list of text locations
# we use "quads", not rectangles because text may be tilted!
#rl = page.search_for(t, quads = True)
r1=page.search_for(t)
# for area in r1:
if isinstance(r1,fitz.fitz.Rect):
    annot=page.addRectAnnot(r1)
    annot.setColors(stroke=fitz.utils.getColor('red'))
doc.save("hi.pdf")
    # r1=PageObj.sear

# mark all found quads with one annotation
#page.add_squiggly_annot(rl)
#page.add_highlight_annot(rl)

# save to a new PDF
#doc.save("a-squiggly.pdf")