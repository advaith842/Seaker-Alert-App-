import psutil
import time

def get_system_metrics():
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage_gb": round(psutil.virtual_memory().used / (1024**3), 2),
        "disk_usage_gb": round(psutil.disk_usage('/').used / (1024**3), 2),
        "uptime_hours": round((time.time() - psutil.boot_time()) / 3600, 2),
    }
  
