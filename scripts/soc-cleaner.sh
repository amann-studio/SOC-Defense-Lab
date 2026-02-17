
#!/bin/bash
# Pulizia Log Suricata (file compressi vecchi di 7 giorni)
find /var/log/suricata/ -name "*.gz" -mtime +7 -exec rm -f {} \;

# Pulizia Log Wazuh (alert vecchi di 7 giorni)
find /var/ossec/logs/alerts/ -name "*.gz" -mtime +7 -exec rm -f {} \;
find /var/ossec/logs/archives/ -name "*.gz" -mtime +7 -exec rm -f {} \;

# Svuota i file correnti se superano i 2GB (opzionale, per sicurezza)
find /var/log/suricata/eve.json -size +2G -exec truncate -s 0 {} \;
