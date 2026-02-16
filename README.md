# SOC-Defense-Lab
Descrizione tecnica del mio laboratorio di monitoraggio e difesa cyber. Architettura, Hardening e Analisi SIEM.

## Lab Architecture
- **Host:** Windows 11 Hardened (i7-14700K | 32GB RAM | RTX 4060Ti)
- **Networking:** Dual-Router Cascade (TIM + Cudy WR3000H) con segmentazione IoT/Guest.
- **SIEM:** Wazuh (Ubuntu Server 22.04 VM) - *In fase di implementazione*
- **Monitoring:** Microsoft Sysmon + Wireshark.

### Legacy Hardware Integration
- **Asset Recovery:** Recupero funzionale di un notebook legacy (HP Pavilion dv6 - 2010) tramite manutenzione hardware straordinaria (Thermal Repasting con Arctic MX-4 e upgrade SSD SATA).Installazione nativa di Ubuntu Server 22.04 LTS, eliminando l'overhead della virtualizzazione e ottimizzando le prestazioni su hardware datato.
- **Ruolo:** Server SIEM Dedicato (Bare Metal) su Ubuntu Server LTS.
- **Obbiettivo:** Off-loading dei compiti di monitoraggio dalla workstation principale e creazione di una console di controllo dedicata.

## SIEM Infrastructure Migration
- **Manager Migration:** Trasferimento del Wazuh Manager da ambiente virtuale (VMware) a server fisico dedicato.
- **Resource Off-loading:** Recupero di 6GB di RAM e 4 vCPU sulla workstation principale, migliorando la stabilità complessiva del laboratorio durante le fasi di attacco simulato.
- **Persistence Tuning:** Configurazione dei parametri di sistema (logind.conf) per garantire l'operatività del server "Headless" anche con coperchio chiuso (ignore lid switch).

## SOC Operational Cockpit
- **Multi-Monitor Monitoring:** Implementazione di una postazione di controllo dedicata sfruttando una GPU RTX 4060Ti per gestire un monitor secondario da 13" dedicato esclusivamente alla telemetria.
- **Terminal Multiplexing:** Utilizzo di tmux per il monitoraggio simultaneo dei log in tempo reale (alerts.json) e l'amministrazione remota via SSH.
- **Log Filtering:** Implementazione di filtri via CLI (grep -v "keepalive") per la pulizia del rumore di fondo e la visualizzazione focalizzata sugli eventi di sicurezza critici.

## Networking & Connettività Sicura
- **Implementazione Rete in Cascata:** Configurazione di un'architettura a doppio router per creare una zona di rete sicura.
- **Segmentazione e Isolamento (VLAN/Guest):** Reti isolate per dispositivi IoT/Guest (Zero Trust).
- **Overlay Network (SD-WAN):** Implementazione ZeroTier per accesso remoto sicuro.
- **Privacy DNS:** Configurazione DNS over HTTPS (DoH) e DNS over TLS (DoT).

### Network Intrusion Detection (NIDS) Implementation
- **Tool:** Suricata IDS (8.0.3 RELEASE)
- **Deployment:** Installazione Bare Metal su server dedicato (HP .60).
- **Hardening & Tuning:** 
    - Ottimizzazione delle performance tramite disabilitazione dei log non critici (HTTP, DNS, Flow).
    - Implementazione di filtri di soppressione per falsi positivi (Ethertype unknown, ICMP unknown code) tramite `threshold.config`.
- **SIEM Integration:** Pipeline integrata per l'ingestione dei log JSON (`eve.json`) in Wazuh, permettendo la correlazione tra eventi di rete ed eventi endpoint.
- **Test di Validazione:** Rilevamento riuscito della firma `GPL ATTACK_RESPONSE` (ID: 2100498) simulando un'esfiltrazione di privilegi.

## Monitoring 
[Wazuh Dashboard](https://github.com/amann-studio/SOC-Defense-Lab/blob/main/image.png)

"Configurazione di una pipeline di telemetria completa: Sysmon (Endpoint) -> Wazuh Agent -> Wazuh Manager (SIEM). Capacità di analisi granulare dei log tramite archives.json per il tracking di esecuzioni di processi (EventID 1) e command-line auditing."

## Vulnerability Management & Remediation
- **SCA Analysis:** Identificazione di vulnerabilità critiche tramite il modulo Security Configuration Assessment di Wazuh (es. Weak Password Policy su account amministrativi).
- **Remediation Cycle:** Applicazione del ciclo di vita dell'incidente: Detection (Wazuh) -> Analysis (SCA logs) -> Remediation (PowerShell net user hardening) -> Verification.

### Attack & Detection Simulations
- **Brute Force Attack (Credential Guessing):** Simulato attacco via SMB tramite `smbclient` e `Hydra` da Kali Linux.
- **Detection:** Rilevamento riuscito tramite Wazuh Rule 60122 (Multiple logon failures) mappata su MITRE T1110.
- **Advanced Telemetry:** Identificazione di processi critici di sistema tramite Sysmon (EventID 1), con rilevamento di tecniche di *Application Shimming* (T1546.011) tramite il processo `sdbinst.exe`.

###  Active Response & Automated Defense
Ho implementato una logica di difesa attiva per mitigare attacchi di tipo Brute Force in tempo reale.

- **Trigger Rule:** `60122` (Multiple Windows logon failures).
- **Action:** Esecuzione automatica di `netsh.exe` sull'endpoint per il ban temporaneo dell'IP sorgente nel Firewall di Windows (10 minuti).
- **Log Evidence (Internal Protection Test):**
  Durante i test di stress locali, il sistema ha correttamente identificato i fallimenti di login, attivando il modulo di risposta.

```json
  "program": "active-response/bin/netsh.exe",
  "command": "check_keys",
  "parameters": {"keys": ["::1"]},
  "status": "Aborted"
```

Il log seguente dimostra la capacità del SIEM di distinguere tra attacchi esterni e attività locale:

  [Visualizza log](./logs/active-response-demo.json)
