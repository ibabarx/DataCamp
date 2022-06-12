"""
Divvy Up This Exercise
We have pre-loaded an HTML into the string variable html. In this two part problem you will use this html variable as the HTML document to set up a Selector object 
with, and create a SelectorList which selects all div elements; then, you will check your understanding of what happens within the SelectorList.
"""

'''
1> Set up the Selector object sel with the html variable passed as the text argument.
2> Assign to the variable divs a SelectorList of all div elements within the HTML document.
'''

from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector( text=html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )
