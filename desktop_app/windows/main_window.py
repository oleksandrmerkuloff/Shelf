import customtkinter


class ScrollableBookFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=650, height=700)


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shelf')
        self.geometry('1280x720')
        self.resizable(False, False)

        # widgets config
        self.book_frame = ScrollableBookFrame(self)
        self.book_frame.place(x=315, y=5)
