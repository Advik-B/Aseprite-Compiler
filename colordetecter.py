import re

RGB_REGEX = re.compile(r"(\d+),\s*(\d+),\s*(\d+)\)")

with open("testclr.py", "r") as f:
    colors = f.read().splitlines()

colors_ = []
for line in colors:
    finding = re.findall(RGB_REGEX, line)
    if len(finding) > 0:
        colors_.append(re.findall(RGB_REGEX, line)[-1])

colors = [
    {"r": int(color[0]), "g": int(color[1]), "b": int(color[2])} for color in colors_
]

for color in colors:
    print(color)

# Generate a css file for the colors.

with open("out.css", "w") as css:
    css.write("/* Generated by testclr.py */\n")
    css.write("body {\n")
    for color in colors:
        css.write("    background-color: rgb({r}, {g}, {b});\n".format(**color))
    css.write("}\n")
