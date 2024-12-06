a = input()
op = "+"
z = ""
re = 0
for i in a:
    if i == "-" or i == "+":
        re = eval(f"{re}{op}{int(z)}")
        z = ""
        if i == "-":
            op = "-"
    else:
        z += i
re = eval(f"{re}{op}{int(z)}")
print(re)