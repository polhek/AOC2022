from pathlib import Path

p = Path(__file__).with_name("input.txt")

with p.open("r") as file:
    data = file.read().splitlines()

tasks: list[str] = data
fullyOverlappingPairsCount: int = 0
overlappingPairsCount: int = 0


for task in tasks:
    firtElfTask, secondElfTask = task.split(",")
    countDownFirst, countUpFirst = [int(x) for x in firtElfTask.split("-")]
    countDownSecond, countUpSecond = [int(x) for x in secondElfTask.split("-")]
    if (
        countDownFirst <= countDownSecond
        and countUpFirst >= countUpSecond
        or countDownFirst >= countDownSecond
        and countUpFirst <= countUpSecond
    ):
        fullyOverlappingPairsCount += 1
    if set(range(countDownFirst, countUpFirst + 1)) & set(
        range(countDownSecond, countUpSecond + 1)
    ):
        overlappingPairsCount += 1

print("First part answer: " + str(fullyOverlappingPairsCount))
print("Second part answer: " + str(overlappingPairsCount))
print("--------------")
