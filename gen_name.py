#! ./venv/bin/python

import sys
import getopt
import random

MALE_FIRST_NAMES = [
  "Abel",
  "Admassu",
  "Amir",
  "Amsalu",
  "Asmerom",
  "Baslios",
  "Bazin",
  "Belachew",
  "Boru",
  "Bruk",
  "Dawit",
  "Eskinder",
  "Ezana",
  "Fassilidas",
  "Gabreel",
  "Hagos",
  "Kidus",
  "Liben",
  "Melaku",
  "Mirtus",
  "Selemon",
  "Seth",
  "Tariku",
  "Teru",
  "Zufan"
]

FEMALE_FIRST_NAMES = [
  "Adina",
  "Altaye",
  "Amara",
  "Bathsheba",
  "Bethania",
  "Bila",
  "Candace",
  "Chuni",
  "Delilah",
  "Eden",
  "Fana",
  "Hawani",
  "Helina",
  "Lalla",
  "Lia",
  "Lidya",
  "Masresha",
  "Miniya",
  "Muna",
  "Rohama",
  "Semhale",
  "Sitina",
  "Yohanna",
  "Zenna"
]

FAMILY_NAMES = [
  "Abdimelech",
  "Admassu",
  "Basliel",
  "Berhanu",
  "Caleb",
  "Dagmawi",
  "Degu",
  "Dejen",
  "Ebissa",
  "Fikre",
  "Gedeyon",
  "Goliad",
  "Habtamu",
  "Ketema",
  "Kidane",
  "Markos",
  "Mihret",
  "Nazwari",
  "Nebiat",
  "Rada",
  "Sirak",
  "Teshale",
  "Wakeyo",
  "Yideg",
  "Zewedu"
]

HELP_TEXT = """\nGodbound Ancalian Name Generator v1
    -h --help       Show this message
    -m --male       Create a male name
    -f --female     Create a female name
"""

def gen_name(female_name = True):
  if female_name:
    index = random.randint(0, len(FEMALE_FIRST_NAMES) - 1)
    first_name = FEMALE_FIRST_NAMES[index]
  else:
    index = random.randint(0, len(MALE_FIRST_NAMES) - 1)
    first_name = MALE_FIRST_NAMES[index]

  index = random.randint(0, len(FAMILY_NAMES) - 1)
  last_name = FAMILY_NAMES[index]

  return first_name + " " + last_name


def main(argv):
  random.seed()

  try: 
    opts, args = getopt.getopt(argv, "hmf", ["help", "male", "female"])
  except getopt.GetoptError:
    print(HELP_TEXT)
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('-h', '--help'):
      print(HELP_TEXT)
    elif opt in ('-f', '--female'):
      result = gen_name(True)
    elif opt in ('-m', '--male'):
      result = gen_name(False)
    else:
      print("Internal Error - sorry!")
      sys.exit(2)

    print(result)

if __name__ == "__main__":
  main(sys.argv[1:])