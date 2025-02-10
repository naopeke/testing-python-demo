# import mymodule
from mymodule import divide

print("code.py:", __name__)

# 下記の順番で出力される
# operator.py: libs.operations.operator
# mylib.py: libs.mylib
# mymodule.py: mymodule
# code.py: __main__