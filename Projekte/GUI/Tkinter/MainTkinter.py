'''
Insgesamt gibt es 15 sogenannte widges:
- Button
- Canvas: Leinwand für Linien, Ovals, Polygone, Rechtecke etc.
- Checkbutton
- Entry: einzeiliges Textfeld für Eingaben
- Frame
- Label
- Listbox: Anzeige einer Liste
- Menubutton: Teil eines Dropdown Menüs
- Menu
- Message: Message Dialog
- Radiobutton
- Scale: Slider
- Scrollbar
- Text: Textfeld mehrzeilig
- Toplevel
- Spinbox: Eingabefeld wie Entry mit Cursor hoch runter um Werte zu erhöhen/reduzieren 
- PanedWindow
- LabelFrame: Rahmen mit einer Beschriftung
- messagebox: Message in eigenem Dialog

Geometry: Anordnung der widgets
1) pack(): organisiere widget im Block. Als Parameter gehen expand, fill, size
2) grid(): Anordnung in Tabellen Grid Form (Spalten, Zeilen)
3) place(): exakte Positionierung anhand der x,y Koordinaten z.B. button1.place(x = 35,y = 50)

'''
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import S

class MyGui:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Main Window")
        #self.__root.geometry("800x600")
        #self.__root.attributes("-fullscreen", True) # fullscreen without titlebar
        #self.__root.state('zoomed') # fullscreen with titlebar

        window_width = 1024
        window_height = 768
        # get the screen size of your computer [width and height using the root object as foolows]
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        # Get the window position from the top dynamically as well as position from left or right as follows
        position_top = int(screen_height/2 -window_height/2)
        position_right = int(screen_width / 2 - window_width/2)
        # this is the line that will center your window
        self.__root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


        self.__init_widges()

        self.__root.mainloop()

    def __init_widges(self):
        """ initialisiere alle GUI Komponenten beim Start der Anwendung """
        self.label1 = tk.Label(self.__root, text="Es gibt 15 widgets (GUI Komponenten)", bg="yellow")
        self.label1.pack(side=tk.TOP, fill=tk.X)

        # Button
        self.button1 = tk.Button(self.__root, text = "Klick mich", fg = "red", command = self.hello)
        self.button1.place(x = 35,y = 50)
        #message.pack()

        # Button
        self.button_filechooser = tk.Button(self.__root, text = "Choose file", command = self.print_on_label)
        self.button_filechooser.place(x = 35,y = 80)

        # Frame mit Eingabefeld Entry und Label
        self.entry_frame = tk.Frame(self.__root, bg="yellow")
        self.entry_frame.pack(side=tk.BOTTOM, fill=tk.X) # füllt auf x Ebene
        self.name_label = tk.Label(self.entry_frame, text="Name", fg="white", bg="blue")
        #self.name_label.grid(row=0, column=0)
        self.name_label.pack(side=tk.TOP)

        self.entry_content = tk.StringVar(self.__root, "Default Value") # extra variable für den Inhalt des Entry
        self.name_entry = tk.Entry(self.entry_frame, textvariable=self.entry_content)
        #self.name_entry.grid(row=0, column=1)
        self.name_entry.pack(side=tk.TOP)


    def hello(self):
        messagebox.showinfo("Title", "Hello World")

    def print_on_label(self):
        # überschreibe label1 mit dem Inhalt von Entry name_entry
        self.label1.config(text=self.entry_content.get(),font=('Helvetica bold',40))



        


if __name__ == "__main__":
    myGui = MyGui()


