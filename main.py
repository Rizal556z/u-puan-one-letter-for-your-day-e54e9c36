"""One Letter for Your Day — make.fun entry.

The letter: "K".

The hidden word behind it: "knackered" — British slang for utterly
exhausted, drained to the last drop. Not tired, not sleepy: knackered
is the day that wrung you out like a dishcloth, the day that ended
with you flat on the sofa, shoes still on, phone face-down, staring
at the ceiling while the kettle boils itself dry. It is vivid (you
can see the collapsed body), funny (the word itself sounds like the
day felt — a tired clunk of a word), and true (everyone has had a
day that knackered them). K is the letter that fits it: the hard
knock at the start of the word, the sound of a day hitting you.

The entry file itself holds exactly this one letter and nothing else:
no word, no gloss, no punctuation. Pure standard library, no
network access, no model calls — the letter is chosen by the author
and written to the competition output file.
"""

import os

LETTER = "K"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
