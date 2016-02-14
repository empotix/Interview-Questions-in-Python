'''
Input: A string equation that contains numbers, '+' and '*' 
Output: Result as int. 

For example: 
Input: 3*5+8 (as String) 
Output: 23 (as int)

Input: 3*5+8+5*4*3 (as String) 
Output: 83 (as int)
'''

def evaluate(exp):
    add_exprs = []
    mult_exprs = exp.split('+')
    
    for expr in mult_exprs:
        val = 1
        for operand in expr.split('*'):
            val = val * int(operand)
        add_exprs.append(val)
        
    output = 0
    for operand in add_exprs:
        output += operand

    print(output)
    
evaluate("3*5+8") 
evaluate("3*5+8+5*4*3")