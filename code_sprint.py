import time

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
print("A) while energy > 0: run()")
print("B) if tired: sleep()")
answer2 = input("Your choice (A/B): ").strip().upper()

if answer2 == "A":
    print("✅ Smart! You ran efficiently until your energy ran out.\n")
    score += 1
else:
    print("❌ You stopped running. No energy left.\n")

time.sleep(1)

# Level 3
print("🧠 Level 3: There's a wall AND low energy.")
print("Which code solves both problems?")
print("A) if obstacle == 'wall': jump()\n   while energy > 0: run()")
print("B) run()")
answer3 = input("Your choice (A/B): ").strip().upper()

if answer3 == "A":
    print("✅ Well done! You used the right logic.\n")
    score += 1
else:
    print("❌ You hit the wall and ran out of energy.\n")

time.sleep(1)

# Final Score
print("🎉 You finished Code Sprint!")
print(f"Your final score: {score}/3")

if score == 3:
    print("🏆 Perfect! You think like a real programmer.")
elif score == 2:
    print("👍 Great job! You're on your way.")
else:
    print("💡 No worries — every mistake is a chance to learn.")

print("\nThanks for playing, Lore!")