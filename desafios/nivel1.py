results = []

for i in range(2000, 3200+1):
    if i % 7 == 0 and i % 5 != 0:
        results.append(i)
    else:
       pass # nenhuma ação é necessária
   
print(results)