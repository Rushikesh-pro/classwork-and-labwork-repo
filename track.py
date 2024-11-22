system_status = "offline"

def start_system():
 global system_status
 system_status = "online"
 print("System started")

def stop_system():
    global system_status
    system_status = "offline"
    print("system status")

def check_system_status():
    print("The system is currently: ",system_status)

check_system_status()
start_system()
check_system_status()
stop_system()
check_system_status()
