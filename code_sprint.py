import time
import ast
import random
import threading
from colorama import Fore, Style, init

init(autoreset=True)

# ==========================
# Utilities & UI helpers
# ==========================

def correct(msg):
    print(Fore.GREEN + "✅ " + msg + Style.RESET_ALL)


def wrong(msg):
    print(Fore.RED + "❌ " + msg + Style.RESET_ALL)


def info(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)


def input_with_timeout(prompt: str, timeout: int = 10):
    """Return input string or None after timeout seconds (cross‑platform)."""
    result = [None]

    def worker():
        try:
            result[0] = input(prompt)
        except EOFError:
            result[0] = None

    t = threading.Thread(target=worker, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive():
        print()  # move to next line after timeout
        return None
    return result[0]


# ==========================
# Theming, Facts, Difficulty
# ==========================
THEMES = [
    {"name": "Jungle", "emoji": {"run": "🏃‍♂️", "wall": "🌴", "ice": "🦎", "boulder": "🗿", "ok": "🍌", "bad": "🐍"}},
    {"name": "Space", "emoji": {"run": "🚀", "wall": "🛰️", "ice": "🧊", "boulder": "🪐", "ok": "✨", "bad": "🕳️"}},
    {"name": "Ice", "emoji": {"run": "⛷️", "wall": "🧊", "ice": "❄️", "boulder": "🧱", "ok": "☃️", "bad": "🌬️"}},
    {"name": "Cave", "emoji": {"run": "🧗", "wall": "🪨", "ice": "💧", "boulder": "🗿", "ok": "🔥", "bad": "🦇"}},
]

FUN_FACTS = [
    "In Python, strings are immutable—operations create new strings.",
    "`range(5)` produces 0..4; use `range(1,6)` for 1..5.",
    "Functions are first‑class: you can pass them as arguments.",
    "`break` exits the nearest loop; `continue` skips to next iteration.",
    "`elif` avoids checking later branches once one matches.",
    "`while True:` with a `break` is common for read‑eval loops.",
]

# Track concepts for recap
CONCEPTS = {
    "conditionals": "if/elif/else",
    "loops": "while & for",
    "functions": "functions & reuse",
    "flow": "break/continue",
    "collections": "lists & iteration",
}

# ==========================
# Level bank (variants by difficulty)
# ==========================
# Each entry: {concept, variants: [ {title, question, options, answer, explain, diff} ]}
LEVEL_BANK = [
    {
        "concept": "conditionals",
        "variants": [
            {
                "title": "📦 Level 1: There's a wall ahead.",
                "question": "Which code makes your avatar jump?",
                "options": {"A": "if obstacle == 'wall': jump()", "B": "run()"},
                "answer": "A",
                "explain": {"A": "You checked for the wall and jumped!", "B": "`run()` ignores the wall, so you crash."},
                "diff": "easy",
            },
            {
                "title": "📦 Level 1b: A wall or a puddle ahead.",
                "question": "Pick the best conditional.",
                "options": {
                    "A": "if obstacle == 'wall' or obstacle == 'puddle': jump()",
                    "B": "if obstacle == 'wall' and obstacle == 'puddle': jump()",
                },
                "answer": "A",
                "explain": {
                    "A": "`or` matches either case, perfect here.",
                    "B": "An obstacle can't be both 'wall' and 'puddle' at once.",
                },
                "diff": "medium",
            },
            {
                "title": "📦 Level 1c: Classify speed.",
                "question": "Which code handles >0, ==0, else correctly?",
                "options": {
                    "A": "if v > 0: print('go')\nelse: print('stop')",
                    "B": "if v > 0: print('go')\nelif v == 0: print('idle')\nelse: print('reverse')",
                },
                "answer": "B",
                "explain": {"A": "No branch for negative.", "B": "`elif` covers all three cases."},
                "diff": "hard",
            },
        ],
    },
    {
        "concept": "loops",
        "variants": [
            {
                "title": "🔋 Level 2: You only have 3 energy points left.",
                "question": "Which code keeps you running while you still have energy?",
                "options": {"A": "if tired: sleep()", "B": "while energy > 0: run()"},
                "answer": "B",
                "explain": {"A": "That's a single check, not a loop.", "B": "`while` continues until condition is false."},
                "diff": "easy",
            },
            {
                "title": "🌉 Level 3: Cross a bridge in 5 steps.",
                "question": "Which code helps you do that?",
                "options": {"A": "for step in range(5): walk()", "B": "walk() * 5"},
                "answer": "A",
                "explain": {"A": "For‑loop repeats action step by step.", "B": "You can't multiply a function call like that."},
                "diff": "easy",
            },
            {
                "title": "🧪 Level 4: Test all paths.",
                "question": "Which code tries each one?",
                "options": {"A": "for path in paths: try(path)", "B": "if path == 'safe': try(path)"},
                "answer": "A",
                "explain": {"A": "Loop iterates over all paths.", "B": "Only checks a single path variable."},
                "diff": "medium",
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
        ],
    },
    {
        "concept": "functions",
        "variants": [
            {
                "title": "⚡ Level 5: Repeat a sprint sequence.",
                "question": "Which code is best?",
                "options": {
                    "A": "run(); run(); jump(); run(); run(); jump()",
                    "B": "def sprint(): run(); run(); jump()\nsprint(); sprint()",
                },
                "answer": "B",
                "explain": {"A": "Works but repeats a lot.", "B": "Functions enable reuse and clarity."},
                "diff": "easy",
            },
            {
                "title": "⚡ Level 5b: Parameterize effort.",
                "question": "What's better style?",
                "options": {
                    "A": "def push(): force = 10; return force",
                    "B": "def push(force=10): return force",
                },
                "answer": "B",
                "explain": {"A": "Hard‑coded constant makes reuse harder.", "B": "Default parameter is flexible and readable."},
                "diff": "medium",
            },
        ],
    },
    {
        "concept": "flow",
        "variants": [
            {
                "title": "🌀 Level 6: You're stuck in a loop.",
                "question": "Which code helps you escape?",
                "options": {"A": "while stuck: break()", "B": "if stuck: continue()"},
                "answer": "A",
                "explain": {"A": "`break` exits the loop immediately.", "B": "`continue` just skips to next iteration."},
                "diff": "easy",
            },
        ],
    },
    {
        "concept": "conditionals",
        "variants": [
            {
                "title": "🪨 Level 7: A boulder blocks the path.",
                "question": "Which code helps you push it away?",
                "options": {"A": "if obstacle == 'boulder': push()", "B": "while obstacle == 'boulder': jump()"},
                "answer": "A",
                "explain": {"A": "Choose the action that matches the situation.", "B": "Jumping won't move the boulder."},
                "diff": "easy",
            },
        ],
    },
    {
    "concept": "flow",
    "variants": [
        {
            "title": "🌀 Level 8: You're stuck in a loop and need to break out.",
            "question": "Which code helps you escape?",
            "options": {
                "A": "while stuck: break()",
                "B": "if stuck: continue()",
            },
            "answer": "A",
            "explain": {
                "A": "Yes! `break` escapes a loop.",
                "B": "`continue` just skips to the next iteration.",
            },
            "diff": "easy",
        },
    ],
},
{
    "concept": "loops",
    "variants": [
        {
            "title": "🧪 Level 9: You need to test multiple paths.",
            "question": "Which code lets you try each one?",
            "options": {
                "A": "for path in paths: try(path)",
                "B": "if path == 'safe': try(path)",
            },
            "answer": "A",
            "explain": {
                "A": "Yes, a loop tries all paths.",
                "B": "That only checks one path.",
            },
            "diff": "medium",
        },
    ],
},
{
    "concept": "conditionals",
    "variants": [
        {
            "title": "🔀 Level 10: Choose between multiple conditions.",
            "question": "Which code correctly handles several cases?",
            "options": {
                "A": "if x > 0: print('positive')\nelse: print('zero')",
                "B": "if x > 0: print('positive')\nelif x == 0: print('zero')\nelse: print('negative')",
            },
            "answer": "B",
            "explain": {
                "A": "That misses the negative case.",
                "B": "Correct! `elif` lets you cover all.",
            },
            "diff": "hard",
        },
    ],
},
]

# Optional Easter‑egg trivia level (randomly inserted)
TRIVIA_LEVELS = [
    {
        "title": "🐍 Trivia: What does PEP stand for?",
        "question": "Choose the correct expansion.",
        "options": {
            "A": "Python Enhancement Proposal",
            "B": "Performance Extension Patch",
        },
        "answer": "A",
        "explain": {"A": "Correct—design proposals for Python.", "B": "Sounds cool, but not it."},
        "concept": "meta",
    },
]

# Challenge‑mode typed questions
CHALLENGE_TYPED = [
    {
        "prompt": "Define a function 'boost' that prints 'Speed up!'",
        "check": lambda tree: (
            any(isinstance(n, ast.FunctionDef) and n.name == 'boost' and
                any(isinstance(b, ast.Expr) and isinstance(b.value, ast.Call) and getattr(getattr(b.value, 'func', None), 'id', '') == 'print'
                    for b in n.body)
                for n in tree.body)
        ),
        "concept": "functions",
        "hint": "Example: def boost(): print('Speed up!')",
    },
    {
        "prompt": "Write a loop that prints numbers 0 to 2 (inclusive).",
        "check": lambda tree: any(
            isinstance(n, ast.For) and getattr(getattr(n.iter, 'func', None), 'id', '') == 'range' and
            len(getattr(n.iter, 'args', [])) == 1 and getattr(getattr(n.iter, 'args', [None])[0], 'n', None) == 3
            for n in ast.walk(tree)
        ),
        "concept": "loops",
        "hint": "Example: for i in range(3): print(i)",
    },
]


# ==========================
# Game core
# ==========================

def banner():
    print(Fore.CYAN + r"""
  ____          _       ____             _       _   
 / ___|___   __| | ___ / ___| _ __  _ __(_)_ __ | |_ 
| |   / _ \ / _` |/ _ \\___ \| '_ \| '__| | '_ \| __|
| |__| (_) | (_| |  __/ ___) | |_) | |  | | | | | |_ 
 \____\___/ \__,_|\___||____/| .__/|_|  |_|_| |_|\__|
                             |_|                      
    """ + Style.RESET_ALL)


def choose_variant(variants, difficulty):
    # prefer matching difficulty, else any
    pool = [v for v in variants if v.get("diff") == difficulty] or variants
    return random.choice(pool)


def show_fact_maybe():
    if random.random() < 0.35:
        info("💡 " + random.choice(FUN_FACTS))


def play_classic(theme, time_limit=10):
    score = 0
    streak = 0
    practiced = set()

    # dynamic difficulty: start easy, then medium/hard if doing well
    difficulties = ["easy", "easy", "medium", "medium", "hard"]
    diff_idx = 0

    # Optionally insert a trivia level
    levels = []
    for bank in LEVEL_BANK:
        levels.append(bank)
    if random.random() < 0.25:  # 25% chance
        levels.insert(random.randrange(1, len(levels)), {"concept": "meta", "variants": TRIVIA_LEVELS})

    for bank in levels:
        difficulty = difficulties[min(diff_idx, len(difficulties) - 1)]
        variant = choose_variant(bank["variants"], difficulty)

        print()
        print(variant["title"])  # titles already have emojis
        print(variant["question"])
        for k, v in variant["options"].items():
            print(f"{k}) {v}")

        ans = input_with_timeout(f"Your choice (A/B) — {time_limit}s: ", time_limit)
        if ans is None:
            wrong("Time's up! No answer given.")
            streak = 0
        else:
            ans = ans.strip().upper()
            if ans == variant["answer"]:
                correct(variant["explain"][ans])
                score += 1
                streak += 1
                # multiplier bonus every 3 correct in a row
                if streak % 3 == 0:
                    info("Streak x3! +1 bonus point")
                    score += 1
                    show_fact_maybe()
                # scale difficulty up on success
                diff_idx += 1
            else:
                wrong(variant["explain"][variant["answer"]])
                streak = 0
        practiced.add(bank["concept"])
        time.sleep(0.6)
        show_fact_maybe()

    return score, practiced


def play_challenge(theme, time_limit=18):
    score = 0
    practiced = set()

    for ch in CHALLENGE_TYPED:
        print()
        print(f"🎯 Challenge: {ch['prompt']}")
        src = input_with_timeout(f"Type code — {time_limit}s: ", time_limit)
        if not src:
            wrong("Time's up or empty input.")
        else:
            try:
                tree = ast.parse(src)
                if ch["check"](tree):
                    correct("Looks good!")
                    score += 2  # challenges are worth more
                else:
                    wrong("Not quite. " + ch["hint"]) 
            except Exception:
                wrong("Invalid Python. " + ch["hint"]) 
        practiced.add(ch["concept"])
        time.sleep(0.6)
        show_fact_maybe()

    return score, practiced


def recap(total_score, practiced_concepts):
    print("\n" + Fore.CYAN + "📘 Recap: What you practiced today" + Style.RESET_ALL)
    for c in practiced_concepts:
        label = CONCEPTS.get(c, c)
        print(" • " + label)
    print(f"\nFinal score: {total_score}")
    if total_score >= 14:
        print(Fore.MAGENTA + "🏆 Legendary! You're a Python master.")
    elif total_score >= 10:
        print("🔥 Excellent! You're coding like a pro.")
    elif total_score >= 6:
        print("👍 Solid effort! You're learning fast.")
    else:
        print("✨ Keep going! Practice makes progress.")


# ==========================
# Main loop
# ==========================

def play_game():
    banner()
    theme = random.choice(THEMES)
    print(f"{theme['emoji']['run']} Welcome to Code Sprint! Theme: {theme['name']}")
    print("Answer within the time limit for streak bonuses.\n")

    # choose mode
    mode = None
    while mode not in {"1", "2"}:
        print("Select mode: 1) Classic (A/B)   2) Challenge (type code)")
        mode = input("Your choice: ").strip()

    total_score = 0
    practiced = set()

    if mode == "1":
        s, p = play_classic(theme)
        total_score += s
        practiced |= p
        # small bonus stage (optional typed) to mix it up
        if random.random() < 0.4:
            info("Bonus mini‑challenge unlocked!")
            s2, p2 = play_challenge(theme, time_limit=14)
            total_score += s2
            practiced |= p2
    else:
        s, p = play_challenge(theme)
        total_score += s
        practiced |= p
        # add a short classic tail so answers vary next time
        info("Classic lightning round!")
        s2, p2 = play_classic(theme)
        total_score += s2
        practiced |= p2

    recap(total_score, practiced)
    print("\nThanks for playing Code Sprint! 🚀")


if __name__ == "__main__":
    while True:
        play_game()
        again = input("\n🔄 Play again? (Y/N): ").strip().upper()
        if again != "Y":
            print("👋 See you next time in Code Sprint!")
            break
