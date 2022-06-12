"""
This exercise is similar to the previous, but differs in that you will be selecting text from multiple generations of a given element.
You will write an XPath and CSS Locator strings to direct to the text of a specific paragraph p element. The p element in the HTML is uniquely defined by its id 
attribute, which is "p3". With this small piece of information, you should be able to create the desired strings; however, we have preloaded the variable html with a 
string containing the HTML in which this link belongs, if you want to peruse it.
In this exercise, you will only be selecting the text within the element which includes all text within the future generations. We have created a function print_results 
for you to compare which elements your strings direct to.
"""

"""
1> Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which includes the text of future generations 
of this p element.
2> Assign to the variable css_locator a CSS Locator string directing to this same text.
"""

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )

