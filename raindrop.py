# For the numbers 1 - 100
# "Plink", "Plank", "Plonk"

# if the number is divisible by 3, print Plink
# by 5, print Plank
# by 7 print Plonk

# if it is divisible by a combination, print all the appropriate words. 
# For example, if divisible by 3 & 5, print "PlinkPlank"

# user the python operator % - modulo, means 'remainder when divided by'

def make_rain_sounds():
    for number in range(1, 101):
        #if number is divisible by 3
        if number % 3 == 0 and number % 5 == 0:
            print(number, 'PlinkPlank')
        elif number % 3 == 0 and number % 7 == 0:
            print(number, 'PlinkPlonk')
        elif number % 5 == 0 and number % 7 == 0:
            print(number, "PlankPlonk")
        elif number % 3 == 0:
            print(number, 'Plink')
        elif number % 5 == 0:
            print(number, 'Plank')
        elif number % 7 == 0:
            print(number, 'Plonk')

        
make_rain_sounds()
