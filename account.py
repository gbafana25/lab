class Account:
	def __init__(self, name):
		self.__account_name = name
		self.__account_balance = 0
		
	def get_name(self):
		return self.__account_name

	def get_balance(self):
		return self.__account_balance
