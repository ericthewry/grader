#! /usr/bin/env python

from argparse import ArgumentParser

import re
import time
import getpass
import csvParser
import mailer

def main():
     parser = ArgumentParser(description="The command line tool for grading")
     parser.add_argument('command')
     parser.add_argument('--send', action='store_true')
     parser.add_argument('--test', action='store_true')
     parser.add_argument('--refresh', action='store_true')

     args = parser.parse_args()

     if args.command == "init":
          print("initializing grading environment")
          course = input("Please input the course number: ")
          i, j = re.search('[0123456789]+', course).span()
          courseNum = int(course[i:j])
          print("Welcome to the Grading environment for CS%d ..." % courseNum)

     elif args.command == "make-pdfs":
          source = input("Please specify the input directory: ")
          dest   = input("Please specify the output directory: ")

          print("making your pdfs...")
          time.sleep(2)
          print("Done!")
     elif args.command == "emails":
          if args.send:
               emails   = input("Please specify the path to emails.csv: ")
               gradeDir = input("Please specify the directory of the Grade Files:")
               sender   = input("Which email would you like to use? ")
               password = getpass.getpass("What is your password? ")

               print("sending your emails...")
               time.sleep(4)
               print("Done!")
          elif args.test:
               emails   = input("Please specify the path to emails.csv: ")
               gradeDir = input("Please specify the directory of the Grade Files: ")
               labNum   = input("Please specify the lab number: ")

               print("linting grade submissions...")
               print(emails)
               emailDict = csvParser.parseEmails(labNum, emails)
               mailer.checkGrades(gradeDir, emailDict)
          elif args.refresh:
               emails   = input("Please specify the path to emails.csv: ")

               print("refreshing sent emails")
               time.sleep(1)
               print("Done!")
     else:
          print("unrecognized command")



if __name__ == "__main__" : main()