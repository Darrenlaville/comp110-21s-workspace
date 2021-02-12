"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730322809"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
   """Random Fortune Program"""
   lucky: int = (randint(1, 4))
   if lucky == 1:
    return "The grasshopper looks for better days"
   else:
        if lucky == 2:
            return "The journey of 1000 miles begins with a single step."
        else:
            if lucky == 3:
                return "Just do it."
            else:
                return "Don't text em, nothing good will come from this."




# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
