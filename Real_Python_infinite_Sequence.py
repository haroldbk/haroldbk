#https://realpython.com/introduction-to-python-generators/

def infinite_sequence():
    num=0
    while True:
        yield num
        num += 1

#for i in infinite_sequence():
 #   print (i, end=" ")
gen = infinite_sequence()
for i in range(10): 
    g = next(gen)
    print(g)
