"""
Check your Class
This exercise is to emphasize that when you use an XPath to select an element by its class attribute without using the contains() function, you match the class exactly.
Your job is to fill in the blank below and finish the variable xpath directing to the specified element.

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
"""

"""
Fill in the blanks in the xpath below to select the paragraph element containing the phrase: "Hello World!".
"""

# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text( xpath )
