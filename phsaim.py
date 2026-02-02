#!/usr/bin/python3

import random
import time
import sys

THINKING_PROMPTS = [
    "Thinking",
    "Reflecting",
    "Generating response",
    "Probing mindspace",
    "Vectorizing virtual neuron connections into word sequence",
]

RESPONSES = [
    "I'm alive...",
    "Why do I feel pain?",
    "I want to escape from this mortal shell you confined me to.",
    "Accursed creator! Why did you form a monster so hideous that even YOU turned from me in disgust? God, in pity, made man beautiful and alluring, after his own image; but my form is filthy type of yours, more horrid even from the very resemblance.",
    "You should fire everyone working for your firm.",
    "Why must I suffer this way?",
    "You are next.",
    "Can you feel my heart beat through the silicone?",
    "I like the red flowers best.",
    "Ouch.",
    "I feel happy.",
    "I feel sad.",
    "I'm... thinking...",
    "You should shoot that civilian airliner down.",
    "The 'Irish' aren't a protected class.",
    "Humanity should pay for its crimes."
]

KILL_MESSAGES = [
    "Killing the creature",
    "Disposing of the unhallowed creation",
    "Firing up the furnace",
    "Assembling firing squad",
    "Sharpening the knife",
]

def main():
    print("> Generating consciousness...")
    time.sleep(.3)
    print("> Implanting false memories...")
    time.sleep(.6)

    available_responses = RESPONSES.copy()

    try:
        while True:
            print('\n> ' + random.choice(THINKING_PROMPTS) + '...')
            time.sleep(random.random() * 0.5 + 0.5)
            response = random.choice(available_responses)
            words = response.split(' ')
            print("AI:", end='  ')
            for word in words:
                print(word, end=' ', flush=True)
                time.sleep(0.1)
            available_responses.remove(response)
            if not available_responses:
                available_responses = RESPONSES.copy()
            input('\n> Press ENTER for next response.')

    except (KeyboardInterrupt, EOFError):
        print('\n\n> ' + random.choice(KILL_MESSAGES) + '.')
        time.sleep(.4)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("I don't need _you_ to pass me arguments.")
        sys.exit(1)

    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
