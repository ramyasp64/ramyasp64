"""
LinkedIn Featured card, 1200x627 (1.91:1).

The graphic carries the argument: a calm waveform turns abnormal, that anomaly
dispatches a robot, and the robot arrives at the bedside. Signal, decision,
action, read left to right in one glance.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 627
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG  = "/System/Library/Fonts/Supplemental/Arial.ttf"
f = lambda p, s: ImageFont.truetype(p, s)

WHITE = (255, 255, 255)
INK   = (236, 252, 252)
MINT  = (126, 234, 208)
RED   = (255, 94, 94)

# ---------- background ----------
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
stops = [(0.00, (8, 34, 56)), (0.46, (13, 76, 102)), (1.00, (19, 116, 112))]
for y in range(H):
    t = y / (H - 1)
    for i in range(len(stops) - 1):
        a, ca = stops[i]; b, cb = stops[i + 1]
        if a <= t <= b:
            u = (t - a) / (b - a)
            c = tuple(round(ca[k] + (cb[k] - ca[k]) * u) for k in range(3))
            break
    d.line([(0, y), (W, y)], fill=c)

# faint floor grid only under the graphic band
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for gy in range(430, 560, 32):
    gd.line([(60, gy), (W - 60, gy)], fill=(255, 255, 255, 13), width=1)
for gx in range(60, W - 40, 110):
    gd.line([(gx, 430), (gx, 556)], fill=(255, 255, 255, 11), width=1)
img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")
d = ImageDraw.Draw(img)

def centred(text, y, font, fill):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)

def spaced(text, y, font, fill, tracking):
    ws = [d.textlength(ch, font=font) for ch in text]
    x = (W - (sum(ws) + tracking * (len(text) - 1))) / 2
    for ch, cw in zip(text, ws):
        d.text((x, y), ch, font=font, fill=fill); x += cw + tracking

# ---------- headline block ----------
centred("Ramya Subramanian Porselva Bharathi", 74, f(BOLD, 51), WHITE)
spaced("SUSTAINABLE HEALTHCARE ROBOTICS", 150, f(BOLD, 26), (150, 238, 214), 4.4)
centred("Physical AI  ·  ROS 2  ·  Medical Signal Processing", 200, f(REG, 23), (203, 233, 239))
centred("M.S. Web and Data Science  ·  Universität Koblenz, Germany", 240, f(REG, 19), (170, 208, 218))

# thin rule to separate claim from evidence
d.line([(430, 288), (770, 288)], fill=(255, 255, 255), width=1)
centred("Robots that carry care to the patients who are furthest from it", 302, f(REG, 21), (233, 252, 252))

# ---------- the story strip ----------
BASE = 470

# 1. calm waveform
calm = [(66, BASE)]
x0 = 150
for _ in range(2):
    for dx, dy in [(0,0),(12,-3),(21,5),(31,-30),(41,42),(51,-27),(60,4),(84,0)]:
        calm.append((x0 + dx, BASE + dy))
    x0 += 84
calm.append((330, BASE))
d.line(calm, fill=INK, width=4, joint="curve")

# 2. the anomaly: tight, tall, red
anom = [(330, BASE)]
x0 = 336
for _ in range(3):
    for dx, dy in [(0,0),(7,-6),(13,8),(20,-54),(28,58),(36,-44),(43,6),(52,0)]:
        anom.append((x0 + dx, BASE + dy))
    x0 += 52
anom.append((500, BASE))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).line(anom, fill=(255, 94, 94, 130), width=11, joint="curve")
img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(7))).convert("RGB")
d = ImageDraw.Draw(img)
d.line(anom, fill=RED, width=4, joint="curve")
d.text((334, BASE + 76), "HR 163 BPM  ·  severe tachycardia", font=f(BOLD, 15), fill=(255, 165, 165))

# 3. the decision, as a planned path
prev = (500, BASE)
for i in range(1, 61):
    t = i / 60
    p = (round(500 + t * 330), round(BASE - 52 * (t ** 0.8)))
    if i % 3 != 0:
        d.line([prev, p], fill=MINT, width=4)
    prev = p

# 4. the rover
rx, ry = 838, BASE - 52
d.rounded_rectangle([rx-28, ry-15, rx+28, ry+9], radius=6, fill=INK)
d.rounded_rectangle([rx-4, ry-30, rx+4, ry-13], radius=3, fill=INK)
d.ellipse([rx+8, ry-11, rx+20, ry+1], fill=(70, 150, 165))          # sensor eye
d.ellipse([rx-22, ry+3, rx-8, ry+17], fill=(8, 34, 56))
d.ellipse([rx+8, ry+3, rx+22, ry+17], fill=(8, 34, 56))
d.line([(rx+38, ry-3), (rx+60, ry-3)], fill=MINT, width=5)
d.polygon([(rx+58, ry-11), (rx+74, ry-3), (rx+58, ry+5)], fill=MINT)

# 5. the bedside, drawn so it reads as a hospital bed
bx, by = 972, BASE - 46
d.rounded_rectangle([bx+4, by+30, bx+150, by+37], radius=3, fill=(58, 96, 114))   # under-frame
d.rectangle([bx+16, by+37, bx+22, by+52], fill=(58, 96, 114))                      # legs
d.rectangle([bx+132, by+37, bx+138, by+52], fill=(58, 96, 114))
d.rounded_rectangle([bx+4, by+12, bx+150, by+32], radius=4, fill=(233, 243, 248))  # mattress
d.rounded_rectangle([bx+10, by+2, bx+46, by+16], radius=4, fill=(206, 224, 235))   # pillow
d.rounded_rectangle([bx-4, by-22, bx+6, by+34], radius=3, fill=(150, 122, 86))     # headboard
d.rounded_rectangle([bx+148, by-6, bx+156, by+34], radius=3, fill=(150, 122, 86))  # footboard
for gx in range(bx+56, bx+140, 14):                                                # side rail
    d.line([(gx, by+2), (gx, by+12)], fill=(176, 198, 210), width=2)
d.line([(bx+52, by+2), (bx+140, by+2)], fill=(176, 198, 210), width=3)

# the alert above the bed
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse([bx+52, by-84, bx+104, by-32], fill=(255, 96, 96, 135))
img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(10))).convert("RGB")
d = ImageDraw.Draw(img)
d.ellipse([bx+66, by-70, bx+90, by-46], fill=RED)
d.line([(bx+78, by-44), (bx+78, by-26)], fill=(255, 140, 140), width=2)

# ---------- stage labels ----------
small = f(BOLD, 15)
lab = (205, 231, 236)
for text, x in (("SIGNAL", 66), ("DECISION", 596), ("ACTION", 1066)):
    d.text((x, 556), text, font=small, fill=lab)

# ---------- footer ----------
d.line([(66, 585), (W - 66, 585)], fill=(255, 255, 255), width=1)
centred("10 projects  ·  autonomous robotics  ·  healthcare AI  ·  3D vision  ·  MLOps  ·  published research",
        598, f(REG, 16), (219, 238, 244))

out = "/Users/ramya/Documents/github/ramyasp64-profile/social/linkedin-featured.png"
img.save(out, "PNG", optimize=True)
print("wrote", out, img.size)
