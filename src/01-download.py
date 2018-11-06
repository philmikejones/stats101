#! ~/miniconda3/bin/python3
# Run from project root

# Download data files:
# - Living costs and food survey
# - Sheffield census age
# - Eastbourne census age

import os
import requests
import shutil

# store unprocessed data in ../data/external
os.makedirs("../data/external", exist_ok = True)

# Living costs and food survey
if not os.path.isfile("../data/external.food.zip"):
    food = "https://beta.ukdataservice.ac.uk/Umbraco/Surface/Discover/GetDownload?studyNumber=7932&fileName=7932tab_818dcb297393b2557b07f05acaae70b9.zip"
    food = requests.get(food)
    food = food.content
    outfile = open("../data/external/food.zip", "wb")
    outfile.write(food)

if os.stat("../data/external/food.zip").st_size < 970000:
    raise Exception("Size of food.zip too small. Likely a json error")

# unzip
if not os.path.isdir("../data/external/UKDA-7932-tab/"):
    shutil.unpack_archive(
        "../data/external/food.zip",
        extract_dir = "../data/external/"
    )


# Sheffield census
if not os.path.isfile("../data/external/age_shf.csv"):
  age_shf = "https://www.nomisweb.co.uk/api/v01/dataset/NM_503_1.data.csv?date=latest&geography=1946157123&rural_urban=0&c_age=1...101&measures=20100&signature=NPK-0c73734c0f725c979cee3a:0xa9b892a105be9e9449cdb6c88bdac678e12b229e"
  age_shf = requests.get(age_shf)
  age_shf = age_shf.text
  outfile = open("../data/external/age_shf.csv", "w")
  outfile.write(age_shf)

# Eastbourne census
if not os.path.isfile("../data/external/age_ebn.csv"):
    age_ebn = "https://www.nomisweb.co.uk/api/v01/dataset/NM_1531_1.data.csv?date=latest&geography=1946157295&c_age=1...101&measures=20100&signature=NPK-0c73734c0f725c979cee3a:0x65c03934cecfca562500f65e9cb1bd2083fbea01"
    age_ebn = requests.get(age_ebn)
    age_ebn = age_ebn.text
    outfile = open("../data/external/age_ebn.csv", "w")
    outfile.write(age_ebn)
