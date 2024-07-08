import re

print("A POP DEMAND TWEAK")
pop_need_multiplier = 1.5
# pop_need_multiplier = input("hello, please add multiplier: ")

new_lines = []
with open("TT_price_employ_buy_packages.txt", 'r') as file_pop_needs:
     Lines = file_pop_needs.readlines()
     
     for line in Lines:
        if  "popneed_services" in line and line != "":
            test = re.findall("\\d+",line)
            number = test.pop()
            number = int(number) * pop_need_multiplier
            line = re.sub("\\d+", str(number), line)
        new_lines.append(line)
f= open("TT_1_price_employ_buy_packages.txt","w+")
f.writelines(new_lines)

