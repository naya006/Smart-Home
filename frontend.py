##import tkinter as tk
##from backEnd import *
##
##
##def setUp():
##    global manager
##    manager = Manager()
##    item1 = Item(2, 3)
##    item2 = Item(3, 678.6)
##    item3 = Item(4, 55.67)
##    manager.addItem(item1)
##    manager.addItem(item2)
##    manager.addItem(item3)
##
##
##
##def test():
##    setUp()
##
##    win = tk.Tk()
##    global labelValues
##    labelValues = []
##    for i, item in enumerate(manager.getItems()):
##        key = tk.Label(win, text=item.key)
##        key.grid(row=i, column=0)
##        selectedLabelValue = tk.StringVar(value=str(item.getValue()))
##        labelValues.append(selectedLabelValue)
##        valueEntry = tk.Entry(win, textvariable=selectedLabelValue)
##        valueEntry.grid(row=i, column=1)
##        buttonText = "update item {}".format(i+1)
##        updateButton = tk.Button(
##            win,
##            text=buttonText,
##            command=lambda selectedItem=item,
##                           selectedLabelValue=selectedLabelValue:
##            updateHandler(selectedItem, selectedLabelValue)
##        )
##
##        updateButton.grid(row=i, column=2)



##
##from tkinter import *
## 
### Create Object
##root = Tk()
## 
### Add Title
##root.title('On/Off Switch!')
## 
### Add Geometry
##root.geometry("500x300")
##
##
### Keep track of the button state on/off
###global is_on
##is_on = True
## 
### Create Label
##my_label = Label(root,
##    text = "The Switch Is On!",
##    fg = "green",
##    font = ("Helvetica", 32))
## 
##my_label.pack(pady = 20)
## 
### Define our switch function
##def switch():
##    global is_on
##     
##    # Determine is on or off
##    if is_on:
##        on_button.config(image = off)
##        my_label.config(text = "The Switch is Off",
##                        fg = "grey")
##        is_on = False
##    else:
##       
##        on_button.config(image = on)
##        my_label.config(text = "The Switch is On", fg = "green")
##        is_on = True
## 
### Define Our Images
##on = PhotoImage(file = "on.png")
##off = PhotoImage(file = "off.png")
## 
### Create A Button
##on_button = Button(root, image = on, bd = 0,
##                   command = switch)
##on_button.pack(pady = 50)
## 
### Execute Tkinter
##root.mainloop()
##
##updateAllButton = tk.Button(win, text="update all", command=updateAllHandler)
##updateAllButton.grid(row=len(manager.getItems()), column=0, columnspan=3)
##win.mainloop()
##
##
##def updateHandler(selectedItem, selectedLabelValue):
##    # Update the corresponding item with the new value
##    selectedItem.setValue(selectedLabelValue.get())
##    # Refresh the text in the text widget
##    selectedLabelValue.set(str(selectedItem.getValue()))
##    # Verify that the manager object is updated
##    print(f"Updated item: {selectedItem}")
##    print(manager)
##
##def updateAllHandler():
##    # Initialize an empty list to store the output
##    values = []
##    # Iterate over the list of labelValues
##    for v in labelValues:
##        # Get the value of the current label as a string
##        value_str = v.get()
##        # Convert the string to a float and append it to the output list
##        value_float = float(value_str)
##        values.append(value_float)
##
##    # Update all the items in the Manager object with the latest values
##    manager.updateAll(values)
##    # Refresh all the text in the Entry widgets
##    for i, item in enumerate(manager.getItems()):
##        labelValues[i].set(str(item.getValue()))
##    # Verify that the manager object is updated
##    print(manager)
##
##if __name__ == '__main__':
##    test()




from tkinter import *
from backend.py import *

root = Tk()
root.title('Smart Home')
root.geometry("600x400")
 
# Keep track of the button state on/off
#global is_on
is_on = True
 

# Define our switch function
def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        my_label.config(text = "The Switch is Off",
                        fg = "black")
        is_on = False
    else:
       
        on_button.config(image = on)
        my_label.config(text = "The Switch is On", fg = "green")
        is_on = True
 
# Define Our Images
on = PhotoImage(file = "on.jpg")
off = PhotoImage(file = "off.jpg")
 
# Create A Button
on_button = Button(root, image = on, bd = 0,
                   command = switch)
on_button.pack(pady = 50)
 
# Execute Tkinter
root.mainloop()



def setupHome():
    # Create Labels for GUI
    title = Label(root,
        text = "Smart Home",
        fg = "black",
        font = ("Helvetica", 26)) 
    title.pack(pady = 20)

    cplug_1 = Label(root,
        text = "Door",
        fg = "black",
        font = ("Helvetica", 16)) 
    cplug_1.pack(pady = 10)

    plug_1 = Label(root,
        text = "Plug",
        fg = "black",
        font = ("Helvetica", 16)) 
    plug_1.pack(pady = 10)

    cplug_2 = Label(root,
        text = "Door",
        fg = "black",
        font = ("Helvetica", 16)) 
    cplug_2.pack(pady = 10)
      
    plug_2 = Label(root,
        text = "Plug",
        fg = "black",
        font = ("Helvetica", 16)) 
    plug_2.pack(pady = 10)

    cplug_3 = Label(root,
        text = "Door",
        fg = "black",
        font = ("Helvetica", 16)) 
    cplug_3.pack(pady = 10)

global mainwin






