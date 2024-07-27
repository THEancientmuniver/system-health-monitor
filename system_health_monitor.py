import psutil
import subprocess

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Check CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > CPU_THRESHOLD:
    print(f"CPU usage is above threshold: {cpu_usage}%")

# Check Memory usage
memory_info = psutil.virtual_memory()
memory_usage = (memory_info.used / memory_info.total) * 100
if memory_usage > MEMORY_THRESHOLD:
    print(f"Memory usage is above threshold: {memory_usage:.2f}%")

# Check Disk usage
disk_usage = psutil.disk_usage('/').percent
if disk_usage > DISK_THRESHOLD:
    print(f"Disk usage is above threshold: {disk_usage}%")

# Check running processes
print("Running processes:")
for process in psutil.process_iter(['pid', 'name']):
    print(f"PID: {process.info['pid']}, Name: {process.info['name']}")
