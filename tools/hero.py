#!/usr/bin/env python3
"""Procedural hero loop for seijaku: soft vertical light columns in the champagne / pearl /
ice palette over graphite, drifting on integer-cycle sines so the loop is seamless by
construction. Renders 168 PNG frames (7 s at 24 fps, 1920x1080).

    python3 -m venv .venv && .venv/bin/pip install numpy pillow
    .venv/bin/python tools/hero.py /tmp/hero-frames
    ffmpeg -framerate 24 -i /tmp/hero-frames/%04d.png -vf format=yuv420p10le \
      -c:v libsvtav1 -preset 4 -crf 34 -g 168 -svtav1-params tune=0 -loop 0 -f avif static/images/raskell-hero.avif
    cwebp -q 72 /tmp/hero-frames/0000.png -o static/images/raskell-hero.webp

Tuning: `regions` are the broad hue columns (colour, centre as a fraction of width, sigma in px,
intensity); `streaks` are the narrow highlights; `slats` add the fine band structure; `hm` keeps
the left of the frame dark for the headline. Keep every motion an integer number of cycles per loop.
"""
import numpy as np, os, sys, math
from PIL import Image
W, H, N = 1920, 1080, 168
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
rng = np.random.default_rng(5)
hexc = lambda h: np.array([int(h[i:i+2], 16) for i in (1, 3, 5)], np.float32) / 255
C = {"champagne": hexc("#e9bd70"), "gold": hexc("#f0cf8a"), "pearl": hexc("#f4f0df"), "ice": hexc("#b9ecec"),
     "cyan": hexc("#6fd6da"), "teal": hexc("#3aa7aa"), "amber": hexc("#d9a55c")}
bg_top, bg_bot = hexc("#060707"), hexc("#0a1c1a")
x = np.arange(W, dtype=np.float32)[None, :]
y = np.arange(H, dtype=np.float32)[:, None]
bg = (bg_top[None, None, :] * (1 - y / H)[:, :, None] + bg_bot[None, None, :] * (y / H)[:, :, None])
bg = np.broadcast_to(bg, (H, W, 3)).copy()
# left stays calm for the headline; light opens up from ~35% to the right edge
hm = 0.10 + 0.90 * (0.5 - 0.5 * np.cos(np.pi * np.clip((x - 0.28 * W) / (0.50 * W), 0, 1)))
# broad hue regions, neighbours in distinct hues, modest overlap
regions = []
for i, (name, cx, sig, it) in enumerate([("teal", 0.42, 130, 0.10), ("champagne", 0.55, 120, 0.22), ("pearl", 0.66, 90, 0.26),
                                          ("ice", 0.76, 110, 0.24), ("gold", 0.86, 100, 0.22), ("cyan", 0.95, 120, 0.20), ("pearl", 1.04, 90, 0.18)]):
    regions.append(dict(color=C[name], x0=cx * W, sig=sig, it=it, amp=rng.uniform(10, 30), k=int(rng.integers(1, 3)),
                        phi=rng.uniform(0, 2 * math.pi), m=int(rng.integers(1, 3)), psi=rng.uniform(0, 2 * math.pi),
                        yc=rng.uniform(0.2, 0.8) * H, sy=rng.uniform(0.4, 0.9) * H))
# narrow highlight streaks
streaks = []
for name, cx, sig, it in [("pearl", 0.62, 16, 0.30), ("ice", 0.80, 22, 0.28), ("champagne", 0.71, 14, 0.24), ("pearl", 0.91, 18, 0.26), ("cyan", 0.49, 12, 0.16)]:
    streaks.append(dict(color=C[name], x0=cx * W, sig=sig, it=it, amp=rng.uniform(18, 40), k=int(rng.integers(1, 3)),
                        phi=rng.uniform(0, 2 * math.pi), yc=rng.uniform(0.25, 0.75) * H, sy=rng.uniform(0.3, 0.6) * H))
# slats: three soft vertical band patterns, each drifting exactly one period per loop
slats = [dict(P=150.0, off=rng.uniform(0, 150), dirn=1), dict(P=236.0, off=rng.uniform(0, 236), dirn=-1), dict(P=372.0, off=rng.uniform(0, 372), dirn=1)]
for f in range(N):
    tt = f / N
    slat = np.zeros((1, W), np.float32)
    for s in slats:
        slat += 0.5 + 0.5 * np.cos(2 * math.pi * (x - s["off"] - s["dirn"] * s["P"] * tt) / s["P"])
    slat = (slat / len(slats)) ** 1.6                      # deeper valleys between bands
    light = np.zeros((H, W, 3), np.float32)
    for r in regions:
        xt = r["x0"] + r["amp"] * math.sin(2 * math.pi * r["k"] * tt + r["phi"])
        it = r["it"] * (1 + 0.18 * math.sin(2 * math.pi * r["m"] * tt + r["psi"]))
        gx = np.exp(-((x - xt) ** 2) / (2 * r["sig"] ** 2)) * (0.30 + 0.70 * slat)
        gy = 0.6 + 0.4 * np.exp(-((y - r["yc"]) ** 2) / (2 * r["sy"] ** 2))
        light += (it * (gy @ gx))[:, :, None] * r["color"][None, None, :]
    for s in streaks:
        xt = s["x0"] + s["amp"] * math.sin(2 * math.pi * s["k"] * tt + s["phi"])
        gx = np.exp(-((x - xt) ** 2) / (2 * s["sig"] ** 2))
        gy = 0.35 + 0.65 * np.exp(-((y - s["yc"]) ** 2) / (2 * s["sy"] ** 2))
        light += (s["it"] * (gy @ gx))[:, :, None] * s["color"][None, None, :]
    breathe = 1 + 0.035 * math.sin(2 * math.pi * tt)
    img = bg + light * hm[:, :, None] * breathe
    img = 1 - np.exp(-1.25 * img)
    Image.fromarray((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)).save(f"{out}/{f:04d}.png", compress_level=1)
    if f % 56 == 0: print("frame", f, "max", round(float(img.max()), 3), "left-55% max", round(float(img[:, : int(0.55 * W)].max()), 3), flush=True)
print("done")
