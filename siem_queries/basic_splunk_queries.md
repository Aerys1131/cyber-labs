# 🔍 Basic Splunk Queries

## Failed Logins
```spl
index=auth sourcetype=linux_secure "Failed password"
