from pathlib import Path

mostCalories = int(0)
arr = []
p = Path(__file__).with_name("calories.txt")
with p.open("r") as calories:
    lines = calories.readlines()
    index = int(0)

    for line in lines:
        if line.strip() == "":
            index += 1
        else:
            try:
                arr[index]
            except IndexError:
                arr.insert(index, 0)
            arr[index] += int(line)

print("omg")


def sort_array(arr):
    return sorted(arr, reverse=True)


sortedCalories = sort_array(arr)
sumoOfTopThreeCalories = int(0)

i = 0
while i < 3:
    sumoOfTopThreeCalories += sortedCalories[i]
    i += 1
mostCalories = max(arr)

print(mostCalories)
print(sumoOfTopThreeCalories)
