class Solution:
    def calculate(self, s: str) -> int:
        operator = []
        operand = []
        int_flag = False
        
        for ch in s:
            if ch.isdigit():
                print(ch,ch.isdigit())
                if int_flag:
                    operand[-1] = operand[-1]*10 + int(ch)
                else:
                    operand.append(int(ch))
                int_flag = True
        
            elif ch == " ":
                int_flag = False
                continue
            
            elif ch in "+-":
                while len(operator) and operator[-1]!='(':
                    self.process(operator,operand)
                operator.append(ch)
                int_flag = False
            
            elif ch == "(":
                operator.append(ch)
                int_flag = False
            
            elif ch == ")":
                while(operator[-1] != "("):
                    self.process(operator,operand)
                operator.pop()
                int_flag = False

        while len(operator):
            self.process(operator, operand)
        return operand.pop()
    
    def process(self,operator,operand):
        num2 = operand.pop()
        num1 = operand.pop()
        op = operator.pop()
        
        if op == "+":
            result = num1 + num2
        if op == "-":
            result = num1 - num2
    
        operand.append(result)
        
        