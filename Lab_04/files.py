import sys

with open("common.txt") as passwords:
    for line in passwords:
        try:
            (passwd, variant) = line.split(", ")
            print(f"Password: {passwd}, Variant(s): {variant}")
        except Exception as err:
            print(f"{line=}", file=sys.stderr)
            print("Line does not conform to expected format", file=sys.stderr)
            print(f"Exception({err.__class__.__name__}): {err}", file=sys.stderr)
