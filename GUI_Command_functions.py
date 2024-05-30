import serial
import tkinter as tk



#port = serial.Serial('COM12',parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)

window = tk.Tk()





# function to receive cell voltages
def receive_cell_voltages():
    data = port.readline(5).decode().strip() # Read a line of data from the serial port and decode it
    return data





def update_cell_labels():
    updated_cell_labels = 0
    for i in range(22):
        value = port.readline(5).decode().strip() # Read a line from the serial port and decode it
        if not value:
            # No more values are being received, so check if all labels have been updated
            if updated_cell_labels == 22:
                return # All labels have been updated, so return
            else:
                # Less values have been received than the number of labels, so display an error message
                tk.messagebox.showerror("Error", "Received fewer values than expected!")
                return
        Cell_Labels[i].config(text=value) # Assign the value to the label at index i
        updated_labels += 1

    # If we get here, it means that all 5 labels have been updated
    while True:
        value = port.readline(4).decode().strip()
        if not value:
            # No more values are being received, so break out of the loop
            break

    # Display an error message if more values are being received
    tk.messagebox.showerror("Error", "Received more values than expected!")








#function for updating temperature labels
def update_temperature_labels():
    update_temperature_labels =0
    for i in range(4):
        value= port.readline(5).decode().strip()
        if not value:
            if update_temperature_labels == 4 :
                return
            else:
                tk.messagebox.showeerror("Error","Received fewer values than expected!")
                return
        Temperature_Labels[i].config(text=value)
        update_temperature_labels+=1

    while True:
        value = port.readline(4).decode().strip()
        if not value:
            break

    tk.messagebox.showerror("Error", "Received more values than expected!")





#  check for msg sending from stm32 to bms -rs485
def RS485_Send_check():
    pre_defined_value = 42
    value = port.readline(5).decode().strip()
    if value < pre_defined_value:
        RS485_Send_check.config(bg="yellow")
    else:
        RS485_Send_check.config(bg="red")

# check for msg receive to stm32 from bms - rs485
def RS485_Receive_check():
    pre_defined_value = 42
    value = port.readline(5).decode().strip()
    if value < pre_defined_value:
        RS485_Receive_check.config(bg="yellow")
    else:
        RS485_Receive_check.config(bg="red")


#  check for msg sending from stm32 to bms
def CAN_Send_check():
    pre_defined_value = 42
    value = port.readline(5).decode().strip()
    if value < pre_defined_value:
        CAN_Send_check.config(bg="yellow")
    else:
        CAN_Send_check.config(bg="red")

# check for msg receive to stm32 from bms - CAN
def CAN_Receive_check():
    pre_defined_value = 42
    value = port.readline(5).decode().strip()
    if value < pre_defined_value:
        CAN_Receive_check.config(bg="yellow")
    else:
        CAN_Receive_check.config(bg="red")







def VBUS_value_read():
    value = port.readline(5).decode().strip()
    return value

def update_VBUS_label():
    data = VBUS_value_read()
    VBUS_value_label.config(text=data)




def Contactor_MAIN_read():
    value = port.readline(5).decode().strip()
    return value

def update_Contactor_MAIN_label():
    data = Contactor_MAIN_read()
    CONTACTOR_Main_value.config(text=data)





def Contactor_PRECHARGER_read():
    value = port.readline(5).decode().strip()
    return value

def update_Contactor_PRECHARGER_label():
    data = Contactor_PRECHARGER_read()
    CONTACTOR_Precharger_value.config(text=data)








# function to Begin Test button click
def Begin_Test():
    
    # command to stm32 to start sending cell voltage values to pc
    port.write(b'Cell Voltages')

    #collecting values - read the serial port-  display in labels -checking for timeou +  message for timeout
    update_cell_labels()





    # if success moving request to send temperature values
    port.wtite(b'Temperatures')

    #collecting values - read the serial port-  display in labels -checking for timeout +  message for timeout
    update_temperature_labels()




   # send command to stm32 for sending rs485 value to pc
    port.write(b'RS485_Send')

    #check with pre defined value and display the state
    RS485_Send_check()



    # send command to stm32 for sending rs485 value to pc
    port.write(b'RS485_Receive')

    #check with pre defined value and display the state
    RS485_Receive_check()


   # send command to stm32 for sending send CAN value to pc
    port.write(b'CAN_Send')

    #check with pre defined value and display the state
    CAN_Send_check()



    # send command to stm32 for sending received CAN value to pc
    port.write(b'CAN_Receive')

    #check with pre defined value and display the state
    CAN_Receive_check()




    #send command to stm32 to send v bus values
    port.write(b'VBUS')

    #read vbus value from port and display in label
    update_VBUS_label()



def Conractor_MAIN():

    port.write(b'Contactor_MAIN')

    update_Contactor_PRECHARGER_label()




def Contactor_PRECHARGER():

    port.write(b'Contactor_PRECHARGER')

    update_Contactor_PRECHARGER_label()

















