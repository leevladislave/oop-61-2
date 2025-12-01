class Phone:
    def __init__(self, model, memory, battery):
       self.model = model
       self.memory = memory
       self.battery = battery
       self.empty = True
    def call(self):

       return f"{self.model} Звонит!"

    def charge(self, charger="charger"):
       self.empty = False
       return f"{self.model}  {charger} Заряжен!"

    def info(self):
       status = "Разряжен" if self.empty else "Заряжен"
       return f"Телефон {self.model}, {self.memory} Gb, Батарея: {self.battery}, сейчас {status}"



phone1 = Phone("Samsung", 256, "0")
phone2 = Phone("Iphone", 256, "0")
phone3 = Phone("Xiaomi", 256, "0")


print(phone1.info())
print(phone1.call())
print(phone1.charge("100"))


print("\n"+phone2.info())
print(phone2.call())
print(phone2.charge(100))

print("\n"+phone3.info())
