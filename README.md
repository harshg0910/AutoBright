##   AutoBright
##   README		Steps for Running 



------------------------
Steps to run the program
------------------------

**************SOFTWARE CURRENTLY WORKING ON UBUNTU 12.10 AND GREATER
PREREQUISITES:
1. PyQt4
2. dbus
3. Python

Instructions
1) Double Click on the AutoBright.py file. If this doesn't run try
	python AutoBright.py

2) Set the screen brightness (if current is not appropriate for you)
by adjusting the sliding bar & click on set for applying the changes.

3) Minimize the application (currently it's not running as a service),
so that it continues to run in the background & hence able to adjust
the screen brightness automatically.


--------------------
KNOWN BUGS
-------------------
1) Termination of the program through GUI is not enough. The pythod thread
needs to be killed through the terminal

----------------------------------------------------------------------
