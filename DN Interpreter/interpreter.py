class Interpreter:
    def __init__(self, filename="main.dn"):
        self.filename = filename
        with open(filename, "r+") as f:
            self.code = f.readlines()
        for i in range(len(self.code)-1):
            self.code[i] = self.code[i].removesuffix("\n")
        print(self.code)
        if not self.code[0] == "START":
            self = None
        self.index = 0
    
    def interpret(self, line):
        args = line.split(" ")
        start = args.pop(0)
        if start.lower() == "start":
            pass
        elif start.lower() == "print":
            print(" ".join(args))
        elif start.lower() == "title":
            print("Set title to", " ".join(args))
        else:
            print(start+": Command not found")
    
    def start_interpreter(self):
        for self.index in range(len(self.code)):
            self.interpret(self.code[self.index])

if __name__ == "__main__":
    interp = Interpreter("tmp.dn")
    interp.start_interpreter()
    