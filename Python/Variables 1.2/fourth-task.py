weight = input("Enter your weight. ")
planet = input("Which planet? ")

if planet=="Mercury":
    mercury = int(weight) * 0.4
    print("mercury: ", mercury)

elif planet == "Venus":
    venus = int(weight) * 0.9
    print("Venus: ", venus)

elif planet == "Mars":
    mars = int(weight) * 0.38
    print("Mars: ", mars)

elif planet == "Jupiter":
    jupiter = int(weight) * 2.3
    print("Jupiter: ", jupiter)

elif planet == "Saturn":
    saturn = int(weight) * 1.1
    print("Saturn: ", saturn)

elif planet == "Uranus":
    uranus = int(weight) * 0.92
    print("Uranus: ", uranus)

elif planet == "Neptune":
    neptune = int(weight) * 1.2
    print("Neptune: ", neptune)