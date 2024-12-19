class ClassTest:
    def instance_method(self):
        print(f"called instance_method {self}")

test = ClassTest()
test.instance_method() # called instance_method <__main__.ClassTest object at 0x000001E2087C6A50>
ClassTest.instance_method(test) # called instance_method <__main__.ClassTest object at 0x000001E2087C6A50>


class ClassTest2:
    def instance_method(self):
        print(f"called instance_method {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

ClassTest2.class_method() # Called class_method of <class '__main__.ClassTest2'>


class ClassTest3:
    def instance_method(self):
        print(f"called instance_method {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method")

ClassTest3.static_method() # Called class_method of <class '__main__.ClassTest2'>