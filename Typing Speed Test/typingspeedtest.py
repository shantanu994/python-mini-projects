import time 
import random

def typing_speed_test(name):
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "In the middle of difficulty lies opportunity.",
        "The only limit to our realization of tomorrow is our doubts of today.",
    ]

    # Randomly select a sentence from the list
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)

    # Wait for the user to be ready
    input("Press Enter when you're ready...")

    # Start the timer and record the input
    while True:
        start = time.time()
        typed = input("\nStart typing: ")
        end = time.time()
        
        # Check if the typed sentence matches the original sentence
        if typed==sentence:
            time_taken = end - start
            words = len(sentence.split())
            wpm = (words / time_taken) * 60

            print(f"\nTime Taken: {time_taken:.2f} seconds")
            print(f"Your Speed: {wpm:.2f} words per minute")

            with open("typing_scores.txt", "a") as file:
                file.write(f"{name}:{wpm:.2f} WPM in {time_taken:.2f} sec\n")

            if wpm < 30:
                print("Typing Speed: Slow (Keep practicing!)")
            elif wpm < 50:
                print("Typing Speed: Average (You can improve!)")
            elif wpm < 70:
                print("Typing Speed: Good (Nice work!)")
            elif wpm < 100:
                print("Typing Speed: Fast (You're a pro!)")
            else:
                print("Typing Speed: World-class! ")
            break
        else:
            print("There were some mistakes. Try again!")
            
# Main loop to run the typing speed test
while True:
    User_name = input("Enter your name: ")
    typing_speed_test(User_name)
    again = input("\nStart the test again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for participating!")   
        break
