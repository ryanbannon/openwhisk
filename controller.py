from time import sleep
import os
import pandas as pd
import sys

def container_exists(container):
    cmd = "docker ps --format '{{.Names}}' | grep %s"%(container)
    list = os.popen(cmd).readlines()
    cmd2 = "docker ps --format '{{.Names}}' | grep %s | wc -l"%(container)
    count =  os.popen(cmd2).read().strip()
    if int(count) >= 1:
        exists = True
    else:
        exists = False
    return (exists,list)

def create_container(container,count):
    print("Creating container")
    cmd = "docker run -v /doesnt/exist:/foo -w /foo -dit --name %s_1 python:3"%(container)
    os.popen(cmd)

container = "expr_"+str(sys.argv[1])
predictions = pd.read_csv('predictions/experiment_1_2_times.csv')
predictions = predictions['wait']
for i in predictions:
    seconds = round(i*0.001,2) # Convert milliseconds to seconds for sleep method - 0.001 * time
    print(seconds)
    exists, list = container_exists(container)
    count = len(list)
    if not exists:
        print("Container", container, "doesnt exist!")
        create_container(container)
    sleep(seconds)
