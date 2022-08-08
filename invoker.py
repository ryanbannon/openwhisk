from datetime import datetime
from time import sleep
import csv
import sys
import os

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

def container_in_use(container):
    cmd = "ps -ef | grep %s | grep docker | wc -l"%(container)
    count =  os.popen(cmd).read().strip()
    if int(count) >= 1:
        in_use = True
    else:
        in_use = False
    return (in_use)

def create_container(container,in_use,count):
    sleep(1)
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

def execute(container,function,count):
    try:
        print("Container", container, "exists!")
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
        name = create_container(container=container,in_use=True,count=count)
        execute(name,function,count)

def serverless_func(container,function):
    start_time_obj = datetime.now()
    start_time = start_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    container = "expr_"+str(container)
    function = str(function)+".py"
    exists, list = container_exists(container)
    count = len(list)
    if exists:
        type = "warm"
        print("Container", container, "exists!")
        print(list)
        name = list[0].rstrip('\n')
    else:
        type = "cold"
        print("Container", container, "doesnt exist!")
        name = create_container(container=container,in_use=False,count=count) # Count = 0

    print("Execute",name)
    execute(name,function,count)

    end_time_obj = datetime.now()
    end_time = end_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    time_diff = end_time_obj - start_time_obj
    run_time = int(time_diff.total_seconds()*1000)
    print(start_time, end_time, run_time) 

    with open('predictions/experiment_1_2_results.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([start_time, run_time, name, function, type])

serverless_func(sys.argv[1],sys.argv[2])