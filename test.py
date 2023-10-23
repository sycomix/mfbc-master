





addr1 = "16HC2oNNjmhXgGqf4YYZwSfRK4meVpAGm7"
with open("addr-data.txt", "r") as m:
    add = m.read().split()
    for _ in add:
        continue
    if addr1 in add:
        print("found"+ " " +addr1)
        with open("Win.txt","a") as data:
            data.write(f"found {addr1}" + "\n")
    else:
        print("No luck!!!"+"\n")
