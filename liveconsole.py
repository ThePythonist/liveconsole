import threading, tkinter, time
from PIL import ImageTk
from pygments import lex
from pygments.lexers import PythonLexer

class consoleThread (threading.Thread):
    def __init__(self):
        self.command = None
        self.root = tkinter.Tk()
        self.root.bind('<Return>', self.process)
        self.root.geometry("300x50")
        self.root.configure(background="white")
        self.root.title("liveconsole")
        self.commandVar = tkinter.StringVar()
        tkinter.Label(self.root, text=">>", font="consolas", background="white", foreground="blue").pack(side=tkinter.LEFT)
        e = tkinter.Entry(self.root, textvariable=self.commandVar, font="consolas", relief=tkinter.FLAT)
        e.focus_set()
        e.pack(side=tkinter.LEFT)
        threading.Thread.__init__(self)
    def run(self):
        self.root.mainloop()
    def process(self, event):
        self.command = self.commandVar.get()
        self.commandVar.set("")

thread = consoleThread()
def activate():
    thread.start()

def hasCommand():
    return thread.command is not None

def getCommand():
    command = thread.command
    thread.command = None
    return command

if __name__ == "__main__":
    activate()
