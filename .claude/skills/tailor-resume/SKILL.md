---
name: tailor-resume
description: Tailor Fred Koran's one-page resume to a specific job. Use when Fred pastes a job description or posting, links one, names a role or company he is applying to, or asks to tailor, target or customize his resume.
---

# Tailor Fred's resume to a job

Fred pastes a job description; you produce a tailored copy of his resume at its own
link, which he saves as a PDF and uploads. If he only names a company or role, ask
for the posting text first.

## Sources (read before writing anything)

1. `profile.md` (this folder): everything known about Fred, a fact sheet for each of
   his 16 projects with ready bullets and "don't claim" limits, a table of which
   projects fit which kind of job, and the facts still unknown. **Read it in full.**
2. `python3 .claude/skills/tailor-resume/portfolio.py list`, then
   `portfolio.py <N>` for each project you shortlist. That prints the full write-up
   text from `index.html`, which is too large (embedded images) to read directly.
3. `resume/index.html`: the master resume. Its design is final and approved.

## Rules

1. **Truth only.** Every claim must trace to `profile.md`, a portfolio write-up, the
   master resume, or something Fred said. If the job wants something Fred has not
   shown (a tool, a credential, a date), leave it off and list it for Fred as a gap
   or a question. Never write "led", "managed" or "supervised" for team projects
   unless Fred confirms his role. Respect each project's "Don't claim" line.
2. **Use the job's words where they are true.** If the posting says "soft
   lithography" and Fred has PDMS soft lithography, say "soft lithography". Do not
   add a keyword Fred cannot back up, and never hide keywords in white or tiny text.
3. **Keep it readable by resume parsers** (the master is built this way; keep it so):
   - one column, sections in this order unless the job clearly favours another:
     Education, Experience, Projects, Technical Skills, Athletics
   - plain section names (Education, Experience, Projects, Technical Skills…)
   - every job keeps its organization, dates and role line; Experience stays newest
     first and keeps all three jobs (application forms autofill work history from it)
   - dates go in `<span class="date">`, as "Apr 2026 – Aug 2026"; no invented months
   - no `position`, `transform`, `clip-path`, `float` or wide `letter-spacing` on
     anything that holds text: Chrome writes such elements into the PDF out of
     order, and parsers read that order
4. **One Letter page.** Make room by cutting content (see the space budget below),
   never by shrinking fonts, spacing or margins.
5. **Don't restyle.** Leave the CSS alone; tailoring changes content only.
6. **The master stays as it is** unless Fred asks to change it.

## Steps

1. **Read the job.** List its must-haves, nice-to-haves and repeated keywords, and the
   kind of work (device design, lab research, QA, computation…).
2. **Match evidence.** For each requirement find Fred's strongest proof using the
   table in `profile.md`. Note anything with no proof: those are gaps to report.
3. **Pick two projects** (see the space budget) and read their full write-ups with
   `portfolio.py`.
4. **Make the copy:** `resume/<slug>/index.html`, copied from `resume/index.html`.
   Use a short slug such as the company name (`resume/medtronic/`). The repo is
   public, so folder names are visible; use a neutral slug if Fred prefers. In the copy:
   - add `<meta name="robots" content="noindex">` to `<head>`
   - point `canonical` and `og:url` at the new URL
   - set the saved-PDF name in the `beforeprint` script to
     `Frederic_Koran_Resume_<Company>`
5. **Tailor the content:**
   - **Projects:** replace the single summary entry with two project entries (format
     and space budget below), most relevant first.
   - **Experience:** keep every job; you may reorder or tighten bullets toward the
     job's language, keeping Fred's facts.
   - **Technical Skills:** put the job's skills first within each line; you may add
     skills from the "also evidenced" list in `profile.md` if the job asks for them.
   - **Coursework:** usually dropped to make room for the projects (see the space
     budget). If a job specifically values coursework and space allows, keep only the
     relevant courses.
6. **Check:** `node .claude/skills/tailor-resume/check.js resume/<slug>/index.html`
   must report one page for both font setups, and the text must read top to bottom
   with each job's dates and bullets together. Then re-read every line against
   `profile.md` for claims that drifted.
7. **Report to Fred:** the link it will live at, what you emphasized and why, the
   gaps or questions (e.g. "the posting asks for SolidWorks; you list Fusion 360"),
   and a preview image of the PDF if you can render one. Merge only when Fred says
   so. He usually reviews and then says "merge".
8. **Remember:** add any new fact Fred tells you to "Learned from Fred" in
   `profile.md` in the same change.

For a matching cover letter, Fred has a separate `/cv` skill.

## Space budget (measured)

The master fills its page, with about two lines to spare. Each project entry costs
about three lines (title line plus one two-line bullet). What fits on one page:

| Projects section | Also required | Fits |
|---|---|---|
| 2 projects, 1 bullet each | drop the coursework line | yes |
| 2 projects, 3 bullets total | drop coursework, landscaping job down to 1 bullet | yes |
| 3 projects, 1 bullet each | drop coursework, landscaping job down to 1 bullet | **no**, needs more cuts |

So plan on **two projects**. Make room in this order: the coursework line, the second
landscaping bullet, then shorter bullets. Keep every job and the Athletics section.
`check.js` has the final say.

## Project entry format

Use this inside the Projects section, one block per project. The styles for it
(`h3 a`, `.meta`) are already in the master CSS.

```html
<div class="entry">
  <div class="head"><h3><a href="https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p01">Sickle Cell Point-of-Care Device</a> <span class="meta">· four-person team</span></h3><span class="date">Winter 2026</span></div>
  <ul>
    <li>Designed and 3D-printed four microfluidic channel geometries for a sickle cell point-of-care device and tested them under matched conditions with a cell-scale blood surrogate.</li>
  </ul>
</div>
```

- Title: a short descriptive name (not the portfolio's full title), linked to the
  write-up (`#p01` to `#p18`).
- `.meta`: team size ("four-person team", "sole-authored") or the course ("BIEN 290").
- Date pill: the portfolio's date in short form ("Feb 2026", "Sep – Oct 2025",
  "Winter 2026"). If the portfolio gives no date, leave the pill out rather than
  guessing.
- One or two bullets, each with a concrete number from the write-up where possible.
- Rename the section heading to "Projects" or keep "Selected Engineering Projects".
