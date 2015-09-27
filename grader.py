from argparse import ArgumentParser

import re
import time

def main():
     parser = ArgumentParser("""The command line tool for grading""")
     parser.add_argument('command')
     parser.add_argument('--send')
     parser.add_argument('--test')
     parser.add_argument('--refresh')

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
     elif args.command == "send-emails":
          emails   = input("Please specify the path to emails.csv: ")
          gradeDir = input("Please specify the directory of the Grade Files:")
          print("sending your emails...")
          time.sleep(4)
          print("Done!")
     elif args.command == "test-emails":
          emails   = input("Please specify the path to emails.csv: ")
          gradeDir = input("Please specify the directory of the Grade Files:")
          print("linting grade submissions...")
          time.sleep(4)
          print("Done!")
     elif args.command == "refresh-emails":
          emails   = input("Please specify the path to emails.csv: ")
          print("refreshing sent emails")
          time.sleep(1)
          print("Done!")
     else:
          print("unrecognized command")



if __name__ == "__main__" : main()