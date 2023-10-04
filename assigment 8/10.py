 class MyClass:
    def _init_(self, name):
        self.name = name
    def get_class_name(self):
        return self._class.name_
my_instance = MyClass("MyInstance")
print(my_instance.get_class_name())