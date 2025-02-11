# dividend は「割られる数」、つまり分子
# divisor は「割る数」、つまり分母

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

# この関数は、いろいろな 引数 (values) と演算子 (operator) を渡す ために使います。
#  *values は「可変長引数」で、複数の値をリストのように渡せるようになっています。例えば 20, 4 などです。
#  operator は、何かしらの演算を実行するための関数です。ここでは、divide を渡しています。
def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)

