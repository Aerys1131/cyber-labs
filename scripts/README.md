# 🧪 Cybersecurity Scripts

This folder contains hands-on cybersecurity tools developed as part of the Google Cybersecurity Certificate training. Each script demonstrates a practical concept used in threat detection, log analysis, or network scanning.

---

## 📜 `port_scan.py`

A basic TCP port scanner for scanning common service ports on a specified IP address.

**Usage:**
```bash
python3 port_scan.py
```

**Prompts:**
- Target IP (e.g., `192.168.1.1`)

---

## ⚙️ `brute_force_sim.sh`

Simulates brute force SSH login attempts by echoing repeated failed login entries. Useful for testing log parsing and brute-force detection logic.

**Usage:**
```bash
bash brute_force_sim.sh >> fake_auth.log
```

---

## 🧠 `log_parser_enhanced.py`

A Python-based log parser that:
- Parses failed/successful SSH login attempts
- Detects brute-force IPs based on threshold
- Optionally exports to CSV
- Accepts command-line arguments for flexibility

**Usage:**
```bash
python3 log_parser_enhanced.py -f /var/log/auth.log
python3 log_parser_enhanced.py -f auth.log -o output.csv -t 3
```

**Options:**
- `-f`: Path to log file (required)
- `-o`: Output CSV path (optional)
- `-t`: Brute force threshold (default: 5)

---

These scripts are part of a live training repo and can be expanded as more tools are developed.

_Last updated: May 29, 2025_
