# 🔐 SSH SIEM Queries

This file includes Splunk-style queries and explanations for monitoring Secure Shell (SSH) activity in a Security Information and Event Management (SIEM) platform.

---

## ✅ Successful SSH Logins

```spl
index=syslog sourcetype=linux_secure "Accepted password" OR "Accepted publickey"
```
**Description:**  
Detects successful SSH logins using either a password or a public key.

---

## 🚫 Failed SSH Logins

```spl
index=syslog sourcetype=linux_secure "Failed password" OR "authentication failure"
```
**Description:**  
Flags failed login attempts, often a sign of password brute-force attempts or misconfigured systems.

---

## 🚨 Brute Force Attempt Detection

```spl
index=syslog sourcetype=linux_secure "Failed password"
| stats count by src_ip, user
| where count > 10
```
**Description:**  
Shows IP addresses and users with 10 or more failed SSH login attempts — potential brute-force activity.

---

## 🌍 SSH Access from External IPs

```spl
index=syslog sourcetype=linux_secure "Accepted"
| lookup geoip clientip as src_ip
| where country != "United States"
```
**Description:**  
Flags successful SSH logins from outside the expected geographic region.

---

## 🕵️‍♂️ SSH Session Duration Estimation (Advanced)

```spl
index=syslog sourcetype=linux_secure ("session opened" OR "session closed")
| transaction user startswith="session opened" endswith="session closed"
```
**Description:**  
Estimates session duration per user using open/close logs — useful for anomaly detection or tracking insider behavior.

---

_Last updated: May 29, 2025_
