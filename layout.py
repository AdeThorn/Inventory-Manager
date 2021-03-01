import tkinter as tk
from tkinter import ttk    
import buy_tab 
import sell_tab

def fetch():
    name_info=entries[0].get()
    price_info=entries[1].get()
    brand_info=entries[2].get()
    size_info=entries[3].get()
    
    #put all entries in a list
    list_entries=[name_info,price_info,size_info,brand_info]
    
    #verify format of price
    price=price_info
    #remove dot and $ in price and see if its digit
    if "$" in price:
        price=price.split("$")[1] #assums $ at front
    if "." in price:
        price="".join(price.split("."))
    price=price.split()[0]
    

    if  price.isdigit():
        out.delete(0.0,tk.END)
        out.insert(tk.END,'Submitted')
        buy_tab.add_to_stock(list_entries,"./docs/inventory.xlsx")
    else:
        out.delete(0.0,tk.END)
        out.insert(tk.END,'Price is of wrong format: need (#.##)')
   
    
root=tk.Tk()
root.title('bam bam')
root.geometry('500x500')

#make root background black
root.configure(background='black')

#Define grid

rows=0
while rows<50:
    root.rowconfigure(rows,weight=1)
    root.columnconfigure(rows,weight=1)
    rows+=1

#create notebook object and attach it to
#to main window
nb=ttk.Notebook(root)         
nb.grid(row=1,column=0,columnspan=50,rowspan=49,sticky='NESW')

###############################################bought_tab##############################################################

bought_tab =ttk.Frame(nb)   #attaching page 1 to notebook
nb.add(bought_tab, text='Bought')       


#make tuple to hold name of entry fields in buy tab
fields=('What item have you purchased recently: ', 'Price: ','Brand: ','Size: ')



#make labels and entry boxes for each label
entries=[]
for i in range(len(fields)-1):
    row=tk.Frame(bought_tab)
    #make labels for each field
    item_text=tk.Label(row,text=fields[i],bg='white',fg='black',anchor='w')

    item=tk.StringVar()
    #make entry box for each label and hold entry in variable
    item_entry=tk.Entry(row,textvariable=item)
    row.pack(side=tk.TOP, fill=tk.X, padx=5,pady=5)
    item_text.pack(side=tk.LEFT)
    item_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

    #put entries in entry list
    entries.append(item)

row=tk.Frame(bought_tab)
size_text=tk.Label(row,text=fields[3],bg='white',fg='black',anchor='w')
size=tk.DoubleVar()

#make entry box for size
size_entry=tk.Entry(row,textvariable=size)
row.pack(side=tk.TOP, fill=tk.X, padx=5,pady=5)
size_text.pack(side=tk.LEFT)
size_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)
entries.append(size)

#make output box to verify wheter inputs are of correct form
out=buy_tab.make_output_box(bought_tab)

#make a submit button which gets all the data entered in form
submit_but=tk.Button(bought_tab,text='submit',width=6,command=fetch)
submit_but.pack(side=tk.TOP)

################################################sold_tab################################################################
sold_tab =ttk.Frame(nb)   #attaching page 1 to notebook
nb.add(sold_tab, text='Sold')      

sell_page=tk.Frame(sold_tab)
#Make label to find out which sneaker user sold
sell_text=tk.Label(sell_page,text='Which sneaker have you sold recently: ',bg='white',fg='black')
#position label
sell_page.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)
sell_text.pack(side=tk.LEFT)

#make text entry for user to input what sneaker he sold
sell_entry=tk.Entry(sell_page,textvariable=tk.StringVar)

def onReturn(event):
    #make output box that shows possible sneakers based on name typed
    possible_s=sell_tab.get_options(sell_entry.get(),sell_tab.get_stock_sheet())
    
    box.delete(0.0,tk.END) #delete old contents of box
    for i in possible_s:
        box.insert(tk.END,i)

#function for submitting ID of sneaker to sell
def sub_id():
    id_num=id_entry.get()
    price=price_sold_entry.get()
    sell_tab.sell_sneaker(int(id_num),str(price),"./docs/inventory.xlsx")
    print("Sold!")


#bind sell_entry with enter key 
sell_entry.bind("<Return>",onReturn)
sell_entry.pack(side=tk.LEFT,expand=tk.YES,fill=tk.X)

#FRAME
sell_page=tk.Frame(sold_tab)
sell_page.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)


box=tk.Text(sell_page,width=75,height=4,wrap=tk.WORD,bg='white')
box.pack(side=tk.RIGHT)    



#FRAME
sell_page=tk.Frame(sold_tab)
sell_page.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)

#make box to enter id
id_enter_label= tk.Label(sell_page,text="Enter ID",bg='white',fg='black')
id_enter_label.pack(side=tk.LEFT)

id_to_sell=tk.IntVar()
id_entry=tk.Entry(sell_page,textvariable=id_to_sell)
id_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

#FRAME
sell_page=tk.Frame(sold_tab)
sell_page.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)

#make box to enter price sold for
price_sold_label= tk.Label(sell_page,text="Enter price sold for",bg='white',fg='black')
price_sold_label.pack(side=tk.LEFT)

PRICE_SOLD=tk.IntVar()
price_sold_entry=tk.Entry(sell_page,textvariable=PRICE_SOLD)
price_sold_entry.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)

#FRAME
sell_page=tk.Frame(sold_tab)
sell_page.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)

#make submit button for entering id
id_submit=tk.Button(sell_page,text='submit',width=6,command=sub_id)
id_submit.pack(side=tk.BOTTOM)

#run main loop
root.mainloop()