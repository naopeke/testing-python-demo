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
print(result)


# sequence は探索するリストやシーケンス。
# expected は探したい値。
# finder は、各要素を引数にとって何らかの操作をして、検索に使用する値を返す関数です。

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "John Doe", "age":24},
    {"name": "Jane Doe", "age":30},
    {"name": "Richard Gere", "age":30},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Richard Gere", get_friend_name))

# lambda を使うことで、get_friend_name の代わりに一行で関数を作成することもできます。
# lambda 引数: 式
print(search(friends, "Richard Gere", lambda friend: friend["name"]))