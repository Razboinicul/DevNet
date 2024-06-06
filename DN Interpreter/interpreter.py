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
        self.forever = []
    
    def interpret(self, line):
        argg = line.split(" ")
        args = []
        txt = ""
        for i in argg:
            if i.startswith('"') or i.startswith("'"):
                txt += i.removeprefix('"') if i.startswith('"') else i.removeprefix("'")
            elif not (i.endswith("'") or i.endswith('"')) and txt != "":
                txt += i
            elif (i.endswith("'") or i.endswith('"')):
                txt += i.removesuffix('"') if i.endswith('"') else i.removesuffix("'")
                args.append(txt)
                txt = ""
            else:
                args.append(i)
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
        elif start.lower() == "input":
            arg = []
            for i in args:
                arg.append(i.split("="))
            obj = sg.InputText('')
            for i in arg:
                if len(i) == 2:
                    if i[0].lower() == "text":
                        obj.DefaultText = i[1]
                    if i[0].lower() == "whileTrue":
                        self.forever.append(f"{i[1]}()")
            self.layout.append([obj])
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
    