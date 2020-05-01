
from tkinter import *
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("diabetes.csv")
X = data.iloc[:,1:6]
y = data.iloc[:,8:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)
regressor = LinearRegression()
regressor.fit(X_train,y_train)

window = Tk()

window.title("Welcome to Diabetes detection App")

window.geometry('650x450')



def get_list():
    list1 = []
    glucose = txt1.get()
    #plc.insert(END,int(glucose))
    list1.append(int(glucose))
    blood_pressure = txt2.get()
    list1.append(int(blood_pressure))
    skin_thick = txt3.get()
    list1.append(int(skin_thick))
    insulin = txt4.get()
    list1.append(int(insulin))
    bmi = txt4.get()
    list1.append(int(bmi))
   # plc.insert(END,sum(list1)) 
    list1 = pd.DataFrame(list1)
    list1 = pd.DataFrame.transpose(list1)
    result = regressor.predict(list1)
    if result > 0.6:
        op = "You have Diabetes"
        plc.insert(END,str(op))
    else:
        op = "You dont have Diabetes"
        plc.insert(END,str(op))



#btn1 = Button(window, text = "Submit")
#btn1.place(x = 60 ,y = 80)
txt1 = Entry(window , text = 'glucose',bd = 5 )
txt1.place(x = 70 , y = 50)
lb1  = Label(window, text = 'glucose')
lb1.place(x = 90 , y = 30)


#btn2 = Button(window, text = "Submit")
#btn2.place(x = 360 ,y = 80)
txt2 = Entry(window , text = 'Blood Pressure',bd = 5 )
txt2.place(x = 370 , y = 50)
lb2  = Label(window, text = 'Blood Pressure')
lb2.place(x = 390 , y = 30)


#btn3 = Button(window, text = "Submit")
#btn3.place(x = 60 ,y = 280)
txt3 = Entry(window , text = 'Skin Thickness',bd = 5 )
txt3.place(x = 70 , y = 250)
lb3  = Label(window, text = 'Skin Thickness')
lb3.place(x = 90 , y = 230)


#btn4 = Button(window, text = "Submit")
#btn4.place(x = 360 ,y = 280)
txt4 = Entry(window , text = 'Insulin',bd = 5 )
txt4.place(x = 370 , y = 250)
lb4  = Label(window, text = 'Insulin')
lb4.place(x = 390 , y = 230)


txt5 = Entry(window , text = 'BMI',bd = 5 )
txt5.place(x = 60 , y = 350)
lb5  = Label(window, text = 'BMI')
lb5.place(x = 80 , y = 330)


btn6 = Button(window, text = "Make Predictions",width = '30',command = get_list)
btn6.place(x = 350 ,y = 380)
plc  = Entry(width = '30')
plc.place(x = 350 , y = 350)

    

window.mainloop()



