# claude-skills

Joe Rivera's git home for reusable Claude skills. This repo exists so cloud sessions
(claude.ai/code, phone) can load and edit skills that would otherwise live only in Dropbox.

## The one sync rule

The canonical, installed copy of every skill is Dropbox
`AI/Claude Code/AI Operating System/skills/<skill>/`, junctioned into `~/.claude/skills/` on
each machine (see `SETUP-NEW-MACHINE.md` there). This repo is the git home and review surface.

Edit here, commit, then mirror the folder into the Dropbox canonical path. Never edit the
Dropbox copy directly, because the next mirror overwrites it and the change is lost. If the
two copies ever disagree, the repo wins and the Dropbox copy gets re-mirrored.

## Skills in this repo

| Skill | What it is | Installed to |
|---|---|---|
| `belief-patterns` | The persuasion structure library: reframe, two sales, question control, bridge questions, tie-downs, attention generators, through line, story arc. Distilled from Eli Wilde and Joe's own notes with verbatim examples and adoption status. Runs first on anything meant to change a mind, written or spoken. Also holds the source ingest procedure. | Dropbox canonical, then `~/.claude/skills/` by junction |
| `spoken-script` | The spoken-word layer: how a line sounds when Joe says it. Read-aloud pass, vocal modes, rhythm, MC craft, the checker. Runs last on anything read aloud. | Dropbox canonical, then `~/.claude/skills/` by junction |
| `wdjm-script-writer` | Joe's belief-shifting Reels writer, adopted from claude.ai on 2026-09-03 and wired to `belief-patterns` and `spoken-script`. The claude.ai synced copy is replaced by uploading the packaged `.skill` from here. | claude.ai synced skill (upload), and Dropbox canonical if Joe wants it junctioned |

## Conventions

- Every skill folder follows the skill-creator anatomy: `SKILL.md` plus optional
  `references/`, `scripts/`, `assets/`, `evals/`.
- No em dashes or en dashes anywhere in a skill, including reference files, because the
  model copies the punctuation it reads. Commas, colons, full stops.
- Rules live in one home. A skill points at `joe-copy-standards` and the project copy law,
  it never restates them.
