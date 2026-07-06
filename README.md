# Watershed Environment Lab — Homepage

A minimal, single-page lab homepage (pure HTML + CSS, no build step required).
Lab-centric layout: hero = Watershed Environment Lab (logo + mission), About Me = Guowangchen Liu.

## Structure

```
index.html          # all content (edit this to update bio/news/publications)
css/style.css       # styling (accent color, layout)
images/lab-logo.svg # Watershed Environment Lab logo (vector; also used as favicon)
images/profile.jpg  # your profile photo (add this — 400×400px+ square recommended)
```

## Deploy to GitHub Pages

Site URL: **https://guoliu-lab.github.io** (via a GitHub organization named `guoliu-lab`).

One-time setup on github.com (logged in as `GuowangchenLiu`):

1. Create the free organization: https://github.com/organizations/plan
   → choose **Free**, organization name **guoliu-lab**.
2. In that organization, create a new **public** repository named
   **guoliu-lab.github.io** (empty — no README/license, this folder already has one).
3. Push this folder (git is already initialized and committed locally):

   ```bash
   git push -u origin main
   ```

4. If Pages doesn't activate automatically: repo **Settings → Pages →
   Source: Deploy from a branch → main / (root)**.
   The site goes live at https://guoliu-lab.github.io within a minute or two.

## Updating content

- **News**: add a `<li>` at the top of the `#news` list in `index.html`.
- **Publications**: copy an existing `<li>` block in `#publications` and edit.
- **Accent color**: change `--accent` in `css/style.css`.

## To-do before publishing

- [ ] Add `images/profile.jpg` (a circular crop is applied automatically)
- [ ] Check the Chinese name rendering (刘国王辰) — correct it if wrong
- [ ] Optional: replace `images/lab-logo.svg` with the original logo PNG
      (save it as `images/lab-logo.png` and update the two references in `index.html`)
