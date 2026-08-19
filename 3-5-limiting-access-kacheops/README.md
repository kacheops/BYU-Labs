[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=24243673)
# Career Connections

**You will use the limiting_access.py file to write your code.**

In the last assignment, 3.5 Tilling The Soil, you wrote a Python program (`tilling_the_soil.py`) that allows a landscaping company to determine the cost of applying fertilizer to a swath of land. This information is useful to the company in determining profit margins, calculating labor needs, and estimating the time required for a given project. That information, however, is not meant for public consumption. Unethical competitors might undermine the efforts of the company by stealing and exploiting its customer, expense, and profit data. It is up to you to add security to the program so that only authorized users can access it. This will ensure that the landscaping company can reap the benefits of its hard work!

The landscaping company would like you to ask anyone using the program to log in first, using a company-issued username and password. Because the credentials need to be changed often, it has been determined that a text file, provided by the company, will be used to define the username and password of an authorized user. Additionally, the document will provide an integer indicating the access level of an authorized user. Later on, this information could be used to allow different levels of access to different users.

The text file, called `authorized_users.txt`, can be found in the GitHub assignment. Now, many of you will spot the holes in this security scheme: For a start, the data provided is un-encrypted and stored in an unprotected device. That is fair criticism. Keep in mind, however, that we are just beginning our Python and data-security journey. We have to start somewhere!

Click the terminal in the codespace and type `pytest` to test your code.

# Rubric

Criteria: The Algorithm for authorization works as requested, 10 pts.

Criteria: Code submitted to GItHub and program is running properly, 10 pts.

