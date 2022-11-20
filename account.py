class Account:
	def __init__(self, name: str):
		"""sets default values for the account class, name and balance"""
		self.__account_name = name
		self.__account_balance = 0

	def deposit(self, amount: float) -> float:
		"""if a deposit is less than 0, skip, otherwise add to balance and push True"""
		if amount <= 0:
			return False
		else:
			self.__account_balance += amount
			return True

	def withdraw(self, amount: float) -> float:
		"""if too much to withdraw, skip, otherwise take from balance and push True"""
		if amount <= 0 or amount > self.__account_balance:
			return False
		else:
			self.__account_balance -= amount
			return True
		
	def get_name(self):
		"""return name of bank account"""
		return self.__account_name

	def get_balance(self):
		"""return balance of bank account"""
		return self.__account_balance
