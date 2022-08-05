from datetime import datetime
import os

def container_exists(container):
    cmd = "docker ps --format '{{.Names}}' | grep %s | wc -l"%(container)
    count =  os.popen(cmd).read().strip()

    if int(count) >= 1:
        exists = 1
    else:
        exists = 0
    return (exists)

def execute(container):
    start_time_obj = datetime.now()
    start_time = start_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    if container_exists(container):
        print("Container", container, "exists!")
    else:
        print("Container", container, "doesn't exist!")
    end_time_obj = datetime.now()
    end_time = end_time_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    time_diff = end_time_obj - start_time_obj
    print(start_time, end_time, time_diff.total_seconds())

execute('abc_123')