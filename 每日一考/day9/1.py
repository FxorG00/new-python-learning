str="123abc"
with open("error.log","w") as f:
    try:
        num=int(str)
    except ValueError as e:
        f.write(e.__str__())
        print(e)