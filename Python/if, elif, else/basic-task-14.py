angle_1 = input("Angle 1? ")
angle_2 = input("Angle 2? ")
angle_3 = input("Angle 3? ")

if angle_1 == angle_2 == angle_3:
    print("This triangle is an equilateral.")
elif angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_1 or angle_2 == angle_3 or angle_3 == angle_1 or angle_3 == angle_2:
    print("This triangle is an isoceles.")
elif angle_1 != angle_2 != angle_3:
    print("This triangle is scalene.")