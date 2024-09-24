class ExecutionCursor():
    value = 0
    # The cursors help in exexution of a certain function.
    def __init__(self, name):
        self.name = name
    def init(self):
        self.value = True
    def makeUP(self):
        self.value = True
    def makeDOWN(self):
        self.value = False
    def isUP(self):
        return self.value
    def isDOWN(self):
        return not self.value