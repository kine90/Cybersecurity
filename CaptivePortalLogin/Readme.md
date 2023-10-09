Simple script using Selenium to demostrate how to bypass the login to an open WiFi Access Point captive portal seerving Javascript challenges.
It pings Google´s DNS to check if internet is up, otherwise it starts Selenium and uses chromedriver to load the captive portal, find the login button and click it.

The script can be run in a Proxmox Debian container and scheduled using crontab and the bash script.
