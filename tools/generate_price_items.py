
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

        outer_output = ""

        output=""
        index = 1
        package = "Basic"
        for price in basic:

            output += individual_item.format(package=package, index=str(index), price=price)
            index += 1

        outer_output += item.format(function_name="changeSelectLevel" + package, individual_items=output)

        output=""
        index = 1
        package = "Standard"
        for price in standard:

            output += individual_item.format(package=package, index=str(index), price=price)
            index += 1

        outer_output += item.format(function_name="changeSelectLevel" + package, individual_items=output)

        output=""
        index = 1
        package = "Premium"
        for price in premium:

            output += individual_item.format(package=package, index=str(index), price=price)
            index += 1

        outer_output += item.format(function_name="changeSelectLevel" + package, individual_items=output)

        print(outer_output)

