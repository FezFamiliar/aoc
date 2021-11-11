
# parameter modes:
# 0 - position mode (take the value at position x)
# 1 - immediate mode (just take the value x)

# instructions:
# 1 - add (num1, num2, store_value), 3 params
# 2 - multiply (num1, num2, store_value) 3 params
# 3 - take an input and save it to its only parameter (store_value) 1 param
# 4 - out the value at its only parameter (store_value) 1 param
# 99 - break () 0 params


# additional notes:
# 1. Encountering an unknown opcode means something went wrong.
# 2. The values used immediately after an opcode, if any, are called the instruction's parameters
# 3. The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction finishes, 
#    the instruction pointer increases by the number of values in the instruction; 
#    until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters)
# 4. Parameter modes are stored in the same value as the instruction's opcode.
# 5. The instruction pointer should increase by the number of values in the instruction after the instruction finishes. (step value)

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


    
    
