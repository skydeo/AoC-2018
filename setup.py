import datetime
import os
import re
import requests

"""
This is all kinda messy, but as a first pass and first time using requests,
not a terrible showing. Only intended for use by me anyway, so if something
breaks, 🤷🏼‍♂️
"""

v = True

with open("token.txt") as t:
  token = t.read().strip()

today = min(datetime.datetime.today().day, 25)
month = datetime.datetime.today().month

dir_list = sorted(os.listdir(os.path.expanduser(".")))
folders = [f for f in dir_list if re.search(r"day[0-9]{2}", f) and os.path.isdir(f)]

max_date = max([int(folder[-2:]) for folder in folders]) if len(folders) > 0 else 0



def download_input(day=None, year=None, session=token):
  url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"
  r = requests.get(url, cookies={"session": session})

  if not r.ok:
    return bytearray("An error occured in requesting data.", 'utf-8')
  else:
    return r.content




if today > max_date and month == 12:
  if v:
    if max_date == 0:
      print("No folders exist.")
    else:
      print("Last folder is day{}.".format(str(max_date).zfill(2)))

  new_dates = range(max_date+1, today+1)

  for d in new_dates:
    if v:
      print("Preparing day {}.".format(d))

    new_dir = "day" + str(d).zfill(2)
    os.mkdir(new_dir)

    if v:
      print("\tCreated folder {}.".format(new_dir))
      print("\tDownloading input file for day {}.".format(d))
    

    with open(os.path.join(new_dir,"input.txt"), "wb") as input_file:
      input_file.write(download_input(d, 2018))
    
    if v:
      print("Day {} complete.".format(d))
elif month != 12:
  print("It's not December! Advent of Code starts December 1st.")
elif today == max_date:
  print("Today's folder already created.")
else:
  print("I missed something.")
