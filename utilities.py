from os import system


def getValidInt(prompt, min=0, max=100):
    """ Repeat until a valid integer within the inclusive range is entered; return the integer."""
    while True:
        try:
            number = int(input(prompt))
            if min <= number <= max:
                return number
            else:
                print(f"Enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid input, enter a whole number.")


def getValidResponse(prompt, validResponses):
    """Repeat until an accepted response is entered. Ignore case and surrounding spaces; use a list comprehension to lowercase valid responses. Return lowercase input."""
    validResponses = [response.lower() for response in validResponses]
    while True:
        response = input(prompt).strip().lower()
        if response in validResponses:
            return response
        print("Invalid response, try again")


def getNonEmptyString(prompt):
    """Reject empty or whitespace-only input; return the trimmed string"""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty, try again")


def clearScreen():
    """Clear the Windows console."""
    system("cls")


def pause(message ="press enter enter to continue: "):
    """Show the message and wait for Enter"""
    input(message)


def printNumberedList(items):
    """Print each item with a number starting at 1."""
    if not items:
        print("No items to display")
        return
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


def filterByLength(items, minLength, maxLength):
    """Return strings whose lengths are within the specified range"""
    return [item for item in items if minLength <= len(item) <= maxLength]


def analyzeNumbers(numbers):
    """Return positive numbers and counts of positive, negative, and zero values"""
    positiveNumbers = [number for number in numbers if number > 0]
    positiveCount = len(positiveNumbers)
    negativeCount = len([number for number in numbers if number < 0])
    zeroCount = len([number for number in numbers if number == 0])

    return positiveNumbers, positiveCount, negativeCount, zeroCount



if __name__ == "__main__":
    choice = getValidInt("Enter a number (1-3): ", 1, 3)
    print("You entered:", choice)
    answer = getValidResponse("Play again? (Y/N): ", ["y", "n"])
    print("Your answer:", answer)
    name = getNonEmptyString("Enter your name: ")
    print("Welcome,", name)
    pause()
    print("Continuing the program!")
    printNumberedList(["Dark Cave", "Sandy Beach", "Ancient Ruins"])
    printNumberedList([])   

    words = ["Cat", "Tiger", "Dog", "Elephant"]
    result = filterByLength(words, 3, 5)
    print(result)

    results = analyzeNumbers([10, -5, 0, 20, -3, 0])

    positives, positiveCount, negativeCount, zeroCount = results

    print("Positive numbers:", positives)
    print("Positive count:", positiveCount)
    print("Negative count:", negativeCount)
    print("Zero count:", zeroCount)

    clearScreen()
    print("The screen has been cleared!")
