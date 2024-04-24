class Begin:
   def __init__(self):
       self.b = B()  # Створюємо об'єкт класу B при створенні об'єкта класу Begin


   def handle(self):
       return self.b.handle()  # Викликаємо метод handle() об'єкта b, який є об'єктом класу B




class B:
   def __init__(self):
       self.success = Success()  # Створюємо об'єкт класу Success при створенні об'єкта класу B


   def handle(self):
       return self.success.handle_message()  # Викликаємо метод handle_message() об'єкта success, який є об'єктом класу Success




class E:
   def __init__(self):
       self.ne = NE()  # Створюємо об'єкт класу NE при створенні об'єкта класу E


   def handle(self):
       return self.ne.handle()  # Викликаємо метод handle() об'єкта ne, який є об'єктом класу NE




class NE:
   def __init__(self):
       self.ng = NG()  # Створюємо об'єкт класу NG при створенні об'єкта класу NE


   def handle(self):
       return self.ng.handle()  # Викликаємо метод handle() об'єкта ng, який є об'єктом класу NG




class NG:
   def __init__(self):
       self.ni = NI()  # Створюємо об'єкт класу NI при створенні об'єкта класу NG


   def handle(self):
       return self.ni.handle()  # Викликаємо метод handle() об'єкта ni, який є об'єктом класу NI




class NI:
   def __init__(self):
       self.error = Error()  # Створюємо об'єкт класу Error при створенні об'єкта класу NI


   def handle(self):
       return self.error.handle_message()  # Викликаємо метод handle_message() об'єкта error, який є об'єктом класу Error




class Error:
   def handle_message(self):
       return "Error"  # Повертаємо рядок "Error"




class Success:
   def handle_message(self):
       return "Success"  # Повертаємо рядок "Success"




# Виклик обробників
begin = Begin()
print(f"Begin: {begin.handle()}")  # Викликаємо метод handle() об'єкта begin, який є об'єктом класу Begin




b = B()
print(f"B: {b.handle()}")  # Викликаємо метод handle() об'єкта b, який є об'єктом класу B
