""" Main data for json file (in json format). """

from database import getText, getNum, getFile
from const import *
import json

db = {
    "swd": {
        "timings": getText(SWD_TIME, "SWD"),
        "number": getText(SWD_NUM, "SWD"),
        "email": getText(SWD_EMAIL, "SWD")
    },
    "arcd": {
        "timings": getText(ARCD_TIME, "ARCD"),
        "number": getText(BK_ROUT_NUM, "BK Rout Assoc Dean"),
        "email": getText(ARCD_EMAIL, "ARCD")
    },
    "pizzeria": {
        "timings": getText(PIZZ_TIME, "Pizzeria"),
        "number": getText(PIZZ_NUM, "Pizzeria"),
        "menu": getFile(PIZZ_MENU, "image"),
        "address": getText(PIZZ_ADD, "Pizzeria")
    },
    "ic": {
        "timings": getText(IC_TIME, "IC")
    },
    "s9": {
        "timings": getText(S9_TIME, "S9"),
        "number": getText(S9_NUM, "S9")
    },
    "skylabs": {
        "timings": getText(SKY_TIME, "Skylabs"),
        "menu": getFile(SKY_MENU, "image")
    },
    "foodking": {
        "timings": getText(FK_TIME, "Food King"),
        "number": getText(FK_NUM, "Food King"),
    },
    "looters": {
        "timings": getText(LOOTERS_TIME, "Looters"),
        "menu": getFile(LOOTERS_MENU, "image")
    },
    "anc": {
        "timings": getText(ANC_TIME, "ANC")
    },
    "akshay": {
        "timings": getText(AKSHAY_TIME, "Akshay")
    },
    "library": {
        "timings": getText(LIBRARY_TIME, "Library")
    },
    "ipc": getText(IPC_TIME, "IPC"),
    "devsaria": {
        "number": getText(DEVSARIA_NUM, "Devsaria")
    },
    "kamals": {
        "number": getText(KAMALS_NUM, "Kamals Restaurant")
    },
    "sharmas": {
        "number": getText(SHARMAS_NUM, "Sharmas Restaurant")
    },
    "macncheese": {
        "number": getText(MACNCHEESE_NUM, "Mac and Cheese"),
        "address": getText(MACNCHEESE_ADD, "Mac and Cheese")
    },
    "sandpiper": {
        "number": getText(SANDPIPER_NUM, "Sandpipers Cafe"),
        "address": getText(SANDPIPER_ADD, "Sandpipers Cafe"),
        "timings": getText(SANDPIPER_TIME, "Sandpiper Cafe")
    },
    "roongta": {
        "number": getText(ROONGTA_NUM, "Roongta Book Store")
    },
    "nlforman": {
        "number": getText(NL_NUM, "NL Forman")
    },
    "nobles": {
        "number": getText(NOBLES_NUM, "Nobles")
    },
    "whatsapp": {
        "linguistics": getNum(LING_GRP, "Ling group", "web_url"),
        "cinead": getNum(CINEAD_GRP, "CineAd group", "web_url"),
        "pava": getNum(PAVA_GRP, "PAVA group", "web_url"),
        "masscom": getNum(MASSCOMM_GRP, "Mass Comm group", "web_url"),
        "pom": getNum(POM_GRP, "POM group", "web_url")
    },
    "dezire": getText("Dezire address:\n172.17.29.12"),
    "laundromat": getText(LAUNDRO_TIME, "Laundromat Timings"),
    "twelve": {
        "timings": getText(TWELVE_TIME, "Twelve Tables"),
        "number": getText(TWELVE_NUM, "Twelve Tables"),
        "address": getText(TWELVE_ADD, "Twelve Tables"),
        "menu": getFile(TWELVE_MENU, "image")

    },
    "laptop": getText(LAPTOP_REP, "Laptop Repair, Akshay"),
    "momo": getText(MOMO, "Momos, BITS gate"),
    "chamber": getText("Ae ghot!\nI don't know the chamber numbers :P"),
    "consultation":
        getText("Ae ghot!\nI don't know the consultation hours :P"),
    "sunshine": {
        "address": getText(SUNSHINE_ADD, "Hotel Sunshine"),
        "number": getText(SUNSHINE_NUM, "Hotel Sunshine")
    },
    "dc": getNum(["dezire"], ["Dezire"], "postback"),
    "nalanda":
        getText("Sorry, Nalanda updates are not available right now"),
    "medc": getFile(MEDC, "image"),
    "hospital": getText(SARVAJANIK, "Birla Sarvajanik"),
    "calender": getFile(CALENDER, "image"),
    "help": getText(HELP),
    "dentist": getText(DENTIST_TIME, "Dentist"),
    "handout": getText("Handouts:\n" + HANDOUT_ID),
    "chief": getText(CW_NUM, "CW Shibasish C"),
    "vc": getText(VC_NUM, "VC, Souvik B."),
    "amit": getText(AMIT_CAB, "Amit Travels"),
    "pathak": getText(PATHAK_CAB, "Pathak Travels"),
    "verma": getText(VERMA_CAB, "Verma Travels"),
    "sangam": getText(SANGAM_CAB, "Sangam Travels"),
    "director": getText(DIRECTOR_NUM, "Director AK Sarkar"),
    "president": getText(PREZ_NUMBER, "Bharat Puli"),
    "secretary": getText(GENSEC_NUMBER, "Shivam Jindal"),
    "creator": getText(CREATOR, "BoB ke builders"),
    "cab": getNum(CAB_TAGS, CAB_NAMES, "postback"),
    "hotels": getNum(HOTEL_TAGS, HOTEL_NAMES, "postback"),
    "connaught": getNum(CON_TAGS, CON_NAMES, "postback"),
    "nudes": getText("You first ;)"),
    "mess":
        getNum(
            ['breakfast',
             'lunch',
             'dinner'],
            ["Breakfast",
             "Lunch",
             "Dinner"],
     "postback"),
    "timetable": getFile(TIMETABLE),
    "bulletin": getNum(BULLETIN_LINK, "Bulletin", "web_url"),
    "prereq": getFile(PREREQ),
    "breakfast": "breakfast",
    "lunch": "lunch",
    "dinner": "dinner",
    "midsem": {
        "seating": getFile(MIDSEM_SEATING),
        "dates": getFile(MIDSEM_DATES)
    },
    "erp": {
        "inside": getText("ERP inside campus:\n" + ERP_INSIDE),
        "outside": getNum(
            ERP_OUTSIDE,
            "ERP Outside campus link",
            "web_url")
    },
    "map": getFile(MAP, "image"),
    "wifi": getFile(WIFI_SETUP),
    "bus": {
        "jaipur": getNum(RSRTC_LINK, "RSRTC Bus Enquiry", "web_url"),
        "delhi": getFile(DELHIBUS, "image"),
    },
    "bye": getText("Goodbye! :D"),
    "thanks": getText("Welcome! :D"),
    "vfast": getText(VFAST_NUM, "VFAST"),
    "valentine": getText(
        ["I don't talk about such things.\nI'm already committed to another bot",
         "Try asking Siri out, she is still single"])
}

for hostel in HOSTELS:
    db[hostel[0]] = {}
    db[hostel[0]]["supri"] = getText(hostel[1], hostel[0].upper() + " Supri")
    db[hostel[0]]["chowki"] = getText(hostel[2], hostel[0].upper() + " Chowki")
    db[hostel[0]]["warden"] = getText(hostel[3], hostel[0].upper() + " Warden")

with open('db/database.json', 'w') as f:
    f.write(json.dumps(db))
