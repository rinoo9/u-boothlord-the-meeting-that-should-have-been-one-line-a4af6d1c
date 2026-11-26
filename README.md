[![make.fun](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rinoo9/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rinoo9/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

# The Meeting That Should Have Been One Line

A [make.fun](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c) entry: one sentence that could have replaced an entire pointless meeting. No context, no explanation, just the line that kills the meeting.

> Six people, one hour, and a shared calendar invite later, we all agreed to do the thing the email already said to do.

Six people, one hour, one calendar invite — and the meeting's grand decision is to do exactly what the email already said. The meeting exists only to approve the email.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

It writes the line to `/output/entry.txt`. Before writing, `main.py` runs the line through its own gate check (non-blank, one line, at most 200 characters) and refuses to write anything if it fails. Deterministic: the same output every run, well under the 200-character gate.

## License

MIT — see [LICENSE](LICENSE).
