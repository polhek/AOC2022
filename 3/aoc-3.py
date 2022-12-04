from pathlib import Path

""" B == BADGE """

p = Path(__file__).with_name("input.txt")
lowerCaseAlphabet: list[str] = list("abcdefghijklmnopqrstuvwxyz")
upperCaseAlphabet: list[str] = list("abcdefghijklmnopqrstuvwxyz".upper())
prioritySum: int = int(0)
badgePrioritySum = int(0)
groupRucksacksList: list[list[str]] = []


def check_upper_case_priority(char: str) -> int:
    return upperCaseAlphabet.index(char) + 1 + 26


def check_lower_case_priority(char: str) -> int:
    return lowerCaseAlphabet.index(char) + 1


def find_badge(groupRucksackList: list[list[str]]) -> list[str]:
    commonCharsList: list[str] = []
    for group in groupRucksacksList:
        firstRucksack = group[0]
        secondRucksack = group[1]
        thirdRuckSack = group[2]
        commonChar = list(
            set(firstRucksack) & set(secondRucksack) & set(thirdRuckSack)
        )[0]
        commonCharsList.append(commonChar)
    return commonCharsList


with p.open("r") as rucksackItems:
    lines = rucksackItems.read().splitlines()
    groupIndex: int = 0

    for index, line in enumerate(lines, 0):
        try:
            groupRucksacksList[groupIndex]
        except IndexError:
            groupRucksacksList.insert(groupIndex, [])

        groupRucksacksList[groupIndex].append(line)
        if (index + 1) % 3 == 0:
            groupIndex += 1
        firstPart, secondPart = line[: len(line) // 2], line[len(line) // 2 :]
        commonChar: str = list(set(firstPart) & set(secondPart))[0]
        isUpperCase: bool = commonChar.isupper()
        if isUpperCase:
            prioritySum += check_upper_case_priority(commonChar)
        else:
            prioritySum += check_lower_case_priority(commonChar)

badgeList = find_badge(groupRucksacksList)

for badge in badgeList:
    isUpperCase: bool = badge.isupper()
    if isUpperCase:
        badgePrioritySum += check_upper_case_priority(badge)
    else:
        badgePrioritySum += check_lower_case_priority(badge)


print(prioritySum)
print(badgePrioritySum)
