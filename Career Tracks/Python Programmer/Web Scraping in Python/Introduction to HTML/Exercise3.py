"""
Where am I?
In this exercise, you will navigate to a specific element using your new knowledge of XPath notation.

Consider the HTML code:

<html>
  <body>
    <div>
      <p>Good Luck!</p>
      <p>Not here...</p>
    </div>
    <div>
      <p>Where am I?</p>
    </div>
  </body>
</html>
Your job will be to create an XPath string using single forward-slashes and brackets which navigates to the paragraph p element which contains the text "Where am I?".
"""

"""
Using only single forward-slashes to move between generations, and brackets to select the correct element, assign a string to the variable xpath that directs to the 
paragraph element containing "Where am I?".
Do not include any blank spaces in the string you assign to xpath.
"""

# Fill in the blank
xpath = '/html/body/div[2]/p'
