# coordinates.py
import math
from collections import Counter

def distance(p1, p2):
    """Calculate the distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def midpoint(p1, p2):
    """Find the midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def coordinate_operations():
    print("\n--- Coordinate System ---")
    try:
        x1, y1 = map(float, input("Enter coordinates of Point A (x y): ").split())
        x2, y2 = map(float, input("Enter coordinates of Point B (x y): ").split())
    except ValueError:
        print("Invalid input! Please enter numeric values separated by space.")
        return

    pointA = (x1, y1)
    pointB = (x2, y2)

    print("\nDistance between A and B:", round(distance(pointA, pointB), 2))
    print("Midpoint between A and B:", midpoint(pointA, pointB))

    points = (pointA, pointB)
    print("\nAll Points Tuple:", points)

    # Demonstrate immutability of tuples
    try:
        pointA[0] = 10
    except TypeError as e:
        print("\nTuples are immutable! Error:", e)

def unique_word_counter():
    print("\n--- Unique Word Counter with Sets ---")
    text = input("Enter a sample text (at least 3 sentences): ").lower()

    # Remove periods and split into words
    words = text.replace(".", "").split()
    unique_words = set(words)

    print("\nTotal words:", len(words))
    print("Unique words:", len(unique_words))
    print("Unique word set:", unique_words)

    # Count word frequency using Counter
    word_count = Counter(words)
    print("\nWord Frequency:", word_count)
    print("Most common word:", word_count.most_common(1)[0])

# === Main Menu ===
while True:
    print("\n=== MAIN MENU ===")
    print("1. Coordinate Operations")
    print("2. Unique Word Counter")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        coordinate_operations()
    elif choice == "2":
        unique_word_counter()
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
