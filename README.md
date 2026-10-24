# seijaku 静寂

A cinematic, hand-made [Zola](https://www.getzola.org) theme. Oversized modern
typography, a cinematic homepage hero, dense dated post indexes, and quiet
technical detail. Dark and light palettes follow the system preference, with an optional
System / Light / Dark control in the footer. No external requests, and no
JavaScript unless you enable that control (about twenty inline lines).

Inspired by premium biological-computing campaigns, translated for a personal
technical publication rather than a product company.

## Features

- **Optional announcement** — a slim site notice above the navigation, hidden
  when unset
- **Versioned brand** — seasonal `title · ver. aw26` treating the site like a
  fashion collection
- **Pill navigation** — floating translucent nav with a bevelled active state,
  and a CSS-only hamburger sheet on phones
- **Dense post index** — archive, tag, and homepage listings are dated rows
  (title, one-line deck, tags, read time); archive and tag pages group by year
- **Projects** — a tiered projects page (ventures, flagship, labs) driven by
  small TOML files, with status pills, product visuals, and a homepage strip
- **Metadata table** — a spec-sheet header on every article (duration /
  updated / topics)
- **Contents list** — automatic on long reads (8+ minutes, 3+ headings): a
  sticky rail beside the text on wide screens, a short list above it on phones;
  `extra.toc = true/false` in front matter overrides
- **Structured footer** — a brand column with a short introduction, small-type
  link groups, and a legal line; light on paper, charcoal in dark mode,
  ring-gradient rule on top
- **Article covers** — `extra.cover` (and `extra.cover_alt`) shows an image beside the
  title on wide screens and under the metadata on phones. Covers get a tritone grade in the
  theme palette, film grain, and a ring border, so mixed imagery reads as one series; hover or
  focus fades back to the original. Opt out per page with `extra.cover_grade = false` or
  site-wide with `cover_grade = false` under `[extra.seijaku]`
- **After the article** — related reading (`extra.related = ["slug", ...]`, otherwise posts
  that share tags) and links to the older and newer post
- **Now list** — optional `[[extra.now]]` blocks (`name`, `text`, `url`) in
  `content/_index.md` render a "What I am working on" section on the homepage
- **Search** — with `build_search_index = true`, a nav button (and the `/` key) opens a
  search dialog; the index and the elasticlunr library load on first open
- **Code blocks** — language label (or diagram title) as a quiet first line;
  `code_copy = true` adds a copy button (a few lines of inline JS)
- **Site hooks** — create `templates/partials/head_extra.html` or
  `templates/partials/body_end.html` in your site to add tags without overriding layouts
- **"You are here"** — breadcrumb trail in the footer of every page
- **Local type** — compact Geist and IBM Plex Mono subsets, with system-stack
  fallbacks and license notes in `static/fonts/`
- **Original hero imagery** — project-local, compressed AVIF/WebP assets;
  no third-party imagery or network requests
- **Colour-scheme control** — optional System / Light / Dark toggle in the
  footer, remembered per browser; the only script the theme can emit
- Sections with optional pagination, tag taxonomy, RSS, a distinctive 404,
  print styles, reduced-motion support, and visible keyboard focus states

## Usage

```toml
theme = "seijaku"

taxonomies = [{ name = "tags", feed = true }]

[extra.seijaku]
version = "aw26"                 # optional seasonal version label
banner = "A quiet announcement." # optional; omit to hide
tagline = "(a personal site)"    # optional, next to the brand
footer_note = "made with care"   # optional footer sign-off
footer_about = "What this site is."  # optional introduction under the footer brand (markdown)
scheme_toggle = true             # optional System / Light / Dark control in the footer
mark = "images/mark.svg"         # optional monochrome SVG mark, inlined (nav + cards)
mark_play = true                 # optional: the mark blinks, glances, and reacts to clicks
portrait = "images/me.webp"      # optional circular portrait above the hero deck
hero_motion = "images/hero.avif"   # optional animated AVIF loop behind the hero
hero_poster = "images/hero.webp" # optional poster / reduced-motion fallback (defaults to images/raskell-hero.webp)
og_image = "images/og.png"       # optional default social image
main_section = "articles"        # section listed on the homepage
projects_section = "projects"    # optional; enables the homepage projects strip
cta = { name = "Start here", url = "@/start-here.md" }   # optional nav button
nav = [
  { name = "Articles", url = "@/articles/_index.md" },
  { name = "Projects", url = "@/projects/_index.md" },
  { name = "About", url = "@/about.md" },
]
explore = [ { name = "Tags", url = "/tags" }, { name = "RSS", url = "/rss.xml" } ]
social = [ { name = "GitHub", url = "https://github.com/you" } ]
```

### Projects

`content/projects/_index.md` uses `template = "projects.html"` and lists tiers,
each naming the project slugs to show in order. Every project is a small TOML
file at `data/projects/<slug>.toml` with `title`, `description`, `status`,
optional `logo` or `image`, `stack`, `links`, and `featured`. See `theme.toml`
for the full shape. Projects have no pages of their own; cards link out.
A tier can carry a call to action between its head and its cards:
`cta = { eyebrow = "...", title = "...", text = "...", links = [{ name = "...", url = "@/invest.md" }] }`.
A project with a brandtype shows it as the card title: `wordmark` (and `wordmark_dark`) sit beside the
`logo`, or `logo_wide = true` marks a logo that already holds the name. The description then opens
with the name in bold. `pitch = "@/..."` names an investor brief, linked from `project_cards(pitch=true)`.
Pages with `template = "venture.html"` and `extra.project = "<slug>"` render such a brief: a hero in the
project's colours, section links from the headings, and the page's building blocks.
Cards can carry `support = [{ name, url }]` (GitHub Sponsors, Open Collective, Ko-fi, ...) and
`tagline` for the `support_cards` shortcode.

### Facet filters on a post list

Set `facets = ["topic", "technology", "form", "length", "series"]` under `[extra]` in a section's `_index.md`
to put filters above its list (any subset, in that order). Topics are the `domain` tags of the tag
vocabulary, each post's tags rolled up through `broader`; technologies are the `technology` tags;
form picks out reviews; length comes from the reading time. The whole section is listed on one page,
the choice is kept in the URL, and without JavaScript the list shows in full.

### Reading log

A page with `template = "reading.html"` lists the works in `data/reading.toml` (config
`reading_data`): `[[works]]` with `id`, `title`, `subtitle`, `author`, `kind` (book, novel, paper,
report, article, essay, journal), `year`, `edition` or `publisher`, `url`, `status` (reading, next, backlog,
read, set-aside), `started` / `finished` ("YYYY", "YYYY-MM", or "YYYY-MM-DD"; read works need `finished`;
`when` shows a vaguer date such as "summer 2025" while `finished` keeps the order),
`topics` (tag slugs), a one-line `take`, `cover` (a path under `static/`), and
`suggested_by` / `suggested_url` / `suggested_note` to credit a reader who suggested the work. Each row shows the
cover, graded with the theme's tritone until hovered or opened (works without one get a typographic
tile), with title and author; the rest opens below them, and `/reading/#<id>` opens that row.
Shelves are Reading now, Up next, Backlog, Read (by year), and Set aside; `facets = ["form", "topic"]` under the page's `[extra]` adds filters. Point
`extra.seijaku.reading = "@/reading.md"` at the page so map nodes and references link to it.

A review is any article or note with `review = "<id>"` under `[extra]`: it gets a "Review of" row
(notes: an "On ..." line), a review label in post lists, and the work's title on the reading page
opens it. Pages that discuss a work without reviewing it name it in `reads = ["<id>", ...]`. On the
map, works are outlined diamonds joined to their shelf, their topics, their reviews and mentions,
and any page that links to the work's `url`.

### Building blocks for pages

Shortcodes that set parts of a page apart from the running text:

- `{{ project_cards(slugs=["a", "b"]) }}`: the projects page cards, inside any page
- `{{ support_cards(slugs=["a"]) }}`: ways to fund an open-source project, from its `support` list
- `{% tiles(cols=3) %} - **Title**: text {% end %}`: a list set as a grid of tiles; numbered lists count up
- `{% card(title, url, eyebrow, meta, links=["Name|url"]) %} markdown {% end %}`: a card around a block of prose
- `{% panel(eyebrow, title, links=["Name|url"], contact=true) %} markdown {% end %}`: a call to action in a gradient frame
- `{{ contact() }}`: the `extra.seijaku.social` profiles as buttons

`zola serve` does not watch `data/`, so restart it after editing project files.

Develop the theme in isolation with `zola serve` in this directory — the
bundled `config.toml`, `content/`, and `data/` are a self-contained demo that
currently mirrors raskell.io's real content.

## License

MIT
