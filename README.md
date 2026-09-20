# Watershed Environment Lab — Homepage

Live at **https://guoliu-lab.github.io**

Built with [Jekyll](https://jekyllrb.com/), which GitHub Pages compiles automatically
on every push — no build step or GitHub Actions needed on your side.

## Where the content lives

Day-to-day updates only touch the files in `_data/`:

| To do this | Edit this file |
|---|---|
| Add a paper | `_data/publications.yml` |
| Add a news item | `_data/news.yml` |
| Add a lab member | `_data/people.yml` |
| Change the lab intro / About Me | `index.html` |
| Change contact details | `_config.yml` (emails, profile links) |
| Add a nav menu item | `_config.yml` → `nav:` |

### Adding a paper

Copy an existing block in `_data/publications.yml` and edit it:

```yaml
- title: "Full paper title"
  authors: "W. Wang, G. Liu, Z. Shen*"   # * marks corresponding authors
  journal: "Water Research"
  details: "284, 124042"                  # volume(issue), pages or article no.
  year: 2026
  doi: "10.1016/j.watres.2025.124042"
  figure: "images/papers/filename.jpg"    # optional
  first_author: true                      # true → Selected First-Author Papers
```

`G. Liu` is underlined automatically; no HTML needed. First-author papers also
appear (top 3) on the home page.

## Page structure

```
/              index.html        lab intro + About Me + latest news + selected papers
/news/         news.html         all news from _data/news.yml
/publications/ publications.html all papers from _data/publications.yml
/people/       people.html       members from _data/people.yml, grouped by institution
/contact/      contact.html

_layouts/default.html    shared page shell (head, footer)
_includes/nav.html       navigation bar — defined once, used everywhere
_includes/publication.html  how one paper entry is rendered
css/style.css            all styling
```

## Publishing changes

```bash
git add -A && git commit -m "Add new paper" && git push
```

GitHub rebuilds the site within a minute or two.
Changes can also be made directly on github.com — the site rebuilds the same way.

## Updating Google Scholar stats

Publication count, citations and h-index on the home page come from
`data/scholar.json`. Refresh them with:

```bash
"/Users/guo/Documents/科研/personal homepage/scripts/update_scholar_local.sh"
```

It fetches Google Scholar and commits + pushes only if the numbers changed.

## Optional: previewing locally before pushing

Not required — pushing is safe, since a failed build leaves the live site untouched.
If you do want a local preview:

```bash
export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:$PATH"
jekyll serve
```

Then open http://localhost:4000.
