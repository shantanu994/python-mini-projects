import time
import random

# Typing Speed Test Program
sentences = [
    "Python is a powerful programming language.",
    "Practice makes you a better coder.",
    "Keep your code clean and readable.",
    "Always comment important parts of your code.",
    "Debugging is an essential skill for programmers.",
    "Learning to code opens many opportunities.",
    "Collaboration is key in software development.",
    "Version control helps manage code changes.",
    "Testing your code ensures it works as expected.",
]

# Randomly select a sentence from the list
print("Typing Speed Test!")
sentence = random.choice(sentences)
print("\nType this sentence:")
print(sentence)

# Wait for the user to be ready
input("Press Enter when you're ready...")
start = time.time()
typed = input("\nStart typing: ")
end = time.time()

# Calculate time taken and words per minute
time_taken = end - start
words = len(sentence.split())
wpm = (words / time_taken) * 60 #wpm means words per minute

# Display results
print(f"\n Time Taken: {time_taken:.2f} seconds")
print(f" Your Speed: {wpm:.2f} words per minute")

# Check if the typed sentence matches the original
if typed == sentence:
    print(" Great! You typed it perfectly.")
else:
    print(" There were some mistakes. Try again!")

# Save results
with open("typing_scores.txt", "a") as file:
    file.write(f"{wpm:.2f} WPM in {time_taken:.2f} sec\n")
