## Roadmap del Progetto

Il laboratorio è in costante evoluzione. Lo sviluppo è strutturato per macro-aree, partendo dalle fondamenta di rete fino ad arrivare all'automazione e all'integrazione dell'Intelligenza Artificiale.

### Network & Infrastructure
- [x] Configurazione Router in cascata e segmentazione LAN.
- [x] Implementazione Switch Managed con Port Mirroring (SPAN) per monitoraggio passivo.
- [x] Setup Failover LTE (Cold Standby) per garantire la Business Continuity.
- [x] Hardening Server: Accesso esclusivo via chiavi crittografiche (SSH RSA 4096).

### Detection Engineering & Blue Team 
- [x] Deploy centralizzato SIEM/XDR (Wazuh) e NIDS (Suricata) in modalità promiscua.
- [x] Endpoint Hardening tramite Sysmon (SwiftOnSecurity) e auditing avanzato di Windows.
- [x] Scrittura regole custom su Wazuh (es. Alert Livello 12 per accessi negati a partizioni isolate).
- [x] Operational Tuning: Ottimizzazione termica server HP e soppressione falsi positivi per evitare Alert Fatigue.
- [x] Threat Intelligence: Integrazione API VirusTotal per il file hashing e analisi reputazione.

### Vulnerability Research & Red Team (In corso)
- [x] Analisi manuale Web App in ambiente di staging tramite Burp Suite e Postman.
- [x] Identificazione e bypass di vulnerabilità critiche (IDOR, Stored XSS via Event Handler Injection).
- [ ] Simulazione d'attacco interno (Reconnaissance + Lateral Movement) per testare la correlazione dei log.

### Security Automation & Scripting (In corso)
- [x] Sviluppo script Bash (`soc-cleaner.sh`) con Cronjob per la Data Lifecycle Management (Log Retention).
- [x] Acquisizione fondamenti Python 3 (Control Flow, Data Structures).
- [x] Creazione script Python custom per il monitoraggio real-time dello stato degli asset (TTL Ping verification).

### Next Steps 
- [ ] Studio e pratica su piattaforme enterprise (Splunk Basics / SPL).
- [ ] Integrazione di "AI-Assisted Operations" (LLM applicati al Log Triage e incident response).
- [ ] Implementazione di scansioni DAST automatizzate (OWASP ZAP) su target controllati.

## Percorsi di Formazione & Certificazioni
Qui tengo traccia del mio studio quotidiano.

| Corso / Certificazione | Piattaforma | Status | Progresso |
| :--- | :--- | :--- | :--- |
| **Cybersecurity Technician** | Time Vision Srl | In corso | [=======>--] 70% |
| **ISC2 CC (Certified in Cybersecurity)** | ISC2 | Candidato | [----------] 0% |
| **SOC Level 1 Path** | TryHackMe | In corso | [==>-------] 15% |
| **Splunk Fundamentals** | TryHackMe | In corso | [=---------] 10% |
| **DevSecOps Path** | TryHackMe | In corso | [==>-------] 15% |
| **Cybersecurity Fundamentals** | IBM SkillsBuild | In corso | [===>------] 25% |
| **Python Fundamentals** | NetworkChuck/Self | Completato | [==========] 100% |

---
*Legenda: [=] = 10% di completamento.*