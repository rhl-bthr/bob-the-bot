""" Main data for json file (in json format). """

from api_functions import get_file
from api_functions import get_url
from api_functions import get_text
from api_functions import get_postback
import json


HELP = ["""Please write precise queries\nFor example:
1. When does akshay open ?\n2. Whats in dinner today ?
3. Ram Chauki Contact Number\n4. What are the Medc timings ?
5. Pizzeria Menu\n6. Give a list of hotels nearby"""]

WHATSAPP_LINK = "https://chat.whatsapp.com/"
BOB_FILES = "https://www.pro-panda.tech/bob-the-bot/db/BOBFiles/"
MIDSEM_SEATING = BOB_FILES + "seating.pdf"
ERP_INSIDE = "https://10.2.102.21:9000/psp/hcsprod/?cmd=login"
ERP_OUTSIDE = "https://erp.bits-pilani.ac.in:4431/psp/hcsprod/?cmd=login"
HANDOUT_ID = "https://172.18.6.180/ID/Handouts.do"
RSRTC_LINK = "https://rsrtconline.rajasthan.gov.in/busenquiry"
CALENDER = BOB_FILES + "calender.jpg"
WIFI_SETUP = BOB_FILES + "wifisetup.pdf"
TIMETABLE = BOB_FILES + "TIMETABLE.pdf"
PREREQ = BOB_FILES + "prerequisites.pdf"
MIDSEM_DATES = BOB_FILES + "midsem_dates.pdf"
MAP = BOB_FILES + "map.jpg"
DELHIBUS = BOB_FILES + "delhibus.jpg"
MEDC = BOB_FILES + "medc.jpg"


SWD_TIME = "Weekdays: 9 AM - 5 PM\nSaturday: 9 AM - 2 PM\nClosed on Sunday."
PIZZ_TIME = "10 AM - 11 PM"
IC_TIME = "9 AM to 6 PM.\nSunday closed"
SKY_TIME = "Open all days.\n9 AM to 6 PM."
S9_TIME = "Open all days.\n9:30 AM - 8:30 PM"
AKSHAY_TIME = ("Weekdays:\n10am - 1:30pm, 4:30pm - 9pm\n"
               "Weekends:\n10am - 2pm, 4pm - 9pm\n"
               "Monday Closed")
IPC_TIME = ("All 7 days:\n9 AM to Midnight.\n"
            "1 PM to 2 PM - Lunch.\n7PM to 8 PM - Dinner.")
LIBRARY_TIME = "Weekdays: 9 AM - 11 PM\nHolidays: 9 AM - 5 PM\nGHOT!"
DENTIST_TIME = "Saturday 4PM - 7PM"
ARCD_TIME = "Weekdays: 9 AM - 5 PM\nLunch Hours 2 PM - 3 PM\nClosed on Sunday."

SANDPIPER_TIME = "Open all days\n11 AM - 11 PM"
FK_TIME = "Open all days\n5 PM - 2:15 AM"
LOOTERS_TIME = "Open all days\n5 PM - 2:15 AM"
ANC_TIME = "5 PM - 6 PM\n8:30 PM - 1:45 AM"
TWELVE_TIME = "Open all days\n11 AM - 10 PM"
LAUNDRO_TIME = "Open Everyday\n10 AM - 7 PM"
CREATOR = "Rahul Bothra\nSankalp Sangle\nManan Soni\nChinmay Hebbar"
BULLETIN = "http://arcd.bits-pilani.ac.in/imp_documents/Bulletin_2017-18.pdf"
LAPTOP_REP = "7055504472"
MOMO = "9953520309"

SWD_EMAIL = "swd@pilani.bits-pilani.ac.in"
ARCD_EMAIL = "arcd@bits-pilani.ac.in"
PIZZ_ADD = "Vatika Restaurant, Ganesh Colony"
SANDPIPER_ADD = "Near Panchwati, Pilani"
MACNCHEESE_ADD = "BK PLAZA, CEERI Road Pilani"
TWELVE_ADD = "RJ SH 13, Ganesh Nagar, Pilani"
SUNSHINE_ADD = "Near Ganga Colony, W. No. 14, Bus Stand, Pilani,"

PIZZ_MENU = [
    BOB_FILES + "pizzeria" + str(
        x) + ".jpg" for x in range(
            2,
             10)]
LOOTERS_MENU = [BOB_FILES + "looter" + str(x) + ".jpg" for x in range(1, 3)]
FK_MENU = [BOB_FILES + "fk" + str(x) + ".jpg" for x in range(1, 8)]
TWELVE_MENU = [BOB_FILES + "twelve" + str(x) + ".jpg" for x in range(1, 3)]
SKY_MENU = [BOB_FILES + "sky" + str(x) + ".jpg" for x in range(1, 3)]

BK_ROUT_NUM = "+91-01596515430"
SWD_NUM = "+91-01596242282"
S9_NUM = "9672673038"
DEVSARIA_NUM = "9829375581"
ROONGTA_NUM = "9694840027"
SARVAJANIK = "+91-01596242114"
MACNCHEESE_NUM = "8302334444"
SANDPIPER_NUM = "9680774044"
SANGAM_CAB = "9829236193"
AMIT_CAB = "9462239023"
VFAST_NUM = "+91-01596242183"
PATHAK_CAB = "9829612176"
VERMA_CAB = "9829438025"

CW_NUM = "9694096457"
VC_NUM = "+91-01596515255"
DIRECTOR_NUM = "+91-01596515244"
PIZZ_NUM = "9660432653"
FK_NUM = "7297835134"
KAMALS_NUM = "9460735551"
SHARMAS_NUM = "9887485601"
NL_NUM = "9784288555"
NOBLES_NUM = "7297059865"
TWELVE_NUM = "9309223344"
SUNSHINE_NUM = "+91-01596242651"

PREZ_NUMBER = "8297039977"
GENSEC_NUMBER = "9717024281"
GN_WARDEN = "9694096452"
SK_WARDEN = "9509045002"
VY_WARDEN = "9694096457"
RM_WARDEN = "9694096490"
BD_WARDEN = "9694096472"
BG_WARDEN = "9694196400"
RP_WARDEN = "9694096453"
AK_WARDEN = "9694096450"
MB_WARDEN = "9694096462"
SR_WARDEN = "9414082754"
VK_WARDEN = "9694096453"
MAL_WARDEN = "9694096460"
CVR_WARDEN = "9694096453"

GN_CHOWKI = "9460673162"
SK_CHOWKI = "<I don't have it. Sorry>"
VY_CHOWKI = "8769640715"
RM_CHOWKI = "9610302288"
BD_CHOWKI = "9929110686"
BG_CHOWKI = "<I don't have it. Sorry>"
RP_CHOWKI = "<I don't have it. Sorry>"
AK_CHOWKI = "<I don't have it. Sorry>"
MB_CHOWKI = "<I don't have it. Sorry>"
SR_CHOWKI = "7231066148"
VK_CHOWKI = "<I don't have it. Sorry>"
CVR_CHOWKI = "<I don't have it. Sorry>"
MAL_CHOWKI = "8769366142"

GN_SUPRI = "9694096485"
SK_SUPRI = "9694096474"
VY_SUPRI = "9694096474"
RM_SUPRI = "<I don't have it. Sorry>"
BD_SUPRI = "9785644053"
BG_SUPRI = "<I don't have it. Sorry>"
RP_SUPRI = "<I don't have it. Sorry>"
AK_SUPRI = "<I don't have it. Sorry>"
MB_SUPRI = "9694096469"
SR_SUPRI = "9694096464"
VK_SUPRI = "9694096474"
MAL_SUPRI = "<I don't have it. Sorry>"
CVR_SUPRI = "<I don't have it. Sorry>"

HOTEL_NAMES = [
    "Sharmas",
    "Kamals",
    "ANC",
    "LaPizzeria",
    "NL Forman",
    "Foodking",
    "Nobles",
    "Twelve Tables",
    "Sunshine",
    "Skylabs",
    "Sandpiper",
    "MacNCheese"]
HOTEL_TAGS = [
    "sharmas",
    "kamals",
    "anc",
    "pizzeria",
    "nlforman",
    "foodking",
    "nobles",
    "twelve",
    "sunshine",
    "skylabs",
    "sandpiper",
    "macncheese"]
CAB_NAMES = [
    "Amit Travels",
    "Pathak Travels",
    "Sangam Travels",
    "Verma Travels"]
CAB_TAGS = ["amit", "pathak", "sangam", "verma"]
CON_NAMES = ["Sharmas", "Kamals", "Nobles"]
CON_TAGS = ["sharmas", "kamals", "nobles"]

HOSTELS = [
    ["vk", VK_SUPRI, VK_CHOWKI, VK_WARDEN],
    ["bhagirath", BG_SUPRI, BG_CHOWKI, BG_WARDEN],
    ["ashok", AK_SUPRI, AK_CHOWKI, AK_WARDEN],
    ["meera", MB_SUPRI, MB_CHOWKI, MB_WARDEN],
    ["malviya", MAL_SUPRI, MAL_CHOWKI, MAL_WARDEN],
    ["sr", SR_SUPRI, SR_CHOWKI, SR_WARDEN],
    ["cvr", CVR_SUPRI, CVR_CHOWKI, CVR_WARDEN],
    ["shankar", SK_SUPRI, SK_CHOWKI, SK_WARDEN],
    ["gandhi", GN_SUPRI, GN_CHOWKI, GN_WARDEN],
    ["ram", RM_SUPRI, RM_CHOWKI, RM_WARDEN],
    ["budh", BD_SUPRI, BD_CHOWKI, BD_WARDEN],
    ["vyas", VY_SUPRI, VY_CHOWKI, VY_WARDEN],
    ["ranapratap", RP_SUPRI, RP_CHOWKI, RP_WARDEN]]


db = {
    "swd": {
        "timings": get_text(SWD_TIME, "SWD"),
        "number": get_text(SWD_NUM, "SWD"),
        "email": get_text(SWD_EMAIL, "SWD")
    },
    "arcd": {
        "timings": get_text(ARCD_TIME, "ARCD"),
        "number": get_text(BK_ROUT_NUM, "BK Rout Assoc Dean"),
        "email": get_text(ARCD_EMAIL, "ARCD")
    },
    "pizzeria": {
        "timings": get_text(PIZZ_TIME, "Pizzeria"),
        "number": get_text(PIZZ_NUM, "Pizzeria"),
        "menu": get_file(PIZZ_MENU, "image"),
        "address": get_text(PIZZ_ADD, "Pizzeria")
    },
    "ic": {
        "timings": get_text(IC_TIME, "IC")
    },
    "s9": {
        "timings": get_text(S9_TIME, "S9"),
        "number": get_text(S9_NUM, "S9")
    },
    "skylabs": {
        "timings": get_text(SKY_TIME, "Skylabs"),
        "menu": get_file(SKY_MENU, "image")
    },
    "foodking": {
        "timings": get_text(FK_TIME, "Food King"),
        "number": get_text(FK_NUM, "Food King"),
    },
    "looters": {
        "timings": get_text(LOOTERS_TIME, "Looters"),
        "menu": get_file(LOOTERS_MENU, "image")
    },
    "anc": {
        "timings": get_text(ANC_TIME, "ANC")
    },
    "akshay": {
        "timings": get_text(AKSHAY_TIME, "Akshay")
    },
    "library": {
        "timings": get_text(LIBRARY_TIME, "Library")
    },
    "ipc": get_text(IPC_TIME, "IPC"),
    "devsaria": {
        "number": get_text(DEVSARIA_NUM, "Devsaria")
    },
    "kamals": {
        "number": get_text(KAMALS_NUM, "Kamals Restaurant")
    },
    "sharmas": {
        "number": get_text(SHARMAS_NUM, "Sharmas Restaurant")
    },
    "macncheese": {
        "number": get_text(MACNCHEESE_NUM, "Mac and Cheese"),
        "address": get_text(MACNCHEESE_ADD, "Mac and Cheese")
    },
    "sandpiper": {
        "number": get_text(SANDPIPER_NUM, "Sandpipers Cafe"),
        "address": get_text(SANDPIPER_ADD, "Sandpipers Cafe"),
        "timings": get_text(SANDPIPER_TIME, "Sandpiper Cafe")
    },
    "roongta": {
        "number": get_text(ROONGTA_NUM, "Roongta Book Store")
    },
    "nlforman": {
        "number": get_text(NL_NUM, "NL Forman")
    },
    "nobles": {
        "number": get_text(NOBLES_NUM, "Nobles")
    },
    "dezire": get_text("Dezire address:\n172.17.32.87"),
    "laundromat": get_text(LAUNDRO_TIME, "Laundromat Timings"),
    "twelve": {
        "timings": get_text(TWELVE_TIME, "Twelve Tables"),
        "number": get_text(TWELVE_NUM, "Twelve Tables"),
        "address": get_text(TWELVE_ADD, "Twelve Tables"),
        "menu": get_file(TWELVE_MENU, "image")

    },
    "laptop": get_text(LAPTOP_REP, "Laptop Repair, Akshay"),
    "momo": get_text(MOMO, "Momos, BITS gate"),
    "chamber": get_text("Ae ghot!\nI don't know the chamber numbers :P"),
    "consultation":
        get_text("Ae ghot!\nI don't know the consultation hours :P"),
    "sunshine": {
        "address": get_text(SUNSHINE_ADD, "Hotel Sunshine"),
        "number": get_text(SUNSHINE_NUM, "Hotel Sunshine")
    },
    "dc": get_postback(["dezire"], ["Dezire"]),
    "nalanda":
        get_text("Sorry, Nalanda updates are not available right now"),
    "medc": get_file(MEDC, "image"),
    "hospital": get_text(SARVAJANIK, "Birla Sarvajanik"),
    "calender": get_file(CALENDER, "image"),
    "help": get_text(HELP),
    "dentist": get_text(DENTIST_TIME, "Dentist"),
    "handout": get_text("Handouts:\n" + HANDOUT_ID),
    "chief": get_text(CW_NUM, "CW Shibasish C"),
    "vc": get_text(VC_NUM, "VC, Souvik B."),
    "amit": get_text(AMIT_CAB, "Amit Travels"),
    "pathak": get_text(PATHAK_CAB, "Pathak Travels"),
    "verma": get_text(VERMA_CAB, "Verma Travels"),
    "sangam": get_text(SANGAM_CAB, "Sangam Travels"),
    "director": get_text(DIRECTOR_NUM, "Director AK Sarkar"),
    "president": get_text(PREZ_NUMBER, "Bharat Puli"),
    "secretary": get_text(GENSEC_NUMBER, "Shivam Jindal"),
    "creator": get_text(CREATOR, "BoB ke builders"),
    "cab": get_postback(CAB_TAGS, CAB_NAMES),
    "hotels": get_postback(HOTEL_TAGS, HOTEL_NAMES),
    "connaught": get_postback(CON_TAGS, CON_NAMES),
    "nudes": get_text("You first ;)"),
    "mess":
        get_postback(
            ['breakfast',
             'lunch',
             'dinner'],
            ["Breakfast",
             "Lunch",
             "Dinner"]),
    "timetable": get_file(TIMETABLE, "file"),
    "bulletin": get_url(BULLETIN, "Bulletin"),
    "prereq": get_file(PREREQ, "file"),
    "breakfast": "breakfast",
    "lunch": "lunch",
    "dinner": "dinner",
    "midsem": {
        "seating": get_file(MIDSEM_SEATING, "file"),
        "dates": get_file(MIDSEM_DATES, "file")
    },
    "erp": {
        "inside": get_text("ERP inside campus:\n" + ERP_INSIDE),
        "outside": get_url(
            ERP_OUTSIDE,
            "ERP Outside campus link")
    },
    "map": get_file(MAP, "image"),
    "wifi": get_file(WIFI_SETUP, "file"),
    "bus": {
        "jaipur": get_url(RSRTC_LINK, "RSRTC Bus Enquiry"),
        "delhi": get_file(DELHIBUS, "image"),
    },
    "bye": get_text("Goodbye! :D"),
    "thanks": get_text("Welcome! :D"),
    "vfast": get_text(VFAST_NUM, "VFAST"),
}

for hostel in HOSTELS:
    db[hostel[0]] = {}
    hostel_name = hostel[0].upper()
    db[hostel[0]]["supri"] = get_text(hostel[1], hostel_name + " Supri")
    db[hostel[0]]["chowki"] = get_text(hostel[2], hostel_name + " Chowki")
    db[hostel[0]]["warden"] = get_text(hostel[3], hostel_name + " Warden")

SRY_PREF = ["Sorry,", "Umm,", "Err,", "Whoops,"]
SRY_MSG = ["Dunno what you asked for :(", "I Didn't get you.",
           "I ain't that smart", "I have failed you :("]
HELP_MSG = ["Typing help might help", "Need help? type help"]
INTRO_PREF = ["Hey,", "Hi,", "Whassup", "Yo"]
INTRO_MSG = ["I'm BOB!", "It's me, BOB!", "My name is BOB!"]
INTRO_HELP = "Type 'help' to see the query guide."
master_dict = []

SRY_MSG_CONTENT = [[prefix + " " + content, help_msg] for prefix in SRY_PREF
                   for content in SRY_MSG for help_msg in HELP_MSG]
INTRO_MSG_CONTENT = [[pref + " <USERNAME>\n" + msg + " :D",
                     INTRO_HELP] for pref in INTRO_PREF for msg in INTRO_MSG]
hello_sorry = {
    "hello": INTRO_MSG_CONTENT,
    "sorry": SRY_MSG_CONTENT
}


def get_keys(dictionary):
    """
    Traverse the entire dictionary (inclding all subdictionaries)
    and store all keys in master_dict.
    """
    for key, value in dictionary.items():
        master_dict.append(key)
        if isinstance(value, dict):
            get_keys(value)


def update_dict():
    with open("../db/database.json") as f:
        db = json.load(f)

    with open("../db/mapping.json") as map_file:
        mapping = json.load(map_file)

    get_keys(db)
    get_keys(mapping)
    master_list = list(set(master_dict))
    with open('../db/dictionary.txt', 'w') as f:
        for word in master_list:
            f.write(word)
            if word != master_list[-1]:
                f.write("\n")


if __name__ == "__main__":
    with open('../db/database.json', 'w') as f:
        json.dump(db, f, indent=4)
    update_dict()
    with open('../db/hello-sorry.json', 'w') as f:
        json.dump(hello_sorry, f, indent=4)
