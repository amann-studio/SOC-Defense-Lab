# Network Architecture & Security Strategy

## Segmentazione della Rete
Il laboratorio adotta una struttura a router in cascata per isolare il traffico di test dalla rete domestica (ISP).

*   **Subnet Operativa:** `192.168.10.0/24`
*   **Management Switch:** `192.168.10.250`
*   **SOC Server:** `192.168.10.60`

## Visibilità (L2 SPAN)
Il monitoraggio è garantito tramite **Port Mirroring** sullo switch TP-Link:
*   **Source:** Porta 2 (Main Desktop).
*   **Destination:** Porta 5 (HP Server).
*   Suricata opera in **Promiscuous Mode** sull'interfaccia `enp3s0` per analizzare il traffico specchiato.

## Business Continuity (Failover)
È implementato un sistema di ridondanza WAN tramite il router LTE **Cudy LT700E**.
*   **Protocollo:** Manual Failover (Cold Standby).
*   **Configurazione LTE:** MTU fissato a `1420` per reti mobili.
*   **Isolamento:** Sottorete LTE `192.168.20.0/24` per prevenire conflitti durante lo switchover.

## Overlay Network (VPN)
Accesso remoto sicuro gestito via **ZeroTier**:
*   **Indirizzamento:** `10.101.152.0/24`
*   **Optimization:** MTU settato a `1400` su tutti i nodi per evitare frammentazione dei pacchetti e "Black Holes" ICMP.
