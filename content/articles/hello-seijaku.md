+++
title = "Hello, seijaku"
date = 2024-01-01
updated = 2024-01-02
description = "A tour of the theme's typography and components."
[taxonomies]
tags = ["meta", "design"]
+++

Headlines, chrome, and prose share one grotesk, set large and loose the way a
product page reads. Only code keeps the monospace.

## Code

A request filter in Rust, the kind of thing the edge posts are full of:

```rust
use std::time::Duration;

#[derive(Debug, Clone)]
pub struct RateLimit {
    pub requests: u32,
    pub window: Duration,
}

impl RateLimit {
    /// Returns true when the caller still has budget in the current window.
    pub fn allows(&self, seen: u32) -> bool {
        seen < self.requests // 静寂: no allocation on the hot path
    }
}
```

Configuration in TOML:

```toml
[tools]
zola = "0.22.1"

[tasks.serve]
description = "Serve the site with drafts"
run = "zola serve --drafts --port 1111"
```

And a shell session:

```bash
$ mise run serve
Building site...
-> Creating 14 pages (0 orphan) and 2 sections
Web server is available at http://127.0.0.1:1111
```

Inline `code` sits on a soft tint. Blockquotes become statements rather than
asides:

> We can't "go back" — we're remembering it wrong anyway.

---

The rule above is a hairline. Images, tables, and code blocks share the same
soft rounded corners.

| element | face |
|---------|------|
| headlines and prose | Geist / system sans |
| code | IBM Plex Mono / ui-monospace |
