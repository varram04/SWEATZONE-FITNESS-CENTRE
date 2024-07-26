from tkinter import*
from tkinter import filedialog,messagebox #tkinter-filedialog module provides classes and factory functions for creating file/directory selection windows.
import random # for showing random values or numbers with limits we give
import time # for displaying date in receipt
import requests #external module library

root=Tk()
root.geometry('1350x750+0+0') #0+0 ( X axis and Y-axis )
root.resizable(0,0) #resizable means you can't change the size i.e we cannot maximise the window
root.title('SweatZone Champ Calories Intaker')
root.config(bg='firebrick4') #configure is used to update or authorize
topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')#bd=border , relief =styling like css in HTML
topFrame.pack(side=TOP) #PACK-displays in the window like mainloop()
labelTitle=Label(topFrame,text='✔Sweatzone Champ Calorie Intake✍',font=('arial',30,'bold'),fg='yellow',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0) #grid is used to place it in the window

###############################################defining receipt ######################################

def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()
        auth='pLo3gdKjO4syBHPNwi7QecFk1Mqzr826fhZGCRunXYUIaTVWEbtZgR7uF4kOvoGWQymx29THKNDV5Clw'
        url='https://www.fast2sms.com/dashboard/dev/bulk'

        params={
            'authorization':auth,
            'message':message,
            'numbers':number,
            'sender-id':'FSTSMS',
            'route' :'p',
            'language':'english'
        }
        response=requests.get(url,params=params)#params dictionary 
        dic=response.json() #json converts into dictionary 
        result=dic.get('return')
        if result==True:
            messagebox.showinfo('Send successfully','Message sent successfully')
            
        else:
            messagebox.showerror('Error','Something went wrong')
            
    root2=Toplevel()

    root2.title("SEND BILL")
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')

    
    
    numberLabel=Label(root2,text='Mobile number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberLabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billLabel=Label(root2,text='Bill Details',font=('arial',18,'bold underline'),bg='red4',fg='white')
    billLabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+champnumber+'\t\t'+date+'\n\n')

    textarea.insert(END,f'Calories of Breakfast\t\t\t{calofBreakfast} calories\n\n') # to print calories in the field 
    textarea.insert(END,f'Calories of Lunch\t\t\t{calofLunch} calories\n\n')
    textarea.insert(END,f'Calories of Dinner\t\t\t{calofDinner} calories\n\n')

    textarea.insert(END,'***************************************************************\n')

    textarea.insert(END,f'Subtotal Calories of the Day\t\t\t{subtotalofFood} calories\n\n')
    
    textarea.insert(END,f'Total Calories of the Day\t\t\t{totalofFood} calories\n\n')
    

    sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg) #The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
    sendButton.pack(pady=5)

    root2.mainloop()
    

def save():
   url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') #asksaveasfile() is the function which is used to save user’s file
   bill_data=textReceipt.get(1.0,END)
   url.write(bill_data)
   url.close()
   messagebox.showinfo('Information','Your Bill is successfully is Saved')
   
    
def receipt():
    global champnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,10000)
    champnumber='CHAMP'+str(x) #converting to string
    date=time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Intake Ref:\t\t'+champnumber+'\t\t'+date+'\n') #\t--> TAB spaces \n=new line character
    textReceipt.insert(END,'***************************************************************\n')
    textReceipt.insert(END,'Food Items:\t\t\t Calories of Food\n')
    textReceipt.insert(END,'***************************************************************\n')
    if e_roti.get()!='0':
        textReceipt.insert(END,f'chapati (with kuruma)\t\t\t\t{int(e_roti.get())*180}\n\n') # The get() method returns the value of the item with the specified key.
        
    if e_idli.get()!='0':
        textReceipt.insert(END,f'Idli (with all sides)\t\t\t\t{int(e_idli.get())*90}\n\n')

    if e_dosa.get()!='0':
        textReceipt.insert(END,f'Dosa (with all sides)\t\t\t\t{int(e_dosa.get())*151}\n\n')

    if e_upma.get()!='0':
        textReceipt.insert(END,f'Upma/khichdi (with all sides)\t\t\t\t{int(e_upma.get())*190}\n\n')

    if e_Bread.get()!='0':
        textReceipt.insert(END,f'Bread (per Slice)\t\t\t\t{int(e_Bread.get())*32.0}\n\n')

    
    if e_pongal.get()!='0':
        textReceipt.insert(END,f'Pongal (with all sides)\t\t\t\t{int(e_pongal.get())*212}\n\n')

    
    if e_omelette.get()!='0':
        textReceipt.insert(END,f'Omelette\t\t\t\t{int(e_omelette.get())*154}\n\n')

    if e_cereal.get()!='0':
        textReceipt.insert(END,f'Cereal\t\t\t\t{int(e_cereal.get())*100}\n\n')

    if e_Salad.get()!='0':
        textReceipt.insert(END,f'Salad (veggies/fruits)\t\t\t\t{int(e_Salad.get())*38.8}\n\n')

    if e_sambar.get()!='0':
        textReceipt.insert(END,f'Sambar Rice (with sides)\t\t\t\t{int(e_sambar.get())*210}\n\n')

    if e_rasam.get()!='0':
        textReceipt.insert(END,f'Rasam Rice (with sides)\t\t\t\t{int(e_rasam.get())*147}\n\n')

    if e_curd.get()!='0':
        textReceipt.insert(END,f'Curd Rice (with sides)\t\t\t\t{int(e_curd.get())*207}\n\n')

    if e_lemon.get()!='0':
        textReceipt.insert(END,f'Lemon Rice\t\t\t\t{int(e_lemon.get())*175}\n\n')

    if e_biryani.get()!='0':
        textReceipt.insert(END,f'Biryani\t\t\t\t{int(e_biryani.get())*241}\n\n')

    if e_chicken.get()!='0':
        textReceipt.insert(END,f'Chicken Gravy (with rice)\t\t\t\t{int(e_chicken.get())*190}\n\n')

    if e_fish.get()!='0':
        textReceipt.insert(END,f'Fish Gravy (with rice)\t\t\t\t{int(e_fish.get())*192}\n\n')

    if e_aviyal.get()!='0':
        textReceipt.insert(END,f'Aviyal (with rice)\t\t\t\t{int(e_aviyal.get())*81}\n\n')

    if e_egg.get()!='0':
        textReceipt.insert(END,f'Egg rice\t\t\t\t{int(e_egg.get())*181}\n\n')

    if e_paneer.get()!='0':
        textReceipt.insert(END,f'Paneer Masala (with naan/fulka)\t\t\t\t{int(e_paneer.get())*229}\n\n')

    if e_pizza.get()!='0':
        textReceipt.insert(END,f'Pizza\t\t\t\t{int(e_pizza.get())*266}\n\n')

    if e_burger.get()!='0':
        textReceipt.insert(END,f'Burger (with cheese)\t\t\t\t{int(e_burger.get())*295}\n\n')

    if e_BBQ.get()!='0':
        textReceipt.insert(END,f'BBQ/Grilled (Full)\t\t\t\t{int(e_BBQ.get())*280}\n\n')

    if e_shawarma.get()!='0':
        textReceipt.insert(END,f'Shawarma (single)\t\t\t\t{int(e_shawarma.get())*315}\n\n')

    if e_pasta.get()!='0':
        textReceipt.insert(END,f'Pasta (alfredo/arabito)\t\t\t\t{int(e_pasta.get())*200}\n\n')

    if e_noodles.get()!='0':
        textReceipt.insert(END,f'Noodles (Veg/Non-Veg)\t\t\t\t{int(e_noodles.get())*140}\n\n')

    if e_friedrice.get()!='0':
        textReceipt.insert(END,f'friedrice(Veg/Non-veg)\t\t\t\t{int(e_friedrice.get())*165}\n\n')

    if e_butter.get()!='0':
        textReceipt.insert(END,f'Butter Chicken (with naan/biryani)\t\t\t\t{int(e_butter.get())*288}\n\n')
        
    textReceipt.insert(END,'***************************************************************\n') # insert is used to display in the field provided for receipt 

    textReceipt.insert(END,f'Calories of Breakfast\t\t\t{calofBreakfast} calories\n\n') # to print calories in the field 
    textReceipt.insert(END,f'Calories of Lunch\t\t\t{calofLunch} calories\n\n')
    textReceipt.insert(END,f'Calories of Dinner\t\t\t{calofDinner} calories\n\n')

    textReceipt.insert(END,'***************************************************************\n')

    textReceipt.insert(END,f'Subtotal Calories of the Day\t\t\t{subtotalofFood} calories\n\n')
    
    textReceipt.insert(END,f'Total Calories of the Day\t\t\t{totalofFood} calories\n\n')
    
    textReceipt.insert(END,'***************************************************************\n')


    
    
    
        


 
################################################################################### DEFINING Functions ######################################################################################

def chapati():
    if var1.get()==1:              #The get() method returns the value of the item with the specified key
        textchapati.config(state=NORMAL)
        textchapati.delete(0,END)
        textchapati.focus()      # focus is used to set the focus  to (blink) on the desired widget 
    else:
        textchapati.config(state=DISABLED)
        e_roti.set('0')  # set()--linking the two and converting them to specified value especially  for already defined function 

def idli():
    if var2.get()==1:
        textidli.config(state=NORMAL)
        textidli.delete(0,END)
        textidli.focus()
    else:
        textidli.config(state=DISABLED)
        e_idli.set('0')

def dosa():
    if var3.get()==1:
        textdosa.config(state=NORMAL)
        textdosa.delete(0,END)
        textdosa.focus()
    else:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')

def upma():
    if var4.get()==1:
        textupma.config(state=NORMAL)
        textupma.delete(0,END)
        textupma.focus()
    else:
        textupma.config(state=DISABLED)
        e_upma.set('0')


def Bread():
    if var5.get()==1:
        textBread.config(state=NORMAL)
        textBread.delete(0,END)
        textBread.focus()
    else:
        textBread.config(state=DISABLED)
        e_Bread.set('0')

def pongal():
    if var6.get()==1:
        textpongal.config(state=NORMAL)
        textpongal.delete(0,END)
        textpongal.focus()
    else:
        textpongal.config(state=DISABLED)
        e_pongal.set('0')

def omelette():
    if var7.get()==1:
        textomelette.config(state=NORMAL)
        textomelette.delete(0,END)
        textomelette.focus()
    else:
        textomelette.config(state=DISABLED)
        e_omelette.set('0')


def cereals():
    if var8.get()==1:
        textcereal.config(state=NORMAL)
        textcereal.delete(0,END)
        textcereal.focus()
    else:
        textcereal.config(state=DISABLED)
        e_cereal.set('0')

def Salad():
    if var9.get()==1:
        textSalad.config(state=NORMAL)
        textSalad.delete(0,END)
        textSalad.focus()
    else:
        textSalad.config(state=DISABLED)
        e_Salad.set('0')
        
def sambar():
    if var10.get()==1:
        textsam.config(state=NORMAL)
        textsam.delete(0,END)
        textsam.focus()
    else:
        textsam.config(state=DISABLED)
        e_sambar.set('0')

def rasam():
    if var11.get()==1:
        textrasam.config(state=NORMAL)
        textrasam.delete(0,END)
        textrasam.focus()
    else:
        textrasam.config(state=DISABLED)
        e_rasam.set('0')

def curd():
    if var12.get()==1:
        textcurd.config(state=NORMAL)
        textcurd.delete(0,END)
        textcurd.focus()
    else:
        textcurd.config(state=DISABLED)
        e_curd.set('0')

def lemon():
    if var13.get()==1:
        textlemon.config(state=NORMAL)
        textlemon.delete(0,END)
        textlemon.focus()
    else:
        textlemon.config(state=DISABLED)
        e_lemon.set('0')

def biryani():
    if var14.get()==1:
        textbiryani.config(state=NORMAL)
        textbiryani.delete(0,END)
        textbiryani.focus()
    else:
        textbiryani.config(state=DISABLED)
        e_biryani.set('0')

def chicken():
    if var15.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def fish():
    if var16.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def aviyal():
    if var17.get()==1:
        textaviyal.config(state=NORMAL)
        textaviyal.delete(0,END)
        textaviyal.focus()
    else:
        textaviyal.config(state=DISABLED)
        e_aviyal.set('0')


def egg():
    if var18.get()==1:
        textegg.config(state=NORMAL)
        textegg.delete(0,END)
        textegg.focus()
    else:
        textegg.config(state=DISABLED)
        e_egg.set('0')

def paneer():
    if var19.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def pizza():
    if var20.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete(0,END)
        textpizza.focus()
    else:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')

def burger():
    if var21.get()==1:
        textburger.config(state=NORMAL)
        textburger.delete(0,END)
        textburger.focus()
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

def BBQ():
    if var22.get()==1:
        textBBQ.config(state=NORMAL)
        textBBQ.delete(0,END)
        textBBQ.focus()
    else:
        textBBQ.config(state=DISABLED)
        e_BBQ.set('0')

def shawarma():
    if var23.get()==1:
        textshawarma.config(state=NORMAL)
        textshawarma.delete(0,END)
        textshawarma.focus()
    else:
        textshawarma.config(state=DISABLED)
        e_shawarma.set('0')

def pasta():
    if var24.get()==1:
        textpasta.config(state=NORMAL)
        textSalad.delete(0,END)
        textSalad.focus()
    else:
        textSalad.config(state=DISABLED)
        e_Salad.set('0')
        
def noodles():
    if var25.get()==1:
        textnoodles.config(state=NORMAL)
        textnoodles.delete(0,END)
        textnoodles.focus()
    else:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')

def friedrice():
    if var26.get()==1:
        textfriedrice.config(state=NORMAL)
        textfriedrice.delete(0,END)
        textfriedrice.focus()
    else:
        textfriedrice.config(state=DISABLED)
        e_friedrice.set('0')

def butter():
    if var27.get()==1:
        textbutter.config(state=NORMAL)
        textbutter.delete(0,END)
        textbutter.focus()
    else:
        textbutter.config(state=DISABLED)
        e_butter.set('0')
        
##############################################################TOTAL#######################################################################

def totalcost():
    global calofBreakfast,calofLunch,calofDinner,subtotalofFood,totalofFood
 #Global keyword is a keyword that allows a user to modify a variable outside of the current scope
    item1=int(e_roti.get())
    item2=int(e_idli.get())
    item3=int(e_dosa.get())
    item4=int(e_upma.get())
    item5=int(e_Bread.get())
    item6=int(e_pongal.get())
    item7=int(e_omelette.get())
    item8=int(e_cereal.get())
    item9=int(e_Salad.get())
    item10=int(e_sambar.get())
    item11=int(e_rasam.get())
    item12=int(e_curd.get())
    item13=int(e_lemon.get())
    item14=int(e_biryani.get())
    item15=int(e_chicken.get())
    item16=int(e_fish.get())
    item17=int(e_aviyal.get())
    item18=int(e_egg.get())
    item19=int(e_paneer.get())
    item20=int(e_pizza.get())
    item21=int(e_burger.get())
    item22=int(e_BBQ.get())
    item23=int(e_shawarma.get())
    item24=int(e_pasta.get())
    item25=int(e_noodles.get())
    item26=int(e_friedrice.get())
    item27=int(e_butter.get())

    calofBreakfast=(item1*180)+(item2*90)+(item3*151)+(item4*190)+(item5*32)+(item6*212)+(item7*154)\
                     +(item8*100)+(item9*38.8)
        
    calofLunch=(item10*210)+(item11*147)+(item12*207)+(item13*175)+(item14*241)+(item15*153)\
                 +(item16*142)+(item17*81)+(item18*181)

    calofDinner=(item19*229)+(item20*266)+(item21*295)+(item22*280)+(item23*315)+(item24*200)\
                  +(item25*140)+(item26*165)+(item27*288)
        
    caloofbreakvar.set(str(calofBreakfast)+' calories')   #linking the two and converting them to specified value especially  for already defined function

    calooflunchvar.set(str(calofLunch)+' calories')    

    caloofdinnervar.set(str(calofDinner)+' calories')

    subtotalofFood=calofBreakfast+calofLunch+calofDinner
    subtotalvar.set(str(subtotalofFood)+' calories')

    totalofFood=calofBreakfast+calofLunch+calofDinner
    totalvar.set(str(totalofFood)+' calories')

        
#JAMES CAMERON HOLLYWOOD FRAMES :) ################################## :)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT) #Side gives us the option to show where we want to place in output window

calorieFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
calorieFrame.pack(side=BOTTOM) #gives the in bottom of OUTPUT window 

foodFrame=LabelFrame(menuFrame,text='Breakfast',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='blue')
foodFrame.pack(side=LEFT)

LunchFrame=LabelFrame(menuFrame,text='Lunch',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='blue')
LunchFrame.pack(side=LEFT)

DinnerFrame=LabelFrame(menuFrame,text='Dinner',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='blue')
DinnerFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=8,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

# namakku SORRU oda calories dhan mukkiyam
   #                      -SWEATZONE champs

#Variables---->(defining variables) :)  :)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_idli=StringVar()
e_dosa=StringVar()
e_upma=StringVar()
e_Bread=StringVar()
e_pongal=StringVar()
e_omelette=StringVar()
e_cereal=StringVar()
e_Salad=StringVar()

e_sambar=StringVar() 
e_rasam=StringVar()
e_curd=StringVar() 
e_lemon=StringVar()
e_biryani=StringVar()
e_chicken=StringVar()
e_fish=StringVar()
e_aviyal=StringVar()
e_egg=StringVar()

e_paneer=StringVar()
e_pizza=StringVar()
e_burger=StringVar()
e_BBQ=StringVar()
e_shawarma=StringVar()
e_pasta=StringVar()
e_noodles=StringVar()
e_friedrice=StringVar()
e_butter=StringVar()

e_roti.set('0')
e_idli.set('0')
e_dosa.set('0')
e_upma.set('0')
e_Bread.set('0')
e_pongal.set('0')
e_omelette.set('0')
e_cereal.set('0')
e_Salad.set('0')

e_sambar.set('0')
e_rasam.set('0')
e_curd.set('0')
e_lemon.set('0')
e_biryani.set('0')
e_chicken.set('0')
e_fish.set('0')
e_aviyal.set('0')
e_egg.set('0')

e_paneer.set('0')
e_pizza.set('0')
e_burger.set('0')
e_BBQ.set('0')
e_shawarma.set('0')
e_pasta.set('0')
e_noodles.set('0')
e_friedrice.set('0')
e_butter.set('0')

caloofbreakvar=StringVar()
calooflunchvar=StringVar()
caloofdinnervar=StringVar()
subtotalvar=StringVar()
totalvar=StringVar()


##FOOD - namakku sorru dhan mukkiyam ,calories also mukkiyam (-_-)  #STICKY=W ----> keyword argument and W stands for West DIRECTION

chapati=Checkbutton(foodFrame,text='chapati',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=chapati) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
chapati.grid(row=0,column=0,sticky=W)

idli=Checkbutton(foodFrame,text='Idli',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=idli) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
idli.grid(row=1,column=0,sticky=W)

dosa=Checkbutton(foodFrame,text='Dosa',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=dosa) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
dosa.grid(row=2,column=0,sticky=W)

upma=Checkbutton(foodFrame,text='Upma',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=upma) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
upma.grid(row=3,column=0,sticky=W)

Bread=Checkbutton(foodFrame,text='Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=Bread) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Bread.grid(row=4,column=0,sticky=W)

pongal=Checkbutton(foodFrame,text='Pongal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=pongal) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
pongal.grid(row=5,column=0,sticky=W)

omelette=Checkbutton(foodFrame,text='Omelette',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=omelette) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
omelette.grid(row=6,column=0,sticky=W)

Cereals=Checkbutton(foodFrame,text='Cereals',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=cereals) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Cereals.grid(row=7,column=0,sticky=W)

Salad=Checkbutton(foodFrame,text='Salad',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=Salad) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Salad.grid(row=8,column=0,sticky=W)


### ENTRY FIELDS FOR FOOD ITEMS # # # 

textchapati=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti) #DISABLED--> Cannot access , text variable--->Function Call
textchapati.grid(row=0,column=1)

textidli=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_idli)
textidli.grid(row=1,column=1)

textdosa=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dosa)
textdosa.grid(row=2,column=1)

textupma=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_upma)
textupma.grid(row=3,column=1)

textBread=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Bread)
textBread.grid(row=4,column=1)

textpongal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pongal)
textpongal.grid(row=5,column=1)

textomelette=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_omelette)
textomelette.grid(row=6,column=1)

textcereal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cereal)
textcereal.grid(row=7,column=1)

textSalad=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Salad)
textSalad.grid(row=8,column=1)

### ###### LUNCH ########     # ARIVU LA APPALAM PORIPPOM MAKKALE,FITNESS LA CONCENTRATE PANNUNGA MAKKALE VAANGA - SWEATZONE

sambar=Checkbutton(LunchFrame,text="Sambar Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=sambar)
sambar.grid(row=0,column=0,sticky=W)

rasam=Checkbutton(LunchFrame,text="Rasam Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=rasam)
rasam.grid(row=1,column=0,sticky=W)

curd=Checkbutton(LunchFrame,text="Curd Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=curd)
curd.grid(row=2,column=0,sticky=W)

lemon=Checkbutton(LunchFrame,text="Lemon Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=lemon)
lemon.grid(row=3,column=0,sticky=W)
                       
biryani=Checkbutton(LunchFrame,text="Biryani",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=biryani)
biryani.grid(row=4,column=0,sticky=W)

chicken=Checkbutton(LunchFrame,text="Chicken gravy",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=chicken)
chicken.grid(row=5,column=0,sticky=W)

fish=Checkbutton(LunchFrame,text="Fish Gravy",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=fish)
fish.grid(row=6,column=0,sticky=W)

aviyal=Checkbutton(LunchFrame,text="Aviyal/Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=aviyal)
aviyal.grid(row=7,column=0,sticky=W)

egg=Checkbutton(LunchFrame,text="Egg Rice",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=egg)
egg.grid(row=8,column=0,sticky=W)


###  ENTRY  fields for Lunch ITEMS ###

textsam=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sambar)
textsam.grid(row=0,column=1)

textrasam=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rasam)
textrasam.grid(row=1,column=1)

textcurd=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_curd)
textcurd.grid(row=2,column=1)

textlemon=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lemon)
textlemon.grid(row=3,column=1)

textbiryani=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_biryani)
textbiryani.grid(row=4,column=1)

textchicken=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=5,column=1)

textfish=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=6,column=1)

textaviyal=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_aviyal)
textaviyal.grid(row=7,column=1)

textegg=Entry(LunchFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_egg)
textegg.grid(row=8,column=1)

############## :) DINNER:( ################

Paneer=Checkbutton(DinnerFrame,text='Paneer Masala',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=paneer) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Paneer.grid(row=0,column=0,sticky=W)

Pizza=Checkbutton(DinnerFrame,text='Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=pizza) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Pizza.grid(row=1,column=0,sticky=W)

Burger=Checkbutton(DinnerFrame,text='Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=burger) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Burger.grid(row=2,column=0,sticky=W)

BBQ=Checkbutton(DinnerFrame,text='BBQ/Grilled',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=BBQ) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
BBQ.grid(row=3,column=0,sticky=W)

Shawarma=Checkbutton(DinnerFrame,text='Shawarma',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=shawarma) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Shawarma.grid(row=4,column=0,sticky=W)

Pasta=Checkbutton(DinnerFrame,text='Pasta',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=pasta) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Pasta.grid(row=5,column=0,sticky=W)

Noodles=Checkbutton(DinnerFrame,text='Noodles',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=noodles) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Noodles.grid(row=6,column=0,sticky=W)

FriedRice=Checkbutton(DinnerFrame,text='Fried Rice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=friedrice) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
FriedRice.grid(row=7,column=0,sticky=W)

Butter=Checkbutton(DinnerFrame,text='Butter Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=butter) #on value is 1 that is checked (ticked) , off value is zero that is unchecked (unticked)
Butter.grid(row=8,column=0,sticky=W)

##########Enteries for DINNER ITEMS ###############       #####nenjam undu nermai undu odu raaja####

textpaneer=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=0,column=1)

textpizza=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizza)
textpizza.grid(row=1,column=1)

textburger=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_burger)
textburger.grid(row=2,column=1)

textBBQ=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_BBQ)
textBBQ.grid(row=3,column=1)

textshawarma=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shawarma)
textshawarma.grid(row=4,column=1)

textpasta=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pasta)
textpasta.grid(row=5,column=1)

textnoodles=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_noodles)
textnoodles.grid(row=6,column=1)

textfriedrice=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_friedrice)
textfriedrice.grid(row=7,column=1)

textbutter=Entry(DinnerFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_butter)
textbutter.grid(row=8,column=1)


#############################################################################COST LABELS & ENTRY FIELDS################################################################################################################################################

labelCalofood=Label(calorieFrame,text='Calories of Breakfast',font=('arial',16,'bold'),bg='firebrick4',fg='cyan')
labelCalofood.grid(row=0,column=0)

textCaloofFood=Entry(calorieFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=caloofbreakvar)
textCaloofFood.grid(row=0,column=1,padx=41)


labelCalooflunch=Label(calorieFrame,text='Calories of Lunch',font=('arial',16,'bold'),bg='firebrick4',fg='cyan')
labelCalooflunch.grid(row=1,column=0)

textCalooflunch=Entry(calorieFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=calooflunchvar)
textCalooflunch.grid(row=1,column=1,padx=41)

labelCaloofdinner=Label(calorieFrame,text='Calories of Dinner',font=('arial',16,'bold'),bg='firebrick4',fg='cyan')
labelCaloofdinner.grid(row=2,column=0)

textCaloofdinner=Entry(calorieFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=caloofdinnervar)
textCaloofdinner.grid(row=2,column=1,padx=41)


labelsubtotal=Label(calorieFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='cyan')
labelsubtotal.grid(row=0,column=2)

textsubtotal=Entry(calorieFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)


labeltotalcalo=Label(calorieFrame,text='Total Calories',font=('arial',16,'bold'),bg='firebrick4',fg='cyan')
labeltotalcalo.grid(row=2,column=2)

texttotalcaro=Entry(calorieFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalvar)
texttotalcaro.grid(row=2,column=3,padx=41)

################################ Buttons #########################################################

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
buttonReset.grid(row=0,column=4)

############################## TEXT area FOR reciept ##############

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

########################## CALCULATOR ######################################
operator=''         #String Variable #07+09 example

def buttonClick(numbers):
    global operator  #Global keyword is a keyword that allows a user to modify a variable outside of the current scope
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7')) #lambda-allows to create small, inline functions for the command parameter.
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)



root.mainloop()

