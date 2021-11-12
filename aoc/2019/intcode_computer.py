
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
    def __init__(self, input, noun = '', verb = ''):
        self.input = input
        self.input = self.input.split(',')
        self.input = [int(x) for x in self.input]
        self.n = len(self.input)
        self.instructions = [1, 2, 99]
        self.step = 0   
        self.mode = 0
        
        if noun != '':
            self.input[1] = noun
        if verb != '':
            self.input[2] = verb
            
    def run(self):
        i = 0
        while i < self.n:
    
            pos0 = str(self.input[i])
            
            if self.execute(pos0, i):
                break
            
            i += self.step
            
            
    def execute(self, opcode, i):
        
        opcode = opcode.rjust(5, '0')
        new_opcode = int(opcode[-2:])
        
        if new_opcode == 99:
            return True
       
        mode1 = opcode[-3:-2]
        mode2 = opcode[-4:-3]
        mode3 = opcode[-4:-3]
    

        if new_opcode == 1:         # sum
            self.sum(i, mode1, mode2, mode3)
            self.step = 4      # sum operation has 4 params, 1 opcode + 3 params

        if new_opcode == 2:       # multiply
            self.multiply(i, mode1, mode2, mode3)
            self.step = 4
            
        
    
    def sum(self, i, mode1, mode2, mode3):
        pos1 = self.input[i + 1]
        pos2 = self.input[i + 2]
        pos3 = self.input[i + 3]
        self.input[pos3] = (self.input[pos1] if mode1 == '0' else pos1) + (self.input[pos2] if mode2 == '0' else pos2)
        
        
    def multiply(self, i, mode1, mode2, mode3): # dont forget about possible mode3 for param3
        pos1 = self.input[i + 1]
        pos2 = self.input[i + 2]
        pos3 = self.input[i + 3]
        self.input[i + 3] = (self.input[pos1] if mode1 == '0' else pos1) * (self.input[pos2] if mode2 == '0' else pos2)
    
    def __eq__(self, other):
        return self.input == other.input
        
    def __repr__(self):
        return "<input:%s length:%s instructions:%s noun:%s verb:%s>" % (self.input, self.n, self.instructions, self.input[1], self.input[2])


    
    
