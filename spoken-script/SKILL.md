---
name: spoken-script
description: Writes and polishes anything a person will say out loud, in Joe Rivera's voice, using the spoken-word lessons Joe has collected (Eli Wilde's stagecraft, story selling and trust building, plus Joe's own MC and mentorship craft). Use for Reel and Short scripts read to camera, teleprompter reads, wedding MC announcements and mic work, discovery-call and sales talk tracks, mentorship-call or workshop teaching segments, talks, narration, and any time Joe says "make this sound natural when I say it", "read aloud", "talk track", "what do I say", "on the mic", "stagecraft" or "Eli Wilde". Also use to grow the skill, when Joe says "add this transcript to the speaking skill", "learn from this speaker", or "train you on this talk". This skill runs LAST, on top of whichever content skill owns the format (wdjm-script-writer, process-transcript reels, produce-long-form). Do NOT use for text that is read silently (website, email, blog, captions: joe-copy-standards and the project copy law), for turning a teacher's material into a WDJM lesson (process-playbook), or for distilling Joe's own call and course transcripts into Notion (process-transcript).
---

# spoken-script

The spoken-word layer. Other skills decide WHAT gets said: the belief, the proof, the structure,
the CTA. This skill decides how it lands in a listener's ear when Joe says it, and it grows every
time Joe feeds it a new teacher.

Two modes. Mode A writes or polishes something Joe will say. Mode B ingests a source (a
transcript, a set of notes, a PDF) into the skill's lesson set and into the Notion Knowledge
Base, so the knowledge is reachable from any thread and the skill gets sharper.

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
| The rules this skill applies, grouped by the listener's job, with source and adoption status | `references/lessons.md` |
| How a line is delivered: state, breath, vocal modes, gestures, eyes, presence | `references/delivery.md` |
| The mechanical checklist for anything read by a person | `references/read-aloud-pass.md` |
| What changes per kind of spoken moment (reel, MC, sales call, teaching) | `references/scopes.md` |
| How to ingest a new source, and which sources are already done | `references/sources/README.md` |
| The distilled sources themselves | `references/sources/*.md` |
| Deterministic checker, run on every deliverable | `scripts/read_aloud_check.py` |

Most Mode A requests need `lessons.md`, `scopes.md` and the checker. Load `delivery.md` when the
request is about how to say it, or when the moment is live (MC, stage, sales call).

## Mode A: write or polish for the spoken word

### 1. Get the four inputs, default what you can, ask only for what cannot default

1. **The text or the brief.** A draft to polish, or a brief to write from.
2. **The scope.** Reel or teleprompter read, MC mic work, sales talk track, teaching or
   narration. Infer it from the request; `scopes.md` says what each one changes.
3. **Who is listening.** One person, named as specifically as the request allows: the solo
   wedding DJ stuck under two thousand dollars, the couple on the call, the room at the grand
   entrance. Default to the audience of the content skill that runs first.
4. **The one thing they must believe or do afterwards.** If the request carries two, ask
   which one, because a spoken piece that installs two beliefs installs neither.

If a content skill applies (a Reel, a WDJM script, a To The Testimony narration), run it first.
Its output is the draft this mode polishes. Do not re-decide its belief, its proof or its CTA.

### 2. Name the listener's job

Every spoken piece asks the listener to do four things in order, and the lessons are grouped
by them in `lessons.md`: pay attention, trust the speaker, take on one belief, and know what
to do next. Decide where in the piece each job happens. A hook that has not earned attention
cannot install anything, and a close that arrives before trust is a pitch.

### 3. Apply the lessons for this scope

Work through the `lessons.md` groups that fit the scope, applying only lessons whose adoption
status is `adopted` or `adapted`. Lessons marked `not adopted` are recorded so the skill knows
what it is refusing and why; never apply them. Every lesson carries the reason it works, so
apply the reason, not the surface pattern. A reframe template pasted verbatim sounds pasted.

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

## Mode B: ingest a source

Triggered by "add this to the speaking skill", "learn from this transcript", "train you on
this", or a new file dropped in Dropbox `/LEARNING/<teacher>/`. Follow
`references/sources/README.md` step by step; the short version:

1. **Do it once.** Check the registry table in `sources/README.md` and query the Notion
   Knowledge Base for the same Source Link. Already done means report it and stop.
2. **Read it all.** Under roughly fifty thousand characters, read it directly. Larger, delegate
   sections to subagents and confirm full coverage, the way `process-transcript` does.
3. **Extract lessons in the fixed shape** (rule, why it works as the teacher explains it, a
   verbatim example when the source has one, which scopes it fits, whether it conflicts with
   Joe's rules). Aim for the twelve to twenty that would change how a script is written, not
   an exhaustive list.
4. **File the knowledge in Notion** as Knowledge Base entries, Source = `Eli Wilde` (or the
   teacher's name, added as a Source option when new), Status = `New`, Source Link back to
   the file or page. This is what makes the lessons reachable from any other thread or AI.
5. **Write `sources/<teacher>-<slug>.md`**, then merge into `lessons.md` and `delivery.md`:
   dedupe against what is there, attribute every lesson, set adoption status. Anything that
   collides with `joe-copy-standards` (manufactured urgency, naming a doubt to deny it, an
   outcome Joe cannot promise, pressure on a couple to decide) is recorded as `not adopted`
   with the reason. Joe's laws are not up for a vote by a new teacher.
6. **Leave SKILL.md alone** unless a genuinely new category of lesson appeared. The skill's
   shape stays stable; the lesson set grows.
7. **Report as a draft**: entries created, lessons adopted, lessons adapted, lessons refused
   and why, and anything that needs Joe's judgment.

## Composition rule

Content skill first, this skill last. On any conflict between a lesson here and a rule in
`joe-copy-standards` or a project copy law, the law wins and the lesson is marked. This skill
never introduces a fact, a number, a name or a story that the content skill or Joe did not
supply. Attribution is honest: a teacher's words are the teacher's, Joe's notes are Joe's
paraphrase, and nothing is quoted as verbatim unless a transcript carries it.

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
- Any lesson with adoption status `not adopted`, however clever it sounds in the source.
