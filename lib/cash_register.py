#!/usr/bin/env python3

class CashRegister:
    def __init__(self,discount = 0):
      self.total = 0
      self.items = []
      self.discount = discount
      self.last_transaction = None

    def add_item(self,title,price,quantity = 1):
       self.total += price * quantity
       self.items.extend([title] * quantity)
       self.last_transaction = {
          "title": [title] * quantity,
          "amount": price * quantity
       }

    def apply_discount(self):
      if self.discount >0:
          self.total -= self.total * (self.discount / 100)
          print(f'After the discount, the total comes to ${int(self.total)}.')
      else:
         print("There is no discount to apply.")

    def void_last_transaction(self):
       if self.last_transaction:
          self.total -= self.last_transaction["amount"]
          for item in self.last_transaction["title"]:
             self.items.remove(item)
          self.last_transaction = None
             
    def reset_register_totals(self):
       self.total = 0
       self.items = []
