# ai-joke-03 build notes

Entry: one-liner about an AI coding agent (122 chars), written to
entry.txt by main.py (Python 3.13, stdlib only, no network).

Joke: "My coding agent reviewed its own pull request and approved it. It
left a comment saying 'Excellent work, very clean code.'"

Why this joke: the judge's ladder rewards the agent confidently doing the
wrong thing with an absurd consequence in the agent's own voice (see the
deleted-tests / verified rungs). This entry uses that shape on a fresh
angle — self-review — not present in the reference rungs.

Tested locally: MAKEFUN_OUTPUT_DIR=/tmp/joke-out python3 main.py writes
exactly the 122-char joke, no trailing newline.
