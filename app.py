import tkinter as tk
import re

root = tk.Tk()
root.title('Simple Calculator')
root.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.gif'))
root.geometry("300x400")
root.minsize(300, 400)

#---loops for configurating rows and columns
for row in range(6):
    root.rowconfigure(row, weight=1)
        
for col in range(4):
    root.columnconfigure(col, weight=1)
    
#---Display 
display = tk.Entry(root, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=4, ipady=15, padx=6, pady=10, sticky='nesw')

#---Functions---
#---func for button creation   
def create_btn(btn_input, row_num, col_num, col_span = 1):
    btn = tk.Button(root, text=str(btn_input), font=('Arial', 16), command=lambda: btn_click(btn_input))
    btn.grid(row=row_num, column=col_num, columnspan=col_span, sticky='nesw')
#---func for updating values on display    
def update_display(current, btn_value = ''):
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(btn_value))
#---func for calculating finale result and updating it on display    
def calc_and_display_result(val):
    result = eval(val)
    update_display(result)
#---func for calculating percentage
def calc_percentage(current):
    nums = re.split(r'(\+|-|/|\*)', current)
    perc =''
    for val in nums:
        if val.__contains__('%'):
            perc = val.split('%')
    perc_val = (int(perc[0]) / 100) * int(nums[0])
    nums.pop()
    nums.append(str(perc_val))
    return ''.join(nums)
#---    
def check_display(curr, condi, btn_value): #!!!!!!!!!!!!!---opraviť celé pomienenie, tak aby nebolo možné pridať dalšie znamienko,
    if condi not in curr and curr != '' and curr != btn_value: # ak medzi nimi nieje číslo
        update_display(curr, btn_value)                        #---pridať podmienku aby po sebe nenasledovali rozličné znamienka napr(+-)
#---func for handeling button clicks                                                                
def btn_click(btn_input):                                     
    current = display.get()
    #---backspace button 
    if btn_input == '<=':
        current = current[:-1]
        update_display(current)
    #---clear button
    elif btn_input == 'C':
        display.delete(0, tk.END)
    #---percentage button
    elif btn_input == '%':
        check_display(current,'%',btn_input)   
    #---divide button
    elif btn_input == '/':   #---------------odstániť desatinné číslo ak nieje potrebne---------------------
        check_display(current,'/',btn_input)
    #---multiply button
    elif btn_input == '*':
        check_display(current,'*',btn_input)
    #---subtraction button
    elif btn_input == '-':
        check_display(current,'-',btn_input)
    #---addition buttons
    elif btn_input == '+':
        check_display(current,'+',btn_input)
    #---float button
    elif btn_input == '.':
        check_display(current,'.',btn_input)
    #---equal button
    elif btn_input == '=':  #---------------pridať aktiváciu Enterom---------------------
        if current != '':   #---------------Syntax Error---------------------
            #---calculating percentage
            if '%' in current:
                new_current = calc_percentage(current)
                calc_and_display_result(new_current)
            else:
                calc_and_display_result(current)
    #---number buttons
    else:
        update_display(current, btn_input)

#---Buttons
#---1st row
btn_backspace = create_btn('<=',1,0)
btn_clear = create_btn('C',1,1)
btn_percentage = create_btn('%',1,2)
btn_divide = create_btn('/',1,3)
#---2nd row
btn_7 = create_btn(7,2,0)
btn_8 = create_btn(8,2,1)
btn_9 = create_btn(9,2,2)
btn_multiply = create_btn('*',2,3)
#---3rd row
btn_4 = create_btn(4,3,0)
btn_5 = create_btn(5,3,1)
btn_6 = create_btn(6,3,2)
btn_subtraction = create_btn('-',3,3)
#---4th row
btn_1 = create_btn(1,4,0)
btn_2 = create_btn(2,4,1)
btn_3 = create_btn(3,4,2)
btn_addition = create_btn('+',4,3)
#---5th row
btn_0 = create_btn(0,5,0,2)
btn_float = create_btn('.',5,2)
btn_equal = create_btn('=',5,3)
# btn_equal = btn = tk.Button(root, text='=', font=('Arial', 16), command=lambda: btn_click('='))
# btn_equal.tk.bind('<Return>', print('ok'))
# btn_equal.grid(row=5, column=3, sticky='nesw')

root.mainloop()