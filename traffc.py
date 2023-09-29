eastbound = input("Is eastbond going True or False:")
westbound = input("Is westbound going True or False:")



printfalse = "false"
printtrue = "true"
printstuck = "good job you made traffic get stuck inside the tunnel"

if eastbound == "True" and westbound == "True":
    print(printstuck)
elif eastbound == "True" and westbound == "False": 
    print(printtrue)
elif eastbound == "False" and westbound == "True":
    print(printtrue)
elif eastbound == "False" and westbound == "False":
    print(printtrue)