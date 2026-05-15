# EarlyWarning — Intrusion Detection System

A network intrusion detection system with a GUI built in Python. It monitors live traffic, detects port scans, manages firewall rules via nftables, and includes a vulnerability scanner targeting Metasploitable 2.

## Features

- **Live Connection Monitoring** — real-time view of active network connections with protocol, source/destination, state, packet count, and byte count
- **Port Scan Detection** — detects SYN, FIN, NULL, XMAS, UDP, and slow/low-and-slow scans using configurable time windows and thresholds
- **Firewall Rule Management** — create, edit, and delete rules (allow/deny/alert) through the GUI or built-in terminal; deny rules are enforced at the kernel level via nftables on Linux
- **Vulnerability Scanner** — scans a target host for known Metasploitable 2 vulnerabilities with banner grabbing and version confirmation
- **Security Logging** — all alerts are timestamped and persisted to a local SQLite database
- **Built-in Terminal** — command-line interface inside the app for scanning, rule management, and firewall control

## Requirements

- Python 3.10+
- macOS or Linux
- Root/sudo privileges (required for packet capture)

### Dependencies

- [Scapy](https://scapy.net/) — packet capture and analysis
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — GUI framework

## Installation

```bash
git clone <repo-url>
cd IDS
python3 -m venv .venv
source .venv/bin/activate
pip install scapy customtkinter
```

## Usage

```bash
python3 main.py
```

The app will prompt for sudo if not already running as root. On first launch it creates a SQLite database in `data/rules.db`.

### Terminal Commands

| Command | Description |
|---|---|
| `connections` | Live-updating connection table (Ctrl+C to stop) |
| `scan <ip>` | Quick scan — known Metasploitable 2 ports |
| `scan <ip> full` | Scan ports 1–1024 |
| `scan <ip> ports <start>-<end>` | Scan a custom port range |
| `rules` | List all firewall rules |
| `addrule <proto> <src_ip> <dst_ip> <src_port> <dst_port> <action>` | Add a rule |
| `editrule <id> <proto> <src_ip> <dst_ip> <src_port> <dst_port> <action>` | Edit a rule |
| `deleterule <id>` | Delete a rule |
| `firewall status\|on\|off` | Firewall control |
| `detector status` | Show port-scan detector settings |
| `clear` | Clear terminal output |

Use `any` or `0` as wildcards for IP/port fields.

## Project Structure

```
├── main.py                          # Entry point
├── src/
│   ├── UI/
│   │   └── home.py                  # CustomTkinter GUI
│   ├── ids/
│   │   ├── flow_monitor.py          # Packet sniffer & connection tracker
│   │   ├── port_scan_detector.py    # Scan detection engine
│   │   ├── firewall.py              # Rule matching & nftables integration
│   │   ├── port_scanner.py          # Vulnerability scanner
│   │   ├── terminal_controller.py   # In-app terminal command handler
│   │   └── refresh_connections.py   # Connection display helper
│   └── db/
│       ├── db_utils.py              # Database init & connection
│       └── CRUD.py                  # Rule & log database operations
└── data/
    └── rules.db                     # SQLite database (auto-created)
```

## Firewall Modes

- **allow** — traffic passes silently
- **deny** — traffic is dropped (nftables `drop` on Linux; software-only on macOS)
- **alert** — traffic is allowed but logged as suspicious

The firewall uses a permissive default policy — unmatched traffic is allowed.

## Port Scan Detection

The detector uses two detection windows:

- **Fast scan** — 25+ distinct ports and 10+ packets within 10 seconds
- **Slow scan** — 40+ distinct ports within a 3-minute window

A 30-second cooldown prevents duplicate alerts for the same source IP.
