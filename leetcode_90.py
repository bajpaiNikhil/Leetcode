n=[1,2,3,4]
start=0
destination=1
current_dis=0
total_dis=0
for i in range(len(n)):
    if start<destination and (i>=start and i<destination):
        current_dis+=n[i]
    if start>destination and(i>=start or i < destination):
        current_dis+=n[i]
    total_dis+=n[i]
print(min(current_dis,(total_dis-current_dis)))