# Main.py
from my_level_class import MyLevelClass # from <Filename> import <Name of class>
from sub_dir.my_sub_class import MySubClass
import MyModule # Import Module: Ein Modul ist im Endeffekt eine .py Datei, daraus kann man Klassen, Funktionen, Variablen etc. aufrufen

# Create an instance of MyClass
my_instance = MyLevelClass("LevelClass")
my_instance_sub = MySubClass("SubClass")

# Call the greet method
print(my_instance.greet())
print(my_instance_sub.greet())

MyModule.module_func() # Funktion aufrufen

my_instance_module_class = MyModule.MyModuleClass("ModuleClass") #Klasse aufrufen
print(my_instance_module_class.greet())