import PySimpleGUI as sg

class Interpreter:
    def __init__(self, filename="main.dn"):
        self.layout = []
        self.filename = filename
        with open(filename, "r+") as f:
            self.code = f.readlines()
        for i in range(len(self.code)-1):
            self.code[i] = self.code[i].removesuffix("\n")
        print(self.code)
        if not self.code[0] == "START":
            self = None
        self.index = 0
        self.win_title = "App"
    
    def interpret(self, line):
        args = line.split(" ")
        start = args.pop(0)
        if start.lower() == "start":
            pass
        elif start.lower() == "print":
            print(" ".join(args))
        elif start.lower() == "title":
            print("Set title to", " ".join(args))
            self.win_title = " ".join(args)
        elif start.lower() == "text":
            self.layout.append([sg.Text(" ".join(args))])
        else:
            print(start+": Command not found")
    
    def start_interpreter(self):
        for self.index in range(len(self.code)):
            self.interpret(self.code[self.index])
        self.window = sg.Window(self.win_title, self.layout)
        while True:
            event, values = self.window.read()

            # if user closes window or clicks cancel
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break


if __name__ == "__main__":
    interp = Interpreter("tmp.dn")
    interp.start_interpreter()
    