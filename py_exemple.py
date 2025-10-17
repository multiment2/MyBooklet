# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 07:24:31 2025

@author: MVSORO21
"""
#import sys
from pypdf import PdfReader, PdfWriter
 #Версия pypdf == 3.15.2

import pdf_pages as pp

#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


reader = PdfReader("book_pdf.pdf")
pages = reader.pages
num_of_pages = len(reader.pages)

output_pdf = PdfWriter()


paper_lists = 4 #Количество физических листов в тетради
notebook_pages = 4*paper_lists #Количество страниц в тетради


list_numbers = pp.add_more_pages(num_of_pages, notebook_pages)
    

groups = pp.split_groups(list_numbers,notebook_pages)


# Заполняем файл PDF по одной странице
print_pages = pp.get_final_list(groups)
for page in print_pages:
    try:
        output_page = pages[page]
        output_pdf.add_page(output_page)
    except:
        output_pdf.add_blank_page() 
    
    
output_pdf.write("print_book_pdf.pdf")
