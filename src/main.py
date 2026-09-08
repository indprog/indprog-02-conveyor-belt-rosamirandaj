motors = int(input())
kg_package = int(input())

if kg_package/motors <= 12: 
    print("Yes! The conveyor belt can carry the packages.")
else: 
    print("No. The conveyor belt cannot carry the packages.")
