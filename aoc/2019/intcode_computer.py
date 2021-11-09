
# modes:
# 0 - position mode
# 1 - immediate mode

class IntcodeComputer:
    def __init__(self, input, mode = 0):
        self.input = input
        self.input = self.input.split(',')
        self.input = [int(x) for x in self.input]
        self.n = len(self.input)
        self.mode = mode
        self.instructions = [1, 2, 99]
    
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
        return "<input:%s mode:%s length:%s instructions:%s>" % (self.input, self.mode, self.n, self.instructions)
        
        
c = IntcodeComputer("1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,2,27,10,31,1,5,31,35,2,35,6,39,1,6,39,43,2,13,43,47,2,9,47,51,1,6,51,55,1,55,9,59,2,6,59,63,1,5,63,67,2,67,13,71,1,9,71,75,1,75,9,79,2,79,10,83,1,6,83,87,1,5,87,91,1,6,91,95,1,95,13,99,1,10,99,103,2,6,103,107,1,107,5,111,1,111,13,115,1,115,13,119,1,13,119,123,2,123,13,127,1,127,6,131,1,131,9,135,1,5,135,139,2,139,6,143,2,6,143,147,1,5,147,151,1,151,2,155,1,9,155,0,99,2,14,0,0", "i")
c.run()
print(c)


    
    