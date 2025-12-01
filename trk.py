import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# COLOR  
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

os.system("clear")

# =============================================================
# ANIMASI BANNER IPAN
# =============================================================

def banner_anim():
    ipan = r"""
██╗██████╗  █████╗ ███╗   ██╗
██║██╔══██╗██╔══██╗████╗  ██║
██║██████  ███████║██╔██╗ ██║
██║██       ██╔══██║██║╚██╗██║
██║██║      ██║  ██║██║ ╚████║
╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝
"""

    colors = [
        "\033[38;5;196m", "\033[38;5;202m", "\033[38;5;208m",
        "\033[38;5;214m", "\033[38;5;220m", "\033[38;5;190m",
        "\033[38;5;46m", "\033[38;5;51m", "\033[38;5;93m",
        "\033[38;5;201m"
    ]

    import itertools
    for color in itertools.islice(itertools.cycle(colors), 15):
        os.system("clear")
        print(color + ipan + "\033[0m")
        time.sleep(0.1)

# Tampilkan animasi
banner_anim()

# =============================================================
# MENU UTAMA
# =============================================================

stderr.writelines(f"""{Gr}

    \033[38;5;196m██\033[38;5;202m██\033[38;5;208m██\033[38;5;214m██\033[38;5;220m██\033[0m   \033[38;5;51m██\033[38;5;45m██\033[38;5;39m██\033[38;5;33m██\033[38;5;27m██\033[0m   \033[38;5;201m██\033[38;5;198m██\033[38;5;200m██\033[38;5;163m██\033[38;5;127m██\033[0m   \033[38;5;118m██\033[38;5;82m██\033[38;5;46m██\033[38;5;40m██\033[38;5;34m██\033[0m

          {Wh}[ + ]  C O D E   B Y  I P A N C O D E S [ + ]  
        
    {Wh}[ 1 ] {Gr}IP Tracker
    {Wh}[ 2 ] {Gr}Show Your IP
    {Wh}[ 3 ] {Gr}Phone Tracker
    {Wh}[ 4 ] {Gr}Username Tracker
    {Wh}[ 0 ] {Gr}Exit
""")

menu = input(f"\n {Wh}IPAN-root → {Gr}")

# =============================================================
# 1. IP TRACKER
# =============================================================
if menu == "1":
    os.system("clear")
    try:
        ip = input(f"\n {Wh}Enter IP Target : {Gr}")
        data = requests.get(f"http://ipwho.is/{ip}").json()

        if not data["success"]:
            print(f"{Re}IP Tidak Valid!")
            exit()

        lat = data["latitude"]
        lon = data["longitude"]

        print(f"""
{Wh}=========== {Gr}IP INFORMATION {Wh}===========

{Wh}IP             : {Gr}{ip}
{Wh}TYPE           : {Gr}{data['type']}
{Wh}COUNTRY        : {Gr}{data['country']}
{Wh}CITY           : {Gr}{data['city']}
{Wh}REGION         : {Gr}{data['region']}
{Wh}LAT            : {Gr}{lat}
{Wh}LON            : {Gr}{lon}
{Wh}GOOGLE MAPS    : {Gr}https://www.google.com/maps/@{lat},{lon},9z
{Wh}ORG            : {Gr}{data['connection']['org']}
{Wh}ISP            : {Gr}{data['connection']['isp']}
{Wh}TIMEZONE       : {Gr}{data['timezone']['id']}
{Wh}CURRENT TIME   : {Gr}{data['timezone']['current_time']}
""")

    except Exception as e:
        print(f"{Re}Error:", e)

# =============================================================
# 2. SHOW YOUR IP
# =============================================================
elif menu == "2":
    os.system("clear")
    try:
        print(f"{Wh}Fetching your IP...\n")
        req = requests.get("https://ipwho.is/").json()

        print(f"""
{Wh}=========== {Gr}YOUR IP INFORMATION {Wh}===========

{Wh}Your IP        : {Gr}{req['ip']}
{Wh}Country        : {Gr}{req['country']}
{Wh}City           : {Gr}{req['city']}
{Wh}ISP            : {Gr}{req['connection']['isp']}
{Wh}ORG            : {Gr}{req['connection']['org']}
{Wh}Timezone       : {Gr}{req['timezone']['id']}
{Wh}Current Time   : {Gr}{req['timezone']['current_time']}
""")

    except:
        print(f"{Re}Gagal mengambil IP!")

# =============================================================
# 3. PHONE TRACKER
# =============================================================
elif menu == "3":
    os.system("clear")
    try:
        num = input(f"\n {Wh}Enter phone number (+62xxxx): {Gr}")
        region = "ID"

        parsed = phonenumbers.parse(num, region)

        print(f"""
{Wh}=========== {Gr}PHONE INFO {Wh}===========

{Wh}Location   : {Gr}{geocoder.description_for_number(parsed, 'id')}
{Wh}Region     : {Gr}{phonenumbers.region_code_for_number(parsed)}
{Wh}Timezone   : {Gr}{", ".join(timezone.time_zones_for_number(parsed))}
{Wh}Provider   : {Gr}{carrier.name_for_number(parsed, 'en')}
{Wh}Valid      : {Gr}{phonenumbers.is_valid_number(parsed)}
{Wh}Possible   : {Gr}{phonenumbers.is_possible_number(parsed)}
{Wh}E.164      : {Gr}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}
""")

    except:
        print(f"{Re}Nomor tidak valid!")

# =============================================================
# 4. USERNAME TRACKER (SHERLOCK OSINT)
# =============================================================
elif menu == "4":
    os.system("clear")
    print(f"\n {Wh}Username Tracker menggunakan OSINT Sherlock API\n")
    
    username = input(f"{Wh}Masukkan username target : {Gr}")

    print(f"\n{Wh}Mencari akun dengan username {Gr}{username}{Wh}...\n")

    try:
        api = requests.get(f"https://api.sherlockproject.xyz/search/{username}").json()

        if "sites" not in api:
            print(f"{Re}API error!")
            exit()

        print(f"{Wh}=========== {Gr}RESULT FOUND {Wh}===========\n")

        for site in api["sites"]:
            if site["exists"]:
                print(f"{Gr}[ FOUND ] {Wh}{site['name']} → {Cy}{site['url']}")

        print(f"\n{Wh}=========== {Gr}SCAN COMPLETE {Wh}===========\n")

    except Exception as e:
        print(f"{Re}Error:", e)

# =============================================================
# EXIT
# =============================================================
elif menu == "0":
    print(f"{Gr}Exit...")

else:
    print(f"{Re}Wrong Input!")
