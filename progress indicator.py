#progress indicator
import time

print ("downloading", end ='')
for n in range(20):
    print('.',end='',flush=True)
    time.sleep(0.1)
print("\nDownload completed!")