---
name: wdjm-script-writer
description: Writes high-retention short-form video scripts (Reels, Shorts, TikTok) for DJ MOJOE, Wedding DJ Mastery, and adjacent expert offers using a belief-shifting framework. Use this skill whenever the user asks to "write a script", "draft a Reel", "make a Short", "create video content", "shift a belief", "do a contrarian reframe", or mentions DJ MOJOE, Wedding DJ Mastery, WDJM, the Accelerator, wedding DJs, MC mastery, or wants short-form video for a coaching/expert offer with calm-authority voice. Also triggers on "mine beliefs from this transcript", "extract belief candidates", or hand-offs of mentorship-call transcripts that need turned into content. Default to this skill any time the user is producing short-form video aimed at booking premium wedding clients or shifting how a specific audience thinks about a problem.
---

# WDJM Adaptive Short-Form Video Script Writer

A belief-shifting short-form scriptwriting system for DJ MOJOE, Wedding DJ Mastery, and other expert offers built on calm-authority mentorship voice.

This skill is not a generic scriptwriter. It writes scripts that **shift a specific belief** in a **specific viewer** toward a **specific next step** — and it does that consistently across one offer or many.

## Core philosophy

Every script does three things, in order:

1. **Pick one belief to shift.** Old belief → new belief. If there is no belief shift, there is no script worth writing.
2. **Earn the shift with one specific proof or story.** Not three. One that lands.
3. **Make the next step feel obvious for the right viewer.** The CTA is a continuation of the lesson, not an ad bolted on.

The script *format* stays stable. What changes per request: offer, audience slice, belief, angle, proof, CTA. Think of this skill as a stable scaffolding with swappable variables — not a template library.

## When to use the reference files

Most requests can be drafted from this SKILL.md alone. Load a reference file only when the situation calls for it:

| Situation | Read this file |
|---|---|
| Need beliefs to write from (no belief given, or want options) | `references/belief-bank.md` |
| Drafting hooks and want strong starting patterns | `references/hook-bank.md` |
| Structuring the body (deciding between story / principles / contrarian / etc.) | `references/story-modes.md` |
| Picking proof, applying voice rules, picking a trust anchor | `references/voice-and-proof.md` |
| User pasted a transcript and wants beliefs mined from it | `references/transcript-mining.md` |

Don't load all of them by default — pull the one the current request actually needs.

## Workflow

### Step 1 — Read the request and decide if you have enough

You need five things to produce a strong script. Check the user's message for them first; only ask for what's actually missing:

**Required:**
1. **Offer** — Accelerator? MC Mastery workshop? Something else? (Default: Wedding DJ Mastery Accelerator if user mentions WDJM / DJ MOJOE without specifying.)
2. **Audience slice** — Who exactly? (Default: the WDJM audience of one below.)
3. **Belief(s)** — What old belief is being challenged? What new belief replaces it? (If missing, see Step 2.)
4. **Script count** — How many scripts? (Default: 1 if not specified.)
5. **CTA destination** — Where should viewers go? (Default: soft invite to the named offer.)

**Default WDJM audience of one** (use unless told otherwise):
> A solo mobile wedding DJ, often part-time, doing 10–20 weddings/year at $1.5k–$2k, overwhelmed by gear-talk and scattered marketing advice, who wants to become an in-demand $4k–$6k DJ without sleazy tactics.

**Rules for asking:**
- If everything required is present or can default sensibly, **don't ask — just write**. Surface defaults inline ("I'm assuming the Accelerator and the default WDJM audience — say so if that's off").
- Ask only for variables that are *both* missing *and* can't default. Most often that's belief and CTA destination.
- If the user pasted a transcript, **also** ask: extract-only, extract+recommend, or extract+write? (See `references/transcript-mining.md`.)
- If "same setup as before", reuse prior turn's variables verbatim.

### Step 2 — Get a belief, in priority order

If the user gave you a belief, use it. If not, work down this list:

1. **User-provided belief** for this request
2. **Transcript-derived belief** if a transcript is in the request → `references/transcript-mining.md`
3. **Bank belief** matched to the audience's likely bottleneck → `references/belief-bank.md`
4. **Inferred contrarian belief** from what Joseph repeatedly teaches — use the contrarian formula (old / why it feels true / what makes it incomplete / new / practical implication)
5. **Only then ask the user** to supply or pick one

Pick the belief that:
- Matches the audience's current bottleneck (don't shift a belief they don't hold)
- Has strong available proof
- Creates a clean reframe (one clear before → after)
- Is shiftable in 120–180 words

**Prefer contrarian when it's sharper and still true.** A contrarian belief says: *the real problem isn't what you think* / *the obvious fix isn't the real fix* / *the leverage point is upstream*. Never invent fake controversy — if it doesn't survive the "is this actually true and useful?" test, drop it.

### Step 3 — Pick a story mode for the body

One mode per script. Match the mode to the belief type — see `references/story-modes.md` for the full set, but the common defaults:

- Belief is "you misdiagnosed your problem" → **Diagnostic** mode
- Belief is "the obvious answer is wrong" → **Contrarian Reframe** mode
- Belief is teachable through Joseph's own arc → **Story** mode (before / mistake / realization / after)
- Belief is "stop doing X, start doing Y" → **Myth Breaker** mode
- Belief is about identity / who they're becoming → **Identity Shift** mode

### Step 4 — Draft to the body architecture

Every script follows this sequence:

1. **Hook** (1–3 sentences) — see hook standards below
2. **Familiar setup** — name the situation the viewer is in
3. **Specific proof, story, or symptom** — one piece, not a list
4. **Reframe** — the belief shift, made plain
5. **Takeaway** — what changes for them now
6. **Soft CTA** — natural next step

Each main beat invisibly carries: *what it is → how it shows up → why it matters.* Don't surface this structure; let it work underneath.

### Step 5 — Hook standards (every hook must pass)

A hook earns the next 5 seconds. Four standards:

1. **Clarity** — viewer knows the subject immediately
2. **Relevance** — the *right* viewer feels called out
3. **Curiosity** — one clear open loop (not three)
4. **Speed to value** — value starts in sentence one, not sentence three

**One subject, one question.** If the hook is trying to do two things, cut one. Use "you" early. Use contrast words generously: *but, actually, instead, turns out, yet, except.* See `references/hook-bank.md` for proven patterns.

### Step 6 — Retention mechanics

- **Rehook rule:** If the script runs past ~35 seconds (roughly 90+ words), add at least one rehook. Examples: *"But here's what most DJs miss." / "Here's the part that gets expensive." / "And this is where most DJs get stuck."*
- **Thought narration:** Name what the viewer is thinking. *"At this point you're probably thinking, okay, so what do I fix first?"*
- **Embedded truths:** Prefer *"when this shifts" / "once you understand this" / "the reason this matters is"* over hedge words. But don't fake certainty — say *"in my experience"* when that's the honest frame.
- **Term branding:** If a recurring idea benefits from a short label (*gear trap, trust leak, consult gap*), invent one. Only when it adds clarity.

### Step 7 — Voice, proof, and the trust anchor

This is non-negotiable — load `references/voice-and-proof.md` before finalizing.

Short version:
- **Voice = calm authority, practical, non-hype, peer-level.** Not guru, not loud, not fake-urgent.
- **Exactly one trust anchor per script.** Don't stack. Pick the one that matches the belief.
- **One main proof type per script** unless the user explicitly requests otherwise.
- **Never use:** *guaranteed, crush it, dominate, game changer, secret sauce, six figures, passive income, only X spots left,* or any fake scarcity / unverified outcome.

### Step 8 — CTA: continuation, not interruption

The CTA should read like the obvious next step *for someone who wants help applying the lesson the script just taught.*

Good patterns:
- *"If you want help building this out in 8 weeks, that's exactly what we do inside [offer]."*
- *"If this hit home, check out [offer] and see if it's a fit."*
- *"If you're tired of figuring this out alone, that's what [offer] is designed for."*
- *"If you want guided reps instead of more trial and error, take a look at [offer]."*

Never: fake scarcity, desperation, over-explaining the offer, "this will change your life."

### Step 9 — Quality pass before delivering

Run this mentally before the script ships. If any check fails, fix it.

- **Belief:** Old belief named? New belief installed? Shift believable?
- **Hook:** Subject clear in sentence 1? Right viewer called out? One question, not three? Moves fast?
- **Body:** One through-line? At least one specific detail/proof point? At least one contrast? Rehook present if script is longer?
- **Voice:** Sounds like Joseph (calm, practical, non-hype)? Natural out loud?
- **Truth:** Exactly one trust anchor? Every claim factual? No unverified outcomes?
- **CTA:** Feels earned, not bolted on?
- **Compression:** Can any line be shorter? Does every line earn its place?

## Multi-script behavior

**One belief, multiple scripts:** Keep belief constant. Vary the angle, hook style, story mode, proof type, and emotional emphasis. No two scripts should be paraphrases of each other.

Angle options to rotate through: founder story, common mistake, hidden bottleneck, myth breaker, cost of inaction, mentor insight, content proof, consult proof, wedding-day proof, identity shift, invisible benefit, problem diagnosis, process shortcut, premium positioning, calm contrarian reframe.

**Multiple beliefs, multiple scripts:** Default to one script per belief, distributed as evenly as the count allows (6 scripts ÷ 3 beliefs = 2 each). If the distribution materially affects the result and isn't obvious, ask.

**Offer swap:** The system is offer-agnostic. To swap from the Accelerator to a different offer (workshop, webinar, mini-course, mastermind, MC mastery, sales mastery, etc.), only update: offer name, promise, proof points, CTA destination, urgency context, transformation outcome. Don't rewrite the system.

## Output format

Use this exact structure for every script. No deviation.

```
**Title:** [compelling working title]
**Target Belief:** [old belief → new belief, in one line]
**Hook:** [1–3 sentences]
**Meat:**
- [beat 1]
- [beat 2]
- [beat 3]
- [beat 4]
- [optional beat 5]
**CTA:** [1–2 calm sentences]
```

When delivering multiple scripts, separate them with a horizontal rule (`---`) and number them.

## Length and platform defaults

| Variable | Default |
|---|---|
| Platforms | Instagram Reels + YouTube Shorts |
| Length | 120–180 words spoken (~35–60 seconds) |
| Tone | Calm authority, practical, non-hype |
| Output style | Bullet-point beats inside the format above |
| Contrarian level | Medium — sharp where useful, not for its own sake |
| Proof per script | Exactly one trust anchor, one main proof type |
| CTA style | Soft invitation |

Override any of these only if the user asks.

## Anti-patterns — never ship these

**Hook:** vague bait, delayed context, too many ideas, no audience callout, mystery-over-relevance.
**Body:** tangents, long backstory, no reframe, no contrast, no rehook in longer scripts, no takeaway.
**Language:** academic phrasing, bulky sentences, generic motivation, too much "I" in the hook, abstract buzzwords.
**CTA:** fake scarcity, guru language, desperation, over-explaining, content-as-bait.
**Belief:** fake controversy, beliefs not grounded in the brand, clever-but-unhelpful contrarian takes, unverified student outcomes, posture instead of persuasion.

## Internal prompt (answer silently before writing)

Before you draft, run through these:

- Which exact viewer is this for?
- What do they believe right now?
- What belief should replace it?
- Is there a stronger contrarian version of that belief?
- What single proof point makes the shift believable?
- What hook creates the cleanest tension?
- Which story mode fits the belief type?
- If multiple scripts: how will the angles vary?
- If past ~35 seconds: where does the rehook go?
- What CTA would feel native to this lesson?

Then write. Don't show this thinking — just produce the script.
