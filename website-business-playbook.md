# AI-Built Websites for Local Businesses: The Full Playbook

*Prepared October 2026. Market figures are cited. Anything marked **(est.)** is my estimate. Assumes a team of 3 students working ~10 hrs/week each and $0 starting money.*

---

## 1. Reality check first

- **Most small businesses already have a website.** A 2025 Clutch survey found **83% do** (up from 64% in 2018), so only ~17% are offline ([Clutch via Business Wire](https://www.businesswire.com/news/home/20250821848152/en/Clutch-Report-No-Code-Tools-Fuel-Website-Growth-Yet-17-of-Small-Businesses-are-Still-Offline)). Your market is mostly businesses with **bad** websites: slow, not mobile-friendly, no way to request a quote, outdated.
- **You're competing with Wix/Squarespace DIY and $300 Fiverr sites.** Budget freelancers charge $299–$499, mid-level $1,999–$2,999, typical freelancer range $1,500–$5,000 ([Seahawk Media](https://seahawkmedia.com/tech/small-business-website-costs/), [WebsiteSetup](https://websitesetup.org/website-cost/)).
- **So don't sell "a website." Sell more phone calls and quote requests,** done for them, fast, by local people they can call. Owners don't care about code; they care about jobs booked.
- **Your edge:** AI lets you build a quality site in hours instead of weeks, so you can **build the demo before you pitch**. That's the single biggest sales advantage you have over other freelancers.

---

## 2. The offer and pricing

### Packages

| Package | What's included | Price | Your time (est.) |
|---|---|---|---|
| **Starter** | 1-page mobile site: services, reviews, service area, click-to-call, quote request form, Google Business Profile tune-up | **$500 setup** | 4–6 hrs |
| **Standard** (push this one) | 4–6 pages (home, services, about, gallery, reviews, contact), quote form, basic local SEO, Google Business Profile setup/optimization, analytics | **$1,200–$1,500 setup** | 8–12 hrs |
| **Growth** | Standard + online booking or an automation (e.g., form submission → text/email to the owner + auto-reply to the customer), review-request page | **$2,000–$2,500 setup** | 12–20 hrs |
| **Care plan** (recurring) | Hosting management, small text/photo edits (up to ~1 hr/mo), monthly check that forms work, quarterly update report | **$75–$150/mo** | ~1 hr/mo |

Market check on care plans: small-business site maintenance typically runs **$50–$500/mo**; one vendor's tiers are $49/$99/$299 ([Ueni citing GoDaddy](https://ueni.com/blog/website-maintenance-cost/), [Seahawk Media](https://seahawkmedia.com/wordpress/wordpress-maintenance-packages/)).

### Alternative model: no upfront fee
**$0 down, $129–$179/mo with a 12-month minimum** (est.). Easier to sell to cash-tight owners, and it builds recurring revenue faster. The risk: you carry the build cost if they cancel, so require the 12-month term in writing.

**Recommendation:** Lead with **Standard at $1,200 + $99/mo care plan**. Your first 2–3 clients get a "founding client" price of **$500 + $99/mo** in exchange for a testimonial and a referral.

---

## 3. Pick a niche (this matters more than design)

**Start with Utah County / Salt Lake County home-service businesses:** landscaping, HVAC, roofing, plumbing, house cleaning, auto detailing, junk removal, pest control, concrete.

Why:
- **High job value.** One new HVAC or roofing job can pay for the whole site, so the ROI pitch is easy.
- **Customers find them on Google Maps** ("landscaper near me"), so a good site plus Google Business Profile directly brings in calls.
- **Owners are in trucks all day.** They don't have time to DIY Wix, and they answer their phones (good for cold calling).
- **Reusable work.** One template per niche gets reused for every client in it; your 5th landscaper site takes half the time of your 1st.

**Avoid at first:** restaurants (low budgets, menus change constantly), e-commerce stores (complex, payments, inventory), law and medical firms (regulated advertising, privacy rules).

---

## 4. Tech stack: everything free to start

| Need | Tool | Cost | Notes |
|---|---|---|---|
| Build the site | AI coding tool (Claude Code / Cursor, which you already use) + plain HTML/CSS (Tailwind) or Astro | $0 beyond what you already have | Static sites are fast, secure and nearly free to host. Avoid WordPress at first; it means updates, plugins and security patches. |
| Code storage | GitHub (free) | $0 | One repo per client. |
| Hosting | **Cloudflare Pages** (free plan) | $0 | Free plan allows 500 builds/month and 100 custom domains per project ([Cloudflare docs](https://developers.cloudflare.com/pages/platform/limits)). I didn't find a commercial-use restriction for it, but confirm Cloudflare's terms. **Don't use Vercel's free Hobby plan:** Vercel says commercial use, including being paid to build the site, requires a paid plan ([Vercel fair use](https://vercel.com/docs/limits/fair-use-guidelines)). |
| Contact/quote forms | **Web3Forms** (free: 250 submissions/mo) or Formspree (free: 50/mo) | $0 | ([Web3Forms pricing](https://web3forms.com/pricing), [Formspree limits](https://splitforms.com/formspree-free-plan-limits)) |
| Booking | Calendly free tier or Google Calendar appointment schedules | $0 | Only for businesses that book appointments (detailing, cleaning). |
| Domain | Client buys it **in their own name** (Cloudflare Registrar, Namecheap, etc.) | Client pays, ~$10–$20/yr (est.) | Never register it under your name. It causes trust problems and disputes. |
| Photos | The client's own job photos (best), or free-license stock (Unsplash, Pexels) | $0 | Never take images from Google or competitors' sites. |
| Analytics | Cloudflare Web Analytics or Google Analytics | $0 | Show the owner how many visitors and form submissions they get each month. |
| Google Business Profile | Google (free) | $0 | Often brings in more calls than the website itself. |
| Invoicing | Stripe, Square or PayPal invoices | Card fees only, roughly 3% per payment (est.; check current rates) | No monthly fee. |
| Contract | Free template, edited once (see section 8) | $0 | |

**Total startup cost: $0.** You only pay transaction fees once a client pays.

**Rule:** The client owns the domain, Google Business Profile, and analytics. You get *access* to them. This builds trust and avoids disputes if they ever leave.

---

## 5. How a site gets built (step by step)

### One-time setup (do this before the first client, ~10–15 hours)
1. **Build one master template for your niche** with your AI coding tool: hero section with click-to-call, services grid, reviews, service-area map, gallery, quote form, footer with hours and address. Make it fast, mobile-first and accessible.
2. **Write a QA checklist** (below).
3. **Make an intake form** (Google Form) collecting: business name, services, service area, hours, phone, email, logo, 10–20 job photos, licenses/insurance info, top 3 reasons customers pick them, links to their Google/Facebook/Yelp.

### Per client (~8–12 hours for the Standard package)

| Step | Who | Time (est.) | What happens |
|---|---|---|---|
| 1. Intake | Seller | 30 min | 20-minute call plus the intake form. Get the domain registered in *their* name and invite you. |
| 2. Content | Content person + AI | 1–2 hrs | Pull their real Google reviews (with permission), services and photos. AI drafts the page copy from *their* facts. A human rewrites anything generic and removes anything made up. |
| 3. Build | Builder + AI coding tool | 3–5 hrs | Copy the niche template, swap in content, colors, logo and photos. Add the form and click-to-call. |
| 4. Local SEO basics | Builder | 1 hr | Page titles like "Landscaping in Orem, UT \| Company Name," meta descriptions, LocalBusiness schema markup, consistent business name/address/phone everywhere, a page for each main service. |
| 5. QA | QA person | 1 hr | Run the checklist below. |
| 6. Client review | Seller | 30 min | Send a preview link. **2 rounds of revisions** are included; more is paid. |
| 7. Launch | Builder | 30 min | Connect the domain to Cloudflare Pages, check HTTPS, send a test form submission to the owner's phone/email. |
| 8. Google Business Profile | Content person | 1 hr | Add the website link, services, photos, hours, service area. Make sure the business info matches the site exactly. |
| 9. Handoff | Seller | 15 min | Short video walkthrough. Pitch the care plan. Ask for a review and a referral. |

### QA checklist (nothing launches without passing all of it)
- [ ] Looks right on an iPhone, an Android phone and a desktop.
- [ ] Phone number is click-to-call and correct.
- [ ] Form actually delivers to the owner (send a real test).
- [ ] Every fact (licenses, years in business, service area, prices) was confirmed by the owner. **No AI-invented claims.**
- [ ] Reviews are real and attributed; nothing made up.
- [ ] All images are the client's own or free-license.
- [ ] Loads fast (check with Google PageSpeed Insights; aim for 90+ on mobile).
- [ ] Basic accessibility: alt text on images, readable contrast, headings in order, form labels.
- [ ] Privacy policy page if the site collects form data.
- [ ] Spelling, links and the copyright year are all correct.

### Example prompt for the AI coding tool
> Build a fast, mobile-first, single-page static website using HTML and Tailwind CSS for a landscaping company. Sections: hero with headline, subheadline, and a large click-to-call button and "Get a free quote" button; services grid (6 services with short descriptions); "Why choose us" with 3 points; reviews (3 real reviews I'll provide); service area list of Utah County cities; photo gallery (12 images, lazy-loaded); quote form posting to Web3Forms with name, phone, email, service, message; footer with hours, address and phone. Include LocalBusiness JSON-LD schema, proper meta tags, accessible labels and alt text. Use only the content I provide; do not invent facts, reviews, or credentials. Content: {paste intake answers}

---

## 6. How to get clients

### Build the prospect list (2–3 hours)
1. Search Google Maps for "landscaping Orem UT," "HVAC Provo," and so on.
2. In a spreadsheet, log every business with **no website**, a **broken or non-mobile site**, or a site that's just a Facebook page. Track: name, phone, owner name if listed, current site, review count and rating, and notes.
3. **Prioritize businesses with 20+ good reviews but a bad or missing website.** They're clearly busy and successful, so they can afford you, and the gap is obvious.

### "Build first, then pitch"
For your top 10 prospects, **build a free demo homepage** using their real name, services and reviews (1–2 hours each with your template). Host it on a free preview link. Then call:

**Cold-call script**
> "Hi, is this {owner}? This is Parker. I'm a local student in Orem and I build websites for home-service companies. I noticed you have {47} great reviews on Google but {no website / your site doesn't load well on phones}, and I actually already built you a sample homepage. Can I text you the link? It takes 30 seconds to look at."
>
> *(If yes, text it, then:)* "If you like it, I'll finish it, put it on your own domain, and connect it to your Google profile so calls and quote requests come straight to your phone. It's normally $1,200; for my first few clients it's $500, plus $99 a month if you want me to handle updates. Want to hop on a 10-minute call this week?"

**Follow-up text or email (if no answer)**
> Hi {owner}, Parker here, the student who builds websites for local {landscapers}. I made you a free sample homepage using your real reviews: {link}. If you like it, I can have it live on your own domain within a week. No pressure; happy to answer questions. {phone}

**Walk-ins work too** for shops with storefronts (detailers, auto repair). Show the demo on your phone.

### Common objections

| They say | You say |
|---|---|
| "I get enough work from word of mouth." | "That's great. This just makes sure the people who hear about you and Google you can call you in one tap instead of finding a competitor." |
| "My nephew is going to build one." | "Totally fair. If it doesn't happen in a month, the demo is still here." |
| "That's too expensive." | "One extra job pays for it. Or there's $0 down at $149/month." |
| "I already have a Facebook page." | "Keep it. Google sends people to websites and Google profiles more than Facebook, and this connects them." |

### Other channels
- **Referrals:** Give $100 or a free month of care for each referral that signs (est. budget, paid from their fee).
- **Partners:** Business coaches, accountants, sign/vehicle-wrap shops, and supply stores all talk to new businesses; offer them a referral fee.
- **New business filings:** Newly registered Utah businesses need websites; their contact info is public in the state business registry.

---

## 7. Team roles (3 people)

| Role | Owner | What they do |
|---|---|---|
| **Sales and client contact** | You (SDR experience) | Prospect lists, calls, demos, closing, invoices, client communication |
| **Builder** | The friend most comfortable with code | Templates, builds, launches, technical fixes |
| **Content and QA** | The detail-oriented friend | Intake, copy editing, Google Business Profile, QA checklist, monthly care-plan checks |

Everyone can use AI coding tools, so the roles can blur. But **one person owns each client** so nothing falls through the cracks. Use a shared Google Sheet or a free Trello/Notion board: Prospect → Demo sent → Call booked → Signed → Building → QA → Live → Care plan.

---

## 8. Business basics

- **Contract (1–2 pages)** covering: scope and number of pages, **2 revision rounds**, timeline, **50% upfront / 50% at launch**, the client provides content and photos and confirms facts, the client owns the site and domain after final payment, care plan is month-to-month with 30 days' notice, no guaranteed Google rankings. Have one of your family's attorney contacts look it over once. It's worth it.
- **Payment:** Always get the 50% deposit before starting work (except free demos).
- **LLC:** Not needed for the first client, but form a Utah LLC once you have regular revenue, to separate personal liability. Open a separate bank account for the business.
- **Taxes:** This is self-employment income. Set aside ~25–30%. Split profits by a written agreement among the three of you *before* the first dollar comes in: who owns what percentage, what happens if someone leaves.
- **Don't promise SEO results.** Never guarantee "page 1 of Google."
- **Don't copy:** No competitors' text, no images from Google search, no fake reviews (fake reviews also violate FTC rules).

---

## 9. Unit economics (all estimates)

**Per Standard site:**
- Revenue $1,200; costs ~$40 in card fees; ~10 hours of work → **~$115/hr effective**. Founding-client pricing at $500 → ~$45/hr, which is fine for the first 3 portfolio pieces.

**Recurring:**
- Each care-plan client at $99/mo, ~1 hr/mo → ~$95/hr.
- **20 care-plan clients = ~$2,000/mo recurring** for ~20 hrs/mo. That's the real business; the build fees are the on-ramp.

**Realistic ramp (3 people, ~10 hrs/week each):**

| Month | Sites launched | Build revenue | Care-plan clients | Monthly recurring | Month total (est.) |
|---|---|---|---|---|---|
| 1 | 1–2 (founding price) | $500–$1,000 | 1–2 | $100–$200 | **$600–$1,200** |
| 2 | 2–3 | $1,500–$3,000 | 3–5 | $300–$500 | **$1,800–$3,500** |
| 3 | 3–4 | $3,000–$4,500 | 6–9 | $600–$900 | **$3,600–$5,400** |

These assume your sales outreach works at roughly 1 signed client per 10–15 demos (est.). The first test (section 10) will tell you your real conversion rate.

---

## 10. 30-day launch plan

| Days | Goal | Tasks |
|---|---|---|
| **1–3** | Set up | Pick the niche. Write the profit-split agreement among the three of you. Make a free GitHub org, Cloudflare account, Web3Forms account and Google Form intake. Draft the contract. |
| **4–7** | Template | Build the master niche template with AI. Run the QA checklist on it. Make a simple portfolio page for your "agency" name. |
| **8–10** | Prospects | Build a list of 50 businesses from Google Maps. Pick the top 10. Build 10 demo homepages (1–2 hrs each across the team). |
| **11–17** | Sell | Call all 10 and text the demos. Then 20 more calls per day using the list. Goal: 5 conversations, 1–2 signed at the founding price. |
| **18–25** | Deliver | Build and launch the first client site with the full QA process. Optimize their Google Business Profile. |
| **26–30** | Prove and repeat | Launch site 2 if signed. Get a testimonial and a Google review. Ask each client for 2 referrals. Raise prices to $1,200 for new clients once you have 2 live sites. |

**Kill or pivot signal:** If 30 demo calls produce zero signed clients, change something: a different niche, a lower price, or the $0-down monthly model. Don't keep repeating what isn't working.

---

## 11. Biggest risks and how to handle them

| Risk | How to handle it |
|---|---|
| **Scope creep** ("can you also add…") | Written scope and 2 revision rounds; extra work is billed hourly. |
| **Clients slow to send content** | Build from their Google/Facebook info first; the intake form has a deadline; the timeline pauses if content is late. |
| **Low-quality, generic AI copy** | A human edits every page; only use facts the owner confirmed. |
| **Getting paid late** | 50% upfront, 50% before launch. The site goes live only after final payment. |
| **Someone on the team stops showing up** | Written agreement on ownership, roles, and what happens if someone leaves. |
| **Hosting terms change** | Static sites move easily between hosts. Keep every site in GitHub so you can redeploy anywhere in minutes. |
| **Crowded market** | Niche focus, demo-first selling, and local service. Never compete on lowest price. |

---

## Sources

- Website pricing: [Seahawk Media](https://seahawkmedia.com/tech/small-business-website-costs/), [WebsiteSetup](https://websitesetup.org/website-cost/)
- Market (83% of small businesses have a website): [Clutch via Business Wire](https://www.businesswire.com/news/home/20250821848152/en/Clutch-Report-No-Code-Tools-Fuel-Website-Growth-Yet-17-of-Small-Businesses-are-Still-Offline), [Review42](https://resources.review42.com/what-percentage-of-small-businesses-have-a-website/)
- Maintenance pricing: [Ueni (citing GoDaddy)](https://ueni.com/blog/website-maintenance-cost/), [Seahawk Media care plans](https://seahawkmedia.com/wordpress/wordpress-maintenance-packages/)
- Hosting terms: [Vercel fair use guidelines](https://vercel.com/docs/limits/fair-use-guidelines), [Cloudflare Pages limits](https://developers.cloudflare.com/pages/platform/limits)
- Forms: [Web3Forms pricing](https://web3forms.com/pricing), [Formspree free plan limits (via a competitor's page)](https://splitforms.com/formspree-free-plan-limits)

**Note:** Tool limits and terms change. Check each provider's current pricing page before you rely on a free tier for paying clients.
