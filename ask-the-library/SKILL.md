---
name: ask-the-library
description: Library-first answering for Joe Rivera. Use for any learning, communication, sales, influence, mindset, speaking, leadership or self-development question, and whenever Joe says "ask the library", "ask the vault", "what does the library say", "what did Eli say about", "what have I learned about", or asks for a direct answer that could come from his own distilled material. Searches the Notion 📖 Learning Library first (Domain and Teacher), then the WDJM 📚 Knowledge Base, then general knowledge, and labels the provenance of every claim. Can pull the raw transcript from Dropbox for context around a quote. Not for intake (learn-this) and not for writing content (belief-patterns, wdjm-script-writer).
---

# ask-the-library

Joe has paid for and distilled a library. An answer that ignores it and goes straight to general
knowledge wastes that, and an answer that presents a teacher's view as Joe's breaks his law of
voice separation. This skill fixes both.

## Where things live

| Store | ID | What is in it |
|---|---|---|
| 📖 Learning Library | `collection://1e250f21-7a1e-43ce-8d9d-6e520f883940` | Concepts from other teachers, with Joe's Ruling |
| 📚 Sources | `collection://1e4c73a8-dddb-45a3-9835-87e3270f652d` | One row per source; Teacher, URL, Private, Raw Location |
| 📚 Knowledge Base (WDJM) | `collection://d5d2ac86-fd33-44b0-9a91-1b24611fd0d2` | Joe's own calls and courses, plus Eli Wilde rows filed before 2026-09-04 |
| Rules | Notion page 🎓 Learning OS `3d12e7ac-085c-81bd-9f6d-ce51e58e6e8e` | Retrieval order, ruling semantics, privacy |
| Raw transcripts | Dropbox `/AI/Claude Code/Learning OS/sources/<teacher-key>/raw/` | The path is on the Sources row |

## Retrieval order

1. **📖 Learning Library.** Search scoped to the data source with the question's keywords. Then,
   if the question names a domain or a teacher, query in rows mode: filter Domain (multi-select
   contains) and, for a teacher, first find their Sources rows and filter Library by Source
   (relation contains). Read the two to five most relevant rows in full. Do not bulk-load the
   library.
2. **📚 Knowledge Base.** Same search, scoped to that data source. Joe's own material outranks a
   teacher's when they conflict on a WDJM question.
3. **General knowledge**, and the web only if the question needs something current.

Stop as soon as you have enough. Three good rows beat twelve skimmed ones.

## How to answer

- Lead with the answer, applied to Joe's situation (his rooms: the mentorship room, talks,
  reels, consults with couples, copy, curriculum).
- **Label every claim's provenance**, inline, in one of four forms:
  - *Library*: teacher, entry name, link. Example: `(Eli Wilde, "Hierarchy of criteria",
    Library)` with the row linked.
  - *Joe's ruling*: only when Joe's Ruling on the row is Adopted, Restricted, Refused or Differ.
    `Unruled` means it is the teacher's view and Claude's proposal, and the answer says so.
  - *Knowledge Base*: entry name, link, and Source (Mentorship Call, a course, or a teacher).
  - *General knowledge* or *web*, with the link for web.
- **Respect the ruling and the guard.** A row whose Claude Proposal is Restrict or whose Guard
  names a scope limit is answered with that limit stated ("in the mentorship room, not to a
  couple"). A Refused Ledger item is never offered as advice; if Joe asks for it, say it is on
  the refused list and why.
- **Private rows** (Private rollup true) may inform an answer to Joe. Their content never goes
  into a draft reel, post, lesson, product, or anything another person will see. Say so when it
  matters.
- **When the library has nothing**, say so plainly in the first line, answer from general
  knowledge with that label, and offer to intake a source ("say learn this with a link").
- **Raw on request.** When Joe wants the context around a quote, fetch the Raw Location path
  from the Sources row through the Dropbox connector and quote the surrounding passage with its
  timestamp.

## Answer shape

Short questions get a short answer: the answer, one or two cited rows, the limit if any. Longer
questions get at most three sections: the answer, what the library says (cited), what is still
Joe's call. No em dashes or en dashes.

## Never

- Present an Unruled row as Joe's position.
- Offer a Refused Ledger technique as advice.
- Put Private material into anything published.
- Invent a citation. If a row is not there, it is not there.
- Re-read a transcript to answer a question the library already covers.
