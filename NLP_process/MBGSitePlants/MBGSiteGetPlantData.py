import requests
import csv
from bs4 import BeautifulSoup
import time
from simple_chalk import chalk
import csv
import re

# clear the existing file data and add header row
# with open('MBGSitePlantData.csv','w+',newline='') as csvfile:
  # writer = csv.writer(csvfile)
  # writer.writerow(['Plant url MBG','Common Name','Botanical Name','Type','Family','Native range','Zone','Zone low','Zone high','Height','Height low','Height high','Unit','Spread','Spread low','Spread high','Unit','Bloom Time','Bloom Description','Sun','Water','Maintenance','Suggested Use','Flower','Attracts','Fruit','Leaf','Other','Tolerate','Culture','Noteworthy characteristics','Problems','Garden uses','Hummingbirds','Butterflies','Birds','Erosion','Rabbit','Black Walnut','Drought','Clay Soil','Deer','Dry Soil','Shallow-Rocky Soil','Heavy Shade','Wet Soil','Air Pollution',])

with open('MGBSitePlantUrls.csv','r',newline='') as csvfile:
  next(csvfile)
  readCSV = csv.reader(csvfile, delimiter=',')

  for plantUrl in readCSV:
    plantUrl = plantUrl
    commonName = ''
    botanicalName = ''
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
    rowText = []
    
    print(plantUrl[0])
    r = requests.get(plantUrl[0])
    soup = BeautifulSoup(r.text,'html.parser')
    botanicalNameSpan = soup.find(id="dnn_srTitle_lblTitle")
    botanicalName = botanicalNameSpan.text
    print(chalk.cyan.bold(botanicalNameSpan.text))
    plant_data = soup.find('div',{'class','column-right'})

    for elements in plant_data:
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
                commonName = splited[1]
              if(splited[0].strip() == 'Type'):
                Type = splited[1]
              if(splited[0].strip() == 'Family'):
                Family = splited[1]
              if splited[0].strip() == 'Native Range':
                NativeRange  = splited[1]
              if splited[0].strip() == 'Zone':
                Zone = splited[1]
                zoneSplit = Zone.split('to')
                if len(zoneSplit) > 1:
                  ZoneLow = zoneSplit[0]
                  ZoneHigh = zoneSplit[1]
                else:
                  ZoneLow = zoneSplit[0]
                  ZoneHigh = zoneSplit[0]
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
          Culture = culture.text
        else:
          Culture = ''
        
        if noteworthy_characters:
          NoteworthyCharacteristics = noteworthy_characters.text
        else:
          NoteworthyCharacteristics = ''
        
        if problems:
          Problems = problems.text
        else:
          Problems = ''
        
        if garden_uses:
          GardenUses = garden_uses.text
        else:
          GardenUses = ''

    with open('MBGSitePlantData.csv','a') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerow([
        plantUrl[0],
        commonName,
        botanicalName,
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
        Problems,
        GardenUses,
        ''])