#!/usr/bin/env python3
import re
import csv
import argparse
from collections import Counter

# CLI argument setup
parser = argparse.ArgumentParser(description="Parse SSH logs for failed/successful login attempts.")
parser.add_argument("-f", "--file", type=str, required=True, help="Path to the SSH auth log file")
parser.add_argument("-o", "--output", type=str, help="Optional output CSV file path")
parser.add_argument("-t", "--threshold", type=int, default=5, help="Brute-force IP threshold")
args = parser.parse_args()

log_file = args.file
output_file = args.output
brute_force_threshold = args.threshold

# Regex patterns
failed_login_pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d.]+)")
successful_login_pattern = re.compile(r"Accepted (\w+) for (\w+) from ([\d.]+)")

# Data storage
failed_logins = []
successful_logins = []

try:
    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                match = failed_login_pattern.search(line)
                if match:
                    user = match.group(2)
                    ip = match.group(3)
                    failed_logins.append((user, ip))
            elif "Accepted" in line:
                match = successful_login_pattern.search(line)
                if match:
                    method = match.group(1)
                    user = match.group(2)
                    ip = match.group(3)
                    successful_logins.append((user, method, ip))

    # Brute-force detection
    failed_ips = [ip for _, ip in failed_logins]
    ip_counter = Counter(failed_ips)
    brute_force_ips = [ip for ip, count in ip_counter.items() if count >= brute_force_threshold]

    # Output results
    print("\n--- Failed Logins ---")
    for user, ip in failed_logins:
        print(f"User: {user} | IP: {ip}")

    print("\n--- Successful Logins ---")
    for user, method, ip in successful_logins:
        print(f"User: {user} | Method: {method} | IP: {ip}")

    print("\n--- Brute Force IPs (>= {brute_force_threshold} attempts) ---")
    for ip in brute_force_ips:
        print(f"IP: {ip} | Attempts: {ip_counter[ip]}")

    # Optional CSV export
    if output_file:
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Type", "User", "Method", "IP"])
            for user, ip in failed_logins:
                writer.writerow(["Failed", user, "", ip])
            for user, method, ip in successful_logins:
                writer.writerow(["Successful", user, method, ip])
        print(f"\nResults saved to {output_file}")

except FileNotFoundError:
    print(f"Log file '{log_file}' not found. Please check the path.")
