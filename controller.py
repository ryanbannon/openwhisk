from datetime import datetime
from time import sleep
import os
import csv

# Need to convert milliseconds to seconds - 0.001 * time

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

def create_container(container,in_use,count):
    sleep(2)
    if in_use:
        print("Creating container because others are in use")
        cmd = "docker run -v /doesnt/exist:/foo -w /foo -dit --name %s_%s python:3"%(container,count+1)
        name = container+'_'+str(count+1)
    else:
        print("Creating container because none exist")
        cmd = "docker run -v /doesnt/exist:/foo -w /foo -dit --name %s_1 python:3"%(container)
        name = container+'_1'
    os.popen(cmd)
    return name

'''
execution_time = execute(container, function) #execute the function in new container
total_time = int(install_time) + int(execution_time) #Calculate total execution time
'''

# execution_type = "cold"
# install_time = 1 / get from registry
with open('functions_list.csv', 'a') as file:
    writer = csv.writer(file)
    #writer.writerow([request_time, function, execution_type]) # ([request_time, function, total_time, execution_type])
