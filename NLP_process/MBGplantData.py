import requests
import csv
from bs4 import BeautifulSoup
from simple_chalk import chalk
import time
import re

with open('MBGPlantDatafinal.csv','w+',newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Plant url','Common name','Common Name - MBG','Botanical name','Type','Family','Native range','Zone','Zone low','Zone high','Height','Height low','Height high','Unit','Spread','Spread low','Spread high','Unit','Bloom Time','Bloom Description','Sun','Water','Maintenance','Suggested Use','Flower','Attracts','Fruit','Leaf','Other','Tolerate','Culture','Noteworthy characteristics','Problems','Garden uses'])

with open('mbg-data.csv','r',newline='') as inputCSV:
  next(inputCSV)
  readCSV = csv.reader(inputCSV, delimiter=',')
  for data in readCSV:
    plant_properties = []
    rowText = []
    commonNameOriginal = data[1]
    CommonNameMBG = ''
    botanical_name = data[2]
    planturl = data[8]
    Type = ''
    Family = ''
    NativeRange = ''
    Zone = ''
    ZoneLow = ''
    ZoneHigh = ''
    Height = ''
    HeightLow = ''
    HeightHigh = ''
    HeightUnit = ''
    Spread = ''
    SpreadLow = ''
    SpreadHigh = ''
    SpreadUnit = ''
    BloomTime = ''
    BloomDescription = ''
    Sun = ''
    Water = ''
    Maintenance = ''
    SuggestedUse = ''
    Flower = ''
    Attracts = ''
    Fruit = ''
    Leaf = ''
    Other = ''
    Tolerate = ''
    Culture = ''
    NoteworthyCharacteristics = ''
    Problems = ''
    GardenUses = ''
    # print(chalk.red.bold(common_name))
    # print(chalk.yellow(botanical_name))
    # print(chalk.green(planturl))
    time.sleep(0.5)
    if planturl == "not found":
      print("not found")
      pass
    else:
      r = requests.get(planturl)
      soup = BeautifulSoup(r.text,'html.parser')
      plant_data = soup.find('div',{'class','column-right'})

    for element in plant_data:
      row = soup.find('div',{'class','row'})
      if(row):
        rowText.append(row.text)
    
    line = rowText[0].splitlines()
    
    for element in line:
      if element:
        cleaned = re.sub(' +', ' ',element)
        # print(cleaned)
        splited = cleaned.split(':')
        # print(chalk.magenta.bold(splited))
        if len(splited) > 1:
          # plant_properties.append(splited[1])
          if(splited[0].strip() == 'Common Name'):
            CommonNameMBG = splited[1]
          if(splited[0].strip() == 'Type'):
            Type = splited[1]
          if(splited[0].strip() == 'Family'):
            Family = splited[1]
          if splited[0].strip() == 'Native Range':
            NativeRange  = splited[1]
          if splited[0].strip() == 'Zone':
            Zone = splited[1]
            zoneSplit = Zone.split('to')
            ZoneLow = zoneSplit[0]
            ZoneHigh = zoneSplit[1]
          if splited[0].strip() == 'Height':
            Height = splited[1]
            heightSplit = Height.split('to')
            HeightLow = heightSplit[0]
            removeFeet = heightSplit[1].split()
            HeightHigh = removeFeet[0]
            HeightUnit = removeFeet[1]
          if splited[0].strip() == 'Spread':
            Spread = splited[1]
            SpreadSplit = Spread.split('to')
            SpreadLow = SpreadSplit[0]
            removeFeet = SpreadSplit[1].split()
            SpreadHigh = removeFeet[0]
            SpreadUnit = removeFeet[1]
          if splited[0].strip() == 'Bloom Time':
            BloomTime  = splited[1]
          if splited[0].strip() == 'Bloom Description':
            BloomDescription  = splited[1]
          if splited[0].strip() == 'Sun':
            Sun = splited[1]
          if splited[0].strip() == 'Water':
            Water = splited[1]
          if splited[0].strip() == 'Maintenance':
            Maintenance = splited[1]
          if splited[0] == 'Suggested Use':
            SuggestedUse  = splited[1]
          if splited[0] == 'Flower':
            Flower = splited[1]
          if splited[0] == 'Attracts':
            Attracts = splited[1]
          if splited[0] == 'Fruit':
            Fruit = splited[1]
          if splited[0] == 'Leaf':
            Leaf = splited[1] 
          if splited[0] == 'Other':
            Other = splited[1]
          if splited[0] == 'Tolerate':
            Tolerate = splited[1]
          

    culture = soup.find(id="MainContentPlaceHolder_CultureRow")
    noteworthy_characters = soup.find(id="MainContentPlaceHolder_NoteworthyRow")
    problems = soup.find(id="MainContentPlaceHolder_ProblemsRow")
    garden_uses = soup.find(id="MainContentPlaceHolder_GardenUsesRow")
    if culture:
      plant_properties.append(culture.text)
      Culture = culture.text
    else:
      Culture = ''

    if noteworthy_characters:
      plant_properties.append(noteworthy_characters.text)
      NoteworthyCharacteristics = noteworthy_characters.text
    else:
      NoteworthyCharacteristics = ''
    
    if problems:
      plant_properties.append(problems.text)
      Problems = problems.text
    else:
      Problems = ''
    
    if garden_uses:      
      plant_properties.append(garden_uses.text)
      GardenUses = garden_uses.text
    else:
      GardenUses = ''
    
    
    # print(chalk.green.bold(plant_properties),'\n')
    # print(len(plant_properties))    
    with open('MBGPlantDatafinal.csv','a',newline='') as outputCSV:
        writer = csv.writer(outputCSV)
        if planturl == "not found":
          writer.writerow([
            planturl,
            commonNameOriginal,
            '0',
            botanical_name,
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            ''
            ])
          print(chalk.green.bold(commonNameOriginal),' saved')
        else:  
          writer.writerow([
            planturl,
            commonNameOriginal,
            CommonNameMBG,
            botanical_name,
            Type,
            Family,
            NativeRange,
            Zone,
            ZoneLow,
            ZoneHigh,
            Height,
            HeightLow,
            HeightHigh,
            HeightUnit,
            Spread,
            SpreadLow,
            SpreadHigh,
            SpreadUnit,
            BloomTime,
            BloomDescription,
            Sun,
            Water,
            Maintenance,
            SuggestedUse,
            Flower,
            Attracts,
            Fruit,
            Leaf,
            Other,
            Tolerate,
            Culture,
            NoteworthyCharacteristics,
            Problems,GardenUses,
            ''
            ])
          print(chalk.green.bold(commonNameOriginal),' saved')
      

