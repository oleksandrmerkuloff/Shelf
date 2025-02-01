import customtkinter

import tkinter as tk


class ShowOnlyBtn(customtkinter.CTkButton):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(
            text='Apply'
        )


class ScrollableBookFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=650, height=700)


class CheckBoxesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # will be frame with checkboxes for show only tags
        self.configure(
            width=220,
            height=320,
        )
        
        # need to create get_tags method for this tags
        self.tags = ['Python', 'SQL', 'Project Managment', 'JS', 'Cybersecurity']
        self.variables = []

        self.setup_checkboxes()

    def setup_checkboxes(self):
        for tag in self.tags:
            var = tk.IntVar()
            tag_checkbox = customtkinter.CTkCheckBox(self, text=tag, variable=var)
            tag_checkbox.grid(sticky=tk.W, ipady=2)
            self.variables.append(var)


class HomePageLabel(customtkinter.CTkLabel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(
            font=('Arial', 28),
        )


class SortingMenu(customtkinter.CTkOptionMenu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Change values to models attr
        self.configure(
            values=[
                'Option 1',
                'Option 2',
                'Option 3',
                'Option 4',
                'Option 5',
            ]
        )
        self.set("None")


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shelf')
        self.geometry('1280x720')
        self.resizable(False, False)

        self.setup_widgets()

    def setup_widgets(self):
        self.book_frame = ScrollableBookFrame(self)
        self.book_frame.place(x=315, y=5)

        self.sorting_label = HomePageLabel(self, text='Sorting')
        self.sorting_label.place(x=112, y=50)

        self.sorting_menu = SortingMenu(self, command=self.sorting_books)
        self.sorting_menu.place(x=90, y=120)

        self.show_only_label = HomePageLabel(self, text='Show Only')
        self.show_only_label.place(x=90, y=200)

        self.show_only_frame = CheckBoxesFrame(self)
        self.show_only_frame.place(x=50, y=270)

        self.show_only_btn = ShowOnlyBtn(self, command=self.show_only_books)
        self.show_only_btn.place(x=150, y=610)

    def sorting_books(self, choice):
        # Here will be function for sorting books by attr
        print(choice)

    def show_only_books(self):
        # Here will be function for show only books what's activated by btn and looking for books tag
        selected_tags = []
        for var, tag in zip(self.show_only_frame.variables, self.show_only_frame.tags):
            if var.get():
                selected_tags.append(tag)
        print(selected_tags)
