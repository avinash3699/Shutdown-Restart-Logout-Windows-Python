from tkinter import *
from tkinter import ttk
import os 

window = Tk()
window.title("Logout Manager")

def shutdown_window():

	shutdown_win = Toplevel(window)
	shutdown_win.title("Shutdown")

	Label(shutdown_win, text = "Are you sure you want to shutdown your computer now?").grid(row = 0, columnspan = 2, padx = 10, pady = 10)
	ttk.Button(shutdown_win, text = "Confirm", command = shutdown).grid(row = 1, column = 0, pady = 10)
	ttk.Button(shutdown_win, text = "Cancel", command = shutdown_win.destroy).grid(row = 1, column = 1, pady = 10)


def restart_window():

	restart_win = Toplevel(window)
	restart_win.title("Restart")

	Label(restart_win, text = "Are you sure you want to restart your computer now?").grid(row = 0, columnspan = 2, padx = 10, pady = 10)
	ttk.Button(restart_win, text = "Confirm", command = restart).grid(row = 1, column = 0, pady = 10)
	ttk.Button(restart_win, text = "Cancel", command = restart_win.destroy).grid(row = 1, column = 1, pady = 10)


def logout_window():

	logout_win = Toplevel(window)
	logout_win.title("Logout")

	Label(logout_win, text = "Are you sure you want to logout your computer now?").grid(row = 0, columnspan = 2, padx = 10, pady = 10)
	ttk.Button(logout_win, text = "Confirm", command = logout).grid(row = 1, column = 0, pady = 10)
	ttk.Button(logout_win, text = "Cancel", command = logout_win.destroy).grid(row = 1, column = 1, pady = 10)


def shutdown():
	os.system("shutdown /s /t 1")

def restart():
	os.system("shutdown /r /t 1")

def logout():
	os.system("shutdown -l")

shutdown_image = PhotoImage(file = "Shutdown.png")
restart_image = PhotoImage(file = "Restart.png")
logout_image = PhotoImage(file = "Logout.png")

shutdown_button = Button(window, image = shutdown_image, command = shutdown_window, bd = 0, cursor = "hand2").grid(row = 0,column = 1, padx = 12, pady = 15)
restart_button = Button(window, image = restart_image, command = restart_window, bd = 0, cursor = "hand2").grid(row = 0,column = 0, padx = 12)
logout_button = Button(window, image = logout_image,  command = logout_window, bd = 0, cursor = "hand2").grid(row = 0, column = 2, padx = 12)

Shutdown_button = Label(window, text = "Shutdown", width = 8).grid(row = 1,column = 1, pady = 5)
restart_button = Label(window, text = "Restart", width = 8).grid(row = 1,column = 0)
logout_button = Label(window, text = "Logout", width = 8).grid(row=1, column =2)

window.mainloop()