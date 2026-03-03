import subprocess
import platform
import time
from datetime import datetime
import os

assets = {
    "Stazione Analista": "192.168.10.236",
    "Gateway (Cudy)": "192.168.10.1",
    "Sentinella (HP)": "192.168.10.60",
    "Switch Managed": "192.168.10.250",
    "Notebook Asus (Cavo)": "192.168.10.148",
    "Notebook Asus (Wi-Fi)": "192.168.9.101"
}

def check_host(ip):
    # Determina il parametro in base all'OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        # Esegue il ping e cattura il testo della risposta
        output = subprocess.check_output(
            ["ping", param, "1", ip], 
            stderr=subprocess.STDOUT, 
            universal_newlines=True,
            timeout=2
        )
        # La prova del nove: se c'è "TTL=" la risposta arriva dall'host reale
        if "TTL=" in output.upper():
            return True
        else:
            return False
    except:
        return False

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        
        print(f"--- [🔵] SOC MONITOR V2.1 - {ora_attuale} ---")
        print("Analisi reale dei pacchetti (Cerca 'TTL')\n")

        for name, ip in assets.items():
            is_online = check_host(ip)
            
            if is_online:
                print(f"[✅] {name:<15} ({ip:<15}) is ONLINE")
            else:
                print(f"[🚨] {name:<15} ({ip:<15}) is OFFLINE!")

        print("\n-------------------------------------------------")
        time.sleep(300) # Abbassiamo a 10 secondi per testare meglio

except KeyboardInterrupt:
    print("\n[!] Monitoraggio arrestato!")
