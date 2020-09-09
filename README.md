# RARNinja: The RAR Password Cracking Utility

## Description & Usage
A dictionary attack implementation, that takes the following as input:

- The RAR file to be cracked
- A dictionary file to be used for the cracking

...and then tries every line in the supplied dictionary file as the password input for the supplied RAR file, until either the correct password is found or the dictionary is exhausted upon the correct password not being found. Upon the discovery of the correct password, the supplied RAR is automatically unlocked and extracted into the "Extracted" folder in the current working directory; so this tool can easily be left to execute in the background as well. 

This project was created in Python, for experimental/observational purposes; and can also be aided with my own super fast numbered dictionary generator [NumNinja](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator)  (700,000+ lines per second) for numeric attacks.



## Optimization
The high password-matching speed is owed to the smart implementation of creating multiple chunks of the dictionary file and then working on all those simplified chunks concurrently (with multithreading) in different directions for better balance, efficiency and performance.

![Single Threaded Vs. Multithreaded Performance](https://github.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility/blob/master/Multithreading%20Presentation.png "Single Threaded Vs. Multithreaded Performance")

The regular version of the program works flawlessly, but the much faster multithreading version is still an active work in progress.

## Dependencies to "pip install"

- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
