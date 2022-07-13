from datetime import datetime
import random

def main():
    startNumber = 1
    endNumber = 10000
    prime = []
    for i in range(startNumber,endNumber):
        for p in range(2, i):
            if (i % p)==0:
                break
        else:
            prime.append(i)
    num = random.sample(prime, 1)
    now = datetime.now()
    message = str("The random prime number this "+now.strftime("%A")+" at "+now.strftime("%R")+" is: "+str(num[0]))
    print(message)
    return {"message": message}

main()