# How We Should Build Client Websites: Verified Research and Test Results

*Prepared 2026-10-12 for the student website team. Companion to `business-plan.md` and `website-kit/`.*

## How to read this document

The founder asked for "one hundred percent true, not a guess." Every claim carries one of these labels:

| Label | Meaning |
|---|---|
| **[V]** | **Verified.** I opened the official source and read the text. Link in §7. |
| **[T]** | **Tested.** I ran it in this environment. The command and output are in §6. |
| **[S]** | **Search-reported, NOT opened. Treat as UNVERIFIED.** The vendor's official page was blocked by this environment's network proxy, so the figure comes from a web-search summary of that official page. Someone must open the linked page before relying on it. |
| **[E]** | **Estimate.** My judgment, not measured. |
| **UNVERIFIED** | Not confirmed by any of the above. |

**Network limits:** the proxy blocked almost every vendor website (cloudflare.com, developers.cloudflare.com, netlify.com, vercel.com, web3forms.com, formspree.io, wix.com, squarespace.com, duda.co, webflow.com, framer.com, godaddy.com, wordpress.com, support.google.com, developers.google.com, schema.org and others; full list in §6.10). Workaround:

- **Cloudflare and GitHub facts** come from their official documentation source repos on GitHub (`cloudflare/cloudflare-docs` and `github/docs`). These are the source files that build developers.cloudflare.com and docs.github.com, so they are primary sources.
- **schema.org facts** come from the official `schemaorg/schemaorg` repo (vocabulary release 30.1, dated 2026-09-16).
- **Web3Forms:** one fact comes from Web3Forms' own GitHub repo.
- **Everything else from a vendor website is [S].**

---

## 1. The recommendation (plain language)

**Keep using our own kit, upgrade it, and host every site on Cloudflare's free plan. Do not switch to Wix, Squarespace, Duda, Webflow or WordPress.**

### The exact stack

| Piece | What to use |
|---|---|
| Site code | `website-kit` (plain HTML/CSS plus `build.py`), with the upgrades in §5 |
| Images | A Pillow step inside the build: resize, convert to WebP, strip GPS/EXIF data (prototyped and tested, §6.3) |
| Hosting | Cloudflare Pages, **Direct Upload** with `npx wrangler pages deploy dist/<slug> --project-name <slug>` (command verified against Wrangler 4.149.0 [T]) |
| Who owns the hosting | **Each client gets their own free Cloudflare account**, in their name, holding their domain and their site. Our team is invited as a member (details in §4.1) |
| Domain | Registered in the client's name. Cloudflare Registrar charges registry cost "with no markup" [V] |
| Forms | Web3Forms free plan, with the access key created using the owner's email (kit default). Plan B is a Cloudflare Worker that emails the owner (§4.4) |
| Analytics and report | Cloudflare Web Analytics (free, one-click on Pages [V]) + Google Business Profile Performance + Search Console. Count form submissions as thank-you-page views |
| Google Business Profile | The client is the **owner** and we are the **manager**, as Google's third-party policy recommends [S] |
| Code storage | One private repo in a free GitHub organization (unlimited private repos [V]) |
| Quality check | One command running Lighthouse, axe and html-validate before every launch (prototyped, 67 s for a 5-page site [T]) |

### Why this stack (the key facts)

1. **Fast where it matters.**
   - The build itself takes **0.05 s** [T].
   - With compressed images, client-style pages score **100/100/100/100** in Lighthouse mobile (Performance/Accessibility/Best Practices/SEO), with LCP 1.4–1.7 s [T].
   - With uncompressed phone photos the same page drops to **Performance 76 and LCP 8.4 s** [T]. Image handling is the single biggest quality risk, and the build can fix it automatically.
2. **$0 per client per month for hosting.**
   - Cloudflare says "requests to static assets are free and unlimited" on free and paid plans [V].
   - The client pays only for the domain. The .com registry fee is **$10.26/yr, rising to $10.97 on Nov 1, 2026** [S, Verisign], plus a small ICANN fee (exact amount UNVERIFIED).
   - Builder plans cost the client every month instead: Wix Light $17/mo, Squarespace Basic $19/mo, Duda $17–19/mo per site (all annual billing [S]).
3. **Client sites are allowed on Cloudflare's free tier (with one open item).**
   - I searched all of Cloudflare's docs for "commercial use" and found **zero restrictions** [V].
   - By contrast, GitHub Pages "is not intended for or allowed to be used as a free web-hosting service to run your online business" [V]. Vercel Hobby is "non-commercial personal use only" [S]. Netlify Free pauses **every** site on the account when one exceeds 300 credits/month [S].
   - **Open item:** Cloudflare's binding contract (the Self-Serve Subscription Agreement at cloudflare.com/terms) could not be opened: **UNVERIFIED**. Search reports a clause against renting or selling access to the services to third parties [S]. Having each client hold their own Cloudflare account sidesteps that ambiguity, because the client is the customer.
4. **Clients can always leave with their site.**
   - Our output is plain HTML/CSS files that run on any static host [T].
   - Wix says sites cannot be moved off Wix [S]. Squarespace exports only part of a site as WordPress XML, with no bulk image export [S]. Duda's export needs its Agency plan or higher [S]. Webflow's export needs a paid Workspace and leaves out CMS content [S].
5. **Little maintenance.** A static site has no server, plugins or database to patch [E]. So care-plan time goes to things clients value (menus, hours, photos, Google posts), not upkeep.

**Should we switch to Eleventy or Astro?** Not now.

- I built the same site in both [T]. Eleventy matched our scores and gave multi-page and automatic image optimization almost free.
- But it adds a Node toolchain (Eleventy: 55 MB, 152 packages; Astro: 161 MB, 191 packages, needs Node ≥22.12 [T]) and a full template port.
- Adding service pages, a restaurant menu with menu JSON-LD and pre-launch checks to our Python kit took **~103 added lines** in my prototype [T], and the results were identical.
- Revisit Eleventy if we ever need more than ~5 templates or a blog [E].

**When not to use our kit:** if an owner insists on visually editing the site themselves every week, suggest Squarespace or Wix and charge only for setup [E].

**Before selling anything, do the P0 fixes in §5** (about 1–2 days of work for the technical person [E]). Testing found real problems:

- **A privacy leak:** hidden home addresses still get published, and phone-photo GPS data is copied as-is.
- **An invalid schema.org type** in the example intake.
- **No 404 page,** so Cloudflare serves soft-404s.
- **Builds succeed silently** with placeholder text or missing images still in them.

---

## 2. Comparison of approaches

Cost figures are what the **client** would pay unless noted. Every cell is labeled. "Human build time" is an estimate for all approaches; the only measured times are machine times.

| | **A. Our kit + Cloudflare (recommended)** | **B. Eleventy/Astro + Cloudflare** | **C. WordPress** | **D. Wix** | **E. Squarespace** |
|---|---|---|---|---|---|
| Machine build time | 0.05 s per site [T] | Eleventy 2.0 s cold / 1.0 s warm; Astro 6.5 s / 1.9 s [T] | n/a | n/a | n/a |
| Human build time | Get Found ~5–8 h, Get Calls ~9–15 h total (business plan's estimates) [E] | Same content work, plus a one-time template port [E] | Similar or more (theme/plugin setup) [E] | Similar; less layout code, more manual clicking [E] | Similar [E] |
| Hosting cost per client/month | $0 [V: static requests free and unlimited]; domain ~$10–11/yr [S] | $0 [V] | WordPress.com Business $25/mo annual; plugins on all paid plans from Personal ($2.75/mo on 3-yr) [S]. Self-hosted: UNVERIFIED | Light $17, Core $29, Business $39 per month (annual) [S] | Basic $19, Core $29, Plus $49, Advanced $99 per month (annual, after a July 2026 increase) [S] |
| Free tier allows client/commercial sites? | No restriction found in Cloudflare docs [V]; contract UNVERIFIED | Same as A | WordPress.org software is GPLv2+, free to use [V] | n/a (paid plans) | n/a |
| Non-technical edits | Edit JSON (GitHub web editor), with build checks to catch mistakes [E] | Same | Yes, visual editor [E] | Yes [E] | Yes [E] |
| Speed/SEO measured | 100/100/100/100 mobile with compressed images [T] | Eleventy 100/100/100/100; Astro 100/100/96/100 (96 was my missing favicon) [T] | UNVERIFIED (not measured) | UNVERIFIED | UNVERIFIED |
| Care-plan workload | Low: content edits only, no patching [E] | Low, plus keeping Node dependencies current [E] | Highest: core, theme and plugin updates and security [E] | Low; client can self-edit, which weakens the care-plan value [E] | Low; same [E] |
| Portability | Plain files, any host [T] | Plain files [T] | Built-in export screen [V]; full portability on self-hosted [E] | "Site has to stay on Wix's servers" [S] | Partial WordPress-XML export; images not bulk-exportable [S] |
| Lock-in / price risk | Low. Cloudflare docs say "Start new projects with Workers" [V], and Pages build images auto-migrate (v1→v3 on 2026-09-15, v2→v3 on 2027-02-23) [V]. Our plain files also run on Workers static assets [V] | Low | Medium (host prices UNVERIFIED) | High (no export) [S] | High; prices raised July 2026 [S] |

| | **F. GoDaddy Airo** | **G. Webflow** | **H. Framer** | **I. Durable (AI builder)** | **J. Duda (agency/white-label)** |
|---|---|---|---|---|---|
| Cost per client/month | Starter $9.99/mo; other tiers reported inconsistently [S] | Basic site $15/mo annual ($25 monthly); Premium (CMS) $25/mo annual [S] | Basic $10/mo, Pro $30/mo [S] | Starter $22/mo, Business $85/mo (annual); figures conflict across Durable's pages [S] | Basic $19/mo annual (1 site); extra sites $17/mo annual on Team+; Agency $52/mo includes 4 sites; **white label only on the White Label plan, $149/mo annual** [S] |
| Client/agency use | Paid plans | Paid plans | Free plan can't connect a custom domain [S] | Paid plans | Built for agencies; no site-count limit [S] |
| Portability | UNVERIFIED | Code export needs a paid Workspace (Core $19/mo) and excludes CMS content [S] | UNVERIFIED | UNVERIFIED | Export zip on Agency plan+; store, blog, 404 and dynamic pages excluded; Duda won't support exported sites [S] |
| Lock-in / price risk | UNVERIFIED | Plans and prices changed May 2026 [S] | Plan structure changed recently [S] | Prices inconsistent [S] | June 2024 price increase [S] |
| Speed measured | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED |

**Other static hosts (would only replace Cloudflare in approach A):**

| Host | Client/commercial use on free tier | Risk for an agency |
|---|---|---|
| **GitHub Pages** | **Not allowed** for "your online business" or commercial-transaction sites [V]. Free accounts get Pages only for public repos [V] | Disqualified |
| **Vercel Hobby** | "Non-commercial personal use only," including when a paid consultant writes the code [S] | Disqualified |
| **Netlify Free** | An older blog post says commercial projects are OK; current terms UNVERIFIED [S] | 300 credits/month hard limit; production deploy costs 15 credits; bandwidth 20 credits/GB; **if one site exceeds its limits, all sites on the account are paused** [S] |
| **Cloudflare Workers static assets** | Same company and terms as Pages | Free and unlimited static requests [V]; 100 Workers per free account [V]; custom domains need an active Cloudflare zone you own [V]. A fine future target; our output deploys there unchanged [E] |

**Restaurant-specific alternative:**

- Square's free plan includes a free branded online-ordering page and website builder ($0/mo; online card fee 3.3% + 30¢) [S].
- For Square restaurants, we **link** to that ordering page from our site (as the business plan already says) rather than replacing it.

---

## 3. Step-by-step build workflows

Roles: **S** = Sales lead, **B** = Builder (the technical person), **C** = Content & Ops. Times marked [T] are measured; everything else is [E]. I cannot measure human time from here. The slow parts I identified by testing are noted.

### 3.0 One-time setup (B, about half a day [E])

1. Create a GitHub organization and one **private** repo `sites` holding the kit plus every client's intake file (free orgs get unlimited private repos [V]).
2. Install Python 3 and `pip install pillow` (the only new dependency) plus Node.js for Wrangler and the QA tools.
3. Make the P0 kit fixes in §5.
4. Create the agency's own Cloudflare account (for our own agency site) and a password-manager vault.

### 3.1 Get Found (1-page site)

| # | Step | Who | Time |
|---|---|---|---|
| 1 | Demo homepage from public Google info, built with `--draft` (the prototype's flag that builds even when checks fail) | B | 1–2 h [E] |
| 2 | Pitch and close | S | 1–2 h [E] |
| 3 | Kickoff call (20–30 min) with the owner. Owner creates their free Cloudflare account and invites our email as a member; registers or transfers the domain; creates the Web3Forms key with their email; adds us as **Manager** on their Google Business Profile | S + C | 45 min [E]. **Slow part: waiting on the owner.** Do it live on the call |
| 4 | Fill the intake JSON. Prefer a Google Form that C converts, rather than hand-editing JSON | C | 30–60 min [E]. **Slow part: hand-typing JSON.** One stray comma stopped the current build with a Python traceback [T] |
| 5 | Drop the owner's photos in `clients/assets/<slug>/img/`. The build resizes, converts and strips GPS | C | 15 min plus alt text [E]. Machine: **2.3–3.5 s** for 4–6 phone-size photos [T] |
| 6 | `python3 build.py clients/<slug>.json`. Pre-launch checks must pass | B or C | 0.05 s [T] |
| 7 | Run the QA command (Lighthouse + axe + html-validate), then check on two real phones | C | ~15 s per page automated [T] + 20 min manual [E] |
| 8 | `npx wrangler pages deploy dist/<slug> --project-name <slug> --branch preview` and send the preview link | B | ~2 min [E]; cannot test here (Cloudflare API blocked) |
| 9 | After approval and final payment: deploy to production, add the custom domain in Pages, confirm HTTPS | B | 15–30 min [E]; DNS and certificate time UNVERIFIED |
| 10 | Send a real form submission and confirm the owner received it | C | 5 min [E]. Must be done live; I could not test Web3Forms here |
| 11 | Google Business Profile cleanup, add the website link, submit the sitemap in Search Console | C | 45–60 min [E] |
| 12 | Handoff video and ask for a review and referrals | S | 30 min [E] |

### 3.2 Get Calls (multi-page, one page per service)

Same as 3.1, plus:

- Set `"service_pages": true`. Each service gets `details` (2–4 paragraphs from the owner's facts), optional FAQs and a photo. The prototype generated 4 service pages plus sitemap entries in 0.05 s [T].
- **Slow part: writing real service-page copy** (about 20–30 min per service with AI drafting and human fact-checking [E]). Thin, near-duplicate pages don't help SEO [E].
- QA: every page must have its own title and meta description. The current `page.html` has no meta description, which gave **SEO 92** in my test [T]. Fix #6 in §5.

### 3.3 Menu & Map (restaurant)

Same as 3.1, plus:

- **Menu:** C types the menu into the intake's `menu.sections[].items[]` (name, description, price) from the owner's current menu. **Slow part:** a 60-item menu is roughly 45–90 min of typing and proofreading [E]. My 24-item test menu built in 0.08 s and scored 100/100/100/100 [T]. The generated `Restaurant → hasMenu → MenuSection → MenuItem → Offer` JSON-LD validated against schema.org [T].
- **Ordering:** add `order_links` pointing to the restaurant's existing Square/Toast ordering page. Never build ordering ourselves.
- **Google menu:** C also enters the menu in the Business Profile **menu editor**. It's "for food and drink businesses only," and changes can take 24–48 h to appear [S].
- **Template:** the current template is written for home services ("Get a free quote," "Areas we serve," quote form). On my restaurant test it rendered that wording [T]. A restaurant variant (improvement #10) is required before selling this package.

### 3.4 Monthly care work

| Task | Who | How | Time |
|---|---|---|---|
| Menu/hours/photo edits | C (B until the GitHub Action exists) | Edit JSON → build → QA → deploy | 10–20 min per edit [E] |
| Uptime/form check | C | Visit the site and send a test form | 5 min per site [E] |
| Google posts | C | GBP dashboard as Manager | 10 min per post [E] |
| Monthly report | C | Visits from Cloudflare Web Analytics; calls, website clicks and directions from GBP Performance [S]; searches from Search Console; form submissions from thank-you-page views | 20–30 min per client [E] |

Cloudflare Web Analytics has **no custom events** [V], so it can't count taps on the phone number. Use GBP "Calls" [S] for calls instead.

---

## 4. Accounts and tools: verified limits and terms

### 4.1 Cloudflare (hosting, DNS, domain)

| Fact | Value | Label |
|---|---|---|
| Pages builds (only matters if Cloudflare builds from Git) | 500/month, 1 at a time, 20-min timeout | [V] |
| Custom domains per Pages project (Free) | 100 | [V] |
| Pages projects per account | 100, "not routinely increased" | [V] |
| Files per site / max file size | 20,000 / 25 MiB | [V] |
| Static asset requests | "free and unlimited" on free and paid plans | [V] |
| Dashboard users per Pages site | Unlimited | [V] |
| Preview deployments | Unlimited | [V] |
| Deploy method is permanent | A Direct Upload project "cannot switch to Git integration later," and vice versa | [V] |
| Monorepo limit (Git integration) | Max **5 Pages projects per repository** | [V] |
| Apex domain (example.com) | "must be a zone on the Cloudflare account you have created your Pages project on" (nameservers pointed to Cloudflare) | [V] |
| Subdomain (www) | Can use a CNAME from any DNS host; zone not required | [V] |
| `.html` handling | Pages redirects `/contact.html` → `/contact` | [V] |
| No top-level `404.html` | Pages assumes a single-page app and serves the homepage for unknown paths | [V] |
| Cloudflare's own advice | "Start new projects with Workers" (Pages remains supported) | [V] |
| Pages build image | Python 3.13.3 and Node 22.16.0 by default (v3) | [V] |
| Members | "On any Cloudflare account, you can collaborate by adding members." Managing members requires Super Administrator | [V] |
| Wrangler account targeting | `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` environment variables | [V] |
| Free-plan commercial use | No restriction in docs [V]; contract (cloudflare.com/terms) **UNVERIFIED**. Search reports §2.2 bars renting or selling access to third parties and §2.6 lets Cloudflare end free services at its discretion [S] | — |

**Why each client should have their own Cloudflare account.** These verified rules combine to favor it:

- A Cloudflare Registrar domain must use Cloudflare nameservers assigned to the account that holds it [V].
- An apex domain must be a zone in the same account as the Pages project [V].

So if the client registers their domain at Cloudflare in their own account, their site must live in that same account. That is also the cleanest ownership:

- When a client leaves, we remove our membership and their site keeps running at $0.
- Our account never hits the 100-project or 10-analytics-site limits.

The cost is about 15 minutes per client on the kickoff call [E]. The B deploys with `CLOUDFLARE_ACCOUNT_ID=<client> npx wrangler pages deploy ...`.

**Alternative for owners who won't create an account:** host in our account and connect `www` by CNAME from their existing registrar [V]. Then forward the apex to `www` at their registrar (registrar-dependent, UNVERIFIED).

**Cloudflare Registrar** [V unless noted]:
- Buys and renews "at cost, without markup."
- WHOIS redacted by default.
- Auto-renew on by default.
- Fees are **non-refundable**.
- A transfer in adds one paid year (not for .uk/.nz).
- ICANN 60-day transfer lock after a registrant change (it can be declined).
- No IDNs.
- The current .com price was not shown in any page I could open: **UNVERIFIED**. The registry fee is $10.26, rising to $10.97 on 2026-11-01 [S].

### 4.2 Analytics

| Tool | Free limits and terms | Label |
|---|---|---|
| **Cloudflare Web Analytics** (recommended) | "Free, privacy-first analytics"; one-click on a Pages project; **soft limit of 10 sites per account** (raise via support); unsampled data kept 7 days then aggregated; **no custom events yet** | [V] |
| Umami Cloud Hobby | Free, 100K events/month, **1 website**, 6-month retention | [S] |
| GoatCounter | Free "for reasonable public usage"; small-to-medium business OK | [S] |
| Google Analytics 4 | Not researched. Uses cookies; would need privacy-policy changes | UNVERIFIED |

### 4.3 Google (Business Profile and Search Console)

All [S]: Google's help pages were blocked, so each item needs a check at the linked page.

- **Roles:** owners and managers. Managers "can't add or remove users or remove the profile." Only owners manage users. New users must wait 7 days before some actions (removing owners, transferring primary ownership).
- **Agencies:**
  - Agencies can register an **organization account** in Business Profile Manager (business.google.com/agencysignup, with a company email that doesn't already manage profiles).
  - An organization can't directly own a profile.
  - Google's third-party policy: "make the business owner the owner of the profile, and make yourself the manager."
  - Start with plain Manager access; consider the agency organization after ~10 clients [E].
- **Menus:** a menu editor for food and drink businesses (sections, items, prices); changes take 24–48 h. Photo/PDF menus and menu links are also allowed.
- **Performance metrics:** calls (taps on the call button), website clicks, direction requests, views and search terms. Verified profiles only.
- **Business Profile websites:** existing ones were turned off in March 2024, with redirects ending June 10, 2024. Owners who still think they "have a Google website" don't.
- **Search Console:** owner, full and restricted user roles; up to 100 non-owner users per property. Have the client be a verified owner and us a full user [E].

### 4.4 Forms

| Option | Free limits | Notes | Label |
|---|---|---|---|
| **Web3Forms** (keep) | 250 submissions/month; Pro $12/mo for 10k | Access key "is an alias to your email… safe to disclose"; **domain lock requires Pro** | Key/domain lock [V]; limits [S] |
| | | Free plan: same-domain redirect only (the kit's thank-you redirect is same-domain, so OK); `botcheck` honeypot "deprecated," with free hCaptcha using a shared sitekey; Web3Forms may suspend for abuse and disclaims liability on free use | [S] |
| Formspree | 50/month free, 2 notification emails, 30-day history; Personal $15/mo (200/mo) | Too small for free use | [S] |
| Netlify Forms | Submissions don't use credits | Only works when hosting on Netlify (see the risks above) | [S] |
| **Cloudflare Worker + Email Routing** (plan B) | Sending to **verified destination addresses is free on all plans** and doesn't count toward any quota; 200 destination addresses per account; Workers Free 100,000 requests/day; Turnstile free (20 widgets, unlimited challenges) | Requires the client's domain on Cloudflare and a short Worker (not written or tested here). Email *Sending* to arbitrary recipients is Beta and paid-only | [V] |

Because each client creates their own Web3Forms key, each client gets their own 250/month allowance. A typical small business is unlikely to exceed that [E].

### 4.5 Build and QA tools (all free; versions tested here [T])

- Python 3.13.16 and Pillow 12.3.0 (WebP and AVIF supported).
- Node 22.22.0 and Wrangler 4.149.0.
- Lighthouse 13.5.0, axe-core 4.14.0, html-validate 11.16.2.
- Eleventy 3.1.6 (MIT, Node ≥18) and Astro 7.3.8 (MIT, Node ≥22.12) [T: from installed package.json].

**Not verified:** Bitwarden free plan, Squoosh, WAVE, Google Rich Results Test. Their sites were blocked. The build's image step replaces Squoosh, and axe/Lighthouse cover most WAVE checks [T].

**Optional later:** Pages CMS (MIT) and Decap CMS (MIT) are open-source Git-based editors [V: licenses]. Whether they edit our JSON format is UNVERIFIED.

---

## 5. Prioritized improvements to `website-kit`

"Prototyped" means I built it in a scratchpad copy (the real kit is untouched) and tested it. Line counts come from that prototype (`build2.py`: 288 → 391 lines).

### P0: fix before the first paying client (about 1–2 days total [E])

| # | Change | Why (evidence) | Effort |
|---|---|---|---|
| 1 | **Image step in the build:** resize (hero 1600 + 800 px for mobile, gallery 800 px), convert to WebP, apply phone rotation, **strip EXIF/GPS** | Raw phone-size photos: mobile Performance **76**, LCP **8.4 s**, 5.1 MB on desktop. Compressed: **100**, LCP **1.7 s**. Compression cut 8.8 MB to 0.65 MB [T]. The current kit copies photos byte-for-byte, so **GPS coordinates are published** (a customer's house, for job photos) [T] | Small: 30-line prototype script + Pillow dependency [T] |
| 2 | **Pre-launch checks that stop the build:** leftover EXAMPLE/PLACEHOLDER/REPLACE text, missing image files, missing alt text, invalid `schema_type`, bad hex colors, brand color below 4.5:1 contrast with white button text, reviews without star numbers; plain-English JSON error messages; `--draft` to override for demos | All of these built silently or crashed with a traceback [T]. A common bright green (#4caf50) is only 2.78:1 against white [T] | Small: ~60 lines, prototyped [T] |
| 3 | **Privacy bug: hidden address still in JSON-LD.** With `"show": false`, the street address and ZIP still go into the page's structured data | Confirmed in the built HTML [T] | Tiny: 2 lines, prototyped [T] |
| 4 | **Invalid schema type in the example.** `LandscapingBusiness` is not a schema.org type. Use `HomeAndConstructionBusiness` or `LocalBusiness`. Valid home-service subtypes: Electrician, GeneralContractor, HVACBusiness, HousePainter, Locksmith, MovingCompany, Plumber, RoofingContractor | Checked against schema.org v30.1 [T/V] | Tiny |
| 5 | **Add `404.html`** and use extensionless URLs (`/privacy`, `/thank-you`) in links, sitemap and the form redirect | Without a top-level 404.html, Pages serves the homepage for bad URLs [V]. Pages redirects `.html` → extensionless [V]. Lighthouse flagged the redirect on the privacy page [T] | Small |
| 6 | **Meta description and canonical in `page.html`** (privacy and service pages) | Privacy and service pages score **SEO 92** for a missing meta description [T] | Small |
| 7 | **Navigation only links to sections that exist** | With no reviews, the nav still linked to `#reviews` (dead link) [T] | Small: prototyped [T] |
| 8 | **Accessibility fixes:** add `role="img"` to the star ratings; wrap the sticky mobile call bar in `<nav aria-label="Quick contact">`; hide the honeypot with `display:none` and drop its `autocomplete` attribute | axe: `region` violation on mobile and `aria-prohibited-attr` needs-review ×3; html-validate flagged the honeypot [T] | Small: stars prototyped [T] |

### P1: before selling Get Calls and Menu & Map

| # | Change | Why | Effort |
|---|---|---|---|
| 9 | **Service pages** (`/services/<slug>/`) with `details`, FAQs, photo, CTA and sitemap entries | Required for Get Calls. The prototype generated 4 pages scoring Perf/A11y/BP 100 and SEO 92 [T]. The only failing SEO audit was the missing meta description, so fix #6 should bring it to 100 [E] | Small code (~25 lines prototyped); the copywriting is the real work [E] |
| 10 | **Restaurant template variant:** hero CTAs "Order online / Call / Directions," hours table, Google Maps link (not a heavy embed [E]), menu section, order links, no quote-form wording | The current wording is wrong for restaurants [T]. Menu section and `hasMenu` JSON-LD are already prototyped and validated [T] | Medium: half a day to a day [E] |
| 11 | **Remove `aggregateRating` from the business JSON-LD** (keep the visible text rating) | Google does not show review stars for LocalBusiness/Organization when the business controls the reviews ("self-serving") [S] | Tiny |
| 12 | **Use `openingHoursSpecification`** for hours, with support for closed days and holiday hours | Google lists it as recommended [S]; restaurants change hours often | Small |
| 13 | **One-command QA** (`qa.sh`: html-validate + axe at 390 px and 1280 px + Lighthouse per page) | 67 s for a 5-page site [T]. Replaces manual PageSpeed/WAVE runs | Small: prototyped [T] |

### P2: as the business grows

| # | Change | Why | Effort |
|---|---|---|---|
| 14 | **Deploy script, then a GitHub Action** (build → checks → `wrangler pages deploy`, with preview branches) so C can edit JSON in GitHub's web editor | Removes B as the bottleneck for care-plan edits. Free orgs get 2,000 Actions minutes/month [V] | Medium: 2–4 h [E]; not testable here |
| 15 | **Responsive `srcset`** for gallery images (400/800 px) | Lighthouse still estimated 172 KiB of savings with 1600 px gallery images [T] | Small |
| 16 | **2–3 layout/color variants** and a **Spanish option** (`lang`, translated strings) | Business-plan items; sites shouldn't all look alike | Medium [E] |
| 17 | **Monthly report template** (Cloudflare Web Analytics + GBP Performance + Search Console + thank-you views) | Shows care-plan value | Small [E] |
| 18 | **hCaptcha option for Web3Forms** if spam appears | The honeypot is reported deprecated [S] | Small |

---

## 6. Test results

All tests ran in this cloud container on 2026-10-12 against a **copy** of the kit in my scratchpad. The only command run against the real kit was the build command requested in the task. It rewrote the gitignored `dist/` with byte-identical files (md5 verified); `git status` stayed clean.

### 6.1 Running the existing kit

```
python3 /home/user/all/website-kit/build.py /home/user/all/website-kit/clients/example-landscaping.json
```

- Result: `real 0m0.049s`. Five more runs on the copy: 0.042–0.103 s.
- Output: 10 files, **19,869 bytes total** (index.html 9,619; styles.css 5,817; privacy 1,899; thank-you 1,155; SVGs 211–260 each). Byte-identical to the existing `dist/`.

### 6.2 Lighthouse

Command (mobile; the default form factor uses simulated throttling):

```
CHROME_PATH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
npx lighthouse http://localhost:<port>/ --quiet \
  --chrome-flags="--headless=new --no-sandbox" --output=json --output-path=<file>
```

- Desktop runs add `--preset=desktop`.
- Sites were served with `serve` (gzip on, extensionless URLs like Cloudflare).
- Lighthouse 13.5.0 and Chromium 141.0.7390.37.
- Medians are shown (3 runs where noted).

| Variant | Runs | Perf | A11y | BP | SEO | LCP | Requests | Transfer |
|---|---|---|---|---|---|---|---|---|
| Original kit, placeholder SVG images (mobile) | 3 | 100 | 100 | 100 | 100 | 0.9 s | 4 | 6 KB |
| Original kit, desktop | 1 | 100 | 100 | 100 | 100 | 0.3 s | 7 | 8 KB |
| Original kit, **privacy page** | 1 | 100 | 100 | 100 | **92** | 1.0 s | 5 | 4 KB |
| Kit + **raw phone-size photos** (mobile) | 3 | **76** | 100 | 100 | 100 | **8.4 s** | 5 | 1,463 KB |
| Kit + raw photos (desktop) | 1 | **83** | 100 | 100 | 100 | 3.1 s | 8 | 5,133 KB |
| Kit + WebP 1600 px (mobile) | 3 | 100 | 100 | 100 | 100 | 1.7 s | 5 | 110 KB |
| Kit + WebP, gallery 800 px (desktop) | 1 | 100 | 100 | 100 | 100 | 0.4 s | 8 | 186 KB |
| Kit + WebP + **hero preload + 800 px mobile hero** | 3 | 100 | 100 | 100 | 100 | **1.4 s** | 5 | 47 KB |
| Prototype: plumber home, 4 services, no reviews | 1 | 99 | 100 | 100 | 100 | 2.0 s | 7 | 284 KB |
| Prototype: **service page** | 1 | 100 | 100 | 100 | **92** | 0.9 s | 4 | 4 KB |
| Prototype: **restaurant, 24-item menu** | 2 | 100 | 100 | 100 | 100 | 1.7 s | 5 | 110 KB |
| Eleventy version (raw photos, auto-optimized) | 3 | 100 | 100 | 100 | 100 | 1.4 s | 5 | 57 KB |
| Astro version (raw photos, auto-optimized) | 3 | 100 | 100 | 96* | 100 | 1.6 s | 10 | 144 KB |

\*Astro's 96 came from a missing favicon (404) in my minimal prototype, not from Astro.

The 92s are all "Document does not have a meta description." The privacy page also showed "Avoid multiple page redirects" (`.html` → extensionless).

### 6.3 Images

**Test photos (simulated):** real photos from OpenCV's sample set (`raw.githubusercontent.com/opencv/opencv/4.x/samples/data/*.jpg`), upscaled to 4032×3024, with mild noise added, saved at JPEG quality 92. Sizes were **1.0–2.3 MB** each. These are not real phone photos; real 12 MP phone photos are often larger [E], so the "raw" results above are, if anything, optimistic.

**Prototype optimizer** (Pillow 12.3.0): resize, `ImageOps.exif_transpose`, WebP quality 78, `method=6`.

| Setting | Input | Output | Time |
|---|---|---|---|
| 6 photos at max 1600 px | 8,838,439 bytes | 646,884 bytes (−93%) | 3.5 s |
| 5 gallery photos at max 800 px, q75 | 7,346,467 bytes | 205,156 bytes | 1.8 s |
| Plumber test, 4 photos at max 1600 px | 5,248,960 bytes | 311,876 bytes | 2.3 s |

**GPS test:**
- I created a JPEG with GPS tags (a Utah County lat/long), Make=Apple and rotation=6.
- Current kit: `shutil.copytree` copies the bytes unchanged, so **GPS is published** (`cmp` identical).
- Optimizer output: EXIF `{}`, no GPS, rotation applied (512×384 → 384×512).

### 6.4 Accessibility (axe-core 4.14.0 via Playwright, WCAG 2.0/2.1/2.2 A/AA + best-practice, at 390 px and 1280 px)

- **Original home page:**
  - 1 violation at 390 px: `region` (moderate), "All page content should be contained by landmarks" on `.mobile-cta`.
  - Needs-review: `aria-prohibited-attr` ×3 (`aria-label` on star `div`s with no role) and `color-contrast` ×9 (text over the hero gradient, which axe can't compute; check manually).
- **Privacy and thank-you pages:** 0 violations.
- **Prototype service page:** 0 violations. **Restaurant page:** same `region` item only.

**Contrast (computed with the WCAG formula):**
- Kit defaults pass: white on brand #2f6b3a is 6.39:1; muted text on white is 6.55:1.
- Star color #c98a00 on white is 2.95:1 (decorative; it has a text label).
- A client brand of #4caf50 would give **2.78:1 (fails)**; #f39c12 gives 2.19:1 (fails).

### 6.5 HTML validation (html-validate 11.16.2, recommended preset)

31 messages on the original 3 pages:

- 19 `tel-non-breaking` (style)
- 3 `doctype-style`
- 3 `no-trailing-whitespace`
- 3 `aria-label-misuse` (stars; same as axe)
- 1 `input-attributes` + 1 `valid-autocomplete` (honeypot checkbox)
- 1 `no-implicit-input-type`

None break the page.

### 6.6 Structured data (checked against schema.org vocabulary 30.1 from `schemaorg/schemaorg`)

- Original example: **`unknown type LandscapingBusiness`**.
- Prototype plumber (`Plumber`) and restaurant (`Restaurant` + `servesCuisine` + `hasMenu` → `Menu` → `MenuSection` → `MenuItem` → `Offer`): "all types/properties valid."
- `Restaurant.menu` is superseded by `hasMenu` in schema.org [V].
- Google's Rich Results Test could not be run (site blocked): **UNVERIFIED** for Google eligibility.

### 6.7 Failure-mode tests on the current `build.py`

| Input problem | Current result | Prototype result |
|---|---|---|
| Extra comma in JSON | Python traceback (`JSONDecodeError`) | "The intake file has a typo on line 11, column 19… Usually a missing or extra comma or quote." |
| Leftover EXAMPLE/PLACEHOLDER/REPLACE-WITH | Builds; 5 occurrences in the page | Blocked (unless `--draft`) |
| Gallery image file missing | Builds (broken image) | Blocked |
| Gallery item without `alt` | `KeyError: 'alt'` traceback | Blocked with a message |
| `schema_type: "PlumbingCompany"` | Builds | Blocked |
| Brand color #4caf50 | Builds (fails contrast) | Blocked: "2.78:1… needs 4.5:1" |
| Brand color `#1d4f9` (5 digits) | Builds with a wrong color | Blocked |
| Review without `stars` | Builds, defaults to 5 stars | Blocked |
| `address.show: false` | Street and ZIP still in JSON-LD | Omitted |
| No reviews | Nav still links `#reviews` | Link omitted |

### 6.8 Alternative prototypes (same intake JSON, same CSS)

| | Our kit (prototype) | Eleventy 3.1.6 | Astro 7.3.8 |
|---|---|---|---|
| Install | None (stdlib) + Pillow (venv 34 MB) | `npm install` 6.8 s, 152 packages, 55 MB | `npm install` 21.6 s, 191 packages, 161 MB; Node ≥22.12 |
| Build | 0.05 s | 2.0 s cold, 1.0 s warm | 6.5 s cold, 1.9 s warm |
| Pages built | home + 4 service + privacy + thank-you | home + 6 service + privacy + thank-you + sitemap | home + 6 service |
| Service pages | ~25 lines of Python | ~12 lines of front matter (pagination) | `getStaticPaths` (~3 lines) |
| Image optimization | Separate Pillow step | Automatic for `<img>` (WebP + JPEG, 400/800/1600 srcset) | Automatic for `<Image>` |
| Gotcha found | — | CSS-background hero images are **not** processed (the hero went missing until I switched to `<img>`) | — |
| Escaping | `html.escape` | Autoescape on (`<script>` became `&lt;script&gt;`) [T] | Escaped [T] |
| Output JS | 0 | 0 | 0 script files (JSON-LD only) |

My own port took minutes as an AI agent. That is **not** representative of a student, so I don't report it as a human time.

### 6.9 New-client timing

- **Plumber:** writing a full intake JSON, compressing 4 photos and building took **2.4 s of machine time**. My authoring time as an AI is not a fair proxy for a human [T].
- **Restaurant:** generating a 24-item menu intake and building took 0.08 s.
- **What is slow for humans** (from the failure tests and workflow, [E]):
  1. Hand-editing JSON (one typo stops the build)
  2. Collecting, compressing and alt-texting photos
  3. Writing and fact-checking copy, especially service pages and menus
  4. Waiting on the owner for domain, Cloudflare, Web3Forms and GBP access
  5. DNS/HTTPS activation and Google verification delays (UNVERIFIED durations)

### 6.10 What failed or could not be tested

- **Blocked sites:** the proxy returned 403 for cloudflare.com, developers.cloudflare.com, netlify.com, docs.netlify.com, vercel.com, web3forms.com, formspree.io, wix.com, squarespace.com, duda.co, webflow.com, framer.com, durable.com, godaddy.com, wordpress.com/.org, support.google.com, developers.google.com, search.google.com, schema.org, w3.org, wave.webaim.org, pagespeed.web.dev, web.archive.org, verisign.com, squareup.com, pagescms.org, goatcounter.com, umami.is, plausible.io, 11ty.dev, docs.astro.build, unpkg.com and cdn.jsdelivr.net. WebFetch failed with DNS errors on the same hosts.
- **PageSpeed Insights API:** returned 429 (daily quota exhausted for the unkeyed API), so no builder or real-world site measurements.
- **Not tested:** real Cloudflare deploys (no account; no signing up per instructions), Web3Forms delivery, Google Rich Results Test, real phone photos, real devices, Cloudflare's actual .com price, and every builder platform's speed.
- **Self-inflicted:** a `pkill -f "serve -l"` matched my own shell and killed one batch. Re-run successfully.

---

## 7. Sources

### Official sources opened

**Cloudflare docs source** (repo `cloudflare/cloudflare-docs`, branch `production`; the published page is the same path under https://developers.cloudflare.com/):

- `src/content/docs/pages/platform/limits.mdx` (Pages limits)
- `src/content/docs/pages/index.mdx` + `src/content/partials/pages/workers-for-new-projects.mdx` ("Start new projects with Workers")
- `src/content/docs/pages/configuration/build-image.mdx` + `src/content/pages-build-environment/v3.yaml` (Python 3.13.3, deprecation dates)
- `src/content/docs/pages/configuration/custom-domains.mdx`
- `src/content/docs/pages/configuration/git-integration/index.mdx`
- `src/content/docs/pages/get-started/direct-upload.mdx`
- `src/content/docs/pages/configuration/monorepos.mdx`
- `src/content/docs/pages/configuration/build-watch-paths.mdx`
- `src/content/docs/pages/configuration/serving-pages.mdx` (`.html` redirects, 404/SPA behavior)
- `src/content/docs/pages/functions/pricing.mdx`
- `src/content/docs/pages/how-to/web-analytics.mdx`
- `src/content/docs/pages/framework-guides/deploy-an-mkdocs-site.mdx`
- `src/content/docs/workers/static-assets/billing-and-limitations.mdx`
- `src/content/docs/workers/platform/limits.mdx`
- `src/content/docs/workers/configuration/routing/custom-domains.mdx`
- `src/content/docs/workers/wrangler/system-environment-variables.mdx`
- `src/content/docs/registrar/index.mdx`
- `src/content/docs/registrar/faq.mdx`
- `src/content/docs/registrar/get-started/register-domain.mdx`
- `src/content/docs/registrar/top-level-domains/index.mdx`
- `src/content/docs/web-analytics/index.mdx`, `about.mdx`, `faq.mdx` + `src/content/partials/web-analytics/web-analytics-definition.mdx`
- `src/content/docs/turnstile/plans.mdx`
- `src/content/docs/email-service/index.mdx`, `platform/pricing.mdx`, `platform/limits.mdx`
- `src/content/docs/fundamentals/manage-members/index.mdx`, `manage.mdx`, `roles.mdx` + `src/content/partials/fundamentals/account-member-manage-limitation.mdx`
- GitHub code search of the whole repo for "commercial use": 0 results

**GitHub docs source** (repo `github/docs`, branch `main`; published at https://docs.github.com/):

- `content/pages/getting-started-with-github-pages/github-pages-limits.md`
- `content/get-started/learning-about-github/githubs-plans.md`

**Other repositories:**

- schema.org: https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/30.1/schemaorg-current-https.jsonld and `versions.json`
- Web3Forms (official org): https://raw.githubusercontent.com/web3forms/web3forms-react/master/README.md
- WordPress: https://raw.githubusercontent.com/WordPress/wordpress-develop/trunk/src/license.txt and `src/wp-admin/export.php`
- Pages CMS: https://raw.githubusercontent.com/pages-cms/pages-cms/main/README.md and `LICENSE`
- Decap CMS: https://raw.githubusercontent.com/decaporg/decap-cms/main/README.md and `LICENSE`

**npm registry (package metadata, installed and run):** lighthouse 13.5.0, axe-core 4.14.0, html-validate 11.16.2, @11ty/eleventy 3.1.6, @11ty/eleventy-img 7.0.0, astro 7.3.8, wrangler 4.149.0. PyPI: Pillow 12.3.0.

### Official pages NOT opened (blocked); search-reported only, all [S]

**Must open before relying on these figures.**

**Hosting and forms**
- Cloudflare: https://www.cloudflare.com/terms/, https://www.cloudflare.com/products/registrar/
- Vercel: https://vercel.com/docs/limits/fair-use-guidelines, https://vercel.com/docs/plans/hobby
- Netlify: https://www.netlify.com/pricing/, https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/, https://docs.netlify.com/manage/accounts-and-billing/billing/resume-paused-projects/
- Web3Forms: https://web3forms.com/pricing, https://web3forms.com/terms, https://docs.web3forms.com/getting-started/customizations/redirection, https://docs.web3forms.com/getting-started/customizations/spam-protection/spam-protection
- Formspree: https://formspree.io/plans, https://help.formspree.io/hc/en-us/articles/47605896654227-Account-limits

**Website builders**
- Wix: https://www.wix.com/plans, https://support.wix.com/en/article/exporting-or-embedding-your-wix-site-elsewhere
- Squarespace: https://www.squarespace.com/pricing, https://support.squarespace.com/hc/en-us/articles/206566687-Exporting-your-site
- Duda: https://www.duda.co/pricing, https://support.duda.co/hc/en-us/articles/26519246857495-Site-Export
- Webflow: https://webflow.com/pricing, https://help.webflow.com/hc/en-us/articles/33961386739347-How-do-I-export-my-Webflow-site-code, https://help.webflow.com/hc/en-us/articles/51059955082387-Updated-pricing-and-simplified-plans-for-May-2026
- Framer: https://www.framer.com/pricing
- Durable: https://durable.com/pricing
- GoDaddy: https://www.godaddy.com/airo
- WordPress.com: https://wordpress.com/pricing/
- Square: https://squareup.com/us/en/online-ordering

**Domains and analytics**
- Verisign: https://investor.verisign.com/news-releases/news-release-details/verisign-reports-first-quarter-2026-results
- Umami: https://umami.is/pricing
- GoatCounter: https://www.goatcounter.com/why, https://goatcounter.com/terms

**Google Business Profile, Search Console and structured data**
- Owners and managers: https://support.google.com/business/answer/3403100
- Agency organizations: https://support.google.com/business/answer/7663063
- Third-party policies: https://support.google.com/business/answer/7353941
- Menu editor: https://support.google.com/business/answer/9455840
- Performance metrics: https://support.google.com/business/answer/9918094
- Business Profile websites shutdown: https://support.google.com/business/answer/14368911
- Search Console users and permissions: https://support.google.com/webmasters/answer/7687615
- LocalBusiness structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Review snippets: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
