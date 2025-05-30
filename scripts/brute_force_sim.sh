#!/bin/bash
# Simulates brute force login attempts in a log format for analysis testing

user="admin"
for i in {1..5}; do
  echo "Failed login for $user from 192.168.1.$i"
done
