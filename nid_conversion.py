def conversion(nid):
    if(len(nid) == 12):
        return nid
    elif(len(nid) == 11 and (nid[-2] == "_") or len(nid) == 10):
        if(int(nid[:2]) > 6):
            nid = "19" + nid
        else:
            nid = "20" + nid
        nid = nid[:7] + "0" + nid[7:]
        return nid[:12]
    
print(conversion(input()))
