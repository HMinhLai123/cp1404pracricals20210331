"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if 50 <= score < 90:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        elif score < 50:
            print("Bad")


if __name__ == '__main__':
    main()
