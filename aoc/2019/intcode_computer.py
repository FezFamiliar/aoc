
# modes:
# 0 - position mode
# 1 - immediate mode

class IntcodeComputer:
    def __init__(self, input, mode, noun = '', verb = ''):
        self.input = input
        self.input = self.input.split(',')
        self.input = [int(x) for x in self.input]
        self.n = len(self.input)
        self.mode = mode
        self.instructions = [1, 2, 99]
        if noun != '':
            self.input[1] = noun
        if verb != '':
            self.input[2] = verb
            
    def run(self):
        for i in range(0, self.n, 4):
    
            opcode = self.input[i]
        
            if opcode == 99:
                break
        
            pos1 = self.input[i + 1]
            pos2 = self.input[i + 2]
            pos3 = self.input[i + 3]
      
            if opcode == 1:
                val = self.input[pos1] + self.input[pos2]
                
            if opcode == 2:
                val = self.input[pos1] * self.input[pos2]
            
            
            self.input[pos3] = val
    
    def __eq__(self, other):
        return self.input == other.input and self.mode == other.mode
        
    def __repr__(self):
        return "<input:%s mode:%s length:%s instructions:%s noun:%s verb:%s>" % (self.input, self.mode, self.n, self.instructions, self.input[1], self.input[2])


    
    
