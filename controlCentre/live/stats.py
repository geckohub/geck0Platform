import os, socket, psutil
from .utils import sh, service_status, bar, GECK0_HOME

def system_panel():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    temp = sh("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null")
    temp = f"{int(temp)/1000:.1f}°C" if temp.isdigit() else "n/a"
    docker = sh("docker ps --format '{{.Names}}' 2>/dev/null | wc -l")
    ports = sh("ss -tuln | grep -E ':(3000|3001|8890|8891|8892|8893|9000|1880|8123)' | wc -l")
    return f"""
╔═ 🖥 SYSTEM TELEMETRY ═╗

HOST        {socket.gethostname()}
USER        {os.getenv("USER", "lucy")}
ROOT        {GECK0_HOME}
IP          {sh("hostname -I | awk '{print $1}'")}
TAILSCALE   {sh("tailscale ip -4 2>/dev/null")}

UPTIME      {sh("uptime -p")}
TEMP        {temp}

CPU         [{bar(cpu)}] {cpu:.0f}%
MEMORY      [{bar(mem)}] {mem:.0f}%
DISK        [{bar(disk)}] {disk:.0f}%

╔═ ⚙ SERVICES ═╗

Docker      {docker} containers
SSH         {service_status("ssh")}
Fail2ban    {service_status("fail2ban")}
Grafana     {service_status("grafana-server")}
Nginx       {service_status("nginx")}
Mosquitto   {service_status("mosquitto")}

╔═ 🌐 WATCHED PORTS ═╗

Open        {ports}
"""
