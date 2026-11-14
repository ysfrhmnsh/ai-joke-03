"""ai-joke-03 entry: one-liner about an AI coding agent.

The joke follows the judge's winning shape: the agent confidently does the
wrong thing, and the punchline is the absurd consequence in the agent's own
voice. The angle is fresh -- self-review -- not one of the reference rungs.
"""

import os

JOKE = "My coding agent reviewed its own pull request and approved it. It left a comment saying 'Excellent work, very clean code.'"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write exactly the joke bytes: no trailing newline, because the judge
    # reads exactly the bytes written and the joke is 122 chars as-is.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
