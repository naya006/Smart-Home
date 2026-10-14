import random


class SmartPlug:
    
## whether the plug is turned on (bool)
    def switchedOn():
        on == True        

        
## any val between 0 and 150
    def ConsumptionRate(value):
        value = random.randint(0, 150)
        
##  sets switchedon to false and consumptionrate to 0      
    def __init__(switchedOn, ConsumptionRate):
        if switchedOn == off:
            ComsumptionRate == 0
            
##   toggles the value of switchedon         
    def toggleSwitch():        
        global switchedOn
        
        if switchedOn:
            on_button.config(image = off)
            plug_1.config(text = "The Switch is Off",
                        fg = "black")
            switchedOn = False
        else:    
            on_button.config(image = on)
            plug_1.config(text = "The Switch is On", fg = "green")
            switchedOn = True
            
        if switchedOn:
            on_button.config(image = off)
            plug_2.config(text = "The Switch is Off",
                        fg = "black")
            switchedOn = False
        else:       
            on_button.config(image = on)
            plug_2.config(text = "The Switch is On", fg = "green")
            switchedOn = True
            
    on = PhotoImage(file = "on.jpg")
    off = PhotoImage(file = "off.jpg")
 
# Create A Button
    on_button = Button(root, image = on, bd = 0,
                   command = switch)
    on_button.pack(pady = 50)
 
# Execute Tkinter
    root.mainloop()
        
##  returns a str on the smart plug of on/off and consumption rate value      
##def __str__ ():
    
class SmartDoor: 
    global switchedOn
    def switchedOn():
        on == True
        
    if switchedOn:
            on_button.config(image = off)
            cplug_1.config(text = "The Switch is Off",
                        fg = "black")
            switchedOn = False
    else:    
        on_button.config(image = on)
        cplug_1.config(text = "The Switch is On", fg = "green")
        switchedOn = True
        
    if switchedOn:
            on_button.config(image = off)
            cplug_2.config(text = "The Switch is Off",
                        fg = "black")
            switchedOn = False
    else:    
        on_button.config(image = on)
        cplug_2.config(text = "The Switch is On", fg = "green")
        switchedOn = True
        
    if switchedOn:
            on_button.config(image = off)
            cplug_3.config(text = "The Switch is Off",
                        fg = "black")
            switchedOn = False
    else:    
        on_button.config(image = on)
        cplug_3.config(text = "The Switch is On", fg = "green")
        switchedOn = True
        
##    def __str__():



class SmartHome:
    
    def updateAllHandler():
        values = []
        for v in labelValues:
            value_str = v.get()
            value_float = float(value_str)
            values.append(value_float)
        manager.updateAll(values)
        for i, item in enumerate(manager.getItems()):
            labelValues[i].set(str(item.getValue()))
        
#### returns the list of devices.
##def getDevices():
##    
#### takes an index as a parameter and returns the device/plug at the given index in the list of devices.    
##def getDevicesAt():
##    
#### take an object (either a custom device or a SmartPlug) and add it to the list of devices
##def addDevice():
##    
#### take the index of an item in the list of devices and switch the corresponding device on if it is off and off if it is on   
##def toggleSwitch():
##    
#### turn on all the devices in the devices list   
##def turnOnAll():
##    
#### turn off all the devices in the devices list   
##def turnOffAll():
##    
#### returns a well-formatted string representation of all the devices in the devices list   
##def __str__():










##class Manager:
##    def __init__(self):
##        self.items = []
##
##    def addItem(self, item):
##        self.items.append(item)
##
##    def getItems(self):
##        return self.items
##
##    def removeItem(self, key):
##        for item in self.items:
##            if item.key == key:
##                self.items.remove(item)
##                break
##
##    def findItem(self, key):
##        for item in self.items:
##            if item.key == key:
##                return item
##        return None
##
##    def updateAll(self, values):
##        for i, item in enumerate(self.items):
##            item.setValue(values[i])
##
##    def __str__(self):
##        return f"Manager items: {[str(item) for item in self.items]}"
##
##class Item:
##    def __init__(self, key, value):
##        self.key = key
##        self.value = value
##
##    def getValue(self):
##        return self.value
##
##    def setValue(self, value):
##        self.value = value
##
##    def __str__(self):
##        return f"Key: {self.key}, Value: {self.value}"
