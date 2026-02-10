# SOC-Defense-Lab
Descrizione tecnica del mio laboratorio di monitoraggio e difesa cyber. Architettura, Hardening e Analisi SIEM.

## Lab Architecture
- **Host:** Windows 11 Hardened (i7-14700K | 32GB RAM | RTX 4060Ti)
- **Networking:** Dual-Router Cascade (TIM + Cudy WR3000H) con segmentazione IoT/Guest.
- **SIEM:** Wazuh (Ubuntu Server 22.04 VM) - *In fase di implementazione*
- **Monitoring:** Microsoft Sysmon + Wireshark.

## Networking & Connettività Sicura
- **Implementazione Rete in Cascata:** Configurazione di un'architettura a doppio router per creare una zona di rete sicura.
- **Segmentazione e Isolamento (VLAN/Guest):** Reti isolate per dispositivi IoT/Guest (Zero Trust).
- **Overlay Network (SD-WAN):** Implementazione ZeroTier per accesso remoto sicuro.
- **Privacy DNS:** Configurazione DNS over HTTPS (DoH) e DNS over TLS (DoT).

## Monitoring 
[Wazuh Dashboard](https://github.com/amann-studio/SOC-Defense-Lab/blob/main/image.png)

"Configurazione di una pipeline di telemetria completa: Sysmon (Endpoint) -> Wazuh Agent -> Wazuh Manager (SIEM). Capacità di analisi granulare dei log tramite archives.json per il tracking di esecuzioni di processi (EventID 1) e command-line auditing."
