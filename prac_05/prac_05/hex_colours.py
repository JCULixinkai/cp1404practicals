
HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

def main():
    colour_name = input("Enter colour name: ").strip()
    while colour_name:
        colour_code = HEX_COLOURS.get(colour_name.capitalize())
        if colour_code:
            print(f"{colour_name} is {colour_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").strip()
    main()

