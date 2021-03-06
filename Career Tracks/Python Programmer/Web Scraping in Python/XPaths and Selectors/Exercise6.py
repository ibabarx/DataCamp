"""
Secret Links
We have loaded the HTML from a secret website and have used it to create the functions how_many_elements() and preview(). The function how_many_elements() allows you to 
pass in an XPath string and it will print out the number of elements the XPath you wrote has selected. The function preview() allows you to pass in an XPath string and 
it will print out the first few elements you've selected.

Your job in this exercise is to create an XPath which directs to all href attribute values of the hyperlink a elements whose class attributes contain the string 
"package-snippet". If you do it correctly, you should find that you have selected 10 elements with your XPath string and that it previews links.
"""

"""
Fill in the blanks below to assign an XPath string to the variable xpath which directs to all href attribute values of the hyperlink a elements whose class attributes 
contain the string "package-snippet". Remember that we use the contains call within the XPath string to check if an attribute value contains a particular string.
"""

# Create an xpath to the href attributes
xpath = '//a[contains(@class,"package-snippet")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )
