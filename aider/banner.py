import random

# ANSI escape codes for yellow and white
colors = [
    "\033[93m",  # Yellow
    "\033[97m",  # White
]
reset = "\033[0m"

# Define block letters for "AIDER Pro"
letters = {
    'A': [
        "   AAAAA   ",
        "  A     A  ",
        " AA     AA ",
        " AAAAAAAAA ",
        " AA     AA ",
        " AA     AA ",
        " AA     AA "
    ],
    'I': [
        " iii ",
        " iii ",
        "     ",
        " III ",
        " III ",
        " III ",
        " III "
    ],
    'D': [
        " DDDDDDD  ",
        " DD    DD ",
        " DD    DD ",
        " DD     D ",
        " DD    DD ",
        " DD    DD ",
        " DDDDDDD  "
    ],
    'E': [
        " EEEEEEEE ",
        " EE       ",
        " EE       ",
        " EEEEEE   ",
        " EE       ",
        " EE       ",
        " EEEEEEEE "
    ],
    'R': [
        " RRRRRRR  ",
        " RR    RR ",
        " RR    RR ",
        " RRRRRRR  ",
        " RR   R   ",
        " RR    RR ",
        " RR     RR"
    ],
    'P': [
        "      PPPPPPP ",
        "      PP    PP",
        "      PP    PP",
        "      PPPPPPP ",
        "      PP      ",
        "      PP      ",
        "      PP      "
    ],
    'r': [
        "        ",
        "        ",
        "rrrrr rr",
        " rr r   ",
        " rr     ",
        " rr     ",
        " rr     "
    ],
    'o': [
        "        ",
        "        ",
        "        ",
        " oooooo ",
        "oo    oo ",
        "oo    oo ",
        " oooooo "
    ],
    ' ': ["", "", "", "", "", "", ""]
}

text = "    AIDER Pro  "
print("\n" * 1)
# Print each row of the banner with first and last 2 rows in yellow
for row in range(7):
    line = ""
    for char in text:
        char = char if char in letters else ' '
        # First 2 and last 2 rows are yellow
        if row in [0, 1, 5, 6]:
            color = "\033[93m"  # Yellow
        else:
            color = random.choice(colors)
        line += color + letters[char][row] + reset + "  "
    print(line)
print("\n" * 1)
