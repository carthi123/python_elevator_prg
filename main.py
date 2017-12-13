import random
'''
Elevator prg
Name : Carthi  P
'''
class Building(object):
	"""
	Builiding class

	Attributes:
    	num_of_floors : It is number of floors in the  buliding  given by the users
        customer_list : It contains the list of the customers

	Functions :
		__run()                : which starts the Excecution (Private)
		default_strategy()     : Strategy which is implemented as normall lift function
		custom_strategy()      : Aternate strategy which is implemented for lift function
		output()               : which compares the default strategy and custom strategy
	"""

	def __init__(self, num_of_floors, no_of_customers):
		self.num_of_floors = num_of_floors
		self.customer_list= list()
		for i in range (1,no_of_customers+1):
			a = Customer(i, num_of_floors)
			self.customer_list.append(a)
		self.__run()

	def __run(self):
		print "*"*64
		print "DEFAULT STRATEGY FOR ELEVATOR"
		print "*"*64
		self.elevator = Elevator(self.num_of_floors)
		self.default_strategy()
		print "*"*64
		print "CUSTOM STRATEGY FOR ELEVATOR"
		print "*"*64
		self.elevator2 = Elevator(self.num_of_floors)
		self.custom_strategy()
		print "*"*64
		print "COMPARING THE EFFICIENCY OF DEFAULT METHOD AND CUSTOM METHOD"
		print "*"*64
		self.output()

	def default_strategy(self):
		'''
		Default strategy is starting at bottom and reaching top and again come down to the bottom
		'''
		# ELEVATOR MOVING UP LOOP
		while(self.elevator.cur_floor <= self.num_of_floors):
			for i in self.customer_list:
				if i.start_point == self.elevator.cur_floor:
					self.elevator.add_customer(i)
			for j in self.elevator.register_list:
				if j.destination_point == self.elevator.cur_floor:
					self.elevator.cancel_customer(j)
			self.elevator.move()

		# Changing the direction of the Elevator
		if self.elevator.cur_floor == self.num_of_floors + 1:
			self.elevator.direction = 1

		# ELEVATOR MOVING DOWN LOOP
		while (self.elevator.cur_floor >= 0 ):
			for j in self.elevator.register_list:
					if j.destination_point == self.elevator.cur_floor:
						self.elevator.cancel_customer(j)
			self.elevator.move()
	def custom_strategy(self):
		'''
		custom startegy is similar to the default but the number of floors visited by the custom startegy will be less than or equal to default method
		the floors visited is reduced by calculating the highest and lowest destination point of customers
        '''
		sm = max(i.start_point for i in self.customer_list) # calculates the highest Floor in the start point of customers
		dm = max(i.destination_point for i in self.customer_list) # calculates the highest Floor in the destination point of customers
		em = min(i.destination_point for i in self.customer_list) # # calculates the lowest Floor in the start point of customers
		topfloor = max (sm ,dm) # calulates top floor to be visited by lift

		# ELEVATOR MOVING UP LOOP
		while(self.elevator2.cur_floor <= topfloor):
			for i in self.customer_list:
				if i.start_point == self.elevator2.cur_floor:
					self.elevator2.add_customer(i)
			for j in self.elevator2.register_list:
				if j.destination_point == self.elevator2.cur_floor:
					self.elevator2.cancel_customer(j)
			self.elevator2.move()

		# Changing the direction of the Elevator
		if self.elevator2.cur_floor == topfloor + 1:
			self.elevator2.cur_floor = self.elevator2.cur_floor - 1
			self.elevator2.direction = 1

		# ELEVATOR MOVING DOWN LOOP
		while (self.elevator2.cur_floor >=  em ):
			for j in self.elevator.register_list:
					if j.destination_point == self.elevator2.cur_floor:
						self.elevator2.cancel_customer(j)
			self.elevator2.move()

	def output(self):
		'''
		Compares the default and custom method
		'''
		print "--"*32
		print "Floors Travelled by the Elevator in default method : ",self.elevator.floor_visited
		print "--"*32
		print "Floors Travelled by the Elevator in Custom  method : ",self.elevator2.floor_visited
		print "--"*32


class Elevator(object):
	'''
	Attributes:
    	num_of_floors : It is number of floors in the  buliding  given by the users
        register_list : It contains the list of the customers who entered into lift
		cur_floor     : it current floor in which elevator is present
		direction     : Direction of the Elevator
		floor_visited : No of floors visited by the Customers
	Functions :
		move()            : which moves the Elevator one floor up based on direction
		add_customer()    : which add the customers into the resister list when they are boarding th elevator
		cancel_customer() : which cancel the customers when the reach the destination point by making the flag to false 
	'''
	def __init__(self, num_of_floors ):
		self.num_of_floors = num_of_floors
		self.register_list = list()
		self.cur_floor = 0
		self.direction = 0
		self.floor_visited = 0
		print"-"*32
		print "LIFT IS IN FLOOR {}".format(self.cur_floor)
		print"-"*32
		print ""

	def move(self):
		if self.direction == 0:
			self.cur_floor = self.cur_floor+1
			self.floor_visited+=1
			if self.cur_floor <= self.num_of_floors:
				print"-"*32
				print "LIFT IS IN FLOOR {}".format(self.cur_floor)
				print"-"*32
				print ""
		elif self.direction == 1:
			self.cur_floor = self.cur_floor-1
			self.floor_visited+=1
			if self.cur_floor >= 0:
				print"-"*32
				print "LIFT IS IN FLOOR {}".format(self.cur_floor)
				print"-"*32
				print ""

	def add_customer(self, customer):
		customer.in_elevator = True
		self.register_list.append(customer)
		print "Customer enter with ID {} start point :{} end point {}".format(customer.ID,customer.start_point,customer.destination_point)
		print ""

	def cancel_customer(self, customer):
		if customer.in_elevator ==	True:
			customer.in_elevator = False
			print "Customer leave  with ID {} start point :{} end point {}".format(customer.ID,customer.start_point,customer.destination_point)
			print ""

class Customer(object):
	'''
	Attributes:
    	ID 			      : It is specific ID of the individual customer
        in_elevator       : It contains information weather he/she is in elevator or not
		start_point       : it is start point of the customer entering into Elevator
		destination_point : it is destination point of the customer where he wants to reach
	'''
	def __init__(self, ID, num_of_floors):
		self.ID = ID
		self.in_elevator = False
		self.finished = False
		# using random fuction for creating the start point
		self.start_point = random.randint(0, num_of_floors )
		# using random fuction for creating the destination  point
		self.destination_point = random.randint(0, num_of_floors )
		while self.start_point == self.destination_point:
			self.destination_point = random.randint(0, num_of_floors )
		print ""
		print "cusID {} st point :{} en point {}".format(self.ID, self.start_point, self.destination_point)
		print ""

def main():
	try :
		print "*******************ELEVATOR SIMULATION************************"
		n = int(input('Enter the number of floors '))
		if n >= 2:
			print 'Floors Entered: ', n
		else:
			print "Enter more than one floor"
			main()
		c = int(input('Enter number of customers: '))
		print'Customers Entered: ', c
		if c <= 0:
			print "There is no customer for operating Elevator"
			exit()
		#Creating the Building object and passing the args number_of_floors and no_of_customers
		building = Building(n, c)
	except NameError as e:
		print('Enter the valid number only')
		main()

if __name__ == '__main__':
	main()
