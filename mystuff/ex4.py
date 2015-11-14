# http://learnpythonthehardway.org/book/ex4.html



# The amount of cars available.
cars = 100


'''
Amount of space in each car.
It's a float because we need a more accurate number when we calculate the average(s).
'''
space_in_car = 4.0


# The amount of drivers available.
drivers = 30


# The amount of passengers we have to transport.
passengers = 90


# The amount of not driven cars.
cars_not_driven = cars - drivers


# The amount of driven cars.
cars_driven = drivers


# The amount of all available space in the driven cars.
carpool_capacity = cars_driven * space_in_car


# The average amount of passengers we have to transport with one car.
average_passengers_per_car = passengers / cars_driven


'''
The average amount of space in each car. That line is added by me and it is not part of the exercise.
You can also calculate this by substracting the "space_in_car" with the "average_passengers_per_car".
'''
average_remaining_space_in_each_car = carpool_capacity / passengers



print "---------------------------------------------------------------"
print "---------------------------------------------------------------"
print " "

print "We are going to calculate some numbers! Buckle up!"

print " "
print "---------------------------------------------------------------"
print "---------------------------------------------------------------"



print "There are", cars, "cars available."


print "There are only", drivers, "drivers available."


print "There will be", cars_not_driven, "empty cars today."


print "We can transport", carpool_capacity, "people today."


print "We have", passengers, "passengers to carpool today."


print "We need to put about", average_passengers_per_car, "passengers in each car."


print "We will have about", average_remaining_space_in_each_car, "free space in each car."



print "---------------------------------------------------------------"
print "---------------------------------------------------------------"
print " "

print "That's it! Have a nice day!:)"

print " "
print "---------------------------------------------------------------"
print "---------------------------------------------------------------"



'''
Mistake:

"Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined"

This means that he did not difine the value of "car_pool_capacity", 
so Python could not calculate the result of the division.
'''