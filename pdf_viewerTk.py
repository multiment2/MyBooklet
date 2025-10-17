# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 08:28:19 2025

@author: MVSORO21
"""
from tkinter import *
from pypdf import PdfReader
 
reader = PdfReader("kol_razum.pdf")
pages = reader.pages[0]
page = pages.extract_text()

root = Tk()
root.title("METANIT.COM")
root.geometry("1200x640")
 
canvas = Canvas(bg="white", width=250, height=200)
canvas.pack(anchor=CENTER, expand=1)
 
#python_image = PhotoImage(file=page)
 
canvas.create_text(300, 200, text=page)
 
root.mainloop()