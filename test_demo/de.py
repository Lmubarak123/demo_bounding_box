# -*- coding: utf-8 -*-
import fitz

# the document to annotate
doc = fitz.open("python-guide.pdf")

# the text to be marked
#t = input("please enter selected string")
t ="python"

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