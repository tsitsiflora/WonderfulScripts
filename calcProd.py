import time

def calcProd():
    #Calculate the product of the first 100 000 numbers
    product = 1
    for i in range(1, 100000):
       product = product*i
    return product

start_time = time.time()
prod = calcProd()
end_time = time.time()

print('The product is {0} digits long'.format(len(str(prod))))
print('It took {0} seconds to calculate the product'.format(end_time - start_time))
 
