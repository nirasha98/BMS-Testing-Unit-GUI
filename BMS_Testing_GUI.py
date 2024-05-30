import serial
import tkinter as tk

from tkinter import *

import GUI_Command_functions


# define port and baudrate
Port = 'COM12'
Baudrate = 9600

# open port
#port = serial.Serial('COM12',parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)





# GUI window
window = tk.Tk()
window.title("BMS Testing Unit")
window.geometry("500x760")





#     FRAME 01      #







    # Cell Voltages #





#creating frame for cell voltages
cell_voltage_frame = Frame(window, width=400, height=750, bg='light grey')
cell_voltage_frame.grid(row=0, column=0, padx=10, pady=5)

#display cell voltage topic
Label(cell_voltage_frame, text="Cell Voltage(V)").grid(row=0, column=0, padx=5, pady=5)

#inside frame for display 22 cell voltages
cell_voltage_value_frame = Frame(cell_voltage_frame, width=180, height=650,bg="light grey")
cell_voltage_value_frame.grid(row=2, column=0, padx=5, pady=5)


# function for read cell voltages from serial port

def receive_cell_voltages():
    data = port.readline(5).decode().strip() # Read a line of data from the serial port and decode it
    return data


# call the function


Cell_Labels =[]
for i in range(22):
    cell_label=Label(cell_voltage_value_frame, text="",height=1,width=25).grid(row=i, column=1, padx=5, pady=5)
    Cell_Labels.append(cell_label)


 




#    FRAME 02    #








# Temperature #





#creating frame for temperature values

temperature_frame = Frame(window, width=400, height=750, bg='light grey')
temperature_frame.grid(row=0, column=1, padx=10, pady=5,sticky="N")

# displaying temperature topics
Label(temperature_frame, text="Temperature(C)").grid(row=0, column=1, padx=5, pady=5)

#inside frame for display temperature values
temperature_value_frame = Frame(temperature_frame, width=190, height=250,bg="light grey")
temperature_value_frame.grid(row=2, column=1, padx=5, pady=5)

# function for read temperature values from serial port



# call the function

Temperature_Labels=[]
for i in range(4):
    temperature_labels=Label(temperature_value_frame, text="",width=25,height=1).grid(row=i, column=1, padx=5, pady=5)
    Temperature_Labels.append(temperature_labels)






# RS485 #

RS485_CAN_frame = Frame(temperature_frame, width=400, height=400, bg='light grey')
RS485_CAN_frame.grid(row=3, column=1, padx=10, pady=27)


#topic for frame rs485
Label(RS485_CAN_frame, text="RS485").grid(row=0, column=2, padx=5, pady=5)


#frame for display values inside RS485 frame
RS485_value_frame = Frame(RS485_CAN_frame, width=280, height=220,bg="light grey")
RS485_value_frame.grid(row=2, column=2, padx=5, pady=5)

# send function  for rs 485


# RS485 send button - need to add command for button
RS485_Send_label=Label(RS485_value_frame,text="Send",width="6",height="1")
RS485_Send_label.grid(row=0, column=0,padx=5)


#check for accuracy of rs485 sending msg
RS485_Send_check=Label(RS485_value_frame,width=3,height=1).grid(row=0, column=3) 


# receive function for rs485

#def read_message():
   # RS485_Receive_Label.config(text=get_message())


#RS485 receive button - need to add command for button
RS485_Receive_Label=Label(RS485_value_frame,text="Receive",width="6",height="1")
RS485_Receive_Label.grid(row=2,column=0,padx=5,pady=5)


#check for accuracy of received rs485 msg
RS485_Receive_check=Label(RS485_value_frame,width=3,height=1).grid(row=2, column=3) 






# CAN #



#display topic for CAN
Label(RS485_CAN_frame, text="CAN").grid(row=4, column=2, padx=5, pady=5)

#inside frame for CAN
CAN_value_frame = Frame(RS485_CAN_frame, width=280, height=220,bg="light grey")
CAN_value_frame.grid(row=6, column=2, padx=5, pady=5)

#function for CAN sending

 

#button for CAN sending
CAN_Send_label=Label(CAN_value_frame,text="Send",width="6",height="1")
CAN_Send_label.grid(row=0, column=0,padx=5,pady=5)

CAN_check=Label(CAN_value_frame,width=3,height=1).grid(row=0, column=3)


# command function for check accuracy



#checking for accuracy of CAN send msg
CAN_Send_check=Label(CAN_value_frame,width=3,height=1).grid(row=0, column=3) 

# function for CAN receiving



#button for receive CAN msg-add command
CAN_Receive_label=Label(CAN_value_frame,text="Receive",width="6",height="1")
CAN_Receive_label.grid(row=2,column=0)


# command function for check accuracy of received function



#checking the accuracy of received CAN msg
CAN_Receive_check=Label(CAN_value_frame,width=3,height=1).grid(row=2, column=3) 






# VBUS values




# topic display FOR VBUS
Label(temperature_frame, text="VBUS").grid(row=5, column=1, padx=10, pady=10)

#inside frame for v bus values 
VBUS_frame = Frame(temperature_frame, width=190, height=100,bg="light grey")
VBUS_frame.grid(row=6, column=1, padx=5, pady=5)

#vbus value display label
VBUS_value_label=Label(VBUS_frame,text="",width="16",height="1")
VBUS_value_label.grid(row=1,column=0)

# function for display VBUS value in the label



# CONTACTORS





#contactor name display label
Label(temperature_frame, text="CONTACTORS").grid(row=7, column=1, padx=5, pady=10)

#inside frame for contactor details
CONTACTOR_frame = Frame(temperature_frame, width=190, height=100,bg="light grey")
CONTACTOR_frame.grid(row=8, column=1, padx=10, pady=10)


#label for "Main:" in contactors
CONTACTOR_Main_button=Button(CONTACTOR_frame,text="Main:",width="8",height="1")
CONTACTOR_Main_button.grid(row=0,column=0)


#label for "main value" in contactors
CONTACTOR_Main_value=Label(CONTACTOR_frame,text="",width="12",height="1")
CONTACTOR_Main_value.grid(row=0,column=1)

# function for display main value in the label

#label for "Recharger" in contactors
CONTACTOR_Precharger_button=Button(CONTACTOR_frame,text="Precharger:",width="8",height="1")
CONTACTOR_Precharger_button.grid(row=2,column=0)

#label for recharger value in contactors
CONTACTOR_Precharger_value=Label(CONTACTOR_frame,text="",width="12",height="1")
CONTACTOR_Precharger_value.grid(row=2,column=1)

# function for display recharger value in the label




# Emergency  FRAME



# frame for EMERGENCY BUTTON

Emergency_frame = Frame(temperature_frame, width=280, height=60,bg="light grey")
Emergency_frame.grid(row=9, column=1, padx=10, pady=10)

# emergency name display
Label(Emergency_frame, text="EMERGENCY").grid(row=1, column=1, padx=5, pady=5)

# function for mergency check button


# button for checking emergency - add command
Emergency_button=Button(Emergency_frame,text="Check",width="12",height="1")
Emergency_button.grid(row=3,column=1,pady=5)






# Frame for BEGIN TEST and REPORT GENERATING 




# INSIDE FRAME
Test_Report_frame = Frame(temperature_frame, width=280, height=50,bg="light grey")
Test_Report_frame.grid(row=10, column=1, padx=5, pady=5)

# function for BEGIN TEST button
#def Begin_Test():




# BEGIN TEST BUTTON - add command
Begin_test_button=Button(Test_Report_frame,text="Begin Test",width="12",height="1")
Begin_test_button.grid(row=0,column=0,padx=10,pady=10)

# function for GENERATE BUTTON 


# GENERATE REPORT BUTTON - add command
Generate_Report_button=Button(Test_Report_frame,text="Generate Report",width="12",height="1")
Generate_Report_button.grid(row=0,column=1,padx=10,pady=10)



window.mainloop()
