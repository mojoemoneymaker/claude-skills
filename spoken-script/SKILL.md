---
name: spoken-script
description: The spoken-word layer, how a line sounds when Joe Rivera says it. Use for Reel and Short scripts read to camera, teleprompter reads, wedding MC announcements and mic work, discovery-call and sales talk tracks, mentorship-call or workshop teaching, talks, narration, and whenever Joe says "make this sound natural when I say it", "read aloud", "talk track", "what do I say", "on the mic", "delivery", "stagecraft", "vocal", "pause". Carries the read-aloud pass, breath and sentence rules, the Sage, Warrior and Lover vocal modes, eyes, gestures, presence, and the rhythm of statement, self-question, answer. Runs LAST, after belief-patterns (structure) and the content skill that owns the format (wdjm-script-writer, process-transcript, produce-long-form). Do NOT use for what is said or how a belief is changed (belief-patterns), for silently read text (joe-copy-standards, copy-law), or for distilling transcripts (belief-patterns Mode B, process-transcript).
---

# spoken-script

The spoken-word layer. `belief-patterns` decides the structure (what the listener must believe
first, how the belief turns, how they are carried point to point). The content skill for the
lane decides the format. This skill decides how it lands in a listener's ear when Joe says it:
sentence length, breath, the vocal mode of each line, where the pause sits, what the hands and
eyes do. It runs last.

New teachers are ingested through `belief-patterns` Mode B, which routes delivery-only lessons
here (`references/delivery.md` and `references/lessons.md`).

## Before writing a word

Read `joe-copy-standards` (global skill, canonical in Dropbox `AI Operating System/skills/`).
It is the base law for every brand and it wins every conflict with anything in this skill. The
two laws that fail spoken scripts most often: no em or en dashes anywhere, and never invent a
story, a stat, a name or a testimonial to make a line land. If a script needs a story and Joe
has not supplied one, leave a bracketed slot and ask.

For DJ MOJOE site copy the project `copy-law` skill stacks on top. For WDJM reels, the 16
Script Writing Standards, the teleprompter format and the current CTA rule live in Notion on the
Knowledge Resources hub (`3882e7ac-085c-8106-8e7e-f3bce80fcefc`) and in `process-transcript`.
Point at them, do not restate them.

## Reference map

| Need | Read |
|---|---|
| The persuasion structure (reframes, two sales, question control, bridges, tie-downs, attention generators, through line, story arc) | `belief-patterns/references/patterns.md`, run first |
| The delivery lessons this skill owns (speak to one person, presence, rhythm, tone) | `references/lessons.md` |
| How a line is delivered: state, breath, vocal modes, gestures, eyes, presence | `references/delivery.md` |
| The mechanical checklist for anything read by a person | `references/read-aloud-pass.md` |
| What changes per kind of spoken moment (reel, MC, sales call, teaching) | `references/scopes.md` |
| How to ingest a new source, and which sources are already done | `belief-patterns/references/sources/README.md` |
| Deterministic checker, run on every deliverable | `scripts/read_aloud_check.py` |

Most requests need `belief-patterns/references/patterns.md` (already applied if the content
skill ran), `scopes.md`, `lessons.md` and the checker. Load `delivery.md` when the request is
about how to say it, or when the moment is live (MC, stage, sales call).

## Write or polish for the spoken word

### 1. Get the four inputs, default what you can, ask only for what cannot default

1. **The text or the brief.** A draft to polish, or a brief to write from.
2. **The scope.** Reel or teleprompter read, MC mic work, sales talk track, teaching or
   narration. Infer it from the request; `scopes.md` says what each one changes.
3. **Who is listening.** One person, named as specifically as the request allows: the solo
   wedding DJ stuck under two thousand dollars, the couple on the call, the room at the grand
   entrance. Default to the audience of the content skill that runs first.
4. **The one thing they must believe or do afterwards.** If the request carries two, ask
   which one, because a spoken piece that installs two beliefs installs neither.

If a content skill applies (a Reel, a WDJM script, a To The Testimony narration), run
`belief-patterns` and then that skill first. Their output is the draft this skill polishes. Do
not re-decide the belief, the order, the proof or the CTA.

### 2. Check the structure is already there

The piece should arrive with its belief, its two-sales order and its bridges in place from
`belief-patterns`. If it did not (a raw brief, a draft from outside), run that skill's Mode A
first. This skill does not restructure; it makes the structure sayable.

### 3. Apply the delivery lessons for this scope

`lessons.md` and `delivery.md`, filtered by `scopes.md`. Speak to one person. Mark where the
vocal mode changes (Sage for setup, Warrior for the turn and the rehook, Lover for the close and
the personal line). Put the self-questions and bridges in Joe's rhythm, not the teacher's.

### 4. Run the read-aloud pass

`references/read-aloud-pass.md`, then the checker:

```
python scripts/read_aloud_check.py <file>
```

The checker is a floor, not a judge. Zero findings and a line that trips the tongue is still
not done. Read it out loud once at speaking pace before delivering.

### 5. Deliver as a draft

Use this exact shape. The spoken text goes in a fenced block tagged `spoken` so the checker
knows which lines are for the mouth.

````
DRAFT, awaiting Joe's approval

**Scope:** [reel / MC / sales talk track / teaching]
**Listener:** [one person]
**They walk away believing or doing:** [one line]

```spoken
the words, exactly as said, nothing else
```

**Delivery notes** (only if they change how a line is said)
- [where to pause, which vocal mode, where the belief turns, what the hands do]

**Checker:** [result line from read_aloud_check.py]
````

No headings, beat labels, stage directions or markdown inside the spoken block. If the content
skill's own output format is required (the wdjm-script-writer Title / Target Belief / Hook /
Meat / CTA block, for instance), deliver that first, then this block as the teleprompter-ready
version.

## Composition rule

`belief-patterns` first, the content skill for the format, this skill last. On any conflict
between a lesson here and a rule in `joe-copy-standards` or a project copy law, the law wins
and the lesson is marked. This skill never introduces a fact, a number, a name or a story that
the content skill or Joe did not supply.

## Quality pass before delivering

- The listener knows in the first line why to keep listening.
- Exactly one thing to believe or do. The listener could repeat it back in one sentence.
- Spoken to one person. No "you all", "everyone", "guys".
- Every sentence says in one breath. Contractions throughout. No punctuation the ear cannot hear.
- The belief turns in the right place for the scope, and trust was earned before the ask.
- Rehook or participation prompt present if the piece runs past roughly thirty five seconds.
- Delivery notes, if any, sit outside the spoken block.
- Every fact, name and story traced to Joe, the content skill, or a bracketed slot.
- Zero em or en dashes, zero banned words, checker run and its result line included.
- Labelled DRAFT.

## Anti-patterns, never ship these

- A pasted reframe template with the blanks filled in. Apply the mechanism, write the line fresh.
- Stage directions inside the spoken block. The teleprompter shows every character.
- Two beliefs in one piece.
- A written-English sentence that would never be said across a table.
- A story, stat or name the sources did not supply.
- Speaking to the room instead of to one person in it.
- Any technique in `belief-patterns/references/refused.md`, however clever it sounds in the source.
