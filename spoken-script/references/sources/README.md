# Sources

How this skill learns from a new teacher, and the record of what it has already learned from.
Read this whole file before ingesting anything.

## Two homes, one run

Every ingest writes to two places on purpose:

1. **Notion Knowledge Base** (`collection://d5d2ac86-fd33-44b0-9a91-1b24611fd0d2`, in the WDJM
   Knowledge Resources hub). One page per lesson, Source = the teacher (`Eli Wilde` today),
   Status = `New`, Source Link back to the file or page it came from. This is the knowledge
   Joe retrieves from any thread or any AI. Joe's global rule: distilled sources are retrieved
   from Notion, never re-read.
2. **This skill** (`sources/<teacher>-<slug>.md`, then `lessons.md` and `delivery.md`). This is
   the operational rule set the skill applies without needing Notion in context. Each lesson
   in `lessons.md` names its Knowledge Base entry so the two stay linked.

The source file in this folder is the record of the extraction. `lessons.md` is the merged,
deduplicated result. When they disagree, fix `lessons.md`; the source file is history.

## The ingest procedure

1. **Do it once.** Find the source in the registry below. If it is there with status `done`,
   report that and stop. Also search the Knowledge Base for the same Source Link before
   creating anything.
2. **Locate and read.** Sources arrive as a Dropbox path (Joe's convention:
   `/LEARNING/<teacher>/<title>.txt` or `.md`), a Google Doc link, a Notion page, or pasted
   text. Under roughly fifty thousand characters, read directly. Larger, split by section and
   delegate each slice to a subagent that returns extracted lessons in the shape below; then
   confirm full coverage. Never summarise the whole thing; extract.
3. **Extract in the fixed shape.** For each lesson worth keeping:

   ```
   Lesson:      short name, the way a speaker would refer to it
   Rule:        one or two sentences, imperative
   Why:         the mechanism, as the teacher explains it (not your own theory)
   Example:     verbatim from the source when it has one, in quotation marks; otherwise
                "no example in source"
   Scopes:      reel / MC / sales / teaching, whichever apply
   Conflict:    none, or which Joe rule it collides with
   Status:      adopted / adapted (how) / not adopted (why)
   ```

   Twelve to twenty lessons is the target for a full talk or course. The test for keeping one:
   would it change how a script gets written or said? A fact about the teacher's business, a
   motivational aside, or a repeat of something already in `lessons.md` does not make the cut.
   Attribute every lesson to exactly who said it; a transcript with a guest speaker or a
   morning session by someone else gets two attributions, not one.
4. **File in Notion.** Fetch the data source schema first to confirm option names. One page per
   lesson. Name it the way the Knowledge Base already names things ("Framework: ...",
   "Principle: ...", "Tactic: ...", "Script/Language: ..."). Knowledge Type per the shape.
   Category `Mindset/Positioning` for stagecraft and speaking, `Sales` for call craft, `MC` for
   mic work. Offer Relevance `General` unless it is plainly one offer's. Belief Mapped only
   where a Core 6 belief genuinely fits. Page body: the rule, the why, the example, the
   adoption status, and the skill reference (`spoken-script/references/lessons.md`).
5. **Write the source file** here, `<teacher>-<slug>.md`, carrying every extracted lesson in the
   fixed shape plus the Knowledge Base URLs the run created, and a short header: where the
   source lives, when it was ingested, who spoke, and what was deliberately left out.
6. **Merge into `lessons.md` and `delivery.md`.** Dedupe against existing lessons (a lesson that
   is already there gets its source list extended, not a second entry). Keep the six job
   groups. Put refused lessons in section 6 with the reason. Update `scopes.md` only if a
   lesson changes what a scope does.
7. **Leave SKILL.md alone** unless a new lesson category appeared that the reference map and
   Mode A steps do not cover.
8. **Update the registry** below. Then report to Joe: entries created (by type), lessons
   adopted, adapted and refused, coverage (full or partial), and anything needing his call.
   Everything is a draft until he approves.

## Registry

| Source | Where it lives | Ingested | Status | Notes |
|---|---|---|---|---|
| Joe's notes, Presentations that Sell, Day 1 (2024-07-31) | Notion `COURSES / Eli Wilde / Presentations that Sell / Day 1 - July 31, 2024` (`c828d25c-4d67-47b6-8e28-25b4a2015ea6`) | 2026-09-03 | done | `eli-wilde-notes-2024.md` |
| Joe's notes, Eli Wilde live event day one (2024-10-04) | Notion `COURSES / Eli Wilde / October 4, 2024` (`1152e7ac-085c-8035-9d87-c2a526a98075`) | 2026-09-03 | done | Morning session was Taylor Welch; attributed separately. `eli-wilde-notes-2024.md` |
| Joe's notes, day two (2024-10-05) | Notion `COURSES / Eli Wilde / Oct. 5, 2024` (`1162e7ac-085c-80e5-b99c-dc648b3d9872`) | 2026-09-03 | done | Mostly Joe's own purpose work; four levels of teaching and linking phrases extracted. `eli-wilde-notes-2024.md` |
| Speak, Sell, Scale (Nov. 2024) | Notion `COURSES / Eli Wilde / Speak, Sell, Scale - Nov. 2024` | | empty | The page has no content. Nothing to ingest. |
| NLP 3.0 Flashcards | Google Drive `Eli Wilde NLP 3.0/NLP 3.0 Flashcards PDF.pdf` (`1GD3N2x6t4pWz5hw_Eg8cLZgFccbpvbRv`), docx copy alongside | 2026-09-03 | done | 177 sales cards; deck does not name an author. A minority adopted or adapted, the pressure techniques refused. `eli-wilde-notes-2024.md` |
| The Presentation Template Top Speakers Use To Sell Up To 80% Of A Room (PDF) | Google Drive `Eli Wilde Presentation/` as a shortcut (`13PdYoBObFHcN7koxRw_irk0Kuy8HTTDg`) | | blocked | The shortcut's target is not exposed to the Drive tool. Joe can open it locally, or share the real file, and it ingests as a normal source. |
| The Art Of The Hook | Google Drive `ELI WILDE/` as a shortcut (`1OzYepwMAstxxk87eaODYCowTIqho611C`) | | blocked | Same shortcut problem. |
| The Story Selling Structure | Google Drive `ELI WILDE/` as a shortcut (`1NjZtKWXXhfJCPvCGXRcqsm4J-q9_RJE_`) | | blocked | Same shortcut problem. The Story Selling System is named in Joe's notes as one of the two style pillars, so this one is worth unblocking. |
| Eli Wilde, NLP For Sales (8-week video course) | Google Drive folder shared by `thehustlersvaultx@gmail.com` (`1vq4S9RU4YZYMSsNL__fRwNtsrPOK_msC`) | | not ingested | Not Joe's purchase, provenance unclear, and video would need transcription. Joe's decision. |
| Eli Wilde video transcript (the one Joe is sending) | Dropbox `/LEARNING/Eli Wilde/` (pending) | | pending | Pass 2. Will carry the first verbatim Eli Wilde quotes in this skill. |
