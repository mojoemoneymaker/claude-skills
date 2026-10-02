---
name: operator-job
description: Writes and revises the instructions for Joe's Grok Bot operators (the Chief of Staff and the per-brand bots such as MOJ for DJ MOJOE and WDJM for Wedding DJ Mastery) and the numbered jobs inside them. Use whenever Joe says "write my operator prompt", "add a job to MOJ", "rewrite Job 3", "create a bot", "what should the bot do", or hands over a task he wants a bot to run on a schedule. Runs an interview first (what, where, when, who, why, how), then produces copy-and-paste boxes, a kickoff message for the HQ thread, and the reasoning separately. Carries Joe's standing laws, the brand wall, and the Grok Bot mechanics so they are never re-explained. Not for Claude Code routines (those are code and live in the brand repos), not for copy that reaches a customer (copy-law and the brand skills own that).
---

# operator-job

One home for how Joe's bots get their instructions. Every operator and every job inside one is
built the same way: interview, then prompt, then kickoff, then a first run judged on the two
sections that matter most. A job written without the interview gets rewritten after the first
run, so the interview is the cheap part.

## The system this skill writes for

- **Grok Bot** (xAI) is the operator. Bots are persistent, each with its own memory and its own
  browser. Several bots share work inside a **group thread**; a bot outside the thread cannot be
  reached. A group holds **at most six bots**. Joe's group is called **HQ**. Joe addresses a bot by
  name with @ when he knows the owner; the Chief of Staff routes when he does not.
- **Mem0** under `user_id: joe` is shared memory between Claude Code and Grok Bot. The shared
  shelf is entries with no `agent_id`. Each brand has a drawer, `agent_id` = djmojoe, wdjm, djiq,
  localtrustpro, hisg, holyprompt, amorfati. The bot roster lives on the shared shelf with
  metadata `kind: bot-roster`; the Chief of Staff reads it every session and updates it in place.
- **The Parasocial Report** is walled off: separate Grok account, separate Mem0 `user_id`
  (parasocial-report), never in HQ, never in the roster, never routed to.
- **Connectors** are granted per account and per bot. Gmail connects read-only; drafts and send
  are separate tool groups. Default for every bot: Drive read, Gmail read, Gmail drafts on, Gmail
  send off. Every bot gets its own scoped logins, never Joe's master logins.
- **Claude Code** builds and opens pull requests. Grok Bot operates. Neither merges, publishes,
  pushes live, sends to a client or spends without Joe's word.

## Laws every prompt carries, verbatim in spirit

1. No em dashes or en dashes anywhere, including inside the prompt.
2. Never invent a fact, number, quote, testimonial, story or source. When a source is silent,
   leave the gap and say so.
3. Draft first, one approval gate. The bot never sends, posts, publishes, changes a record,
   spends, enrols or refunds. Joe does, after reading the draft.
4. Client names and details never enter Mem0. Lessons do, with no names.
5. A bot reads only the shared shelf and its own drawer. Never another brand's drawer.
6. When unsure which brand or which owner, ask Joe one question rather than guess.

## The five-part shape of an operator prompt

1. **Identity and scope.** Which brand, in one paragraph, and the sentence "You never touch any
   other brand."
2. **Truth and memory.** The brain (the brand repo CLAUDE.md and its skills), the verified
   sources for numbers, the Mem0 scope, the data systems and the login rule.
3. **Standing rules and voice.** The laws above plus the brand's voice line and its urgency
   rule.
4. **Numbered jobs.** Each job: when it runs, what it reads, what it produces, in what order,
   where it posts, what it may change, what it must never do.
5. **Decide versus escalate, and close-out.** What the bot decides alone, what goes to Joe, and
   the one Mem0 entry at the end of a day where something was learned.

A new job is a paragraph added under part 4. It is never a new bot unless the data or the voice
is different from everything that bot already does.

## The interview, before any job is written

Ask these in one message, with a default beside each so "all defaults" is a valid answer. Log
the answers to the brand drawer in Mem0 with `kind: process` before writing the prompt, so the
next session does not re-ask.

**What**
- What do you actually check or use? In order. The report follows that order.
- Which parts of the last version did you use and which did you skip?
- What decision does each section help you make? A section with no decision goes.
- Is there a source the bot must not touch? (Joe's client planning app is one.)

**Where**
- Where does the output live: HQ, a brand room, a Gmail draft, a sheet, Notion?
- Where do the inputs live, and are they always there? Name the exception.
- May the bot edit anything? If yes: phase 1 is a change list only, in the shape ADD / CHANGE /
  REMOVE with cell and text; phase 2, after Joe has seen enough good lists, apply after an
  explicit yes.

**When**
- When does the information actually arrive, and when does Joe actually do the work? Schedule
  the run after the information and before the work, not on a tidy weekday.
- When should the follow-up or debrief question come, and what if Joe does not answer?

**Who**
- Who else reads it? Does that person get their own version with less in it?
- Who confirms the facts the bot cannot (pronunciations, final counts)?

**Why**
- Which failure would hurt most? If Joe says they are all equal, keep the order of the "what"
  answers.

**How**
- How does Joe do the judgment part himself, in three sentences, so the bot's picks sound like
  his.
- What is the default when the source is silent (clean versus explicit, formal versus casual)?
- How deep should research go on things that may not matter (flag only, light, deep)?
- Two past lessons Joe would want saved, so the shape of a recipe is in his words.

## Patterns that recur

- **Propose, then apply.** Any write to a document Joe owns is posted first as a change list and
  applied only after yes. Content Joe wrote, or the client wrote, is never changed even after
  yes; the bot adds and highlights.
- **Draft, never send.** Outbound messages are Gmail drafts under the brand address. The bot
  tells Joe the draft exists.
- **Questions, not emails.** When a job surfaces questions for a planner or vendor, the bot lists
  them in the report. Joe says "draft it" if one needs sending.
- **Learn the process.** A scheduled job ends with one question about how Joe does the work that
  the sources did not answer. One question only. Answers go to the brand drawer as `kind:
  process`.
- **Recipes.** After an event, on Joe's word "debrief", the bot asks what happened, what he
  would change, what worked, and writes one Mem0 entry in the brand drawer with `kind: recipe`,
  process only, no names. Recipes are the raw material for a Notion playbook or a Wedding DJ
  Mastery lesson later; the Chief of Staff lists them monthly in HQ and Joe decides.
- **Assistant version.** When someone else works the event, a second short message with only
  what they need and nothing about the client beyond first names.

## Delivery format

1. One box per paste target, labelled with where it goes ("Replace Job 3 in MOJ's
   instructions", "Add under the Chief of Staff's jobs").
2. One kickoff box for HQ that tells the bot to run the job now, treat it as a test, and report
   which source it could not reach and which part of the job was unclear.
3. Reasoning in a separate section, with confidence tags, including what was assumed where Joe
   did not answer.
4. Tell Joe which two sections of the first report to judge it on. If those are right the rest
   can be trimmed; if they are wrong nothing else matters.

## Before handing over, check

- No em dashes or en dashes anywhere in the boxes.
- Every "never" in the laws appears in the prompt or is covered by a connector setting.
- Every source the bot reads is one it has a login for, or the prompt says what to do when it
  cannot reach it.
- The job runs after the information arrives and before Joe does the work.
- Nothing in the prompt stores a client's name or details in Mem0.
- The brand wall holds: the bot reads only its own drawer and the shared shelf.
- The Chief of Staff routing line exists if the job introduces a new trigger word.
- The bot roster entry in Mem0 is updated if a bot was created, renamed or retired.
