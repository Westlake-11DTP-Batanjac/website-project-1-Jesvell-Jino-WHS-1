import re

filename = input("Diary file: ")

with open(filename, "r") as f:
    lines = f.readlines()

python = []
indent = 0

for line in lines:
    stripped = line.strip()

    # ----------------------------
    # Ignore first line
    # ----------------------------
    if stripped.startswith("dear diary"):
        continue

    # ----------------------------
    # Blank line
    # ----------------------------
    if stripped == "":
        python.append("")
        continue

    # ----------------------------
    # Comments
    # ----------------------------
    if stripped.startswith("#"):
        python.append("    " * indent + stripped)
        continue

    # ----------------------------
    # Function
    # marks function - invited; a and b and c
    # ----------------------------
    m = re.match(r"(.+?) function - invited; (.+)", stripped)

    if m:
        name = m.group(1).strip().replace(" ", "_")

        args = [
            x.strip()
            for x in re.split(r"\band\b", m.group(2))
        ]

        python.append(f"def {name}({', '.join(args)}):")
        indent = 1
        continue

    # ----------------------------
    # If statement
    # ----------------------------
    m = re.match(r"if (.+?) is bigger than (.+?) then", stripped)

    if m:
        python.append(
            "    " * indent +
            f"if {m.group(1).strip()} > {m.group(2).strip()}:"
        )
        indent += 1
        continue

    # ----------------------------
    # Input
    # ask the computer 'Question' for name
    # ----------------------------
    m = re.match(r"ask the computer '(.*)' for (.+)", stripped)

    if m:
        python.append(
            "    " * indent +
            f'{m.group(2).strip()} = input("{m.group(1)}")'
        )
        continue

    # ----------------------------
    # Function call
    # tell the computer welcome to marks function: a and b
    # ----------------------------
    m = re.match(
        r"tell the computer welcome to (.+?) function: (.+)",
        stripped,
    )

    if m:
        name = m.group(1).strip().replace(" ", "_")

        args = [
            f'"{x.strip()}"'
            for x in re.split(r"\band\b", m.group(2))
        ]

        python.append(f"{name}({', '.join(args)})")
        indent = 0
        continue

    # ----------------------------
    # Print Addition
    # ----------------------------
    m = re.match(
        r"tell the computer make (.+?) and (.+?) highfive",
        stripped,
    )

    if m:
        python.append(
            "    " * indent +
            f"print({m.group(1).strip()} + {m.group(2).strip()})"
        )
        continue

    # ----------------------------
    # Print Subtraction
    # ----------------------------
    m = re.match(
        r"tell the computer make (.+?) and (.+?) leave",
        stripped,
    )

    if m:
        python.append(
            "    " * indent +
            f"print({m.group(1).strip()} - {m.group(2).strip()})"
        )
        continue

    # ----------------------------
    # Multiplication
    # ----------------------------
    m = re.match(r"make (.+?) and (.+?) hug", stripped)

    if m:
        python.append(
            "    " * indent +
            f"{m.group(1).strip()} * {m.group(2).strip()}"
        )
        continue

    # ----------------------------
    # Division
    # ----------------------------
    m = re.match(r"make (.+?) and (.+?) share", stripped)

    if m:
        python.append(
            "    " * indent +
            f"{m.group(1).strip()} / {m.group(2).strip()}"
        )
        continue

    # ----------------------------
    # Print
    # ----------------------------
    m = re.match(r"tell the computer (.+)", stripped)

    if m:
        python.append(
            "    " * indent +
            f'print("{m.group(1)}")'
        )
        continue

    # ----------------------------
    # Unknown
    # ----------------------------
    python.append("# UNKNOWN: " + stripped)

outfile = filename + ".py"

with open(outfile, "w") as f:
    f.write("\n".join(python))

print("Compiled successfully!")
print("Output:", outfile)