import pickle
f1 = open("matrix_human.html", "r")
list1 = []
for line1 in f1:
        if "style=\"cursor:pointer;\"" in line1:
                tmp = line1.split("par=")[1]
                tmp1 = tmp.split("'")[0]
                tmp2 = tmp.split(">")[1]
                tmp3 = int(tmp2.split("<")[0])
                if tmp3 > 6000:
                        list1.append(tmp1)
list_file = open('par.pickle',"wb")
pickle.dump(list1, list_file)
list_file.close()
