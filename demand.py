"""Docstring for Problem Set 2"""

#Input Quantities and Prices for Determining Elasticity and Demand Function
import math

quantity1=10

quantity2=11

price1=10

price2=9

#Variable names 

q1=quantity1

q2=quantity2

p1=price1

p2=price2


#Problem 1a: set up elasticity function and print elasticity given price/quantity input above and print result

def compute_elasticity(q1,q2,p1,p2):

    return math.log(q2/q1)/math.log(p2/p1)

e = compute_elasticity(q1,q2,p1,p2)

print("Problem 1a: Elasticity of demand =", + e)


#Problem 1b: determine whether elasticity is elastic, inelastic, or unit elastic and print result

def compute_elasticity(q1,q2,p1,p2):

    return math.log(q2/q1)/math.log(p2/p1)

e = compute_elasticity(q1,q2,p1,p2)

if abs(e)>1: elasticity = "elastic"

elif abs(e)<1: elasticity = "inelastic"

else: elasticity = "unit elastic"

print("Problem 1b: Demand is " + elasticity + ".")


#Problem 1c: Compute new demand (newdemand) using elasticities above...input initialdemand, initial price and new price below

initd = 10

initp = 10

newp = 12

#Function to determine new demand (newd) based on inputs above and elasticity

def compute_demand(initd,initp,newp,e):

    return e*math.log(newp/p1)*initd+initd

# new demand = elasticity x % change in price x initial demand + initial demand

newd = compute_demand(initd,initp,newp,e)

changed = newd - initd

print("Problem 1c: New quantity demanded is", + newp)

#Problem 1d
def main():
	input('first input =  elasticity, second input = demand')
variable = input('elasticity')
x = input('Enter price:')
p1 = input('New Quantity:')
q1 = input('Old Quantity:')
p2 = 9
q2 = 11
def compute_elasticity(q1,q2,p1,p2):
   
    e = compute_elasticity(q1,q2,p1,p2)

print("Problem 1d: Elasticity of demand =", + e)

#1d
def main():
	user_entry = input('enter elasticity od demand')
	if user_entry == 'elasticity':
		new_price = input("input the new price")
		old_price = input("input the old price")
		new_quantity = input("input the new quantity")
		old_quantity = input("input the old quantity")
		new_elasticity = compute_elasticity(new_price,old_price,new_quantity,old_quantity)
		print(new_elasticity)
		print(check_elasticity(new_elasticity))

if user_entry = 'demand':
	sales_quant = input('enter sales quantity')
	initial_price = input('enter initial price')
	elasticity = input('')
	n_price_poionts = input('enter the number of price points')
	output_dict = {}
	for p in range(0, n_price_poionts):
		price_point = input("enter the price points")
		demand_quant = compute_demand(sales_quant, initial_price, price_point, elasticity)
		output_dict[price_point]: demand_quant
	print(output_dict)


#problem2
def prisoners_dilemma():
	n = 0
	strategy_a = 'Defect'
	strategy_b = 'Cooperate'
	while strategy_a != strategy_b 
		#where the game is actually played
		strategy_a = input("enter 'Defect' or 'Cooperate' ")
		strategy_b = input("enter 'Defect' or Cooperate") 
		if strategy_a == 'Defect' and strategy_b == 'Cooperate':
			print("A: 0, B: -20")
		#rest of the if statements 
		n += 1
	else:
		return n 

#problem 2b
def factorial(n_arg):
	fact = 1
	for i in range(1, n_arg+1):
		fact = fact * 1
	return fact
		print(i)



print(factorial(5))
input list = ['apple', 'orange', 'pear']

def compute_frequency(input_list):
	return_dict = {}
	for val in input_list: 
		print(val)
		return_dict[val] = input_list.count(val)
		print(return_dict)
	return return_dict
output = compute_frequency([])
print(output)

compute_frequency(input_list)