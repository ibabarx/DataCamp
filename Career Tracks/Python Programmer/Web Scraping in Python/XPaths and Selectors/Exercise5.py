"""
Hyper(link) Active
One of the most important attributes to extract for "web-crawling" is the hyperlink url (href attribute) within an a tag. Here, you will extract such a hyperlink! We 
have created the function print_attribute to print out the data extracted from your XPath, so you can test your XPath strings in the console, if you like.

The exercise refers to the following HTML source code:

<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose 
            <a href="http://datacamp.com">DataCamp!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
"""

"""
Fill in the blanks to complete the variable xpath below to select the href attribute value from the DataCamp hyperlink.
"""

# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute( xpath )
