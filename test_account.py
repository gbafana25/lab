from account import *

class Test:
	def setup_method(self):
		self.a = Account("test")	

	def teardown_method(self):
		del self.a

	def test_init(self):
		assert self.a.get_name() == "test"
		assert self.a.get_balance() == 0

	def test_deposit(self):
		assert self.a.deposit(10) == True
		assert self.a.deposit(-1) == False
	
	def test_withdraw(self):
		self.a.deposit(10)
		assert self.a.withdraw(5) == True 
		assert self.a.withdraw(-4) == False
		assert self.a.withdraw(0) == False





