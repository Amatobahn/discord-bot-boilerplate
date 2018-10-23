import requests


class Command:

    # Converts user-input to 1337 5p34k.
    @classmethod
    def leet_speak(cls, in_string):
        replacement_characters = (('l', '1'), ('e', '3'), ('a', '4'), ('s', '5'), ('t', '7'), ('o', '0'))
        out_string = in_string.lower()
        for old, new in replacement_characters:
            out_string = out_string.replace(old, new)

        return out_string
