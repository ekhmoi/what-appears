# What Appears – Book Workspace

This repo is a playground / studio for writing a book about appearance, field, compression, self, and uncertainty.

There are two main layers:

- **Reader-facing:** `1-chapters/` (the actual book text being developed)  
- **Author-facing:** everything else (project notes, wrappers, snippets, chapter notes, raw dumps, archive)

---

## Folder structure

### `project/` – what am I making?

Meta level.

- `outline.md` – current table of contents for the book (parts + chapters)
- `decisions.md` – style choices, constraints, high-level goals
- `notes.md` – general project thoughts that aren’t tied to a specific chapter

Nothing here is meant for readers.

---

### `_chapters/` – the book itself in flux

Reader-facing manuscript, in order.

Suggested layout:

- `00-front-matter.md` – preface / intro / how to read this  
- `01-part-…/` – part folders, each containing numbered `chapter-*.md` files  
- `99-back-matter.md` – afterword, notes, etc. (optional)

If someone asks to “see the work”, they essentially see content from here.

---

### `wrappers/` – intros around the chapters

Things that *point into* the chapters, with different framings:

- `intro-general.md` – for curious non-specialists
- `intro-rationalist.md` – for model/agent/uncertainty people
- `intro-practice.md` – for meditation / contemplative folks
- anything else like talk outlines, posts that link to chapters, etc.

These are optional, but they help explain the same core material to different audiences.

---

### `snippets/` – reusable pieces

A stash of small, reusable building blocks:

- `examples.md` – scenarios (park, room, uncertainty cases, etc.)
- `metaphors.md` – images and analogies
- `polished-phrases.md` – sentences worth reusing verbatim
- `references-and-ancestry.md` – overlaps with traditions, authors, papers

When something in notes or raw feels like “this is a good example / line”, copy it in here.

---

### `notes/` – per-chapter work

Workspace for each chapter.

Suggested layout:

- `notes/01-part-…/01-chapter-….notes.md` – notes for that specific chapter  
- `notes/cross-cutting-notes.md` – ideas that touch multiple chapters

Use these files for:

- TODOs for that chapter
- alternate openings / structures
- “this section maybe belongs in Part 2 instead?”
- local rants / questions

These are only for you; readers never see them directly.

---

### `raw/` – raw stream

Full goblin-brain. Nothing has to make sense.

- daily dumps: `2025-12-07.md`, `2025-12-08.md`, …
- wild ideas, contradictions, emotional venting
- thoughts that don’t have an obvious home yet

Rule of thumb:  
if you don’t know where it goes, it goes in `5-raw/`.

Later, you can mine good bits out into `4-notes/` or `3-snippets/`.

---

### `archive/` – safe graveyard

Old but maybe-useful stuff:

- `original-pdfs/` – original “What Appears”, “Appearance, Field, and Compression”, “Stabilize / Dissolve” docs
- `cut-chunks.md` – sections removed from the chapters but worth keeping around
- `old-outline-*.md` – previous TOC versions

Nothing here is active, but it means you never have to truly delete anything.

---

## How to use this day-to-day

- **Writing chapters text?** → edit files in `1-chapters/`.
- **Working on a specific chapter (ideas, TODOs, alternative framings)?** → its matching file in `4-notes/`.
- **Came up with a good example / metaphor / line?** → also copy it into `3-snippets/`.
- **Have thoughts but no idea where they belong yet?** → dump into `5-raw/`.
- **Changing the structure of the chapters?** → update `0-project/outline.md`, then mirror that in `1-chapters/` + `4-notes/`.

This README is for me (and any future collaborators) to remember how the studio is laid out.
