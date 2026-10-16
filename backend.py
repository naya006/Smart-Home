"""Smart Home backend"""
import random


class Device:


    def __init__(self, name="Device"):
        self._name = name
        self._switchedOn = False

    def getName(self):
        return self._name

    def getSwitchedOn(self):
        return self._switchedOn

    def switchOn(self):
        self._switchedOn = True

    def switchOff(self):
        self._switchedOn = False

    def toggleSwitch(self):
        """Switch on if off, and off if on."""
        if self._switchedOn:
            self.switchOff()
        else:
            self.switchOn()

    def __str__(self):
        return f"{self._name}: {'on' if self._switchedOn else 'off'}"


class SmartPlug(Device):
    MIN_RATE = 0
    MAX_RATE = 150

    def __init__(self, name="Plug"):
        # Starts switched off with a consumption rate of 0
        super().__init__(name)
        self._consumptionRate = 0

    def getConsumptionRate(self):
        return self._consumptionRate

    def setConsumptionRate(self, value):
        """Set the rate; must be a whole number between 0 and 150."""
        if not isinstance(value, int) or not (self.MIN_RATE <= value <= self.MAX_RATE):
            raise ValueError(f"Consumption rate must be an integer {self.MIN_RATE}-{self.MAX_RATE}")
        self._consumptionRate = value

    def switchOn(self):
        super().switchOn()
        # Simulate the plug drawing power once it is on
        self._consumptionRate = random.randint(self.MIN_RATE, self.MAX_RATE)

    def switchOff(self):
        super().switchOff()
        self._consumptionRate = 0

    def __str__(self):
        state = "on" if self._switchedOn else "off"
        return f"{self._name}: {state}, consumption rate {self._consumptionRate}"


class SmartDoor(Device):
    """Custom device: a door that can be opened (on) or closed (off)."""

    def __init__(self, name="Door"):
        super().__init__(name)

    def __str__(self):
        return f"{self._name}: {'open' if self._switchedOn else 'closed'}"


class SmartHome:
    def __init__(self):
        self._devices = []

    def getDevices(self):
        return self._devices

    def getDeviceAt(self, index):
        if 0 <= index < len(self._devices):
            return self._devices[index]
        return None

    def addDevice(self, device):
        if not isinstance(device, Device):
            raise TypeError("Only Device objects (e.g. SmartPlug, SmartDoor) can be added")
        self._devices.append(device)

    def toggleSwitch(self, index):
        device = self.getDeviceAt(index)
        if device is not None:
            device.toggleSwitch()

    def turnOnAll(self):
        for device in self._devices:
            device.switchOn()

    def turnOffAll(self):
        for device in self._devices:
            device.switchOff()

    def totalConsumption(self):
        return sum(d.getConsumptionRate() for d in self._devices if isinstance(d, SmartPlug))

    def __str__(self):
        if not self._devices:
            return "Smart Home: no devices"
        lines = [f"{i + 1}. {d}" for i, d in enumerate(self._devices)]
        return "Smart Home devices:\n" + "\n".join(lines)


if __name__ == "__main__":
    # Quick console test
    home = SmartHome()
    home.addDevice(SmartPlug("Lamp"))
    home.addDevice(SmartPlug("Kettle"))
    home.addDevice(SmartDoor("Front Door"))
    home.turnOnAll()
    print(home)
    home.toggleSwitch(0)
    print(home)
