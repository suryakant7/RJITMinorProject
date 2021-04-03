from tkinter import*
import random
import time;
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1350x800+0+0")
root.title("Fast Food Management System")
root.configure(background='purple1')

#---------------------------first 3 frames---------------------
Tops = Frame(root, width= 1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width= 900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width= 440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

#----------------------------frame subdivision-----------------
f1a = Frame(f1, width= 900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width= 900, height=330, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width= 440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width= 440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width= 400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width= 400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='purple1')
f1.configure(background='purple1')
f2.configure(background='purple1')

lblInfo = Label(Tops, font=('arial',67,'bold'), text= "Fast Food Management System", bd=10)
lblInfo.grid(row=0,column=0)

#-------------------------------Methods-------------------------------

def CostofItem():
    Item1 = float(E_Chole_Bhature.get())
    Item2 = float(E_Poha_Jalebi.get())
    Item3 = float(E_Aloo_Tikki.get())
    Item4 = float(E_Vada_Pao.get())
    Item5 = float(E_Kachori.get())
    Item6 = float(E_Egg_Roll.get())
    Item7 = float(E_Idli_Sambhar.get())
    Item8 = float(E_Dhosa.get())

    Item9 = float(E_Mango_Shake.get())
    Item10 = float(E_Banana_Shake.get())
    Item11 = float(E_Mix_Fruit_Juice.get())
    Item12 = float(E_Pineapple_Juice.get())
    Item13 = float(E_Anar_Juice.get())
    Item14 = float(E_Orange_Juice.get())
    Item15 = float(E_Soda.get())
    Item16 = float(E_Red_Vine.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice = "Rs", str('%.2f' % (PriceofDrinks))
    CakesPrice = "Rs", str('%.2f' % (PriceofCakes))
    Costoffastfood.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs", str('%.2f' % (1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs", str('%.2f' % ((PriceofDrinks + PriceofCakes + 1.59) * 0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
    TC = "Rs", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)


def qExit():
    qExit= messagebox.askyesno("Quit System","Do you want to quit")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    Costoffastfood.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Chole_Bhature.set("0")
    E_Poha_Jalebi.set("0")
    E_Aloo_Tikki.set("0")
    E_Vada_Pao.set("0")
    E_Kachori.set("0")
    E_Egg_Roll.set("0")
    E_Idli_Sambhar.set("0")
    E_Dhosa.set("0")

    E_Mango_Shake.set("0")
    E_Banana_Shake.set("0")
    E_Mix_Fruit_Juice.set("0")
    E_Pineapple_Juice.set("0")
    E_Anar_Juice.set("0")
    E_Orange_Juice.set("0")
    E_Soda.set("0")
    E_Red_Vine.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtChole_Bhature.configure(state=DISABLED)
    txtPoha_Jalebi.configure(state=DISABLED)
    txtAloo_Tikki.configure(state=DISABLED)
    txtVada_Pao.configure(state=DISABLED)
    txtKachori.configure(state=DISABLED)
    txtEgg_Roll.configure(state=DISABLED)
    txtIdli_Sambhar.configure(state=DISABLED)
    txtDhosa.configure(state=DISABLED)

    txtMango_Shake.configure(state=DISABLED)
    txtBanana_Shake.configure(state=DISABLED)
    txtMix_Fruit_Juice.configure(state=DISABLED)
    txtPineapple_Juice.configure(state=DISABLED)
    txtAnar_Juice.configure(state=DISABLED)
    txtOrange_Juice.configure(state=DISABLED)
    txtSoda.configure(state=DISABLED)
    txtRed_Vine.configure(state=DISABLED)


def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items:\t\t\t\t\t'+ "Cost of Items\n\n")
    txtReceipt.insert(END, 'Chole_Bhature:\t\t\t\t\t' + E_Chole_Bhature.get() + "\n")
    txtReceipt.insert(END, 'Poha_Jalebi:\t\t\t\t\t' + E_Poha_Jalebi.get() + "\n")
    txtReceipt.insert(END, 'Aloo Tikki:\t\t\t\t\t' + E_Aloo_Tikki.get() + "\n")
    txtReceipt.insert(END, 'Vada Pao:\t\t\t\t\t' + E_Vada_Pao.get() + "\n")
    txtReceipt.insert(END, 'Kachori:\t\t\t\t\t' + E_Kachori.get() + "\n")
    txtReceipt.insert(END, 'Egg Roll:\t\t\t\t\t' + E_Egg_Roll.get() + "\n")
    txtReceipt.insert(END, 'Idli:\t\t\t\t\t'+ E_Idli_Sambhar.get() + "\n")
    txtReceipt.insert(END, 'Dhosa:\t\t\t\t\t' + E_Dhosa.get() + "\n")
    txtReceipt.insert(END, 'Mango Shake:\t\t\t\t\t' + E_Mango_Shake.get() + "\n")
    txtReceipt.insert(END, 'Mix Fruit Juice:\t\t\t\t\t' + E_Banana_Shake.get() + "\n")
    txtReceipt.insert(END, 'Pineapple Juice:\t\t\t\t\t' + E_Mix_Fruit_Juice.get() + "\n")
    txtReceipt.insert(END, 'Pine Apple Juice:\t\t\t\t\t' + E_Pineapple_Juice.get() + "\n")
    txtReceipt.insert(END, 'Anar Juice:\t\t\t\t\t' + E_Anar_Juice.get() + "\n")
    txtReceipt.insert(END, 'Orange Juice:\t\t\t\t\t'+ E_Orange_Juice.get() + "\n")
    txtReceipt.insert(END, 'Soda:\t\t\t\t\t' + E_Soda.get() + "\n")
    txtReceipt.insert(END, 'Red Wine:\t\t\t\t\t' + E_Red_Vine.get() + "\n")
    txtReceipt.insert(END, 'Cost of Drinks:\t\t' + CostofDrinks.get() + '\tTax Paid:\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes:\t\t' + Costoffastfood.get() + '\tSubTotal:\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t' + ServiceCharge.get() + '\tTotal Cost:\t\t' + TotalCost.get() + "\n")
#------------------------------------Checkbutton------------------------------
def chkbutton_value():
    if (var1.get() == 1):
        txtChole_Bhature.configure(state=NORMAL)
    elif var1.get()==0:
        txtChole_Bhature.configure(state=DISABLED)
        E_Chole_Bhature.set("0")
    if (var2.get() == 1):
        txtPoha_Jalebi.configure(state=NORMAL)
    elif var2.get()==0:
        txtPoha_Jalebi.configure(state=DISABLED)
        E_Poha_Jalebi.set("0")
    if (var3.get() == 1):
        txtAloo_Tikki.configure(state=NORMAL)
    elif var3.get()==0:
        txtAloo_Tikki.configure(state=DISABLED)
        E_Aloo_Tikki.set("0")
    if (var4.get() == 1):
        txtVada_Pao.configure(state=NORMAL)
    elif var4.get()==0:
        txtVada_Pao.configure(state=DISABLED)
        E_Vada_Pao.set("0")
    if (var5.get() == 1):
        txtKachori.configure(state=NORMAL)
    elif var5.get()==0:
        txtKachori.configure(state=DISABLED)
        E_Kachori.set("0")
    if (var6.get() == 1):
        txtEgg_Roll.configure(state=NORMAL)
    elif var6.get()==0:
        txtEgg_Roll.configure(state=DISABLED)
        E_Egg_Roll.set("0")
    if (var7.get() == 1):
        txtIdli_Sambhar.configure(state=NORMAL)
    elif var7.get()==0:
        txtIdli_Sambhar.configure(state=DISABLED)
        E_Idli_Sambhar.set("0")
    if (var8.get() == 1):
        txtDhosa.configure(state=NORMAL)
    elif var8.get()==0:
        txtDhosa.configure(state=DISABLED)
        E_Dhosa.set("0")
    if (var9.get() == 1):
        txtMango_Shake.configure(state=NORMAL)
    elif var9.get()==0:
        txtMango_Shake.configure(state=DISABLED)
        E_Mango_Shake.set("0")
    if (var10.get() == 1):
        txtBanana_Shake.configure(state=NORMAL)
    elif var10.get()==0:
        txtBanana_Shake.configure(state=DISABLED)
        E_Banana_Shake.set("0")
    if (var11.get() == 1):
        txtMix_Fruit_Juice.configure(state=NORMAL)
    elif var11.get()==0:
        txtMix_Fruit_Juice.configure(state=DISABLED)
        E_Mix_Fruit_Juice.set("0")
    if (var12.get() == 1):
        txtPineapple_Juice.configure(state=NORMAL)
    elif var12.get()==0:
        txtPineapple_Juice.configure(state=DISABLED)
        E_Pineapple_Juice.set("0")
    if (var13.get() == 1):
        txtAnar_Juice.configure(state=NORMAL)
    elif var13.get()==0:
        txtAnar_Juice.configure(state=DISABLED)
        E_Anar_Juice.set("0")
    if (var14.get() == 1):
        txtOrange_Juice.configure(state=NORMAL)
    elif var14.get()==0:
        txtOrange_Juice.configure(state=DISABLED)
        E_Orange_Juice.set("0")
    if (var15.get() == 1):
        txtSoda.configure(state=NORMAL)
    elif var15.get()==0:
        txtSoda.configure(state=DISABLED)
        E_Soda.set("0")
    if (var16.get() == 1):
        txtRed_Vine.configure(state= NORMAL)
    elif var16.get()==0:
        txtRed_Vine.configure(state= DISABLED)
        E_Red_Vine.set("0")

    

    



# -------------------------------variablesla-------------------------------
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()

var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
Costoffastfood=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

E_Chole_Bhature=StringVar()
E_Poha_Jalebi=StringVar()
E_Aloo_Tikki=StringVar()
E_Vada_Pao=StringVar()
E_Kachori=StringVar()
E_Egg_Roll=StringVar()
E_Idli_Sambhar=StringVar()
E_Dhosa=StringVar()

E_Mango_Shake=StringVar()
E_Banana_Shake=StringVar()
E_Mix_Fruit_Juice=StringVar()
E_Pineapple_Juice=StringVar()
E_Anar_Juice=StringVar()
E_Orange_Juice=StringVar()
E_Soda=StringVar()
E_Red_Vine=StringVar()

E_Chole_Bhature.set("0")
E_Poha_Jalebi.set("0")
E_Aloo_Tikki.set("0")
E_Vada_Pao.set("0")
E_Kachori.set("0")
E_Egg_Roll.set("0")
E_Idli_Sambhar.set("0")
E_Dhosa.set("0")

E_Mango_Shake.set("0")
E_Banana_Shake.set("0")
E_Mix_Fruit_Juice.set("0")
E_Pineapple_Juice.set("0")
E_Anar_Juice.set("0")
E_Orange_Juice.set("0")
E_Soda.set("0")
E_Red_Vine.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))


#----------------------------Drinks-----------------------------------
Chole_Bhature = Checkbutton(f1aa, text="Chole Bhature \t", variable = var1, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 0, sticky=W)
Poha_Jalebi = Checkbutton(f1aa, text="Poha Jalebi \t", variable = var2, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 1, sticky=W)
Aloo_Tikki = Checkbutton(f1aa, text="Chole Bhature \t", variable = var3, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 2, sticky=W)
Vada_Pao = Checkbutton(f1aa, text="Vada Pao \t", variable = var4, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 3, sticky=W)
Kachori = Checkbutton(f1aa, text="Kachori \t", variable = var5, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 4, sticky=W)
Egg_Roll = Checkbutton(f1aa, text="Egg Roll \t", variable = var6, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 5, sticky=W)
Idli_Sambhar = Checkbutton(f1aa, text="Idli Sambhar \t", variable = var7, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 6, sticky=W)
Dhosa = Checkbutton(f1aa, text="Dhosa \t", variable = var8, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 7, sticky=W)

#-----------------------------------Cakes-------------------------
Mango_Shake = Checkbutton(f1ab, text="Mango Shake \t", variable = var9, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 0, sticky=W)
Banana_Shake = Checkbutton(f1ab, text="Banana Shake \t", variable = var10, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 1, sticky=W)
Mix_Fruit_Juice = Checkbutton(f1ab, text="Mix Fruit Juice \t", variable = var11, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 2, sticky=W)
Pineapple_Juice = Checkbutton(f1ab, text="Pineapple Juice \t", variable = var12, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 3, sticky=W)
Anar_Juice = Checkbutton(f1ab, text="Anar Juice \t", variable = var13, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 4, sticky=W)
Orange_Juice = Checkbutton(f1ab, text="Orange Juice\t", variable = var14, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 5, sticky=W)
Soda = Checkbutton(f1ab, text="Soda \t", variable = var15, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 6, sticky=W)
Red_Vine = Checkbutton(f1ab, text="Red Wine \t", variable = var16, onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row = 7, sticky=W)

#-----------------------Enter widget for Fast Food-------------------------------------
txtChole_Bhature = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Chole_Bhature, state= DISABLED)
txtChole_Bhature.grid(row =0 ,column=1)
txtPoha_Jalebi = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Poha_Jalebi, state= DISABLED)
txtPoha_Jalebi.grid(row =1 ,column=1)
txtAloo_Tikki = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Aloo_Tikki, state= DISABLED)
txtAloo_Tikki.grid(row =2 ,column=1)
txtVada_Pao = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Vada_Pao, state= DISABLED)
txtVada_Pao.grid(row =3 ,column=1)
txtKachori = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Kachori, state= DISABLED)
txtKachori.grid(row =4 ,column=1)
txtEgg_Roll = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Egg_Roll, state= DISABLED)
txtEgg_Roll.grid(row =5 ,column=1)
txtIdli_Sambhar = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Idli_Sambhar, state= DISABLED)
txtIdli_Sambhar.grid(row =6 ,column=1)
txtDhosa = Entry(f1aa, font=('arial',16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Dhosa, state= DISABLED)
txtDhosa.grid(row =7 ,column=1)

#-----------------------Enter widget for Drinks-------------------------------------
txtMango_Shake = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Mango_Shake, bd=8, width=6, justify='left', state= DISABLED)
txtMango_Shake.grid(row =0 ,column=1)
txtBanana_Shake = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Banana_Shake, bd=8, width=6, justify='left', state= DISABLED)
txtBanana_Shake.grid(row =1 ,column=1)
txtMix_Fruit_Juice = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Mix_Fruit_Juice, bd=8, width=6, justify='left', state= DISABLED)
txtMix_Fruit_Juice.grid(row =2 ,column=1)
txtPineapple_Juice = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Pineapple_Juice, bd=8, width=6, justify='left', state= DISABLED)
txtPineapple_Juice.grid(row =3 ,column=1)
txtAnar_Juice = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Anar_Juice, bd=8, width=6, justify='left', state= DISABLED)
txtAnar_Juice.grid(row =4 ,column=1)
txtOrange_Juice = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Orange_Juice, bd=8, width=6, justify='left', state= DISABLED)
txtOrange_Juice.grid(row =5 ,column=1)
txtSoda = Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Soda, bd=8, width=6, justify='left', state= DISABLED)
txtSoda.grid(row =6 ,column=1)
txtRed_Vine= Entry(f1ab, font=('arial',16, 'bold'), textvariable=E_Red_Vine, bd=8, width=6, justify='left', state= DISABLED)
txtRed_Vine.grid(row =7 ,column=1)


#-----------------------Cost of item information-------------------------------------
lblCostofDrinks=Label(f2aa,font=('arial',16, 'bold'), text="Cost of Drinks", bd=8, anchor="w")
lblCostofDrinks.grid(row=2, column=0, sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial', 16,'bold'),bd=8,insertwidth=2, justify='left',textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2,column=1,sticky=W)

lblCostoffastfood=Label(f2aa,font=('arial',16, 'bold'), text="Cost of cakes", bd=8, anchor="w")
lblCostoffastfood.grid(row=3, column=0, sticky=W)
txtCostoffastfood=Entry(f2aa,font=('arial', 16,'bold'),bd=8,insertwidth=2, justify='left',textvariable=Costoffastfood)
txtCostoffastfood.grid(row=3,column=1,sticky=W)


#-----------------------payment Information-------------------------------------

lblPaidTax =Label(f2ab,font=('arial',16, 'bold'), text=" Paid Tax", bd=8)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax=Entry(f2ab,font=('arial', 16,'bold'),bd=8,insertwidth=2, justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1,sticky=W)

lblSubTotal=Label(f2ab,font=('arial',16, 'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal=Entry(f2ab,font=('arial', 16,'bold'),bd=8,insertwidth=2, justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1,sticky=W)

lblTotalCost=Label(f2ab,font=('arial',16, 'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost=Entry(f2ab,font=('arial', 16,'bold'),bd=8,insertwidth=2, justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1,sticky=W)

#-----------------------Information-------------------------------------
lblReceipt = Label(ft2,font=('arial', 16,'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(ft2, width = 70, height= 28,bg="white",bd=8, font=('arial', 9,'bold'))
txtReceipt.grid(row=1,column=0)


#-----------------------Buttons-------------------------------------

btnTotal=Button(fb2, bd=4,font=(' arial', 16,'bold'), width=5,
                text="Total", command=CostofItem).grid(row=0, column=0,sticky=W)
btnReceipt=Button(fb2, bd=4,font=(' arial', 13,'bold'), width=5,
                text="Receipt", command = Receipt).grid(row=0, column=1,sticky=W)
btnReset=Button(fb2, bd=4,font=(' arial', 16,'bold'), width=5,
                text="Reset",command=Reset).grid(row=0, column=2,sticky=W)
btnExit=Button(fb2,bd=4,font=(' arial', 16,'bold'), width=5,
                text="Exit",command=qExit).grid(row=0, column=3,sticky=W)


root.mainloop()