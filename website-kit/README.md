# Website Kit: What You Need to Build Client Sites (and Do Them Right)

This folder is two things:
1. **The checklist** of people, skills, accounts and standards you need (sections 1–5).
2. **A working starter kit**: a template plus a build script that turns one client's intake file into a finished, fast, mobile-friendly site (sections 6–8). It's built and tested; open `dist/example-landscaping/index.html` after running the build to see the example.

---

## 1. People and skills

You don't need computer science degrees. You need these skills covered across the three of you:

| Skill | Why it matters | How good you need to be | Free way to learn |
|---|---|---|---|
| **Sales and client communication** | No clients, no business | Comfortable calling owners and running a 20-min intake call | You already have this |
| **Reading HTML/CSS** | AI writes the code, but someone must spot when it's wrong | Can read a page's code and change text, colors, images, sections | MDN Web Docs "Learn web development" (developer.mozilla.org) |
| **Directing an AI coding tool** | This is how you build fast | Can describe changes clearly and check the result | Practice on the example site in this kit |
| **Domains and DNS** | Every launch requires connecting a domain | Can add a custom domain in Cloudflare and fix common errors | Cloudflare's docs on custom domains for Pages |
| **Google Business Profile** | Often brings more calls than the site itself | Can set up and fill out a profile completely | Google Business Profile Help Center |
| **Copy editing** | AI copy is generic and sometimes wrong | Can turn the owner's facts into short, clear text | Practice; read your competitors' best sites |
| **Quality checking** | Mistakes on a client's site cost you referrals | Follows the QA checklist every time, no exceptions | The checklist in section 5 |

**Hardware:** Any laptop, plus a phone to test on. Ideally one iPhone and one Android across the team.

---

## 2. Accounts to set up once (all free)

| Account | Purpose | Notes |
|---|---|---|
| Business Gmail or Google Workspace | One shared business email for the team | Use a free Gmail at first; Workspace later with your own domain |
| **Password manager** (e.g., Bitwarden free) | Store client logins safely and share them within the team | **Required.** Never keep client passwords in texts, docs or spreadsheets |
| GitHub organization | Store every client's site code; acts as your backup | One repo per client |
| Cloudflare account | Free hosting (Cloudflare Pages) and DNS | Use the free plan. Don't use Vercel's free Hobby plan for client sites; Vercel says paid client work is commercial use |
| AI coding tool | Build and edit sites | Whatever you already use |
| Google Drive folder | Client photos, intake answers, contracts | One folder per client |
| Stripe, Square or PayPal | Send invoices | No monthly fee; card fees only |
| Google Search Console | Tell Google about each new site | Add each client site after launch |

---

## 3. What you need from each client before building

Collect this with a Google Form, then a 20-minute call:

- [ ] Business name exactly as on their Google profile, plus the legal name (LLC) for the footer
- [ ] Phone, email for quote requests, hours, address, and whether to show it (many home-service businesses don't)
- [ ] Services list, and the 3 that make them the most money
- [ ] Service area (cities)
- [ ] Logo (any format; you can clean it up)
- [ ] 10–20 photos of real jobs (phone photos are fine)
- [ ] License number and insurance status, **only if they confirm it**
- [ ] 3–5 Google reviews they're happy to feature, plus their current rating and review count
- [ ] Their Google Business Profile, Facebook and Yelp links
- [ ] **Domain registered in their own name** with access shared with you (or they already own one)
- [ ] A Web3Forms access key created with **the email that should receive quote requests** (takes 1 minute at web3forms.com)

---

## 4. Tools (all free to start)

| Need | Use | Why |
|---|---|---|
| Site code | This kit (plain HTML + CSS, no framework) | Fast, simple, nothing to update or patch, hosts free anywhere |
| Hosting | Cloudflare Pages | Free plan includes custom domains and HTTPS |
| Forms | Web3Forms (free: 250 submissions/month) | No server needed; submissions go to the owner's email |
| Photos | The client's own photos; free-license stock only as a last resort | Never take images from Google search or other businesses' sites |
| Image compression | Squoosh (squoosh.app, free) | Shrink photos to under ~200 KB each, ideally WebP |
| Speed and quality check | Google PageSpeed Insights / Lighthouse | Aim for 90+ on mobile |
| Accessibility check | WAVE (wave.webaim.org) or Lighthouse, plus keyboard-only testing | Catch missing labels, low contrast, missing alt text |
| Structured data check | Google Rich Results Test | Confirms the business info markup is valid |

---

## 5. "Done right": the standard every site must meet

These are the things that separate a $1,200 site from a $300 Fiverr site.

**Converts visitors to calls**
- [ ] Phone number is click-to-call in the header, the hero, and a sticky bar on phones
- [ ] Quote form is short (name, phone, service, details), works, and sends to the owner
- [ ] The main service and city are in the headline, e.g., "Landscaping in Orem, UT"
- [ ] Real reviews and real job photos are on the homepage

**Fast**
- [ ] PageSpeed mobile score 90+
- [ ] Every image compressed; gallery images lazy-loaded (the kit does this)
- [ ] No heavy page builders, sliders or video backgrounds

**Found on Google (local SEO basics)**
- [ ] Unique page title and meta description (the kit generates them)
- [ ] LocalBusiness structured data (the kit generates it; check with Google's Rich Results Test)
- [ ] **Business name, address and phone identical** on the site, Google Business Profile, Facebook and Yelp
- [ ] Sitemap submitted in Google Search Console (the kit generates `sitemap.xml`)
- [ ] Google Business Profile complete: categories, services, hours, photos, website link
- [ ] For the Standard package: one page per main service (see "Kit limits" below)

**Accessible** (also lowers legal risk)
- [ ] Every image has meaningful alt text
- [ ] Text has readable contrast; nothing relies on color alone
- [ ] Every form field has a label; the whole site works with keyboard only
- [ ] Headings are in order (H1 → H2 → H3)

**Honest and legal**
- [ ] Every fact (license, insurance, years in business, prices) confirmed by the owner in writing
- [ ] Reviews are real, copied word for word, with permission. The FTC's rule against fake reviews applies to businesses and the people who write reviews for them
- [ ] No "best in Utah" or similar claims the owner can't back up
- [ ] Privacy policy page (the kit includes a plain-language starting point; **have an attorney review it once**)
- [ ] Only images the client owns or licensed

**Owned by the client**
- [ ] Domain, Google Business Profile and form email are in the client's name
- [ ] Code backed up in your GitHub
- [ ] Handoff: a short screen-recorded walkthrough and a one-page "who to call for changes" note

---

## 6. How to use the kit

### Folder layout
```
website-kit/
├── build.py                      # builds a site from an intake file
├── template/
│   ├── index.html                # home page layout
│   ├── page.html                 # layout for privacy / thank-you pages
│   └── styles.css                # all styling (brand colors are set per client)
├── clients/
│   ├── example-landscaping.json  # sample intake file (placeholder content)
│   └── assets/example-landscaping/img/   # that client's logo and photos
└── dist/                         # built sites appear here (not committed)
```

### Build a new client site (about 15 minutes once you have their content)
1. Copy `clients/example-landscaping.json` to `clients/<client-slug>.json` and replace **every** value with the client's confirmed info. Search the file for `EXAMPLE` and `PLACEHOLDER`; none may remain.
2. Put their logo and compressed photos in `clients/assets/<client-slug>/img/` and update the `gallery` paths and alt text.
3. Build:
   ```
   python3 build.py clients/<client-slug>.json
   ```
   This creates `dist/<client-slug>/` with the home page, privacy page, thank-you page, `robots.txt` and `sitemap.xml`. Only Python 3 is needed; no installs.
4. Preview locally:
   ```
   cd dist/<client-slug> && python3 -m http.server 8000
   ```
   Then open http://localhost:8000 on your computer. To test on your phone, use the deploy preview link from step 5.
5. **Deploy to Cloudflare Pages:** in the Cloudflare dashboard, go to Workers & Pages → Create → Pages → upload the `dist/<client-slug>` folder. Or from the command line: `npx wrangler pages deploy dist/<client-slug> --project-name <client-slug>`. You get a free `*.pages.dev` preview link to send the client.
6. After approval, connect their domain in the Pages project's **Custom domains** settings, then confirm HTTPS works.
7. Send a real test quote request and confirm the owner receives it.
8. Run section 5's checklist. Then submit the sitemap in Google Search Console and add the site link to their Google Business Profile.

### Making changes beyond the template
Use your AI coding tool on the template or a client's built files. Example request:
> In website-kit/template/index.html and styles.css, add an optional "Service plans" section with 3 pricing cards that only renders if the intake JSON has a "plans" list. Update build.py to render it, keep everything escaped, and don't change any other sections.

Then rebuild the example and check it on a phone and a desktop before using it for a client.

---

## 7. What the kit already does for you

- Mobile-first layout with a sticky call/quote bar on phones and click-to-call everywhere
- Quote form wired to Web3Forms, with spam protection and a thank-you page
- LocalBusiness structured data, page title, meta description, social preview tags, `robots.txt`, `sitemap.xml`
- Accessibility basics: skip link, labeled form fields, alt text, visible keyboard focus, reduced-motion support
- Brand colors set per client from the intake file
- **Only shows a star rating if you enter real rating numbers.** The example leaves them blank on purpose
- All client text is escaped, so a typo or symbol in the intake can't break the page

## 8. Kit limits (what to add as you grow)

- **One home page plus privacy/thank-you pages.** The Standard package needs a page per main service. That's the next thing to add to `build.py`.
- **Photos aren't compressed automatically.** Run them through Squoosh first.
- **No booking or text alerts yet.** For Growth clients, embed a booking tool (e.g., Calendly) and set up automations separately.
- **The privacy policy is a plain-language starting point, not legal advice.** Get it reviewed once by an attorney.
- **The template looks the same for every client** except colors, logo and photos. Make one variant per niche as you learn what converts.
