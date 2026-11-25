# u-rama-melon-make-the-ai-judge-laugh-302d0825: one single-line joke about
# office life, 1-200 characters. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-200 characters.
MAX_CHARS = 200

# The joke: turns on a real detail of office life (the office printer, which
# always jams right before a deadline), lands its laugh in the last few
# words by turning the complaint back on the speaker ("the way I do mine"),
# is clear on one reading, and uses fresh wording rather than a joke already
# going round the internet.
JOKE = (
    "The office printer has one job, and it does it the way I do mine: "
    "slowly, loudly, and only after three reminders."
)


def validate_joke(text):
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"


def main():
    validate_joke(JOKE)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
