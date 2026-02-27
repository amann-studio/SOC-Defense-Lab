# Software Stack & Security Tools

La selezione dei software segue il principio di "Minima Superficie d'Attacco", preferendo versioni Portable e tool Open Source.

## Security & Monitoring
*   **Wazuh:** SIEM/XDR per l'analisi centralizzata dei log e integrità del sistema.
*   **Suricata:** NIDS per l'analisi del traffico di rete in tempo reale.
*   **Sysmon (SwiftOnSecurity config):** Monitoraggio avanzato dei processi Windows.
*   **Wireshark & Npcap:** Analisi profonda dei pacchetti e troubleshooting di rete.
*   **KeePassXC:** Gestione password offline con crittografia AES-256.

## Networking & Remote Access
*   **ZeroTier One:** Overlay Network per accesso remoto sicuro (MTU 1400 optimized).
*   **OpenVPN:** Connettività verso laboratori esterni (TryHackMe).
*   **NetMonster (Android):** Analisi delle bande 4G/5G e segnale radio.

## Vulnerability Research & Application Testing
*   **Burp Suite Professional:** Intercettazione e manipolazione traffico HTTP/S, utilizzo del Decoder locale per analisi Token JWT e Base64.
*   **OWASP ZAP (ZAPROXY):** DAST (Dynamic Application Security Testing) per scansioni di vulnerabilità automatizzate e analisi degli header di sicurezza.
*   **Postman:** Testing metodico di endpoint API, crafting di richieste personalizzate e analisi delle risposte JSON.
*   **Kali Linux (WSL2):** Ambiente operativo per test di penetrazione e ricognizione.

## OSINT, Reconnaissance & Environment Labs
*   **Win-KeX:** Interfaccia grafica per ambiente Kali Linux su Windows.
*   **Subfinder & Httpx:** Reconnaissance e analisi di sottodomini.
*   **GameShell:** Training environment per CLI Linux.

## Maintenance & Forensic Utility
*   **WizTree:** Analisi rapida dello spazio disco.
*   **BleachBit:** Pulizia sicura delle tracce di sistema.
*   **Autoruns:** Audit dei processi all'avvio del sistema.
*   **Revo Uninstaller:** Rimozione completa di software e residui di registro.
*   **ncdu (Linux):** Analisi occupazione disco su Server HP.

## Productivity & Hardening
*   **uBlock Origin Lite:** Content blocking conforme a MV3.
*   **Canvas Fingerprint Defender:** Mitigazione del tracciamento browser.
*   **Greenshot:** Documentazione rapida di incidenti e configurazioni.
*   **G-Helper:** Alternativa leggera al bloatware ASUS per il controllo hardware.

---

## Operational Tuning & Noise Reduction 
Un sistema di monitoraggio non calibrato genera "Alert Fatigue". Ho implementato le seguenti ottimizzazioni per focalizzare l'analisi sulle minacce reali:

### Wazuh Tuning
*   **Rootcheck Exclusion (Alert 510):** Whitelist dell'interfaccia di rete in modalità promiscua per eliminare i falsi positivi legati all'attività legittima dell'IDS.
*   **Active Response (Rule 60122):** Calibrazione del blocco automatico IP tramite `netsh` per prevenire attacchi Brute Force SMB/RDP.

### Suricata Tuning
*   **Signature Suppression (`threshold.config`):**
    *   **SID 2200121:** Silenziamento alert relativi a Ethertype non riconosciuti.
    *   **SID 2200025:** Soppressione rumore ICMP in contesti di rete locale sicura.
*   **Logging Hardening:** Disabilitazione dei log ridondanti (DNS, TLS, Flow) nel file `eve.json` per ridurre l'I/O su disco del 90% e preservare l'hardware legacy.
