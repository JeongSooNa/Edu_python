import sys

input =  sys.argv[1]

input = input.upper()

output = "hi"

if not input == "HELLO":
  output = "none"

f = open("log.csv","a")

f.write(input + "," + output + "\n")