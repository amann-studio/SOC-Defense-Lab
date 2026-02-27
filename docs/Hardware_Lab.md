# Hardware Lab Inventory

L'infrastruttura del laboratorio è composta da hardware eterogeneo, ottimizzato per bilanciare performance e sostenibilità (reuse di hardware legacy).

## 1. Main Workstation (Hardened Node)
*   **Modello:** Custom PC (Andrea)
*   **OS:** Windows 11 Pro (Hardened - Local Account Only)
*   **Storage:** 
    *   C: (System) - SSD 
    *   D: (LAVORO) - Partizione dedicata ai dati sensibili e DB KeePassXC.
    *   E: (SVAGO) - Partizione isolata.
*   **Ruolo:** Endpoint principale monitorato da Wazuh e Sysmon.

## 2. Red Team Node (Rogue Device)
*   **Modello:** ASUS FX503VD (Gaming Series)
*   **CPU:** Intel Core i7-7700HQ @ 2.80GHz
*   **RAM:** 16GB DDR4
*   **GPU:** NVIDIA GeForce GTX 1050 (4GB GDDR5)
*   **Storage:** SSD 128GB (OS) + SSD 1TB (Tools/VM)
*   **Ruolo:** Macchina dedicata ai test di attacco, simulazione minacce e OSINT.

## 3. SOC Sentinel (NIDS/SIEM Server)
*   **Modello:** Notebook HP dv6 (Legacy 2010 - Restaurato)
*   **CPU:** Intel Core i5 (1st Gen)
*   **RAM:** 4GB
*   **Storage:** SSD 128GB (Nuovo)
*   **Manutenzione:** Pasta termica sostituita (Arctic MX-4), configurato per operatività Headless (Lid Switch Ignore).
*   **Ruolo:** Server Ubuntu 22.04 LTS dedicato a Wazuh Manager e Suricata IDS.

## 4. Network Equipment
*   **Edge Router:** Cudy WR3000H (Wi-Fi 6, Dual-Core CPU).
*   **Managed Switch:** TP-Link TL-SG605E (Gigabit, Easy Smart).
*   **Failover Gateway:** Cudy LT700E (4G LTE Connectivity).
