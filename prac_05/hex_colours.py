"""
Hex colours
Estimate: 20 minutes
Actual:   25 minutes
"""
NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Ao": "#0000ff", "Apple Green": "#8db600"}
print(NAME_TO_CODE)

color_name = input("Enter color name: ").title()
while color_name != "":
    if color_name in NAME_TO_CODE:
        print(color_name, "is", NAME_TO_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter short state: ").title()
