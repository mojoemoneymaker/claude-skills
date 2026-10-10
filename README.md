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
| `learn-this` | Intake for the Learning OS: any external teaching (link, paste, inbox file) becomes a 📚 Sources row, Library rows in the Notion 📖 Learning Library, a raw file in Dropbox, and a Refused Ledger. Calls `belief-patterns` Mode B for the merge when the source teaches persuasion. Built 2026-09-04. | claude.ai synced skill (upload, so it works from the phone), and Dropbox canonical for the Mac |
| `ask-the-library` | Library-first answering: searches the 📖 Learning Library, then the WDJM 📚 Knowledge Base, then general knowledge, and labels the provenance of every claim, including whether Joe has ruled on it. Built 2026-09-04. | claude.ai synced skill (upload), and Dropbox canonical for the Mac |
| `influence-architect` | Joe's influence advisor and speechwriter built on Eli Wilde's NLP for Sales system, generalized to sales, business, leadership, dating, relationships, conflict and repair, and self-talk. Diagnoses the trust leak, then writes the words at three intensities with delivery, pushback and risk. `belief-patterns` stays the home for Joe's own copy. `references/master-prompt.md` is the generated paste-in block for any other AI (build with `scripts/build_master.py`). | claude.ai profile via the packaged `.skill` (syncs to Cowork and Claude Code cloud sessions), and Dropbox canonical if Joe wants it junctioned |
| `playbook-build` | Bartek Marzec's Product Design Playbook, build mode: designs any user-facing moment (screens, flows, copy, empty states, paywalls, loading, permissions) by picking 2 to 4 named plays from the 33 and naming them in the output. Purchased skill, adopted 2026-09-25; house dash sweep applied, content otherwise verbatim. | claude.ai synced skill (upload the folder as a zip), and Dropbox canonical if Joe wants it junctioned |
| `playbook-plan` | Playbook plan mode: turns a product goal or a stuck metric (activation, D7 retention, trial conversion) into a ranked play stack with a measurement plan and a deliberately-not-doing list. Same source and adoption date as above. | Same as `playbook-build` |
| `playbook-review` | Playbook review mode: audits an existing flow, screen, spec or copy against the ten non-negotiables and returns a Before / After / Why table plus a Block or Ship verdict. Same source and adoption date as above. | Same as `playbook-build` |
| `impeccable` | Vendored copy of pbakaus/impeccable 4.3.1, the frontend design and UX skill (shape, audit, polish, harden, live browser iteration). Not edited here: upstream is the source of truth, this repo is the git home so any project can copy it into `.claude/skills/`. | Copied per project into `<repo>/.claude/skills/impeccable/`; currently in djmojoe-site, next in the DJ Prep Pool app |
| `archify` | Third-party, vendored. Turns a system description or a repository into a validated, interactive architecture, workflow, sequence, data-flow, or lifecycle diagram as standalone HTML. Node 18+ required, no `npm install`. | Dropbox canonical, then `~/.claude/skills/` by junction |

The Learning OS itself (rules, entry template, the two databases) lives on the Notion page
🎓 Learning OS (`3d12e7ac-085c-81bd-9f6d-ce51e58e6e8e`). Raw transcripts live in Dropbox
`AI/Claude Code/Learning OS/` (`_inbox/` for new, `sources/<teacher>/raw/` once distilled).

## Conventions

- Every skill folder follows the skill-creator anatomy: `SKILL.md` plus optional
  `references/`, `scripts/`, `assets/`, `evals/`.
- No em dashes or en dashes anywhere in a skill, including reference files, because the
  model copies the punctuation it reads. Commas, colons, full stops.
- Rules live in one home. A skill points at `joe-copy-standards` and the project copy law,
  it never restates them.

## Third-party skills

`archify` is vendored from https://github.com/tt-a1i/archify, upstream commit `06dd052`
(v2.17.0-dev.1), staged with upstream's own `scripts/stage-clean-skill.mjs`. The result is
byte-identical to the `archify.zip` upstream publishes, minus tests, lockfile, and dev
dependencies. Do not hand-edit anything under `archify/`. To refresh, clone upstream, run the
staging script into a scratch folder, and replace the whole `archify/` folder.

Two exemptions and one warning:

- The no-dash rule does not apply inside `archify/`. It is upstream text, and editing it would
  break the byte-match that makes refreshes safe. The skill produces diagrams, not copy.
- The skill-creator anatomy rule does not apply either. Upstream ships `bin/`, `renderers/`,
  `schemas/`, `examples/`, and `delta/` alongside the usual folders.
- After the first diagram, the skill runs `scripts/check-update.mjs`, which does one GET to
  `tt-a1i.github.io` roughly every 72 hours to see if a newer version exists. It never
  downloads or installs anything. Set `ARCHIFY_UPDATE_CHECK_DISABLED=1` to turn it off.
