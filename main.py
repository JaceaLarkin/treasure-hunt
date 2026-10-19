
import random
import utilities


def chooseDifficulty():
    """Ask the player to choose a difficulty."""
    print("\nChoose your difficulty:")
    utilities.printNumberedList(["Easy", "Medium", "Hard"])
    return utilities.getValidInt("Enter your choice (1-3): ", 1, 3)


def playRound(roundNumber, totalScore, difficulty):
    """Play one round and return the updated total and round points."""
    locations = ["Dark Cave", "Sandy Beach", "Ancient Ruins"]
    treasurePoints = [10, 20, 30][difficulty - 1]
    trapPoints = [-5, -10, -20][difficulty - 1]

    utilities.clearScreen()
    print("========== TREASURE HUNT ==========")
    print(f"Round {roundNumber} of 5")
    print("\nWhere would you like to dig?")
    utilities.printNumberedList(locations)

    choice = utilities.getValidInt("Enter your choice (1-3): ", 1, 3)
    location = locations[choice - 1]
    print(f"\nYou dig at the {location}...")

    result = random.choice(["treasure", "trap", "nothing"])

    if result == "treasure":
        points = treasurePoints
        message = f"You found treasure! (score +{points})"
    elif result == "trap":
        points = trapPoints
        message = f"It was a trap! (score {points})"
    else:
        points = 0
        message = "You found nothing! (score 0)"

    print(message)
    totalScore += points
    print(f"\nCurrent Total Score: {totalScore}")
    utilities.pause()

    return totalScore, points


def showReport(playerName, roundScores, totalScore):
    """Display round scores, outcome counts, total, and rank."""
    _, treasureCount, trapCount, emptyCount = (
        utilities.analyzeNumbers(roundScores)
    )

    print("\n========== TREASURE REPORT ==========")
    print(f"Explorer: {playerName}")

    for index, points in enumerate(roundScores, start=1):
        print(f"Round {index}: {points:+d}")

    print(f"Treasure Rounds: {treasureCount} | "
          f"Trap Rounds: {trapCount} | Empty Rounds: {emptyCount}")
    print(f"Total Score: {totalScore}")

    if totalScore < 0:
        rank = "Lost Explorer"
    elif totalScore < 20:
        rank = "Beginner Explorer"
    elif totalScore < 50:
        rank = "Treasure Hunter"
    else:
        rank = "Master Treasure Hunter"

    print(f"Rank: {rank}!")


def playGame(playerName):
    """Run five rounds and show the final report."""
    difficulty = chooseDifficulty()
    totalScore = 0
    roundScores = []

    for roundNumber in range(1, 6):
        totalScore, points = playRound(
            roundNumber, totalScore, difficulty
        )
        roundScores.append(points)

    showReport(playerName, roundScores, totalScore)


def main():
    """Run the game and let the player play again."""
    playerName = utilities.getNonEmptyString("Enter your name: ")

    while True:
        playGame(playerName)
        playAgain = utilities.getValidResponse(
            "\nPlay again? (Y/N): ", ["y", "n"]
        )

        if playAgain == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
