"""
Keep it Classy
In this two-part exercise, you will have a chance to show off what you've learned about attributes; in this case, we focus on the class attribute.
"""

"""
1> Given the following HTML
<html>
  <head>
    <title>Website Title</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="class1" id="div1">
      <p class="class2">
        Visit <a href="http://datacamp.com/">DataCamp</a>!
      </p>
    </div>
    <div class="class1 class3" id="div2">
      Hello World!
    </div>
  </body>
</html>
Which elements belong to the class class1?

2> Fill in the blank in the HTML code string html to assign a class attribute to the second div element which has the value "you-are-classy".
"""

# Answer 1 : Only the first and second div elements.

#Answer2 :
html = '''
<html>
  <body>
    <div class="class1" id="div1">
      <p class="class2">Visit DataCamp!</p>
    </div>
    <div class="you-are-classy">
      <p class="class2">Keep up the good work!</p>
    </div>
  </body>
</html>
'''
# Print out the class of the second div element
whats_my_class( html )
