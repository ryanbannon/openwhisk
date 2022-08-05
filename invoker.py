from datetime import datetime
import os

def container_exists(container):
    cmd = "docker ps --format '{{.Names}}' | grep %s"%(container)
    list = os.popen(cmd).read().strip()
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
    print(count)
    if int(count) >= 1:
        in_use = True
    else:
        in_use = False
    return (in_use)

def create_container(container,in_use,count):
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

def execute(container):
    print("Container", container, "exists!")
    cmd = "docker cp test_function.py abc_123:/foo/"
    os.popen(cmd)
    cmd2 = "docker exec -i abc_123 python test_function.py"
    os.popen(cmd2)
    cmd3 = "docker container kill abc_123"
    os.popen(cmd2)
    cmd4 = "docker container rm abc_123"
    os.popen(cmd2)

def serverless_func(container):
    start_time_obj = datetime.now()
    start_time = start_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    
    exists, list = container_exists(container)
    count = len(list)
    if exists:
        print("Container", container, "exists!")
        name = list[0]
    else:
        print("Container", container, "doesnt exist!")
        name = create_container(container,False,count) # Count = 0

    print("Execute",name)
    #execute(container)

    end_time_obj = datetime.now()
    end_time = end_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    time_diff = end_time_obj - start_time_obj
    print(start_time, end_time, time_diff.total_seconds())

serverless_func('abc_123')