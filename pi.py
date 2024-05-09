#This code is simply just importing the random so we can generate the random seed.
import random
#This code is to define the function of the estimate of pi, and so we are getting the user inputs of seed and iterations
#creating the random seed, and keeping track of the points inside the circle.
def pi_value():
    seed = int(input("Enter the seed for the random number generator: "))
    iterations = int(input("Enter the number of iterations to run: "))
    random.seed(seed)
    point_inside = 0

    #This code is so we can generate the points and increment the counts for the points that fall inside the circle
    for _ in range(iterations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            point_inside += 1

   #This code is for estimating the pi value once we see how many points are inside the circle.
    pi = 4 * (point_inside / iterations)
    #This code is for printing the result of our pi estimate.
    print(f"The value of pi is {pi:.2f}.")

#This code is to bring up the whole program we just created.
pi_value()
