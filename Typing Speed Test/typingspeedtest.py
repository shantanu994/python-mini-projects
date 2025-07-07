import time
import random

sentences = [
    "Python is a powerful programming language.",
    "Practice makes you a better coder.",
    "Keep your code clean and readable.",
    "Always comment important parts of your code."
]

print("⌨️ Typing Speed Test!")
sentence = random.choice(sentences)
print("\nType this sentence:")
print(sentence)

input("Press Enter when you're ready...")
start = time.time()
typed = input("\nStart typing: ")
end = time.time()

time_taken = end - start
words = len(sentence.split())
wpm = (words / time_taken) * 60

print(f"\n⏱️ Time Taken: {time_taken:.2f} seconds")
print(f"💨 Your Speed: {wpm:.2f} words per minute")

if typed == sentence:
    print("✅ Great! You typed it perfectly.")
else:
    print("⚠️ There were some mistakes. Try again!")

# Save results
with open("typing_scores.txt", "a") as file:
    file.write(f"{wpm:.2f} WPM in {time_taken:.2f} sec\n")
