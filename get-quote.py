#!/usr/bin/python

## Imports
import random

## Do stuff
def master():
  f = open("quotes.txt") # Open quotes file
  quotes = f.readlines() # Read the lines in variable f
  f.close() # Close the file

  print(quotes[random.randint(0, 13)].replace("\n", "")) # Print random quote, remove newline from end of quote
  print(quotes[random.randint(0, 13)].replace("\n", "")) # Print random quote, remove newline from end of quote

if __name__== "__main__":
  master()
