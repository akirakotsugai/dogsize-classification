import math
import matplotlib.pyplot as plt

#FUNCTION THAT CALCULATES THE DISTANCE BETWEEN TWO DOTS
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#READING DATABASE
bf = open("weight_height_database.txt", "r")
bf2 = bf.readlines()
allDogs = [] #all heights and weights
for line in bf2:

    division = line.strip().split(";")
    weight = division[3]
    height = division[4]
    allDogs.append([weight,height,""]) #the last index is the breed size that is going to vary until the program execution finishes.

#CENTERS TO BE TWEAKED WITH DEFINED INITIAL VALUES (BY GUESSING)
sizes = {    ##index 0 is the weight in kilograms and index 1 is the height in centimeters.
    "mini": {"newCenter" : [3,14], "oldCenter" : [9999,9999], "quantity" : 0},
    "small" : {"newCenter" : [10.5,31.5], "oldCenter" : [9999,9999], "quantity" : 0},
    "medium" : {"newCenter" : [20,42.5], "oldCenter" : [9999,9999], "quantity" : 0},
    "big" : {"newCenter" : [35,59.5], "oldCenter" : [9999,9999], "quantity" : 0},
    "giant" : {"newCenter" : [52.5,79.5], "oldCenter" : [9999,9999], "quantity" : 0}
}


run = True
while(run):  ##THE CENTERS WILL BE RETWEAKED UNTIL THE DISTANCE BETWEEN THE CURRENT CENTER AND THE OLD CENTER IS TOO LITTLE.
    if distance(sizes["mini"]["newCenter"][0], sizes["mini"]["newCenter"][1],sizes["mini"]["oldCenter"][0],sizes["mini"]["oldCenter"][1]) < 0.01:
        if distance(sizes["small"]["newCenter"][0],sizes["small"]["newCenter"][1],sizes["small"]["oldCenter"][0],sizes["small"]["oldCenter"][1]) < 0.01:
            if distance(sizes["medium"]["newCenter"][0],sizes["medium"]["newCenter"][1],sizes["medium"]["oldCenter"][0],sizes["medium"]["oldCenter"][1]) < 0.01:
                if distance(sizes["big"]["newCenter"][0],sizes["big"]["newCenter"][1],sizes["big"]["oldCenter"][0],sizes["big"]["oldCenter"][1]) < 0.01:
                    if distance(sizes["giant"]["newCenter"][0],sizes["giant"]["newCenter"][1],sizes["giant"]["oldCenter"][0],sizes["giant"]["oldCenter"][1]) < 0.01:
                        run = False

    #CURRENT DOG WEIGHTS AND DOG HEIGHTS THAT IS GOING TO BE USED TO PLOT IN THE GRAPH
    weightsMini = []
    heightsMini = []
    weightsSmall = []
    heightsSmall = []
    weightsMedium = []
    heightsMedium = []
    weightsBig = []
    heightsBig = []
    weightsGiant = []
    heightsGiant = []

    #ITERATE OVER ALL DOGS
    #IF THE DISTANCE IS NOT TOO SHORT, ITERATE OVER ALL VALUES TO BE GROUPED, FIND THE CLOSEST CENTER AND ADD TO THIS GROUP.
    for dog in allDogs:
        distances = {}
        for key,value in sizes.items():
            distances[key] = distance(value["newCenter"][0],value["newCenter"][1],float(dog[0]), float(dog[1]))
        closest = min(distances.values())
        for key, value in distances.items():
            if value == closest:
                dog[2] = key

        if dog[2] == "mini":
                weightsMini.append(dog[0])
                heightsMini.append(dog[1])
        elif dog[2] == "small":
                weightsSmall.append(dog[0])
                heightsSmall.append(dog[1])
        elif dog[2] == "medium":
                weightsMedium.append(dog[0])
                heightsMedium.append(dog[1])
        elif dog[2] == "big":
                weightsBig.append(dog[0])
                heightsBig.append(dog[1])
        else:
            weightsGiant.append(dog[0])
            heightsGiant.append(dog[1])

    #AFTER DEFINING EACH ELEMENT'S GROUP, WE NEED TO FIND A NEW CENTER FOR THE GROUP.
    #FOR THAT WE NEED TO TAKE THE AVERAGE AMONG ALL ELEMENTS BELONGING TO A DETERMINED GROUP.
    #SO FIRST WE COUNT HOW MANY ELEMENTS BELONG TO EACH GROUP.
    miniQnt = 0
    smallQnt = 0
    mediumQnt = 0
    bigQnt = 0
    giantQnt = 0

    for dog in allDogs:
        if dog[2] == "mini":
            miniQnt += 1
        elif dog[2] == "small":
            smallQnt += 1
        elif dog[2] == "medium":
            mediumQnt += 1
        elif dog[2] == "big":
            bigQnt += 1
        else:
            giantQnt += 1

    #HERE WE ATTACH THE TOTAL NUMBER OF ELEMENTS FOR EACH GROUP TO ITS RESPECTIVE GROUP
    #THIS ATTRIBUTION IS NOT NECESSARY. WE ONLY DID IT FOR A BETTER VISUALIZATION DURING THE DEVELOPMENT
    #OR IT COULD BE USEFUL IN THE FUTURE.

    sizes["mini"]["quantity"] = miniQnt
    sizes["small"]["quantity"] = smallQnt
    sizes["medium"]["quantity"] = mediumQnt
    sizes["big"]["quantity"] = bigQnt
    sizes["giant"]["quantity"] = giantQnt


    #NOW SE SUM UP ALL WEIGHTS AND HEIGHTS OF EACH GROUP.
    miniSum = [0,0] #indice 0 = peso e indice 1 = altura
    smallSum = [0,0]
    mediumSum = [0,0]
    bigSum = [0,0]
    giantSum = [0,0]

    for dog in allDogs:
        if dog[2] == "mini":
            miniSum[0] += float(dog[0])
            miniSum[1] += float(dog[1])
        elif dog[2] == "small":
            smallSum[0] += float(dog[0])
            smallSum[1] += float(dog[1])
        elif dog[2] == "medium":
            mediumSum[0] += float(dog[0])
            mediumSum[1] += float(dog[1])
        elif dog[2] == "big":
            bigSum[0] += float(dog[0])
            bigSum[1] += float(dog[1])
        else:
            giantSum[0] += float(dog[0])
            giantSum[1] += float(dog[1])

    ##THE GROUP CURRENT CENTER WILL BE THE OLD CENTER BECAUSE THE NEW ONE IS GOING TO BE CALCULATED IN THE NEXT BLOCK
    sizes["mini"]["oldCenter"] = sizes["mini"]["newCenter"]
    sizes["small"]["oldCenter"] = sizes["small"]["newCenter"]
    sizes["medium"]["oldCenter"] = sizes["medium"]["newCenter"]
    sizes["big"]["oldCenter"] = sizes["big"]["newCenter"]
    sizes["giant"]["oldCenter"] = sizes["giant"]["newCenter"]

    ##TAKING THE AVERAGE OF ALL ELEMENTS OF EACH GROUP, IN THE X AND Y POSITION.
    #HERE THERE IS A DIVISION OF THE SUM OF WEIGHTS AND HEIGHTS BY THE NUMBER OF ELEMENTS
    miniNewCenter = [miniSum[0] / sizes["mini"]["quantity"], miniSum[1] / sizes["mini"]["quantity"]]
    smallNewCenter = [smallSum[0] / sizes["small"]["quantity"], smallSum[1] / sizes["small"]["quantity"]]
    mediumNewCenter = [mediumSum[0] / sizes["medium"]["quantity"], mediumSum[1] / sizes["medium"]["quantity"]]
    bigNewCenter = [bigSum[0] / sizes["big"]["quantity"], bigSum[1] / sizes["big"]["quantity"]]
    giantNewCenter = [giantSum[0] / sizes["giant"]["quantity"], giantSum[1] / sizes["giant"]["quantity"]]

    ##THE ATTRIBUTION OF NEW CENTERS TO EACH SIZE.
    sizes["mini"]["newCenter"] = miniNewCenter
    sizes["small"]["newCenter"] = smallNewCenter
    sizes["medium"]["newCenter"] = mediumNewCenter
    sizes["big"]["newCenter"] = bigNewCenter
    sizes["giant"]["newCenter"] = giantNewCenter

    #EACH ITERATION PLOTTING
    print("Central position - mini")
    print("Weight: " + str(sizes["mini"]["newCenter"][0]) + "kg ~ Height: " + str(sizes["mini"]["newCenter"][1]) + "cm\n")
    print("Central position - small")
    print("Weight: " + str(sizes["small"]["newCenter"][0]) + "kg ~ Height: " + str(sizes["small"]["newCenter"][1]) + "cm\n")
    print("Central position - medium")
    print("Weight: " + str(sizes["medium"]["newCenter"][0]) + "kg ~ Height: " + str(sizes["medium"]["newCenter"][1]) + "cm\n")
    print("Central position - big")
    print("Weight:" + str(sizes["big"]["newCenter"][0]) + "kg ~ Height: " + str(sizes["big"]["newCenter"][1]) + "cm\n")
    print("Central position - giant")
    print("Weight: " + str(sizes["giant"]["newCenter"][0]) + "kg ~ Height: " + str(sizes["giant"]["newCenter"][1]) + "cm\n")
    print("\n")
    plt.scatter(weightsMini,heightsMini, label="Mini Size", color="blue", marker=".")
    plt.scatter(weightsSmall,heightsSmall, label="Small Size", color="black", marker=".")
    plt.scatter(weightsMedium,heightsMedium, label="Medium Size", color="green", marker=".")
    plt.scatter(weightsBig,heightsBig, label="Big Size", color="red", marker=".")
    plt.scatter(weightsGiant,heightsGiant, label="Giant Size", color="orange", marker=".")
    plt.axis('off')
    plt.title("DOG GROUPING BY SIZE")
    plt.legend()
    plt.show()

    if run == True:
        input("Type Enter to proceed to the next tweak.")
    else:
        print("Finished.")
