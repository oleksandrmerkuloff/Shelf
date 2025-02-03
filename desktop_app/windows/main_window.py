import customtkinter

import tkinter as tk
import time

from .account import MyAccountWindow


class SearchEntry(customtkinter.CTkEntry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(
            placeholder_text='Enter book or author: ',
            width=220
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
            height=250,
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
        self.set(self.cget('values')[0])


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shelf')
        self.geometry('1280x720')
        self.resizable(False, False)

        self.setup_widgets()

        # windows
        self.account_window = None

    def setup_widgets(self):
        # Central widget
        self.book_frame = ScrollableBookFrame(self)
        self.book_frame.place(x=315, y=5)

        # Left side
        self.search_entry = SearchEntry(self)
        self.search_entry.bind('<Return>', self.search_book)
        self.search_entry.place(x=50, y=90)

        self.search_btn = customtkinter.CTkButton(self, text='Search',
                                                  width=80,
                                                  command=self.search_book)
        self.search_btn.place(x=190, y=130)

        self.sorting_label = HomePageLabel(self, text='Sorting')
        self.sorting_label.place(x=112, y=210)

        self.sorting_menu = SortingMenu(self, command=self.sorting_books)
        self.sorting_menu.place(x=90, y=250)

        self.show_only_label = HomePageLabel(self, text='Show Only')
        self.show_only_label.place(x=50, y=340)

        self.show_only_frame = CheckBoxesFrame(self)
        self.show_only_frame.place(x=50, y=380)

        self.show_only_btn = customtkinter.CTkButton(self, text='Apply',
                                                     command=self.show_only_books)
        self.show_only_btn.place(x=150, y=660)

        # Right side
        # Change theme btn will be change by icon
        self.change_theme_btn = customtkinter.CTkButton(self, text='theme switcher',
                                                        width=50)
        self.change_theme_btn.place(x=1150, y=20)

        self.account_btn = customtkinter.CTkButton(self, text='My Account',
                                                   command=self.open_account_window)
        self.account_btn.place(x=1060, y=200)

        self.add_book_btn = customtkinter.CTkButton(self, text='Add Book',
                                                    command=self.add_book)
        self.add_book_btn.place(x=1060, y=250)

        self.my_shelf_btn = customtkinter.CTkButton(self, text='My Shelf',
                                                   command=self.my_shelf)
        self.my_shelf_btn.place(x=1060, y=300)

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

    def search_book(self, event=None):
        # here will be book searching by author or title
        search_request_text = self.search_entry.get()
        print(search_request_text)
        self.search_entry.delete(0, 'end')

    def open_account_window(self):
        if self.account_window is None or not self.account_window.winfo_exists():
            self.account_window = MyAccountWindow()
        else:
            self.account_window.focus()

    def add_book(self):
        # open account window
        print('Add new book')

    def my_shelf(self):
        # open my shelf window
        print('My shelf')
