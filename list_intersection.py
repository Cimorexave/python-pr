
def intersect(list_of_names1, list_of_names2):
    # TODO: implement this function                    
    ds = {}
    
    for el in list_of_names1:
        ds[el[0]] = {"first_name": el[1], "last_name": el[2], "points1": el[3]}
    
    for el in list_of_names2:
        if (el[0] in ds):
            ds[el[0]]["points2"] = el[3]
        # else:
        #     ds[el[0]] = {"first_name": el[1], "last_name": el[2], "points2": el[3]}

    final_list = []
    for key,value in ds.items():
        if ("points2" in value):
            mlist = [key, value["first_name"], value["last_name"], value["points1"], value["points2"]]
            final_list.append(mlist)

    # print(final_list[0:10])
    return final_list
    pass


def read_points(csv_file):
    data = []
    with open(csv_file) as fh:
        content = fh.readlines()
        # skip header line
        for i in range(1,len(content)):
            line = content[i].strip()
            items = line.split(";")
            data.append( items )
    return data


data1 = read_points("/home/jovyan/shared/191.125-2025W/assignment1/p1_data.csv")
data2 = read_points("/home/jovyan/shared/191.125-2025W/assignment1/p2_data.csv")

print("first 10 persons in data1")
print(data1[0:10])

print("number of persons on data1: %d" % (len(data1)))
print("number of persons on data2: %d" % (len(data2)))

%time dataj = intersect(data1, data2)
if dataj:
    print("number of persons in data_joined: %d" % (len(dataj)))
    print("first 10 persons in data_joined")
    print(dataj[0:10])

