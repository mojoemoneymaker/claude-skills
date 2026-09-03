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
| `spoken-script` | The spoken-word layer: writes and polishes anything Joe says out loud, using the lessons ingested from Eli Wilde and Joe's own craft. Runs last, on top of whichever content skill owns the format. | Dropbox canonical, then `~/.claude/skills/` by junction |
| `archify` | Third-party, vendored. Turns a system description or a repository into a validated, interactive architecture, workflow, sequence, data-flow, or lifecycle diagram as standalone HTML. Node 18+ required, no `npm install`. | Dropbox canonical, then `~/.claude/skills/` by junction |

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
