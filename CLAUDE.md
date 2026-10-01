# CLAUDE.md, claude-skills

Read this first each session.

## Session start and wrap up (2026-10-01)

Joe runs Claude Code on his phone and laptop and Grok Bot (xAI) as an always-on
operator. Mem0 under `user_id: joe` is the shared memory between them: how Joe
works, decisions, lessons, and pointers to where exact state lives. Project
state stays in this repo's own files and in git, never in Mem0.

- **At session start**, search Mem0 under `joe` for "latest session wrap up",
  "how Joe uses Mem0" and "wrap up", and follow what they say. Every Mem0 write
  from Claude Code must pass `user_id: joe` explicitly: the connector's own
  default is a different scope and Grok Bot will not see it. On a laptop or any
  other persistent clone, run `git pull --ff-only` before anything else; a
  cloud session clones fresh and needs no pull.
- **"Wrap up"** means: update this repo's dated status notes (STATE.md if it
  exists, otherwise this file) with what was done, what is unverified and the
  next task; commit and push explicit paths, never `git add -A`; write one Mem0
  entry under `joe` covering what was decided, what changed and where state
  lives; then report what was pushed and what was left out. Nothing goes to
  Dropbox. "Sync to Mem0" alone means only the Mem0 entry.
- **Builder and operator.** Claude Code builds and opens pull requests. Grok Bot
  operates and fires Claude Code routines. Neither merges, publishes or pushes
  live without Joe's word.

## Brand card: claude-skills (2026-10-01)

- **What:** Not a brand. The git home for Joe's reusable Claude skills (belief-patterns, spoken-script, wdjm-script-writer). The one sync rule is in README.md: this repo wins, Dropbox is the mirror.
- **Mem0 drawer:** None. Skills are shared capability, never a bot with its own memory.
- **Operator:** None. Operators read skills from the brand repos that install them.
