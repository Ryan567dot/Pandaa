import pandas as sa

data = {
    "name":["Pankaj","Meghna","David","Lisa"]
    ;"id":[1,2,3,4]
    ;"role":["CEO","COO","COO","COO"]
    ;"salary":[4500,3000,3000,2500,3000]
}

mydata = sa.DataFrame(data,index=["worker1","worker2","worker3","worker4"])

print(mydata["id"])
print(mydata["role"])

print(mydata)

print(mydata.sort_values("Math marks"))
print(mydata.info)