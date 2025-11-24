import shapefile as shp
import matplotlib.pyplot as plt
import pandas as pd
import re

def plot_vienna_map():
    sf = shp.Reader("/home/jovyan/shared/191.125-2025W/assignment1/vienna/BEZIRKSGRENZEOGDPolygon.shp", encoding="latin1")

    plt.figure(dpi=150)

    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y, '-', color = '#aaaaaa')
    
def get_subway_color(subway_line):
    u2col = {
        "U1"  : '#ff0000',
        "U2"  : '#8000ff',
        "U3"  : '#ff8000',
        "U4"  : '#009d00',
        "U6"  : '#A0522D'
    }
    
    col = '#540CF2'  # default
    
    if subway_line in u2col:
        col = u2col[subway_line]
    
    return col
    
    
# HERE: complete the code

def plot_tube_line(csv_file, subway_line):
    # TODO: implement this function

    df = pd.read_csv(csv_file)
    shapes = list(df[df["LBEZEICHNUNG"] == subway_line]["SHAPE"])
    # print(shapes)
    
    for shape in shapes:
        cordinates = []
        match = re.search(r'\((.*?)\)', shape, re.DOTALL)
        cordinates_str = match.group(1).strip()
        cord_pairs = cordinates_str.split(", ")
        for cord_pair in cord_pairs:
            x, y = cord_pair.split(' ')
            x = float(x)
            y = float(y)
            cordinates.append((x,y))
        
        x_cords = [x for x, y in cordinates]
        y_cords = [y for x, y in cordinates]
        print(x,y,get_subway_color(subway_line))
        plt.plot(x_cords,y_cords, '-', color = get_subway_color(subway_line))
            

    pass


plot_vienna_map()

# this is the test code    
csv_file = "/home/jovyan/shared/191.125-2025W/assignment1/OEFFLINIENOGD.csv"
# plot_tube_line(csv_file, "U1")
plot_tube_line(csv_file, "U2")
#plot_tube_line(csv_file, "U3")
#plot_tube_line(csv_file, "U4")
#plot_tube_line(csv_file, "U6")