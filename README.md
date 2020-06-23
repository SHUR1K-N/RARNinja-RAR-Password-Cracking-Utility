# RARNinja: The RAR Password Cracking Utility

A dictionary attack implementation I created, that will take a [RAR file] and [dictionary file] as the input and then try every line in the supplied dictionary file as the password input for the supplied RAR file until either the correct password is found, or the dictionary is exhausted upon the correct password not being found. Upon the discovery of the correct password, the supplied RAR is automatically unlocked and extracted into the "Extracted" folder in the current working directory; so this tool can easily be left to execute in the background as well. This project was created in Python, and can also be aided with my own super fast numbered dictionary generator [NumNinja](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator)  (700,000+ lines per second) for numeric attacks.

**Dependencies to "pip install" before being able to run the Python files:**

**colorama** (for colors)

**termcolor** (for colors)

My website: http://bit.do/SHUR1KN
