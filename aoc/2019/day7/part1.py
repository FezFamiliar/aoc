 #parameter modes:
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
# start's first value is phase setting, second value is input signal
class IntcodeComputer:
    def __init__(self, input, noun = '', verb = '', start = [4, 0]):
        self.input = input
        self.input = self.input.split(',')
        self.input = [int(x) for x in self.input]
        self.n = len(self.input)
        self.instructions = [1, 2, 3, 4, 5, 6, 7, 8, 99]
        self.step = 0   
        self.output = -1
        self.start = start
        self.overwrite = 0
        self.k = 0
        
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
            
            if self.overwrite != 0:
                i = self.overwrite
                self.overwrite = 0
            else:
                i += self.step
            
            
    def execute(self, opcode, i):
        
        opcode = opcode.rjust(5, '0')
        new_opcode = int(opcode[-2:])
        
        if new_opcode == 99:
            #print("output right before program halts: " + str(self.input[i + 1]))
            return True
       
        mode1 = opcode[-3:-2]
        mode2 = opcode[-4:-3]
        mode3 = opcode[-4:-3]
    

        if new_opcode == 1:         
            self.sum(i, mode1, mode2, mode3)
            self.step = 4   

        if new_opcode == 2:       # multiply
            self.multiply(i, mode1, mode2, mode3)
            self.step = 4
        
        if new_opcode == 3:
            self.command3(i, mode1, self.start[self.k])
            self.k += 1
            self.step = 2
            
        if new_opcode == 4:
            output = self.command4(i, mode1)
            self.output = output
           # print("output from opcode 4: " + str(output))
            self.step = 2
            
        if new_opcode == 5:
            self.command5(i, mode1, mode2)
            self.step = 3
            
        if new_opcode == 6:
            self.command6(i, mode1, mode2)
            self.step = 3
            
        if new_opcode == 7:
            i = self.command7(i, mode1, mode2)
            self.step = 4
            
        if new_opcode == 8:
            self.command8(i, mode1, mode2)
            self.step = 4
        
    
    def sum(self, i, mode1, mode2, mode3):
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
        
        self.input[param3] = (self.input[param1] if mode1 == '0' else param1) + (self.input[param2] if mode2 == '0' else param2)
        
        
    def multiply(self, i, mode1, mode2, mode3): 

        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]

        self.input[param3] = (self.input[param1] if mode1 == '0' else param1) * (self.input[param2] if mode2 == '0' else param2)
        
    def command3(self, i, mode1, m_i):  
    
        param1 = self.input[i + 1]
        
        if mode1 == '0':
            self.input[param1] = m_i

        
    def command4(self, i , mode1):
        
        param1 = self.input[i + 1]
        
        if mode1 == '0':
            return self.input[param1]
        else:
            return param1
            
          
    def command5(self, i, mode1, mode2):    
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        
        if mode1 == '0':
            if self.input[param1] != 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                else:
                    self.overwrite = param2
        else:
            if param1 != 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                else:
                    self.overwrite = param2
                    
       
                

        
    def command6(self, i, mode1, mode2):
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        
        if mode1 == '0':
            if self.input[param1] == 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                else:
                    self.overwrite = param2
        
        else:
            if param1 == 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                else:
                    self.overwrite = param2
                    
        
                    
                    
    def command7(self, i, mode1, mode2):
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
        
        if mode1 == '0':
            if mode2 == '0':
                if self.input[param1] < self.input[param2]:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
            else:
                if self.input[param1] < param2:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
        
        else:
            if mode2 == '0':
                if param1 < self.input[param2]:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
            else:
                if param1 < param2:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
                    
                    
        
        
        
    def command8(self, i, mode1, mode2):
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
    
        if mode1 == '0':
            if mode2 == '0':
                if self.input[param1] == self.input[param2]:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
            else:
                if self.input[param1] == param2:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
        
        else:
            if mode2 == '0':
                if param1 == self.input[param2]:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
            else:
                if param1 == param2:
                    self.input[param3] = 1
                else:
                    self.input[param3] = 0
   
        
    def getOutput(self):
        return self.output
        
    def __eq__(self, other):
        return self.input == other.input
        
    def __repr__(self):
        return "<input:%s length:%s instructions:%s noun:%s verb:%s>" % (self.input, self.n, self.instructions, self.input[1], self.input[2])
        
        
counter = 0
k = 0
nums = [0, 1, 2, 3, 4]
n = len(nums)
flag = [False, False, False, False, False]
permutations_aux = []
permutations = []
def permutate(k, n, nums, flag):

    if k >= n:
        permutations_aux.extend(nums)
    else:
        for i in range(0, n):
            if flag[i] == False:
                flag[i] = True
                nums[k] = i
                permutate(k + 1, n, nums, flag)
                flag[i] = False
    
    
    
    
permutate(k, n, nums, flag)

for i in range(0, len(permutations_aux), 5):
    permutations.append(permutations_aux[i:i+5])
    
    

class Amplifier(IntcodeComputer):
  pass
 
 
input = "3,8,1001,8,10,8,105,1,0,0,21,38,63,80,105,118,199,280,361,442,99999,3,9,102,5,9,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,4,9,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,101,3,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99"

result = []

for permutation in permutations:
    j = 0
    amp1 = Amplifier(input, '', '', [permutation[j], 0])
    amp1.run()
    
    amp2 = Amplifier(input, '', '', [permutation[j + 1], amp1.getOutput()])
    amp2.run()
    
    amp3 = Amplifier(input, '', '', [permutation[j + 2], amp2.getOutput()])
    amp3.run()
    
    amp4 = Amplifier(input, '', '', [permutation[j + 3], amp3.getOutput()])
    amp4.run()
    
    amp5 = Amplifier(input, '', '', [permutation[j + 4], amp4.getOutput()])
    amp5.run()
    #print(amp5.getOutput())
    result.append(amp5.getOutput())


print("max output signal is: " + str(max(result)))
