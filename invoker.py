from datetime import datetime
from time import sleep
import csv
import sys
import os
import uuid

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

def create_container(container):
    sleep(2)
    guid = str(uuid.uuid1())
    name = container+'_'+guid
    print("Creating container")
    cmd = "docker run -v /doesnt/exist:/foo -w /foo -dit --name %s python:3"%(name)
    os.popen(cmd)
    return name

def execute(container,function):
    try:
        print("Executing "+container)
        cmd = "docker cp %s %s:/foo/"%(function,container)
        os.popen(cmd)
        cmd2 = "docker exec -i %s python %s"%(container,function)
        os.popen(cmd2)
        cmd3 = "docker container kill %s"%(container)
        os.popen(cmd3)
        cmd4 = "docker container rm %s"%(container)
        os.popen(cmd4)
    except:
        type = "cold"
        name = create_container(container)
        execute(name,function)

def serverless_func(container,function):
    start_time_obj = datetime.now()
    start_time = start_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    container = str(container)
    function = str(function)+".py"
    exists, list = container_exists(container)
    if exists:
        type = "warm"
        print("Container exists!")
        name = list[0].rstrip('\n')
    else:
        type = "cold"
        print("Container doesnt exist!")
        name = create_container(container) # Count = 0

    execute(name,function)

    end_time_obj = datetime.now()
    end_time = end_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    time_diff = end_time_obj - start_time_obj
    run_time = int(time_diff.total_seconds()*1000)
    print(start_time, end_time, run_time) 

    with open('predictions/experiment_1_2_results.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([start_time, run_time, name, function, type])

serverless_func(sys.argv[1],sys.argv[2])