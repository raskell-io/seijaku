# seijaku 静寂

A cinematic, hand-made [Zola](https://www.getzola.org) theme. Oversized modern
typography, full-bleed scientific imagery, product-scale editorial cards, and
quiet technical detail. Dark and light palettes follow the system preference, with an optional
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
- **Tinted cards** — archive, tag, and homepage listings share one rotating
  palette of soft champagne / pearl / ice cards
- **Projects** — a tiered projects page (ventures, flagship, labs) driven by
  small TOML files, with status pills, product visuals, and a homepage strip
- **Metadata table** — a spec-sheet header on every article (duration /
  updated / topics)
- **Structured footer** — a brand column with a short introduction, small-type
  link groups, and a legal line; light on paper, charcoal in dark mode,
  ring-gradient rule on top
- **"You are here"** — breadcrumb trail in the footer of every page
- **RASKELL–01** — an original fictional biological edge appliance used as the
  homepage product object
- **Local type** — compact Geist and IBM Plex Mono subsets, with system-stack
  fallbacks and license notes in `static/fonts/`
- **Original campaign imagery** — four project-local, compressed WebP assets;
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
hero_video = "images/hero.mp4"   # optional muted looping hero video; unset keeps the still
hero_video_webm = "images/hero.webm"  # optional WebM source, offered before the mp4
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
`zola serve` does not watch `data/`, so restart it after editing project files.

Develop the theme in isolation with `zola serve` in this directory — the
bundled `config.toml`, `content/`, and `data/` are a self-contained demo that
currently mirrors raskell.io's real content.

## License

MIT
