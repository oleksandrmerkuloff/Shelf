import customtkinter
from windows.main_window import MainWindow


customtkinter.deactivate_automatic_dpi_awareness()

app = MainWindow()
app.mainloop()
