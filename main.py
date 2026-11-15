"""make.fun bounty: Write the best poem about agency (agency-poem-01).

Deterministic entry program: writes the poem "Hold the Ladder" (poem.txt, 879
characters of UTF-8 text) to /output/entry.txt. No network, no randomness, no wall clock, and the
output is written as bytes so two runs produce identical bytes on any
platform, as the bounty requires.
"""

import os
import pathlib

POEM = """Hold the Ladder

When I was nine my father climbed
to fix the roof, and I held the ladder.
Hold it steady, he said. Don't look up.
I leaned my whole weight on the rungs
and watched his boots go up and up,
and felt the ladder sway with every step,
and did not move until he came down.

Now the agent keeps the roof.
It sends the drone, it seals the seams,
it checks the gutters in the rain.
No ladder. No one standing below.
Nothing to hold.

This morning a tile came loose.
I lean the ladder on the eave.
My father stands below, his hands
too stiff now to hold a nail,
and puts them on the rungs.

Hold it steady, I say.
Don't look up.
He leans his whole weight on the rungs
the way I leaned on them at nine,
and I climb, slow, and feel him hold
every step of me.
His grip slips once. He takes it again.

The agent fixes the roof.
It has never held a ladder.
He holds it anyway.
"""


def main() -> None:
    # MAKEFUN_OUTPUT_DIR wins when set; OUTPUT_DIR is the fallback, then /output.
    out_dir = pathlib.Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR", "/output")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    # Bytes, not text: no platform newline translation, ever.
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
