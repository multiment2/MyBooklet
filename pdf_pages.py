# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 08:19:18 2025

@author: MVSORO21
"""


def add_more_pages(list_num_of_pages, sequment):
    """Доведение количества страниц list_num_of_pages (список индексов страниц) 
    до чила, кратного sequment(количество страниц в тетради)"""
    if list_num_of_pages % sequment == 0:
        return [i for i in range(list_num_of_pages)]
    else:
        a = list_num_of_pages // sequment
        b = a * sequment
        c = list_num_of_pages - b
        
        print("Остаток страниц при первом делении: ", a)
        print("Общее число страниц: ", list_num_of_pages)
        print("Новое умножение: ", b)
        print("Результирующий остаток:", c)
        if (list_num_of_pages - c) % sequment == 0:
            print("Надо добавить страниц:", c)
            print ("Добавлено страниц:", c)
            return [i for i in range(list_num_of_pages + c)]
        
        else:
            print("Подумай еще!")
        import sys
        sys.exit("Я не могу сделать это")
    

def split_groups(list_num_of_pages: list, sequment: int) -> list:
    """Разделяет последовательность list_num_of_pages (список шндексов страниц) 
    на куски размером sequments (количество страниц в тетради)"""
    pages_sequments_list = []
    
    for pos in range(0, len(list_num_of_pages), sequment):
        pages_sequments_list.append(list_num_of_pages[pos:pos + sequment])
    
    return pages_sequments_list
   

def shuffle_pages(one_group: list) -> list:
    '''Перемешиваем страницы в списке one_group для печати тетради.
    Для этого делим список на 2 равные части и вторую часть переворачиваем в 
    обратную последователюгость.
    '''
    lst_groups = split_groups(one_group, len(one_group)//2)
    lst_1 = lst_groups[0]
    lst_2 = lst_groups[1]
    lst_2.reverse()
    
    final_list_notebook_pages = []
    for i in range(len(one_group)//2):
        if i == 0 or i%2 == 0:
            final_list_notebook_pages.append(lst_2[i])
            final_list_notebook_pages.append(lst_1[i])
        else:
            final_list_notebook_pages.append(lst_1[i])
            final_list_notebook_pages.append(lst_2[i])
    
    return final_list_notebook_pages
    

def get_final_list(list_groups: list) -> list:
    '''Отправляем список перемешанных групп и объединяем их
    в окончательный список страниц в нужном (перемешанном) порядке.'''
    final_list = []
    for group in list_groups:
        shuf_list = shuffle_pages(group)
        final_list += shuf_list
        
    return final_list