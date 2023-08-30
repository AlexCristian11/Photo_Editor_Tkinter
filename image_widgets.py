import customtkinter as ctk


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(parent)
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')
        self.import_func = import_func

        self.button = ctk.CTkButton(self, text='Open Image', command=self.open_dialog)
        self.button.pack(expand=True)

    def open_dialog(self):
        path = 'test'
        self.import_func(path)
