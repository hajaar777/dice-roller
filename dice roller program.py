import random
import time
import builtins

# === Force all prints to green ===
def green_print(*args, **kwargs):
    builtins.print("\033[92m", end="")   # green on
    builtins.print(*args, **kwargs)
    builtins.print("\033[0m", end="")   # reset color

print = green_print

# === Dice ASCII Art ===
dice_Art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

# === Main program ===
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

print("\nRolling the dice...")
time.sleep(1)

# Cool rolling animation 🎲
for i in range(5):
    print("\nShaking...")
    for die in range(num_of_dice):
        face = random.randint(1, 6)
        for line in dice_Art[face]:
            print(line)
    time.sleep(0.3)

# Final roll 🎉
dice = [random.randint(1, 6) for _ in range(num_of_dice)]

print("\n✨ Final Result ✨\n")
for die in dice:
    for line in dice_Art[die]:
        print(line)

# Show total
total = sum(dice)
print("\n──────────────")
print(f"Total: {total}")
print("──────────────")
