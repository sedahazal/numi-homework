for i in range(1,100):
    if i > 1:
        for h in range(2,i):
            if(i%h)==0 :
                break
        else:
           print(i)