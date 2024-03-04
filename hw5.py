# This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *
import re


class MyGUI:  # class definition
    __position__ = 1.0
    __lineNum__ = 0
    __inputList__ = []
    __lexerList__ = {}

    # This is the initialize function for a class.
    # Variables belonging to this class will get created and initialized in this function
    # What is the self parameter? It represents this class itself.
    # By using self.functionname, you can call functions belonging to this class.
    # By using self.variablename, you can create and use variables belonging to this class.
    # It needs to be the first parameter of all the functions in your class

    def __init__(self, root):
        # Master is the default parent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("Lexical Analyzer for TinyPie")

        # grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        # it will make self.label=none and you will no longer be able to change the label's content
        self.inlabel = Label(self.master, text="Source Code Input: ")
        self.inlabel.grid(row=0, column=0, sticky=NW)

        self.inputbox = Text(self.master, bd=5, relief=SUNKEN)
        self.inputbox.grid(row=1, column=0, padx=5, pady=5)
        self.inputbox.configure(width=30, height=10)

        self.outlabel = Label(self.master, text="Lexical Analyzed Result: ")
        self.outlabel.grid(row=0, column=1, sticky=W)

        self.outputbox = Text(self.master, bd=5, relief=SUNKEN)
        self.outputbox.grid(row=1, column=1, padx=5, pady=5)
        self.outputbox.configure(width=30, height=10)

        self.nextbutton = Button(self.master, text="Next Line", command=self.nextline)
        self.nextbutton.grid(row=3, column=0, sticky=SW)

        self.currline = Label(self.master, text="Current Processing Line:")
        self.currline.grid(row=2, column=0, sticky=W)

        self.currlinenum = Entry(self.master)
        self.currlinenum.grid(row=2, column=0, padx=15, sticky=E, )
        self.currlinenum.configure(width=7)

        self.quitbutton = Button(self.master, text="Quit", command=self.close)
        self.quitbutton.grid(row=3, column=1, padx=10, sticky=SE)

    def nextline(self):

        self.__lineNum__ += 1
        self.currlinenum.delete(0, END)
        self.currlinenum.insert(2, self.__lineNum__)

        linesCounted = 0
        numList = []
        input_Str = []

        text_input = self.inputbox.get("1.0", 'end').rstrip()
        self.__inputList__ = text_input.split('\n')

        for line in self.__inputList__:
            linesCounted += 1
            numList.append(linesCounted)
            input_Str.append(line)

        self.__lexerList__ = dict(zip(numList, input_Str))

        for key in self.__lexerList__.keys():
            if key == self.__lineNum__:
                line = self.__lexerList__.get(key)
                result = self.cutOneLineTokens(line)
                self.outputbox.delete('1.0', END)  # clear any previous analyzed results
                self.outputbox.insert(self.__position__, result, '\n')

    def close(self):
        self.master.destroy()

    def cutOneLineTokens(self, str1):
        output = []
        tokenlis = {r'\b(if|else|int|float)(?=\s|\t)': 'key',
                    r'[=+>*]': 'op',
                    r'[():\";]': 'sep',
                    r'[a-zA-Z]+\d+|[a-zA-Z]+': 'id',
                    r'^\d+(?![\d+\.])': 'lit',  # int
                    r'\d+\.\d+': 'lit',  # float
                    r'(".+")': 'lit',  # string
                    r'[\s]+': 'space'}

        tempstr = str1
        while len(tempstr) != 0:
            for x in tokenlis:
                token = re.match(x, tempstr)
                if token:
                    if tokenlis[x] == 'space':
                        pos = token.end()
                        tempstr = tempstr[pos:]
                    else:
                        output.append("<" + tokenlis[x] + "," + token.group() + ">")
                        pos = token.end()
                        tempstr = tempstr[pos:]

        print("Output <type,token> list:", output)
        output = '\n'.join(output)  # Add new line characters to returned list
        return output


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyGUI(myTkRoot)
    myTkRoot.mainloop()
