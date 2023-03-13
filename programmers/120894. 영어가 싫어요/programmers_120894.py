def solution(numbers):
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))
    return int(numbers)


numbers = "onefourzerosixseven"

print(solution(numbers))
