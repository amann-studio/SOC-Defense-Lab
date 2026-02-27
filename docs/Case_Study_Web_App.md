# Case Study: Vulnerability Assessment su Web Application .NET

Questo documento descrive l'analisi di sicurezza effettuata su una web application reale (ambiente di sviluppo), evidenziando le vulnerabilità scoperte e le metodologie di mitigazione suggerite.

## Obiettivo
Testare la resilienza dell'applicazione contro i principali attacchi definiti dall'OWASP Top 10.

## Tooling & Methodology
* **Proxy:** Burp Suite Professional (Intercettazione e Manipolazione HTTP).
* **Scanner DAST:** OWASP ZAP (Scansione passiva e attiva controllata).
* **Approccio:** Analisi manuale delle richieste/risposte per identificare falle logiche.

## Vulnerabilità Identificate

### 1. IDOR (Insecure Direct Object Reference)
* **Descrizione:** Manipolando l'ID della risorsa nell'URL, è stato possibile accedere ai dati di altri utenti senza autorizzazione.
* **Impatto:** Critico - Violazione della privacy e potenziale esfiltrazione massiva di dati.

### 2. Stored XSS (Cross-Site Scripting)
* **Descrizione:** Un campo di input non sanificato ha permesso l'iniezione di uno script malevolo salvato permanentemente nel database del server.
* **Impatto:** Alto - Possibilità di furto di cookie di sessione (Session Hijacking) per ogni utente che visualizza la pagina infetta.

## Remediation (Suggerimenti per lo Sviluppatore)
* Implementazione di controlli di autorizzazione lato server per ogni richiesta (Fix IDOR).
* Validazione rigorosa degli input e codifica (Encoding) degli output per prevenire l'esecuzione di script nel browser (Fix XSS).
