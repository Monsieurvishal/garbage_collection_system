from tkinter import *
import tkinter.font as tkFont
from DepthSensor.ultrasonic import dustbin

class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))
        self.text=''
        self.b=dustbin()
        
        
    def co_ordinate(self):
        
        def printd():
            text = textin.get()
            print(str(text))
            return
        
        cordinate = Tk()
        
        cordinate.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        cordinate.title("enter the co_ordinte values")
        
        label1 = Label(cordinate, text= "Enter the co ordinates seperated by comma" )
        label1.pack()
        
        textin = StringVar()
        e=Entry(cordinate, width=30)
        button = Button(cordinate,text='okay',command=printd)
        button.pack(side='bottom')
        
        e.pack()            
        cordinate.mainloop()
        
    def getarea(self):
        def printd():
            text = textin.get()
            print(str(text))
            return
        
        area= Tk()
        area.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        
        label1 = Label(area, text= "Enter the Area" )
        label1.pack()
        
        textin = StringVar()
        e=Entry(area, width=30)
        button = Button(area,text='okay',command=printd)
        button.pack(side='bottom')
        
        e.pack()            
        area.mainloop()
        
        

        
    def get_info(self):
        
        sensor_data = Tk()
        sensor_data.geometry(str(int(0.5*self.height))+"x"+str(int(0.3*self.width)))
        sensor_data.title("Info Page") 
        initial_percentage=b.percentage_Filled()
        initial=b.initial_Depth
        b.update_Initial()
        current=b.current_Depth() 
        current_percentage=b.percentage_Filled()) 
        
        label1 = Label(sensor_data, text= "Initial depth "+str(initial))
        label2 = Label(sensor_data, text= "intially filled % =  "+str(initial_percentage) )
        label3 = Label(sensor_data, text= "current depth in cm = "+str(current))
        label4 = Label(sensor_data, text= "percentage filled now= "+str(current_percentage))
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        
    def start_app(self,object1):
        
        welcome = tkFont.Font(family='arial', size=55)
        welcome = Label(self.obj, text='*** \n App \n\n\n',font=welcome,background="green")
        welcome.pack(fill='both', expand=True, anchor=CENTER)
        
        display_button = Button(object1,text="Get Data",background="white",command=self.get_info )
        display_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        return_button = Button(object1,text="Return Data",background="white" ) #command= from node mcu
        return_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        co_button = Button(object1,text="Enter Co-Ordinates",background="white",command=self.co_ordinate )  
        co_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        area_button = Button(object1,text="Enter Area",background="white",command=self.getarea )  
        area_button.place(relx=0.5, rely=0.8, anchor=CENTER)
 
if __name__ == "__main__": 
    object1 = Tk()
    object2 = app(object1)
    object2.start_app(object1)
    object1.mainloop()
