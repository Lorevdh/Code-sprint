import time
import ast
from colorama import Fore, Style, init

init(autoreset=True)

# Utility functions for colored output
def correct(msg):
    print(Fore.GREEN + "✅ " + msg + Style.RESET_ALL)

def wrong(msg):
    print(Fore.RED + "❌ " + msg + Style.RESET_ALL)

def info(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)

# Levels are stored as dicts in fixed order
LEVELS = [
    {
        "title": "📦 Level 1: There's a wall ahead.",
        "question": "Which code makes your avatar jump?",
        "options": {
            "A": "if obstacle == 'wall': jump()",
            "B": "run()"
        },
        "answer": "A",
        "explain": {
            "A": "You checked for the wall and jumped!",
            "B": "`run()` ignores the wall, so you crash."
        }
    },
    {
        "title": "🔋 Level 2: You only have 3 energy points left.",
        "question": "Which code keeps you running while you still have energy?",
        "options": {
            "A": "if tired: sleep()",
            "B": "while energy > 0: run()"
        },
        "answer": "B",
        "explain": {
            "A": "That would just stop when tired, not manage energy.",
            "B": "Good! A while loop continues until energy runs out."
        }
    },
    {
        "title": "🧠 Level 3: There's a wall AND low energy.",
        "question": "Which code solves both problems?",
        "options": {
            "A": "run()",
            "B": "if obstacle == 'wall': jump()\nwhile energy > 0: run()"
        },
        "answer": "B",
        "explain": {
            "A": "Just running ignores both problems.",
            "B": "Correct, you check and loop!"
        }
    },
    {
        "title": "🌉 Level 4: You need to cross a bridge in 5 steps.",
        "question": "Which code helps you do that?",
        "options": {
            "A": "for step in range(5): walk()",
            "B": "walk() * 5"
        },
        "answer": "A",
        "explain": {
            "A": "Nice, a for loop repeats step by step.",
            "B": "Multiplying functions like that doesn’t work."
        }
    },
    {
        "title": "⚡ Level 5: You want to repeat a sprint sequence.",
        "question": "Which code is best?",
        "options": {
            "A": "run(); run(); jump(); run(); run(); jump()",
            "B": "def sprint(): run(); run(); jump()\nsprint()\nsprint()"
        },
        "answer": "B",
        "explain": {
            "A": "That works, but it's repetitive.",
            "B": "Correct, functions let you reuse logic!"
        }
    },
    {
        "title": "🧊 Level 6: You hit an icy patch and need to slide.",
        "question": "Which code helps you move forward?",
        "options": {
            "A": "if surface == 'ice': slide()",
            "B": "while surface == 'ice': jump()"
        },
        "answer": "A",
        "explain": {
            "A": "Correct, check and slide once.",
            "B": "Jumping forever on ice doesn’t help."
        }
    },
    {
        "title": "🪨 Level 7: There's a boulder blocking the path.",
        "question": "Which code helps you push it away?",
        "options": {
            "A": "if obstacle == 'boulder': push()",
            "B": "while obstacle == 'boulder': jump()"
        },
        "answer": "A",
        "explain": {
            "A": "Good! You push the boulder aside.",
            "B": "Jumping won’t move it."
        }
    },
    {
        "title": "🌀 Level 8: You're stuck in a loop and need to break out.",
        "question": "Which code helps you escape?",
        "options": {
            "A": "while stuck: break()",
            "B": "if stuck: continue()"
        },
        "answer": "A",
        "explain": {
            "A": "Yes! `break` escapes a loop.",
            "B": "`continue` keeps you in the loop."
        }
    },
    {
        "title": "🧪 Level 9: You need to test multiple paths.",
        "question": "Which code lets you try each one?",
        "options": {
            "A": "for path in paths: try(path)",
            "B": "if path == 'safe': try(path)"
        },
        "answer": "A",
        "explain": {
            "A": "Yes, a loop tries all paths.",
            "B": "That only checks one path."
        }
    },
    {
        "title": "🔀 Level 10: Choose between multiple conditions.",
        "question": "Which code correctly handles several cases?",
        "options": {
            "A": "if x > 0: print('positive')\nelse: print('zero')",
            "B": "if x > 0: print('positive')\nelif x == 0: print('zero')\nelse: print('negative')"
        },
        "answer": "B",
        "explain": {
            "A": "That misses the negative case.",
            "B": "Correct! `elif` lets you cover all."
        }
    }
]


def play_game():
    print(Fore.CYAN + r"""
  ____          _       ____             _       _   
 / ___|___   __| | ___ / ___| _ __  _ __(_)_ __ | |_ 
| |   / _ \ / _` |/ _ \\___ \| '_ \| '__| | '_ \| __|
| |__| (_) | (_| |  __/ ___) | |_) | |  | | | | | |_ 
 \____\___/ \__,_|\___||____/| .__/|_|  |_|_| |_|\__|
                             |_|                      
    """ + Style.RESET_ALL)

    print("🏃 Welcome to Code Sprint!")
    print("Help your avatar run by choosing the correct Python logic.\n")
    score = 0

    for lvl in LEVELS:
        print(lvl["title"])
        print(lvl["question"])
        for k, v in lvl["options"].items():
            print(f"{k}) {v}")
        answer = input("Your choice (A/B): ").strip().upper()

        if answer == lvl["answer"]:
            correct(lvl["explain"][answer])
            score += 1
        else:
            wrong(lvl["explain"][answer])

        time.sleep(1)
        print()

    # Bonus round
    print("🎯 BONUS ROUND: Type the correct Python code yourself!")
    print("Challenge: Define a function called 'boost' that prints 'Speed up!' when called.")
    user_code = input("Type your code here (can be multi-line): ").strip()

    try:
        tree = ast.parse(user_code)
        func_defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
        if (func_defs and func_defs[0].name == "boost" and
            any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                and isinstance(n.value.func, ast.Name) and n.value.func.id == "print"
                for n in func_defs[0].body)):
            correct("Nailed it! You wrote a working function.")
            score += 1
        else:
            wrong("Not quite. Example: def boost(): print('Speed up!')")
    except Exception:
        wrong("Invalid Python code. Correct: def boost(): print('Speed up!')")

    print("\n🎉 You finished Code Sprint!")
    print(f"Your final score: {score}/{len(LEVELS)+1}")

    if score == len(LEVELS) + 1:
        print(Fore.MAGENTA + "🏆 Legendary! You're a Python master.")
    elif score >= len(LEVELS) - 1:
        print("🔥 Excellent! You're coding like a pro.")
    elif score >= len(LEVELS) // 2:
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
