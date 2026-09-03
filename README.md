# seijaku 静寂

A cinematic, hand-made [Zola](https://www.getzola.org) theme. Oversized modern
typography, full-bleed scientific imagery, product-scale editorial cards, and
quiet technical detail. Dark and light palettes follow the system preference.
No JavaScript and no external requests.

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
- **"You are here"** — breadcrumb trail in the footer of every page
- **RASKELL–01** — an original fictional biological edge appliance used as the
  homepage product object
- **Local type** — compact Geist and IBM Plex Mono subsets, with system-stack
  fallbacks and license notes in `static/fonts/`
- **Original campaign imagery** — four project-local, compressed WebP assets;
  no third-party imagery or network requests
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
mark = "images/mark.svg"         # optional monochrome SVG mark, inlined (nav + cards)
portrait = "images/me.webp"      # optional circular portrait above the hero deck
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
