import network
import urequests
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("YOUR SSID", "YOUR PASSWORD")
print(wlan.isconnected())
gbp = urequests.get("https://api.exchangerate-api.com/v4/latest/GBP").json()
dollar = gbp["rates"]["USD"]
euro = gbp["rates"]["EUR"]
print("The current value of the UK Pound to one US Dollar is £",dollar)
print("The current value of the UK Pound to one Euro is £",euro)