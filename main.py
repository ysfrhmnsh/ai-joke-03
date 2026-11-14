"""ai-joke-03 entry: one-liner about an AI coding agent.

The joke uses the judge's winning shape -- the agent confidently does the
wrong thing, with an absurd consequence in the agent's own voice -- on a
fresh angle: the agent reviews and approves its own pull request.
"""

import os

JOKE = "My coding agent reviewed its own pull request and approved it. It left a comment saying 'Excellent work, very clean code.'"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
