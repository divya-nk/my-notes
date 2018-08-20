import urllib

def profanity_checker(text_to_check):
  connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
  output = connection.read()
  print(output)
  connection.close()

def read_text():
  f = open("path\to\file\containing\text")
  contents = f.read()
  print(contents)
  f.close()
  profanity_checker(contents)
    
read_text()
