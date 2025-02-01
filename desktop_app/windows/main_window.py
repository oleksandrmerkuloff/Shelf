import customtkinter


class ScrollableBookFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=650, height=700)


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

    def sorting_books(self, choice):
        # Here will be function for sorting books by attr
        print(choice)
