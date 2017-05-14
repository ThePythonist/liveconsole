# liveconsole
A python3 library which allows you to run lines of code while the program runs via a prompt on a tkinter window. It is designed for debugging programs (particularly games) with a loop (such as a game loop). It allows you to enter python code line by line and see its effects without having to reboot the program. The effects of these new lines are temporary and do not affect the source code of the program.

## Installation
To install the library, move the *liveconsole.py* file to the  *Lib* folder in your python installation directory

## Usage
To use this modue in a python script, import it. Then add the following line to your code:
```
liveconsole.activate()
```
Then, in your game loop, add the following code:
```
if liveconsole.hasCommand():
    exec(liveconsole.getCommand())
```
