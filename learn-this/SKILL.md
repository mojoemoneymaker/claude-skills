---
name: learn-this
description: Intake for Joe Rivera's Learning OS. Turns any external teaching (a YouTube link, a podcast transcript, course notes, a book chapter, a pasted transcript, or a file in the Dropbox inbox) into credited rows in the Notion 📖 Learning Library, with a 📚 Sources ledger row, the raw text filed in Dropbox, and a Refused Ledger for anything that collides with a Joe law. Use whenever Joe says "learn this", "add this to my library", "distill this", "process this transcript" for a source that is NOT his own mentorship call or course, or drops a file in `Learning OS/_inbox/`. Runs the belief-patterns Mode B merge when the source teaches persuasion. Not for Joe's own calls and courses (process-transcript) and not for answering questions from the library (ask-the-library).
---

# learn-this

One source in, one Sources row plus twelve to thirty Library rows out, the raw text filed where
any session can find it. Distill once; after that the library is retrieved, never the transcript.

## Where things live

| Thing | Where | ID |
|---|---|---|
| Rules and the entry template | Notion page 🎓 Learning OS | `3d12e7ac-085c-81bd-9f6d-ce51e58e6e8e` |
| Ledger, one row per source | Notion 📚 Sources | `collection://1e4c73a8-dddb-45a3-9835-87e3270f652d` |
| Concepts, one row per idea | Notion 📖 Learning Library | `collection://1e250f21-7a1e-43ce-8d9d-6e520f883940` |
| Joe's own calls and courses (not this skill) | Notion 📚 Knowledge Base | `collection://d5d2ac86-fd33-44b0-9a91-1b24611fd0d2` |
| Raw transcripts waiting | Dropbox `/AI/Claude Code/Learning OS/_inbox/` (paid: `_inbox/private/`) | |
| Raw transcripts filed | Dropbox `/AI/Claude Code/Learning OS/sources/<teacher-key>/raw/` | |

The rules on the 🎓 page win over anything here. Read its "How this library works" section once per
session before filing. `joe-copy-standards` and the project copy law win over both.

## Before anything else

1. **Identify the source.** Teacher, title, medium, URL, date if known, and whether it is paid
   course material (Private). If the teacher is new, add the option to the Teacher select on
   📚 Sources before creating the row.
2. **Do it once.** Query 📚 Sources for the URL (or the title when there is no URL). If a row
   exists with Distill Status `Distilled`, say so, link it, and stop. Also search the 📚 Knowledge
   Base for the same link, because sources ingested before 2026-09-04 were filed there.
3. **Get the text.**
   - A paste: use it. Save it to `_inbox/` first (header below), so the raw survives the session.
   - A file in `_inbox/`: read it with the Dropbox connector.
   - A link only: try to fetch a transcript. If it cannot be fetched, ask Joe for the paste; he has
     a transcript process. Never summarise from a video description.
   - Over roughly fifty thousand characters: split by section and delegate each slice to a
     subagent that returns entries in the shape below. Confirm full coverage and record
     `Partial (truncated)` on the Sources row if any slice failed.

Raw file name and header (also in `_inbox/README.md`):

```
<YYYY-MM-DD>-<teacher-key>-<slug>.md

teacher: Eli Wilde
title: Linguistic frames, the language of influence
url: https://www.youtube.com/watch?v=CHFcyWPjvnM
date: 2026-09-03
medium: YouTube
private: no
```

Then a blank line, then the transcript. Keep timestamps as `[hh:mm:ss]`; strip link markup.

## Distill

Extract discrete, reusable knowledge: a framework, a line of language, an objection response, a
principle, a story or proof, a drill. Not a summary, not a transcript. Twelve to thirty entries
for a full talk or course; fewer for a short clip. The test for keeping one: would it change what
Joe does, says, writes, or believes? A fact about the teacher's business or a motivational aside
does not make the cut.

One entry per row, with these properties:

- **Name**: `<Knowledge Type>: <specific claim>`, the way the Knowledge Base already names
  things.
- **Source**: the Sources row (relation). Teacher and Private roll up from it.
- **Domain**: from the list on the data source. Add a new option only when nothing fits.
- **Knowledge Type**: Framework, Script/Language, Objection Handling, Story/Example, Data/Proof,
  Tactic, Principle, Drill, Refused Ledger.
- **Scopes**: where it may be used. Self, Mentorship room, Talks/Stage, Reels/Content, Consults
  with couples, Copy, Curriculum, Vendor relations.
- **Claude Proposal**: Adopt, Restrict, Partial, Refuse. The reason goes in body heading 6.
- **Joe's Ruling**: always `Unruled` on creation. Never set it yourself.
- **Belief Mapped**: only where a WDJM Core 6 belief genuinely fits.
- **WDJM KB Link**: when the entry extends a row already in the Knowledge Base.
- **Status**: `New`.

Body, with these headings in this order, every time:

1. What it is (paraphrase, two to four sentences)
2. How it works, as taught (the mechanism the teacher gives, not your theory; Joe's use case)
3. Verbatim (timestamped quotes; inside this private library more than one is fine)
4. Where it applies / where it does not
5. Guard (which Joe law it collides with, and what is kept)
6. Claude proposal and why
7. Drill (one practice prompt when the entry is a skill; omit otherwise)
8. Attribution (`Teacher, Show/Course, "Title" (YYYY-MM-DD), link`, then "Verbatim with
   timestamps" or "Paraphrase")

End every body with `🔷 Claude (AI-managed) · 👤 Joe (input & approval)`.

**One Refused Ledger row per source**, always, even when it is short: every technique the source
teaches that collides with a Joe law (joe-copy-standards, the FTC rule, no fake scarcity, rule 9
on planting doubt), with the timestamp and the reason. This is how a later thread avoids
re-adopting pressure by accident. Never invent a refusal to look thorough; if nothing collides,
the row says so.

## File

1. Fetch both data sources first to confirm property names and option values.
2. Create the 📚 Sources row: Name `<Teacher>: <title> (<date>)`, Teacher, Medium, URL, Source
   Date, Private, Distill Status `Distilled`, Distilled On today, Raw Location (the final path
   under `sources/<teacher-key>/raw/`), Notes (speaker identity confidence, coverage, anything
   odd).
3. Create the Library rows in batches of about fifteen, `allow_async` false, relation to the
   Sources row.
4. Move the raw file from `_inbox/` to `sources/<teacher-key>/raw/` (create the folders if
   missing). Private files stay under a folder that carries `.no-sync`.
5. **If the source teaches persuasion or delivery**, run `belief-patterns` Mode B for the merge
   step only: add the source to `belief-patterns/references/sources/README.md` (registry row
   pointing at the Sources row), write the short source record there, merge structural lessons
   into `patterns.md`, refusals into `refused.md`, delivery lessons into
   `spoken-script/references/`. The Library is the knowledge home; the skills are the
   operational rule set. Each pattern names its Library row.

## Report

Tell Joe, in this order: the Sources row link; entries created, grouped by Knowledge Type, with
the Claude Proposal split (adopt / restrict / partial / refuse); coverage (full or partial); what
was refused and why in one line each; anything that needs his ruling first; and one honest note on
the teacher's approach. Everything is a draft until Joe rules.

## Never

- Re-distill a source that is already Distilled.
- Set Joe's Ruling.
- Present a teacher's view as Joe's.
- Put a Private source's material into content, a product, a shared chatbot, or an export.
- Invent a quote, a number, a name, or a refusal.
- Use an em dash or an en dash.
- Mention Viktor on anything new.
