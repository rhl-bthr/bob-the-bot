"""
MIT License

Copyright (c) 2017 Divesh Uttamchandani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import openpyxl
import json
import glob

month = "03"
year = "2018"
nd = 0
breakfast_start = 5
breakfast_end = 13
lunch_start = 16
lunch_end = 24
dinner_start = 27
dinner_end = 34
no_of_days = 15

for wb in glob.glob("*.xlsx"):
    messywb = openpyxl.load_workbook(wb)
    messysheet = messywb.active

    for i in range(1, no_of_days + 1):
        breakfast = []
        lunch = []
        dinner = []
        if i < 10:
            date = "0" + str(i)
        else:
            date = str(i)
        filename = "../db/menu/" + date + "-" + month + "-" + year + ".json"
        for j in range(breakfast_start, breakfast_end + 1):
            # add to breakfast if not empty
            temp = messysheet.cell(row=j, column=i).value
            if(temp is not None and temp[0].isalpha()):
                breakfast.append(temp.strip())
        for j in range(lunch_start, lunch_end + 1):
            # add to lunch if not empty
            temp = messysheet.cell(row=j, column=i).value
            if(temp is not None and temp[0].isalpha()):
                lunch.append(temp.strip())
        for j in range(dinner_start, dinner_end + 1):
            # add to dinner if not empty
            temp = messysheet.cell(row=j, column=i).value
            if(temp is not None and temp[0].isalpha()):
                dinner.append(temp.strip())

        menu = {
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner
        }
        json_string = json.dumps(menu, indent=4)
        fi = open(filename, "w+")
        fi.write(json_string)
        fi.close()
