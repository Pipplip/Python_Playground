import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

class MyGui:

    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("PDF Merge (Version 0.1)")
        window_width = 800
        window_height = 600
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

        self.frame_list = tk.Frame(self.__root)
        self.frame_list.pack(fill=tk.BOTH)

        self.label_headline = tk.Label(self.frame_list, text="Ausgewählte PDFs:")
        self.label_headline.pack(side=tk.TOP, fill=tk.X, pady=10)

        #self.entries_set = set(()) # ein Set für die Ergebnisliste
        self.entries_dict = dict(()) # Dictionary für die Ergebnisliste, key = Index in der ListBox
        self.liste_listbox = tk.Listbox(self.frame_list, width=125)
        self.liste_listbox.pack(side=tk.LEFT,fill=tk.BOTH, padx=10)

        self.scrollbar = tk.Scrollbar(self.frame_list)
        self.scrollbar.pack(side=tk.LEFT,fill=tk.BOTH)
        self.liste_listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.liste_listbox.yview)

        '''self.button_up = tk.Button(self.__root, text="Up")
        self.button_up.pack(side=tk.RIGHT)

        self.button_down = tk.Button(self.__root, text="Down")
        self.button_down.pack(side=tk.RIGHT)'''

        self.frame_buttons = tk.Frame(self.__root)
        self.frame_buttons.pack(fill=tk.BOTH)

        self.button_load = tk.Button(self.frame_buttons, text = "Lade PDFs...", command = self.open_filechooser)
        self.button_load.pack(side=tk.LEFT, padx=10)

        self.button_delete_selected = tk.Button(self.frame_buttons, text="Löschen...", state=tk.DISABLED, command=self.delete_item)
        self.button_delete_selected.pack(side=tk.RIGHT, padx=30)

        self.button_delete_all = tk.Button(self.frame_buttons, text="Alle löschen...", state=tk.DISABLED, command=self.delete_all_items)
        self.button_delete_all.pack(side=tk.RIGHT, padx=10)

        self.button_output = tk.Button(self.__root, text="Speicher-Ort", state=tk.NORMAL, command=self.open_output)
        self.button_output.pack()

        #self.entry_content = tk.StringVar(self.__root, "")
        self.label_output = tk.Label(self.__root, text="C:\\Users\\Public\\result.pdf")
        #self.label_output.insert(tk.END, "C:\\Users\\Public\\result.pdf")
        self.label_output.pack(fill=tk.X)

        self.button_merge = tk.Button(self.__root, text="Starte Merge", state=tk.DISABLED, command=self.merge, bg="red")
        self.button_merge.pack()

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def delete_item(self):
        #for i in self.liste_listbox.curselection():
        #    print(self.liste_listbox.get(i))

        selection = self.liste_listbox.curselection() # Gibt den Index des selektierten Elements zurück
        
        if len(selection) == 0:
            self.show_message("Element auswählen")
            return

        for i in reversed(selection):
            print("Delete aus Set: "+self.liste_listbox.get(i))
            #self.entries_set.remove(self.liste_listbox.get(i))
            self.entries_dict.pop(i, None)
            self.liste_listbox.delete(i)

        if self.liste_listbox.size() == 0:
            # disable buttons
            self.set_button_status(False)

        self.print_entries_dict()


    def delete_all_items(self):
        self.liste_listbox.delete(0, tk.END)
        self.entries_dict.clear()
        #self.entries_set.clear()
        # disable buttons
        self.set_button_status(False)

    def open_filechooser(self):
        """ Choose multiple files. If one is not a pdf return False else True"""
        try:
            self.__root.update()
            filename = askopenfilenames(parent=self.__root, filetypes=[("PDFs","*.pdf")]) # show an "Open" dialog box and return the paths to the selected file tupel
            
        except:
            print("Error opening file chooser")
            return False

        #print(filename)
        #print(type(filename))
        # convert tuple to list
        filename = list(filename)
        
        if not filename:
            # Liste ist leer
            return

        for file in filename:
            if not file.lower().endswith(".pdf"):
                print("One of the selected files is not a pdf!")
                self.show_message("Bitte nur PDFs auswählen!")
                return False
        
        # fülle das dict mit den Entries: key=index
        i = 0
        for file in filename:
            self.entries_dict.update({i:file})
            i += 1
            #self.entries_set.add(file)

        # add dictionary in listbox
        for k, v in self.entries_dict.items():
            value = "[" + str(k) + "] " + v
            self.liste_listbox.insert(k, value)

        
        # enable buttons
        self.set_button_status(True)

        self.print_entries_dict()

        return True

    def open_output(self):
        try:
            self.__root.update()
            filename = asksaveasfilename(parent=self.__root, filetypes=[("PDFs","*.pdf")]) # show an "Open" dialog box and return the paths to the selected file tupel
            #print(type(filename))
            if filename != "":
                if not filename.endswith(".pdf"):
                    filename = filename + ".pdf"
                self.label_output.config(text=filename)

            
        except:
            print("Error opening file chooser")
            return False

    def merge(self):
        try:
            pdf_merger = PdfFileMerger()
            tmp_list = list()

            for k, v in self.entries_dict.items():
                input = PdfFileReader(v)
                if input.isEncrypted:
                    input.decrypt('')


            for k, v in self.entries_dict.items():
                print(v)
                pdf_merger.append(str(v))

            #print(str(self.label_output.cget("text")))
            with open(str(self.label_output.cget("text")), "wb") as f_out:
                pdf_merger.write(f_out)

        except:
            (type, value, traceback) = sys.exc_info()
            print("Type: ", type)
            print("Value: ", value)
            print("traceback: ", traceback)
            self.show_message("Fehler beim Erstellen aufgetreten!\r\n" + str(value))
            return

        self.show_message("Merge erfolgreich abgeschlossen!")
        #exit()

    def print_entries_dict(self):
        for k, v in self.entries_dict.items():
            print(k, v)
        

    def set_button_status(self, delete_buttons):
        """ Setze die Buttons nach Status"""
        if delete_buttons:
            self.button_delete_selected.config(state="normal")
            self.button_delete_all.config(state="normal")
        else:
            self.button_delete_selected.config(state="disabled")
            self.button_delete_all.config(state="disabled")

        if self.label_output.cget("text") != "" and delete_buttons and len(self.entries_dict) >=2 :
            self.button_merge.config(state="normal", bg="green", fg="white")
        else:
            self.button_merge.config(state="disabled", bg="red", fg="white")


if __name__ == "__main__":
    myGui = MyGui()


