import csv

def parseEmails(num, emails):
     csvfd = open(emails, 'r')
     dictionary = {}
     with csvfd as emails:
          reader = csv.DictReader(emails)
          for row in reader:
               dictionary[nameToFile(row['Name'], num)] = row['Email']
     return dictionary

def nameToFile(name, num):
     first = getFirst(name)
     last = getLast(name)
     return "Grade_Lab%s%s%s" % (num,last,first)

# Gets the first name of the full-name input
#      str name -- a full name
# return str -- the first name
def getFirst(name):
     brkIdx = name.index(" ")
     return name[:brkIdx]

# Gets the last name of the full-name input
#      str name -- a full name
# return str -- the last name
def getLast(name):
     brkIdx = -name[::-1].index(" ")
     return name[brkIdx:]