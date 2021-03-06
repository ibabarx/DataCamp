"""
Where it's @
In this exercise, you'll begin to write an XPath string using attributes to achieve a certain task; that task is to select the paragraph element containing the text 
"Thanks for Watching!". We've already created most of the XPath string for you.

Consider the following HTML:

<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose DataCamp!</p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
We have created the function print_element_text() for you, which will print any text contained in your element.
"""

"""
Fill in the blanks in the XPath string to select the paragraph element containing the phrase: "Thanks for Watching!".
"""

# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text( xpath )
