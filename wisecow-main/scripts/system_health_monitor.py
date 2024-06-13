import psutil
import logging

# Set up logging
logging.basicConfig(filename='/var/log/system_health.log', level=logging.INFO)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_info.percent}%')

    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f'Low Disk space detected: {disk_info.percent}% available')

    logging.info(f'System Health: CPU: {cpu_usage}%, Memory: {memory_info.percent}%, Disk: {disk_info.percent}%')

if __name__ == '__main__':
    check_system_health()
