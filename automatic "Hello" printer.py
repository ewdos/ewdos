import pyautogui as pag
import webbrowser
import os
import time as tm

filepath = "chrome.exe"
os.startfile(filepath)

tm.sleep(5)
pag.typewrite(" classroom.google.com/u/0/ ", 0.1)
pag.hotkey('enter')
def repeat():
	pag.hotkey("tab")
tm.sleep(5)
for i in range(9): 
	repeat()
pag.hotkey("enter")
tm.sleep(5)
pag.click() 
for b in range(4):
	repeat()
pag.hotkey("enter")
tm.sleep(5)
for c in range(7):
	repeat()
pag.hotkey("enter")
tm.sleep(5)
pag.click() 
for f in range(3):
	repeat()
pag.hotkey("enter")
pag.typewrite("Hello", 0.5)
for f in range(4):
	repeat()
pag.hotkey("enter")
