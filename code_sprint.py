import time

def play_game():
    print("🏃 Welcome to Code Sprint!")
    print("Help your avatar run by choosing the correct Python logic.")
    print("Type the correct answer for each challenge. Ready? Let's go!\n")
    score = 0

    # Level 1
    print("📦 Level 1: There's a wall ahead.")
    print("Which code makes your avatar jump?")
    print("A) if obstacle == 'wall': jump()")
    print("B) run()")
    answer1 = input("Your choice (A/B): ").strip().upper()

    if answer1 == "A":
        print("✅ Correct! You jumped over the wall.\n")
        score += 1
    else:
        print("❌ Oops! You ran into the wall.\n")

    time.sleep(1)

    # Level 2
    print("🔋 Level 2: You only have 3 energy points left.")
    print("Which code keeps you running while you still have energy?")
    print("A) if tired: sleep()")
    print("B) while energy > 0: run()")
    answer2 = input("Your choice (A/B): ").strip().upper()

    if answer2 == "B":
        print("✅ Smart! You ran efficiently until your energy ran out.\n")
        score += 1
    else:
        print("❌ You stopped running. No energy left.\n")

    time.sleep(1)

    # Level 3
    print("🧠 Level 3: There's a wall AND low energy.")
    print("Which code solves both problems?")
    print("A) run()")
    print("B) if obstacle == 'wall': jump()\n   while energy > 0: run()")
    answer3 = input("Your choice (A/B): ").strip().upper()

    if answer3 == "B":
        print("✅ Well done! You used the right logic.\n")
        score += 1
    else:
        print("❌ You hit the wall and ran out of energy.\n")

    time.sleep(1)

    # Level 4
    print("🌉 Level 4: You need to cross a bridge in 5 steps.")
    print("Which code helps you do that?")
    print("A) for step in range(5): walk()")
    print("B) walk() * 5")
    answer4 = input("Your choice (A/B): ").strip().upper()

    if answer4 == "A":
        print("✅ Nice! You crossed the bridge step by step.\n")
        score += 1
    else:
        print("❌ That didn’t work. You fell off the bridge.\n")

    time.sleep(1)

    # Level 5
    print("⚡ Level 5: You want to repeat a sprint sequence.")
    print("Which code is best?")
    print("A) run(); run(); jump(); run(); run(); jump()")
    print("B) def sprint(): run(); run(); jump()\n   sprint()\n   sprint()")
    answer5 = input("Your choice (A/B): ").strip().upper()

    if answer5 == "B":
        print("✅ Efficient! You reused your sprint function.\n")
        score += 1
    else:
        print("❌ That works, but it's not very clean code.\n")

    time.sleep(1)

    # Level 6
    print("🧊 Level 6: You hit an icy patch and need to slide.")
    print("Which code helps you move forward?")
    print("A) if surface == 'ice': slide()")
    print("B) while surface == 'ice': jump()")
    answer6 = input("Your choice (A/B): ").strip().upper()

    if answer6 == "A":
        print("✅ Smooth move! You slid across the ice.\n")
        score += 1
    else:
        print("❌ Jumping on ice? That’s a slippery mistake.\n")

    time.sleep(1)

    # Level 7
    print("🪨 Level 7: There's a boulder blocking the path.")
    print("Which code helps you push it away?")
    print("A) if obstacle == 'boulder': push()")
    print("B) while obstacle == 'boulder': jump()")
    answer7 = input("Your choice (A/B): ").strip().upper()

    if answer7 == "A":
        print("✅ Strong choice! You pushed the boulder aside.\n")
        score += 1
    else:
        print("❌ Jumping won’t help here. The boulder stays put.\n")

    time.sleep(1)

    # Level 8
    print("🌀 Level 8: You're stuck in a loop and need to break out.")
    print("Which code helps you escape?")
    print("A) while stuck: break()")
    print("B) if stuck: continue()")
    answer8 = input("Your choice (A/B): ").strip().upper()

    if answer8 == "A":
        print("✅ You broke the loop and escaped!\n")
        score += 1
    else:
        print("❌ You continued looping forever...\n")

    time.sleep(1)

    # Level 9
    print("🧪 Level 9: You need to test multiple paths.")
    print("Which code lets you try each one?")
    print("A) for path in paths: try(path)")
    print("B) if path == 'safe': try(path)")
    answer9 = input("Your choice (A/B): ").strip().upper()

    if answer9 == "A":
        print("✅ Great! You tested all paths and found the safe one.\n")
        score += 1
    else:
        print("❌ You only tried one path and missed the safe one.\n")

    time.sleep(1)

    # Bonus Round
    print("🎯 BONUS ROUND: Type the correct Python code yourself!")
    print("Challenge: Define a function called 'boost' that prints 'Speed up!' when called.")
    user_code = input("Type your code here (one line): ").strip()

    if user_code.lower().replace(" ", "") == "defboost():print('speedup!')":
        print("✅ Nailed it! You wrote a working function.\n")
        score += 1
    else:
        print("❌ Not quite. The correct code is: def boost(): print('Speed up!')\n")

    time.sleep(1)


    # ... (alle andere levels en bonusronde hier)

    # Final Score
    print("🎉 You finished Code Sprint!")
    print(f"Your final score: {score}/10")

    if score == 10:
        print("🏆 Legendary! You're a Python master.")
    elif score >= 8:
        print("🔥 Excellent! You're coding like a pro.")
    elif score >= 5:
        print("👍 Solid effort! You're learning fast.")
    elif score >= 3:
        print("✨ Keep going! You're building a strong foundation.")
    else:
        print("💡 Every great coder starts somewhere. Keep practicing!")

    print("\nThanks for playing Code Sprint! 🚀")

# Replay loop
while True:
    play_game()
    replay = input("🔄 Play again? (Y/N): ").strip().upper()
    if replay != "Y":
        print("👋 See you next time in Code Sprint!")
        break