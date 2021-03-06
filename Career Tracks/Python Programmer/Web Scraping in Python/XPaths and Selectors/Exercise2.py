"""
Choose DataCamp!
In this exercise, we want to give you the opportunity to create your own XPath string to achieve a certain task; the task is to select the paragraph element containing 
the text "Choose DataCamp!".

Consider the following HTML:

<html>
  <body>
    <div>
      <p>Hello World!</p>
      <div>
        <p>Choose DataCamp!</p>
      </div>
    </div>
    <div>
      <p>Thanks for Watching!</p>
    </div>
  </body>
</html>
We have created the function print_element_text() for you, which will print the text contained in your element (if it contains any). Feel free to use this function to 
check if your solution is correct!
"""

"""
Assign to the variable xpath an XPath string to direct to the paragraph element containing the phrase: "Choose DataCamp!".
"""

# Create an XPath string to the desired paragraph element
xpath = '/html/body/div/div/p'

# Print out the element text
print_element_text( xpath )
