
#!/usr/local/bin/python3

import sys
import csv

item="""
function {function_name}(){{
    {individual_items}
}} """

individual_item="""if (document.getElementById("dropBox{package}").value == "{index}") {{
    document.getElementById("divText{package}").innerHTML = "{price}";
  }}"""

def loopArray(varname, array):
    retVal = "let " + varname + " = ["
    for index in range(len(array) - 1):
        retVal += array[index][1:]  + ", "
    retVal += array[index][1:]  + "];\n"
    return retVal

if(len(sys.argv) > 1):
    filename = sys.argv[1]

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        basic=[]
        standard=[]
        premium=[]
        for row in reader:
            basic.append(row["basic"])
            standard.append(row["standard"])
            premium.append(row["premium"])

        outer_output = loopArray("basic_prices", basic)
        outer_output += loopArray("standard_prices", standard)
        outer_output += loopArray("premium_prices", premium)

        print(outer_output)

