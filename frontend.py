
import tkinter as tk
from tkinter import simpledialog, messagebox
from backend import SmartHome, SmartPlug, SmartDoor


class ToggleSwitch(tk.Canvas):
    """A clickable on/off switch drawn in code, so no image files are needed."""

    def __init__(self, parent, command):
        super().__init__(parent, width=60, height=30, highlightthickness=0, cursor="hand2")
        self.bind("<Button-1>", lambda event: command())
        self.draw(False)

    def draw(self, on):
        self.delete("all")
        colour = "#4caf50" if on else "#9e9e9e"
        self.create_oval(2, 2, 30, 28, fill=colour, outline=colour)
        self.create_oval(30, 2, 58, 28, fill=colour, outline=colour)
        self.create_rectangle(16, 2, 44, 28, fill=colour, outline=colour)
        x = 34 if on else 4
        self.create_oval(x, 4, x + 22, 26, fill="white", outline="")


class SmartHomeApp:
    def __init__(self, root, home):
        self.root = root
        self.home = home
        self.rows = []  # one dict of widgets per device

        root.title("Smart Home")
        root.geometry("600x500")

        tk.Label(root, text="Smart Home", font=("Helvetica", 26)).pack(pady=10)

        self.deviceFrame = tk.Frame(root)
        self.deviceFrame.pack(pady=10, fill="x", padx=20)

        self.totalLabel = tk.Label(root, font=("Helvetica", 14))
        self.totalLabel.pack(pady=5)

        controls = tk.Frame(root)
        controls.pack(pady=10)
        tk.Button(controls, text="Turn All On", command=self.turnOnAll).grid(row=0, column=0, padx=5)
        tk.Button(controls, text="Turn All Off", command=self.turnOffAll).grid(row=0, column=1, padx=5)
        tk.Button(controls, text="Add Plug", command=lambda: self.addDevice(SmartPlug)).grid(row=0, column=2, padx=5)
        tk.Button(controls, text="Add Door", command=lambda: self.addDevice(SmartDoor)).grid(row=0, column=3, padx=5)

        self.buildRows()
        self.refresh()

    def buildRows(self):
        """(Re)create a row of widgets for every device."""
        for child in self.deviceFrame.winfo_children():
            child.destroy()
        self.rows = []

        for i, device in enumerate(self.home.getDevices()):
            nameLabel = tk.Label(self.deviceFrame, text=device.getName(), width=14,
                                 anchor="w", font=("Helvetica", 14))
            nameLabel.grid(row=i, column=0, pady=4)

            statusLabel = tk.Label(self.deviceFrame, width=26, anchor="w", font=("Helvetica", 12))
            statusLabel.grid(row=i, column=1)

            switch = ToggleSwitch(self.deviceFrame, command=lambda idx=i: self.toggle(idx))
            switch.grid(row=i, column=2, padx=5)

            editButton = None
            if isinstance(device, SmartPlug):
                editButton = tk.Button(self.deviceFrame, text="Set rate",
                                       command=lambda idx=i: self.setRate(idx))
                editButton.grid(row=i, column=3)

            self.rows.append({"status": statusLabel, "switch": switch})

    def refresh(self):
        """Update every label so the GUI matches the backend."""
        for device, row in zip(self.home.getDevices(), self.rows):
            if isinstance(device, SmartDoor):
                text = "Open" if device.getSwitchedOn() else "Closed"
            else:
                text = "On" if device.getSwitchedOn() else "Off"
                text += f"  (rate: {device.getConsumptionRate()})"
            colour = "green" if device.getSwitchedOn() else "black"
            row["status"].config(text=text, fg=colour)
            row["switch"].draw(device.getSwitchedOn())
        self.totalLabel.config(text=f"Total consumption: {self.home.totalConsumption()}")

    def toggle(self, index):
        self.home.toggleSwitch(index)
        self.refresh()

    def turnOnAll(self):
        self.home.turnOnAll()
        self.refresh()

    def turnOffAll(self):
        self.home.turnOffAll()
        self.refresh()

    def setRate(self, index):
        plug = self.home.getDeviceAt(index)
        value = simpledialog.askinteger("Consumption rate",
                                        f"New rate for {plug.getName()} (0-150):",
                                        parent=self.root, minvalue=0, maxvalue=150)
        if value is not None:
            try:
                plug.setConsumptionRate(value)
            except ValueError as err:
                messagebox.showerror("Invalid value", str(err))
            self.refresh()

    def addDevice(self, deviceClass):
        name = simpledialog.askstring("New device", "Device name:", parent=self.root)
        if name:
            self.home.addDevice(deviceClass(name))
            self.buildRows()
            self.refresh()


def main():
    home = SmartHome()
    home.addDevice(SmartPlug("Plug 1"))
    home.addDevice(SmartPlug("Plug 2"))
    home.addDevice(SmartDoor("Door 1"))

    root = tk.Tk()
    SmartHomeApp(root, home)
    root.mainloop()  # called once, at the very end


if __name__ == "__main__":
    main()






