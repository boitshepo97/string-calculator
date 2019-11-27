import re 

def add(numbers):
    """
    Add numbers passed, some can be in the form of a delimeter string
    """

    if len(numbers) == 0:
        return 0

    nums = re.findall(r"\d+|-\d+", numbers)
    sum = 0
    negatives = []
    for num in nums:
        num = int(num)
        if num < 0:
            negatives.append(num)
        if num <= 1000:
            sum = sum + int(num)
    if len(negatives) > 0:
        message = "negatives not allowed! "
        for i in range(len(negatives)):
            if i != len(negatives)-1:
                message += str(negatives[i]) + ", "
            else:
                message += str(negatives[i]) + "."
        raise Exception(message)

    return sum
  
print(add("//[*][%]\n1*2%3"))