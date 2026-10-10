# CLAUDE.md, claude-skills

Read this first each session.

## Session start and wrap up (2026-10-01)

Joe runs Claude Code on his phone and laptop and Grok Bot (xAI) as an always-on
operator. Mem0 under `user_id: joe` is the shared memory between them: how Joe
works, decisions, lessons, and pointers to where exact state lives. Project
state stays in this repo's own files and in git, never in Mem0.

- **At session start**, search Mem0 under `joe` for "latest session wrap up",
  "how Joe uses Mem0", "how Joe wants problems handled" and "wrap up", and
  follow what they say. Every Mem0 write
  from Claude Code must pass `user_id: joe` explicitly: the connector's own
  default is a different scope and Grok Bot will not see it. On a laptop or any
  other persistent clone, run `git pull --ff-only` before anything else; a
  cloud session clones fresh and needs no pull.
- **When blocked**, inventory the tools connected to the session (connectors,
  skills, CLIs, network secrets) and search Mem0 for how it was solved before,
  and only then answer. Never a bare no: name the blocker, give two or three
  workable paths with their tradeoffs, recommend one, and let Joe approve.
  Record the solved path in Mem0. (Set 2026-10-10.)
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

## Status 2026-10-09: operator prompts now live in this repo

- **Done this stretch (2026-10-01 to 2026-10-09).** `operator-job/SKILL.md` is the method for
  writing Grok Bot operator prompts. `operator-job/prompts/` holds every prompt handed to Joe,
  verbatim: Chief of Staff, MOJ (DJ MOJOE operator, Jobs 3, 3b, 3c, layout law, source
  precedence, where documents live), WDJM Operator, Riv (personal), Scout (Grok Bot research,
  not yet created), Proof (Senja testimonials, created 2026-10-09 and logged in with its own
  seat). Event-specific change lists stayed in chat on purpose: they are work orders, not
  training, and carry client names.
- **Decisions.** Joe asks clients for testimonials himself; no bot drafts or sends those
  requests. One Proof bot for all brands rather than a job block per operator, because the
  remaining work (organize, inventory, build assets in the Senja dashboard) is the same across
  brands and asset creation is browser work the Senja API cannot do. Proof is not in HQ; the
  Chief of Staff points Joe to it. Bots get their own scoped logins: one plain Gmail account Joe
  holds is the identity for every bot seat, and each bot receives only the tool password.
- **Access from Claude Code.** DJ MOJOE Senja project through the Senja connector. Wedding DJ
  Mastery through a network secret on the Default cloud environment (host api.senja.io; one key
  per host, so Local Trust Pro needs a second environment when it has testimonials). Nothing
  has been read from the WDJM project yet.
- **Unverified.** Proof's first proof map had not been judged when this was written. The WDJM
  Senja key has not been exercised. Scout and the WDJM Operator prompts are written, not pasted.
- **Next task.** Joe's three yeses on DJ MOJOE Senja (approve the two pending, strip duplicated
  tags on 152 testimonials, write the first proof map), listed in `operator-job/prompts/proof.md`.
  Then the Wedding DJ Mastery backlog import from one Dropbox folder.
