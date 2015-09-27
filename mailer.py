import os

def checkGrades(gradeDir,mapping):
     failures = []
     for filename in mapping:
          rubric = "%s/%s.txt" % (gradeDir, filename)
          comments = "%s/%s.pdf" % (gradeDir, filename)
          if not (os.path.isfile(rubric) and os.path.isfile(comments)):
               failures << filename
     printFails(failures)

def printFails(fails):
     if len(fails) == 0:
          print("No failures!")
     else:
          print("Unable to find the following files:")
          for f in fails:
               print("\t" + f)
