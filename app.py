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
    
#---func for Error Handaling
def err_handle():
    update_display('0')
    
#---func for updating values on display    
def update_display(current, btn_value = ''):
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(btn_value))
    
#---func for calculating finale result and updating it on display    
def calc_and_display_result(val, btn_input = ''):
    try:
        result = str(eval(val))
        #---checking if result is a whole number writen as float. If yes, display only whole number 
        if '.' in result and len(result) == 3 and result[-1] == '0':
            whole_num = result[0] 
            update_display(whole_num, btn_input)
        else:
            update_display(result,btn_input)
    except SyntaxError as err:
        print(err) 
        err_handle()
    except TypeError as err:
        print(err)  
        err_handle()
        
#---func for calculating percentage
def calc_percentage(current):
    try:
        nums = re.split(r'(\+|-|/|\*)', current)
        perc = ''
        #---finding value with percentage
        for val in nums:
            if '%' in val:
                perc = val.split('%')
        perc_val = (int(perc[0]) / 100) * int(nums[0])    
        nums.pop()
        nums.append(str(perc_val))
        return ''.join(nums)
    except ValueError as err:
        print(err)
        err_handle()

#---func for handeling button clicks                                                                
def btn_click(btn_input):                                     
    current = display.get()
    current_isnot_empty = current != ''
    #---backspace button 
    if btn_input == '<=':
        current = current[:-1]
        update_display(current)
    #---clear button
    elif btn_input == 'C':
        display.delete(0, tk.END)
    #---percentage button
    elif btn_input == '%':
        if current_isnot_empty:
            update_display(current, btn_input)   
    #---divide button
    elif btn_input == '/':  
        if current_isnot_empty:
            update_display(current, btn_input)
    #---multiply button
    elif btn_input == '*':
        if current_isnot_empty:
            update_display(current, btn_input)
    #---addition buttons
    elif btn_input == '+':
        if current_isnot_empty:
            update_display(current, btn_input)
    #---float button
    elif btn_input == '.':
        if current_isnot_empty:  
            update_display(current, btn_input)
    #---subtraction button
    elif btn_input == '-':
        update_display(current, btn_input)
    #---equal button
    elif btn_input == '=' or display.bind('<Return>'):  #---------------prida?? aktiv??ciu Enterom---------------------
        if current != '':  
            #---calculating percentage
            if '%' in current:
                new_current = calc_percentage(current)
                calc_and_display_result(new_current)
            else:
                calc_and_display_result(current)
    #---number buttons            
    else:
        update_display(current, btn_input)

    #---if users adds more than one operation 
    #--- calculates current and adds operator 
    if '+' or '-' or '*' or '/' in current:
        if btn_input == '+':
            calc_and_display_result(current, btn_input)
        elif btn_input == '-':
            calc_and_display_result(current, btn_input)
        elif btn_input == '*':
            calc_and_display_result(current, btn_input)
        elif btn_input == '/':
            calc_and_display_result(current, btn_input)

#---Buttons---
#---backspace
create_btn('<=',1,0)
#---clear
create_btn('C',1,1)
#---percentage
create_btn('%',1,2)
#---divide
create_btn('/',1,3)
#---multiply
create_btn('*',2,3)
#---subtracion
create_btn('-',3,3)
#---addition
create_btn('+',4,3)
#---float
create_btn('.',5,2)
#---equal
create_btn('=',5,3)
#---numbers
#---zero
create_btn(0,5,0,2)
#---nums from 1 to 9
btn_val = 1
for row in range(4,1,-1):
    for col in range(0,3):
        create_btn(btn_val, row, col)
        btn_val += 1
    
  

root.mainloop()