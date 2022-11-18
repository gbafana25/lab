class Account:
	def __init__(self, name):
		self.__account_name = name
		self.__account_balance = 0

	def deposit(self, amount):
		if amount <= 0:
			return False
		else:
			self.__account_balance += amount
			return True

	def withdraw(self, amount):
		if amount <= 0 or amount > self.__account_balance:
			return False
		else:
			self.__account_balance -= amount
			return True
		
	def get_name(self):
		return self.__account_name

	def get_balance(self):
		return self.__account_balance
