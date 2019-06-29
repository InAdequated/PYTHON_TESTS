def find(string, sub):
    found = False
    strnum = 0
    subnum = 0
    while found==False:
        if string[strnum]==sub[subnum]:
            subnum+=1
            b = len(sub)
            a = strnum
            strnum+=1
            subfound = False
            while subfound==False or subnum!=b:
                if string[strnum]==sub[subnum]:
                    strnum+=1
                    subnum+=1

                if subnum>=b-1:
                    found=True
                    subfound=True

            if found==True:
                return a
            if subfound==False:
                strnum=a
                subnum=0

        strnum+=1
