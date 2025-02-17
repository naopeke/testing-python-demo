from typing import List, Optional

# class Student:
#     def __init__(self, name: str, grades: List[int]=[]): # This is bad!! grades: List[int]=[] というデフォルト引数は、Student クラスのすべてのインスタンスで同じリストを共有してしまいます
#         self.name = name
#         self.grades = grades
    
#     def take_exam(self, result):
#         self.grades.append(result)


# bob = Student("Bob")
# rolf = Student("Rolf")
# bob.take_exam(90)
# print(bob.grades) #[90]
# print(rolf.grades)#[90]← rolfのgradesも変更されている！


class Student:
    def __init__(self, name: str, grades: Optional[List[int]]= None): # デフォルト値を None にすることで、デフォルト引数が共有される問題を回避
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades) #[90]
print(rolf.grades)#[90]← rolfのgradesも変更されている！