#!/usr/bin/env python3
"""Build a client website from a JSON intake file.

Usage:
    python3 build.py clients/example-landscaping.json

Output goes to dist/<slug>/ and is ready to deploy as a static site
(Cloudflare Pages, Netlify, or any static host). Standard library only.
"""

import datetime
import html
import json
import re
import shutil
import sys
from pathlib import Path
from string import Template

KIT = Path(__file__).resolve().parent
TEMPLATE_DIR = KIT / "template"

REQUIRED = [
    "slug", "business_name", "site_url", "phone", "city", "state",
    "headline", "subheadline", "services", "service_areas", "web3forms_key",
]


def esc(value):
    return html.escape(str(value), quote=True)


def darken(hex_color, factor=0.72):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(int(r * factor), int(g * factor), int(b * factor))


def phone_tel(phone):
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        digits = "1" + digits
    return "+" + digits


def section(section_id, title, inner, alt=False, intro=""):
    cls = ' class="alt"' if alt else ""
    intro_html = f'<p class="lead">{esc(intro)}</p>' if intro else ""
    return (f'<section id="{section_id}"{cls}><div class="container">'
            f"<h2>{esc(title)}</h2>{intro_html}{inner}</div></section>")


def build_schema(c):
    schema = {
        "@context": "https://schema.org",
        "@type": c.get("schema_type", "LocalBusiness"),
        "name": c["business_name"],
        "url": c["site_url"] + "/",
        "telephone": phone_tel(c["phone"]),
        "areaServed": c["service_areas"],
    }
    if c.get("email"):
        schema["email"] = c["email"]
    if c.get("logo"):
        schema["logo"] = c["site_url"] + "/" + c["logo"]
    if c.get("address"):
        a = c["address"]
        schema["address"] = {
            "@type": "PostalAddress",
            "streetAddress": a.get("street", ""),
            "addressLocality": a.get("city", c["city"]),
            "addressRegion": a.get("state", c["state"]),
            "postalCode": a.get("zip", ""),
            "addressCountry": "US",
        }
    if c.get("hours_schema"):
        schema["openingHours"] = c["hours_schema"]
    if c.get("social"):
        schema["sameAs"] = [s["url"] for s in c["social"]]
    # Only include a rating if the owner supplied real numbers from their Google profile.
    rating = c.get("rating")
    if rating and rating.get("value") and rating.get("count"):
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": rating["value"],
            "reviewCount": rating["count"],
        }
    # Keep "</" out of the inline script so it can't close the tag early.
    return json.dumps(schema, indent=2).replace("</", "<\\/")


def render_index(c):
    services_html = "".join(
        f'<article class="card"><h3>{esc(s["name"])}</h3><p>{esc(s["description"])}</p></article>'
        for s in c["services"]
    )
    service_options = "".join(f"<option>{esc(s['name'])}</option>" for s in c["services"])
    areas_html = "".join(f"<li>{esc(a)}</li>" for a in c["service_areas"])

    trust = c.get("trust_points", [])
    trust_html = ('<ul class="trust">' + "".join(f"<li>{esc(t)}</li>" for t in trust) + "</ul>") if trust else ""

    why = c.get("why_us", [])
    why_html = section(
        "why", f"Why {c['business_name']}",
        '<div class="grid grid-3">' + "".join(
            f'<article class="card"><h3>{esc(w["title"])}</h3><p>{esc(w["text"])}</p></article>' for w in why
        ) + "</div>",
        alt=True,
    ) if why else ""

    reviews = c.get("reviews", [])
    reviews_html = ""
    if reviews:
        rating = c.get("rating") or {}
        summary = ""
        if rating.get("value") and rating.get("count"):
            summary = (f'<p class="rating-summary">{esc(rating["value"])} out of 5 stars from '
                       f'{esc(rating["count"])} {esc(rating.get("source", "Google"))} reviews</p>')
        cards = "".join(
            f'<figure class="card review"><div class="stars" aria-label="{int(r.get("stars", 5))} out of 5 stars">'
            f'{"★" * int(r.get("stars", 5))}</div><blockquote>{esc(r["text"])}</blockquote>'
            f'<figcaption><cite>{esc(r["author"])}</cite></figcaption></figure>'
            for r in reviews
        )
        reviews_html = section("reviews", "What customers say", summary + f'<div class="grid grid-3">{cards}</div>')

    gallery = c.get("gallery", [])
    gallery_html = section(
        "work", "Recent work",
        '<div class="gallery">' + "".join(
            f'<img src="{esc(g["src"])}" alt="{esc(g["alt"])}" loading="lazy" width="800" height="600">'
            for g in gallery
        ) + "</div>",
    ) if gallery else ""

    faqs = c.get("faqs", [])
    faq_html = section(
        "faq", "Frequently asked questions",
        "".join(f"<details><summary>{esc(f['q'])}</summary><p>{esc(f['a'])}</p></details>" for f in faqs),
        alt=not gallery,
    ) if faqs else ""

    email_html = (f'<li><strong>Email:</strong> <a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a></li>'
                  if c.get("email") else "")
    address_html = ""
    if c.get("address") and c["address"].get("show", True):
        a = c["address"]
        address_html = (f'<li><strong>Address:</strong> {esc(a.get("street", ""))}, '
                        f'{esc(a.get("city", c["city"]))}, {esc(a.get("state", c["state"]))} {esc(a.get("zip", ""))}</li>')

    license_html = f'<p>{esc(c["license_text"])}</p>' if c.get("license_text") else ""
    social_html = "".join(
        f'<a href="{esc(s["url"])}" rel="noopener">{esc(s["name"])}</a><br>' for s in c.get("social", [])
    )

    logo_html = (f'<img src="{esc(c["logo"])}" alt="" width="40" height="40">' if c.get("logo") else "")
    hero_style = (f' .hero {{ --hero-img: url("{esc(c["hero_image"])}"); }}' if c.get("hero_image") else "")
    og_image = (f'<meta property="og:image" content="{esc(c["site_url"])}/{esc(c["hero_image"])}">'
                if c.get("hero_image") else "")

    brand = c.get("brand_color", "#2f6b3a")
    values = {
        "page_title": esc(c.get("page_title") or f'{c["business_name"]} | {c.get("primary_service", "Services")} in {c["city"]}, {c["state"]}'),
        "meta_description": esc(c.get("meta_description") or c["subheadline"]),
        "site_url": esc(c["site_url"]),
        "og_image": og_image,
        "favicon": esc(c.get("favicon") or c.get("logo") or "data:,"),
        "brand_color": esc(brand),
        "brand_dark": esc(c.get("brand_dark") or darken(brand)),
        "accent_color": esc(c.get("accent_color", "#f2b33d")),
        "hero_style": hero_style,
        "schema_json": build_schema(c),
        "logo_html": logo_html,
        "business_name": esc(c["business_name"]),
        "legal_name": esc(c.get("legal_name") or c["business_name"]),
        "phone_tel": esc(phone_tel(c["phone"])),
        "phone_display": esc(c["phone"]),
        "headline": esc(c["headline"]),
        "subheadline": esc(c["subheadline"]),
        "trust_html": trust_html,
        "services_intro": esc(c.get("services_intro", "")),
        "services_html": services_html,
        "why_html": why_html,
        "reviews_html": reviews_html,
        "city": esc(c["city"]),
        "state": esc(c["state"]),
        "areas_html": areas_html,
        "gallery_html": gallery_html,
        "faq_html": faq_html,
        "response_time": esc(c.get("response_time", "within one business day")),
        "email_html": email_html,
        "hours_display": esc(c.get("hours_display", "")),
        "address_html": address_html,
        "web3forms_key": esc(c["web3forms_key"]),
        "service_options": service_options,
        "footer_blurb": esc(c.get("footer_blurb", f'{c.get("primary_service", "Local service")} in {c["city"]} and nearby.')),
        "license_html": license_html,
        "social_html": social_html,
        "year": datetime.date.today().year,
    }
    return Template((TEMPLATE_DIR / "index.html").read_text()).substitute(values)


def render_page(c, title, body, robots="index,follow"):
    brand = c.get("brand_color", "#2f6b3a")
    values = {
        "title": esc(title),
        "robots": robots,
        "business_name": esc(c["business_name"]),
        "legal_name": esc(c.get("legal_name") or c["business_name"]),
        "favicon": esc(c.get("favicon") or c.get("logo") or "data:,"),
        "brand_color": esc(brand),
        "brand_dark": esc(c.get("brand_dark") or darken(brand)),
        "accent_color": esc(c.get("accent_color", "#f2b33d")),
        "logo_html": (f'<img src="{esc(c["logo"])}" alt="" width="40" height="40">' if c.get("logo") else ""),
        "phone_tel": esc(phone_tel(c["phone"])),
        "phone_display": esc(c["phone"]),
        "body": body,
        "year": datetime.date.today().year,
    }
    return Template((TEMPLATE_DIR / "page.html").read_text()).substitute(values)


def privacy_body(c):
    # Plain-language starting point only. Have an attorney review before relying on it.
    name = esc(c.get("legal_name") or c["business_name"])
    contact = esc(c.get("email") or c["phone"])
    updated = datetime.date.today().strftime("%B %d, %Y").replace(" 0", " ")
    return f"""<h1>Privacy policy</h1>
<p><em>Last updated {updated}</em></p>
<p>{name} ("we") runs this website. This policy explains what information we collect and how we use it.</p>
<h2>What we collect</h2>
<p>When you submit our quote form, we receive the information you enter, such as your name, phone number, email address, and project details. We also use privacy-friendly analytics that count visits without identifying you personally.</p>
<h2>How we use it</h2>
<p>We use your information only to respond to your request and provide our services. We do not sell your information.</p>
<h2>Service providers</h2>
<p>Form submissions are delivered to us through a third-party form service, and the site is hosted by a third-party hosting provider. They process data only to provide those services.</p>
<h2>Contact</h2>
<p>Questions or requests to delete your information: {contact}.</p>"""


def thank_you_body(c):
    return f"""<h1>Thanks, we got your request!</h1>
<p class="lead">We'll get back to you {esc(c.get("response_time", "within one business day"))}.</p>
<p>Need help sooner? Call <a href="tel:{esc(phone_tel(c["phone"]))}">{esc(c["phone"])}</a>.</p>"""


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 build.py clients/<client>.json")
    intake = Path(sys.argv[1])
    c = json.loads(intake.read_text())

    missing = [k for k in REQUIRED if not c.get(k)]
    if missing:
        sys.exit(f"Missing required fields: {', '.join(missing)}")
    c["site_url"] = c["site_url"].rstrip("/")

    out = KIT / "dist" / c["slug"]
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    (out / "index.html").write_text(render_index(c))
    (out / "privacy.html").write_text(render_page(c, "Privacy policy", privacy_body(c)))
    (out / "thank-you.html").write_text(render_page(c, "Thank you", thank_you_body(c), robots="noindex"))
    shutil.copy(TEMPLATE_DIR / "styles.css", out / "styles.css")

    # Client photos and logo live next to the intake file, in assets/<slug>/.
    assets = intake.parent / "assets" / c["slug"]
    if assets.is_dir():
        shutil.copytree(assets, out, dirs_exist_ok=True)

    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {c['site_url']}/sitemap.xml\n")
    today = datetime.date.today().isoformat()
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{esc(c["site_url"])}/</loc><lastmod>{today}</lastmod></url>\n'
        f'  <url><loc>{esc(c["site_url"])}/privacy.html</loc><lastmod>{today}</lastmod></url>\n'
        "</urlset>\n"
    )
    print(f"Built {out}")


if __name__ == "__main__":
    main()
