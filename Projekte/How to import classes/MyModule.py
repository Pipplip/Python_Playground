#MyModule

class MyModuleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
    

def module_func():
    print("Ich bin nur eine Funktion, ausserhalb der Klasse")
    # Aufruf im Main.py-> MyModule.module_func()