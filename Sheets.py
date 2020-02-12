import gspread
import os
import unittest
from lifter import Lifter
from selenium import webdriver
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#retrieve API from google on GoogleDrive and Spreadsheets

creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)
#importing creditensals from Creds file which I downloaded via GoogleDriveAPI

client = gspread.authorize(creds)
#authorizzing my google account with creds - trust this unknown application

sheet = client.open("Lifting_results").sheet1
# opens XML file on Google Drive on the first sheet

data = sheet.get_all_records()
#collects all data that are stored on that first page of XML file

lifterList = []
#empty array of lifters

class TestLifters(unittest.TestCase):
    # making a class of TestLifters which is accompanied by a library of unit tests
    def test_equal(self):   
        for x in data:
            dvigalec = Lifter.make_lifter(x["Ime"], x["Poteg"], x["Sunek"])

            lifterList.append(dvigalec)
            # for every x in data got from Sheet 1, creates a dvigalec based on three characteristics "Ime", "Poteg", "Sunek"
        browser = webdriver.Chrome()
        current_dir = os.getcwd()
        browser.get(current_dir + "\\MojaSpletnaStran.html")  #opens Chrome browser and gets the path to MojaSpletnaStran.html file where you downloaded it
        # opens Chrome browser and gets the path to MojaSpletnaStran.html file where you downloaded it
        elem_name = browser.find_element_by_id("Ime")
        elem_poteg = browser.find_element_by_id("Poteg")
        elem_sunek = browser.find_element_by_id("Sunek")
        # finds elements in html file based on ID

        for l in lifterList:
            elem_name.send_keys(l.name)
            elem_poteg.send_keys(l.snatch)
            elem_sunek.send_keys(l.cj)
            browser.find_element_by_class_name('buttonDodaj').click()
        # for every l in lifterList array of dvigalec, sends keys from data to certain element ID and at the end clicks a button on html page



        elem_table_rows = browser.find_elements_by_class_name('tr')
        # Test for comparrison between Excell sheet and output table on HTML webpage
        keys = ["Ime", "Poteg", "Sunek", "Biatlon"]
        # defining array of strings with values same as elements by class name tr
        indexE = 1
        while indexE < len(elem_table_rows):
            # indexE = 1 as long as it is shorter then the length of elem table rows which is in our case 8 (lifters) and we start at 1 cuz that's the position of the first lifter
            lifter_array = elem_table_rows[indexE].text.split(' ')
            # splits the text by the empty string so that we have 3 values of name, snatch, cj
            indexL = 0
            while indexL < len(lifter_array)-1 :
                self.assertEqual(lifter_array[indexL], str(data[indexE-1][keys[indexL]]))
                # {["Ime":"Luka", "Poteg": "110", ....], ["Ime": "Jure", ....]}    #compares if the a is equal to b on a lifter array which is on the site and with the data extracted from googledrive sheet 1, finds them by the keys we selected


                # if lifter_array[indexL] != str(data[indexE-1][keys[indexL]]):
                #     print('Error!')
                # else:
                #     print(lifter_array[indexL] + ": OK")

                # this whole commented section is the alternative path to compare if the inserted data on html is equal to data in excell document.
                indexL += 1
            indexE += 1
        print("Konec!")

if __name__ == '__main__':
    unittest.main()



