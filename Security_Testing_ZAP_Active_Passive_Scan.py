import time
from zapv2 import ZAPv2

# Define your API key and ZAP proxy
api_key = "ieoq1svrkl3t6uplafk1t0pe1e"
zap = ZAPv2(apikey=api_key, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Target application URL
target_url = "http://targetwebsite.com"

# Passive Scanning
print("Starting passive scan...")

# Open the target URL
zap.urlopen(target_url)
time.sleep(2)  # Allow time for the page to load

# Passive scanning happens automatically when you browse the application
print("Passive scan in progress... Please navigate through the application.")

# Wait for passive scan to finish (you can monitor alerts periodically)
time.sleep(10)  # Adjust as necessary based on the application

# Check passive scan results
passive_alerts = zap.core.alerts()
print("Passive Scan Results:")
for alert in passive_alerts:
    print(f'URL: {alert["url"]}, Risk Level: {alert["risk"]}, Description: {alert["alert"]}')

# Active Scanning
print("Starting active scan...")

# Start the spider to crawl the site
scan_id = zap.spider.scan(url=target_url)

# Wait for the spider scan to finish
while int(zap.spider.status(scan_id)) < 100:
    print(f'Spider progress: {zap.spider.status(scan_id)}%')
    time.sleep(2)

# Now start the active scan
active_scan_id = zap.ascan.scan(url=target_url)

# Wait for the active scan to finish
while int(zap.ascan.status(active_scan_id)) < 100:
    print(f'Active scan progress: {zap.ascan.status(active_scan_id)}%')
    time.sleep(2)

# Check active scan results
active_alerts = zap.core.alerts()
print("Active Scan Results:")
for alert in active_alerts:
    print(f'URL: {alert["url"]}, Risk Level: {alert["risk"]}, Description: {alert["alert"]}')

print("Scanning completed.")