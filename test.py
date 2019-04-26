





addr1 = "16HC2oNNjmhXgGqf4YYZwSfRK4meVpAGm7"
with open("addr-data.txt", "r") as m:
    add = m.read().split()
    for ad in add:
        continue
    if addr1 in add:
        print("found"+ " " +addr1)
        data = open("Win.txt","a")
        data.write("found " +(addr1)+"\n")
        data.close()
    elif addr1 not in add:
        print("No luck!!!"+"\n")
