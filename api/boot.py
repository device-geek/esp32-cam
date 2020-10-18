from network import WLAN,STA_IF,AP_IF

ap = WLAN(AP_IF)
ap.active(True)
ap.config(essid='esp32', password='codetyphon')

wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect('ssid', 'password')
