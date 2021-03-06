"""
Body Appendages
We have loaded the HTML from a secret website and have used it to create a function how_many_elements(). The way this function works is that you pass it an XPath string 
and it will print out the number of elements the XPath you wrote has selected. For example, by running the code how_many_elements('//*') in the console will print out 
the total number of elements the HTML document has (try it!).
Your job in this exercise is to create an XPath string which can be used to direct to all child elements the body (regardless of tag type). To note, you can first test 
your solution with how_many_elements() to find the total number of children in the body element if you wish.
"""

"""
Assign to the variable xpath an XPath string which directs to all child elements of the body element. There is only one body element in this HTML document and it is a 
child of the root html element.
"""

# Create an XPath string to direct to children of body element
xpath = '/html/body/*'

# Print out the number of elements selected
how_many_elements( xpath )
