# Fred Koran's portfolio and resume site

GitHub Pages site, published from `main`:
https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/

- `index.html`: the engineering project portfolio (18 projects). About 1.2 MB of
  embedded images and fonts, so don't read it directly. Use
  `python3 .claude/skills/tailor-resume/portfolio.py list` or `… portfolio.py <N>`
  to get a project's text.
  The same file is printed to `Frederic-Koran-Engineering-Portfolio.pdf`. Its
  screen look lives in `<style id="web-layer">` and the last `<script>`: on screen
  the home page is the cover and contents and each project is its own page (`#p05`
  opens project 05); print ignores all of it and stays the paginated document.
  Don't split visible text into new elements there, or the PDF's copyable text
  changes.
- `resume/index.html`: the master one-page resume. Fred's PDF comes from its
  "Save as PDF" button (browser print to Letter).
- `resume/<slug>/index.html`: copies tailored to specific jobs.
- `.claude/skills/tailor-resume/`: how to tailor the resume to a job description.
  `profile.md` in that folder holds everything known about Fred and his projects;
  treat it as memory and update it when he tells you something new.

## Editing a resume page

- It must stay one Letter page and readable by applicant-tracking systems. The rules
  are in `.claude/skills/tailor-resume/SKILL.md`, and the comment at the top of the
  `<style>` block explains why positioned elements and wide letter-spacing are banned.
- Verify every change with
  `node .claude/skills/tailor-resume/check.js <file>`: one page with both font
  setups, and the PDF text in reading order.
- The design is approved and matches Fred's own PDF (Oct 2026): black and white,
  name and contact line over a rule, caps section titles with a grey hairline, job
  title and date on one line with the organisation in italics below. Don't restyle
  unless Fred asks.

## Working with Fred

- He reviews a preview image of the PDF, then says "merge" to publish. Changes go on
  the session branch, then a pull request squash-merged into `main`. Pages deploys in
  about a minute.
- Never put anything on his resume that he hasn't stated or that isn't in his
  portfolio. Ask instead.
