
# parameter modes:
# 0 - position mode (take the value at position x)
# 1 - immediate mode (just take the value x)
# 2 - relative mode ()
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



input = "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,31,1008,1101,682,0,1027,1101,0,844,1029,1102,29,1,1001,1102,1,22,1014,1101,0,21,1011,1102,428,1,1025,1101,0,433,1024,1101,0,38,1019,1102,1,37,1016,1102,35,1,1017,1102,39,1,1018,1102,32,1,1000,1102,23,1,1012,1102,1,329,1022,1102,26,1,1006,1102,1,24,1003,1102,28,1,1005,1102,36,1,1010,1102,34,1,1004,1101,0,1,1021,1102,326,1,1023,1101,33,0,1015,1101,20,0,1002,1101,0,25,1007,1101,0,853,1028,1102,27,1,1009,1102,1,30,1013,1101,689,0,1026,1102,1,0,1020,109,12,2108,30,-3,63,1005,63,201,1001,64,1,64,1105,1,203,4,187,1002,64,2,64,109,-9,2101,0,6,63,1008,63,29,63,1005,63,227,1001,64,1,64,1106,0,229,4,209,1002,64,2,64,109,-6,1208,5,22,63,1005,63,249,1001,64,1,64,1106,0,251,4,235,1002,64,2,64,109,13,21107,40,41,8,1005,1018,273,4,257,1001,64,1,64,1105,1,273,1002,64,2,64,109,-11,2102,1,8,63,1008,63,25,63,1005,63,299,4,279,1001,64,1,64,1105,1,299,1002,64,2,64,109,15,1205,7,317,4,305,1001,64,1,64,1105,1,317,1002,64,2,64,109,10,2105,1,-1,1105,1,335,4,323,1001,64,1,64,1002,64,2,64,109,-22,1202,1,1,63,1008,63,24,63,1005,63,357,4,341,1106,0,361,1001,64,1,64,1002,64,2,64,109,13,1206,6,373,1106,0,379,4,367,1001,64,1,64,1002,64,2,64,109,11,1206,-6,393,4,385,1105,1,397,1001,64,1,64,1002,64,2,64,109,-32,1208,10,34,63,1005,63,419,4,403,1001,64,1,64,1105,1,419,1002,64,2,64,109,30,2105,1,0,4,425,1106,0,437,1001,64,1,64,1002,64,2,64,109,-28,1207,6,21,63,1005,63,455,4,443,1106,0,459,1001,64,1,64,1002,64,2,64,109,4,2101,0,8,63,1008,63,31,63,1005,63,485,4,465,1001,64,1,64,1105,1,485,1002,64,2,64,109,5,1207,-4,28,63,1005,63,505,1001,64,1,64,1106,0,507,4,491,1002,64,2,64,109,9,21102,41,1,2,1008,1016,39,63,1005,63,531,1001,64,1,64,1106,0,533,4,513,1002,64,2,64,109,-10,1201,4,0,63,1008,63,30,63,1005,63,553,1106,0,559,4,539,1001,64,1,64,1002,64,2,64,109,19,21108,42,41,-4,1005,1019,579,1001,64,1,64,1106,0,581,4,565,1002,64,2,64,109,-26,1201,3,0,63,1008,63,32,63,1005,63,607,4,587,1001,64,1,64,1106,0,607,1002,64,2,64,109,20,1205,3,623,1001,64,1,64,1105,1,625,4,613,1002,64,2,64,109,2,21107,43,42,-1,1005,1018,645,1001,64,1,64,1106,0,647,4,631,1002,64,2,64,109,-11,2102,1,1,63,1008,63,29,63,1005,63,667,1105,1,673,4,653,1001,64,1,64,1002,64,2,64,109,27,2106,0,-8,1001,64,1,64,1105,1,691,4,679,1002,64,2,64,109,-25,2107,25,-4,63,1005,63,713,4,697,1001,64,1,64,1105,1,713,1002,64,2,64,109,-2,21108,44,44,2,1005,1010,735,4,719,1001,64,1,64,1106,0,735,1002,64,2,64,109,11,21101,45,0,-3,1008,1016,45,63,1005,63,757,4,741,1106,0,761,1001,64,1,64,1002,64,2,64,109,-15,1202,3,1,63,1008,63,22,63,1005,63,781,1105,1,787,4,767,1001,64,1,64,1002,64,2,64,109,6,21101,46,0,0,1008,1010,49,63,1005,63,811,1001,64,1,64,1105,1,813,4,793,1002,64,2,64,109,-7,2108,34,1,63,1005,63,835,4,819,1001,64,1,64,1105,1,835,1002,64,2,64,109,15,2106,0,10,4,841,1001,64,1,64,1106,0,853,1002,64,2,64,109,-25,2107,33,7,63,1005,63,873,1001,64,1,64,1106,0,875,4,859,1002,64,2,64,109,7,21102,47,1,10,1008,1010,47,63,1005,63,897,4,881,1105,1,901,1001,64,1,64,4,64,99,21102,1,27,1,21102,915,1,0,1105,1,922,21201,1,12038,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1105,1,922,21202,1,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,22101,0,-2,-2,109,-3,2105,1,0"

#input = "1102,34915192,34915192,7,4,7,99,0"
#
class IntcodeComputer:
    def __init__(self, input, noun = '', verb = '', start = 0):
        self.input = input
        self.input = self.input.split(',')
        self.input = [int(x) for x in self.input]
        self.addDefaultMemory()
        self.n = len(self.input)
        self.instructions = [1, 2, 3, 4, 5, 6, 7, 8, 99]
        self.step = 0   
        self.output = -1
        self.start = start
        self.relative_base = 0
        self.overwrite = 0
        
        if noun != '':
            self.input[1] = noun
        if verb != '':
            self.input[2] = verb
            
    def addDefaultMemory(self):
        for i in range(0, 5000):
            self.input.append(0)

    def run(self):
        
        i = 0
        while i < self.n:
            #print("self overwrite = " + str(self.overwrite))
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
        # print('relative base = ' + str(self.relative_base))
        # print('opcode = ' + str(new_opcode))
        if new_opcode == 99:
            #print("output right before program halts: " + str(self.input[i + 1]))
            return True
       
        mode1 = opcode[-3:-2]
        mode2 = opcode[-4:-3]
        mode3 = opcode[-5:-4]
    

        if new_opcode == 1:         
            self.sum(i, mode1, mode2, mode3)
            self.step = 4   

        if new_opcode == 2:       # multiply
            self.multiply(i, mode1, mode2, mode3)
            self.step = 4
        
        if new_opcode == 3:
            self.command3(i, mode1, self.start)
            self.step = 2
            
        if new_opcode == 4:
            output = self.command4(i, mode1)
            self.output = output
            print("output from opcode 4: " + str(output))
            self.step = 2
            
        if new_opcode == 5:
            self.command5(i, mode1, mode2)
            self.step = 3
            
        if new_opcode == 6:
            self.command6(i, mode1, mode2)
            self.step = 3
            
        if new_opcode == 7:
            i = self.command7(i, mode1, mode2, mode3)
            self.step = 4
            
        if new_opcode == 8:
            self.command8(i, mode1, mode2, mode3)
            self.step = 4
            
        if new_opcode == 9:
            self.command9(i, mode1)
            self.step = 2
        
    
    def sum(self, i, mode1, mode2, mode3):
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
        left = 0
        right = 0
        # print(mode1)
        # print(mode2)
        # print(mode3)
        if mode1 == '0':
            
            left = self.input[param1]
        elif mode1 == '1':
            left = param1
        elif mode1 == '2':
            left = self.input[self.relative_base + param1]
            
            
        if mode2 == '0':
            right = self.input[param2]
        elif mode2 == '1':
            right = param2
        elif mode2 == '2':
            right = self.input[self.relative_base + param2]
        
        # print("left = " + str(left))
        # print("right = " + str(right))
        # print("f = " + str(param3))
        if mode3 == '0':
            self.input[param3] = left + right
        elif mode3 == '2':
            self.input[self.relative_base + param3] = left + right
        
    def multiply(self, i, mode1, mode2, mode3): 

        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]

        left = 0
        right = 0
        
        if mode1 == '0':
            left = self.input[param1]
        elif mode1 == '1':
            left = param1
        elif mode1 == '2':
            left = self.input[self.relative_base + param1]
            
            
        if mode2 == '0':
            right = self.input[param2]
        elif mode2 == '1':
            right = param2
        elif mode2 == '2':
            right = self.input[self.relative_base + param2]
        
        
        if mode3 == '0':
            self.input[param3] = left * right
        elif mode3 == '2':
            self.input[self.relative_base + param3] = left * right
        #self.input[param3] = left * right
        
        
        
    def command3(self, i, mode1, m_i):  
    
        param1 = self.input[i + 1]
        
        if mode1 == '0':
            self.input[param1] = m_i
        elif mode1 == '2':
            self.input[self.relative_base + param1] = m_i

        
    def command4(self, i , mode1):
        
        param1 = self.input[i + 1]
        #print(param1)
        if mode1 == '0':
            return self.input[param1]
        elif mode1 == '1':
            return param1
        elif mode1 == '2':
            return self.input[self.relative_base + param1]
            
          
    def command5(self, i, mode1, mode2):    
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        
        if mode1 == '0':
            if self.input[param1] != 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
        elif mode1 == '1':
            if param1 != 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
                    
        elif mode1 == '2':
            if self.input[self.relative_base + param1] != 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
                    
       
                

        
    def command6(self, i, mode1, mode2):
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        # print('fffff')
        # print("param 1 = " + str(param1))
        # print("param 2 = " + str(param2))
        # print("mode1 1 = " + str(mode1))
        # print("mode1 2 = " + str(mode2))
        if mode1 == '0':
            
            if self.input[param1] == 0:
                if mode2 == '0':
                   
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
        
        elif mode1 == '1':
            if param1 == 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
        
        elif mode1 == '2':
            if self.input[self.relative_base + param1] == 0:
                if mode2 == '0':
                    self.overwrite = self.input[param2]
                elif mode2 == '1':
                    self.overwrite = param2
                elif mode2 == '2':
                    self.overwrite = self.input[self.relative_base + param2]
                    
        
                    
                    
    def command7(self, i, mode1, mode2, mode3):
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
        
        if mode1 == '0':
            if mode2 == '0':
                if self.input[param1] < self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '1':
                if self.input[param1] < param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '2':
                if self.input[param1] < self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
        
        elif mode1 == '1':
            if mode2 == '0':
                if param1 < self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '1':
                if param1 < param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
                    
            elif mode2 == '2':
                if param1 < self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
                    
        elif mode1 == '2':
            if mode2 == '0':
                if self.input[self.relative_base + param1] < self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
                    
            elif mode2 == '1':
                if self.input[self.relative_base + param1] < param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
                    
            elif mode2 == '2':
                if self.input[self.relative_base + param1] < self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                        
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0       
                    
        
        
        
    def command8(self, i, mode1, mode2, mode3):
        
        param1 = self.input[i + 1]
        param2 = self.input[i + 2]
        param3 = self.input[i + 3]
    
        if mode1 == '0':
            if mode2 == '0':
                if self.input[param1] == self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '1':
                if self.input[param1] == param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '2':
                if self.input[param1] == self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
        
        elif mode1 == '1':
            if mode2 == '0':
                if param1 == self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '1':
                if param1 == param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '2':
                if param1 == self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
                    
        elif mode1 == '2':
            if mode2 == '0':
                if self.input[self.relative_base + param1] == self.input[param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '1':
                if self.input[self.relative_base + param1] == param2:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
            elif mode2 == '2':
                if self.input[self.relative_base + param1] == self.input[self.relative_base + param2]:
                    if mode3 == '0':
                        self.input[param3] = 1
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 1
                    
                else:
                    if mode3 == '0':
                        self.input[param3] = 0
                    elif mode3 == '2':
                        self.input[self.relative_base + param3] = 0
   
   
    def command9(self, i, mode1):
        
        param1 = self.input[i + 1]
        val = 0
        if mode1 == '0':
            val = self.input[param1]
        elif mode1 == '1':
            val = param1
        elif mode1 == '2':
            val = self.input[self.relative_base + param1]
            
        self.relative_base += val
        
        
    def getOutput(slef):
        return self.output
        
    def __eq__(self, other):
        return self.input == other.input
        
    def __repr__(self):
        return "<input:%s length:%s instructions:%s noun:%s verb:%s>" % (self.input, self.n, self.instructions, self.input[1], self.input[2])
    
    
c = IntcodeComputer(input, '', '', 1)  # just change this to 2 for part2
c.run()
