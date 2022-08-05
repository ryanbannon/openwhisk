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
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if container_exists(container):
        print("Container", container, "exists!")
    else:
        print("Container", container, "doesn't exist!")
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(start_time, end_time)

execute('abc_123')