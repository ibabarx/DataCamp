"""
A classy span
Although we haven't yet gone deep into XPath, one thing we can do is select elements by their attributes using an XPath. For example, if we want to direct to the div 
element within the HTML document whose id attribute is "uid", then we could write the XPath string '//div[@id="uid"]'. The first part of this string, //div, first looks 
at all div elements in the HTML document. Then, using the brackets, we specify that we want only the div element with a specific id attribute (in this case uid). 
To note, the phrase @id="uid" in the brackets would be read as "attribute id equals uid".

In this exercise, you will select all span elements whose class attribute equals "span-class". (Note: span is just another possible tag-name).
"""

"""
Assign to the variable xpath an XPath string which will select all span elements whose class attribute equals "span-class". You do not need to see the actual HTML code 
to do this!
"""

# Fill in the blank
xpath = '//span[@class="span-class"]'
