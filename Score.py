import sys
def process_scores(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    return total, average, maximum, minimum


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide scores")
        sys.exit(1)

    try:
        scores = [int(x) for x in sys.argv[1:]]

        total, average, maximum, minimum = process_scores(scores)

        print("Scores:", scores)
        print("Sum:", total)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
