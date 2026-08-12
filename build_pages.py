import os

ICONS = {
    "data-connectivity": '<path d="M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z"/><path d="M12 12v-4M12 12l3 2"/>',
    "fixed-solutions": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/>',
    "international-carrier": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 6 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-6-3.8-9s1.3-6.3 3.8-9Z"/>',
    "iot": '<circle cx="12" cy="12" r="3"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M9.5 9.5 6.3 6.3M14.5 9.5l3.2-3.2M9.5 14.5l-3.2 3.2M14.5 14.5l3.2 3.2"/>',
    "voice": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.5 2.1L8 9.7a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.7.6a2 2 0 0 1 1.7 2Z"/>',
    "software": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "communication": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "digital-transformation": '<path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/>',
}

CATEGORIES = [
    {
        "slug": "data-connectivity",
        "name": "Data & Connectivity Solutions",
        "tagline": "Wireless data plans and shared connectivity for growing teams.",
        "products": [
            ("Mobile Broadband", "High-speed wireless connectivity to keep business teams productive from any location."),
            ("Bulk Data Posting", "Distribute data packages across multiple employee lines efficiently and centrally."),
            ("Managed Wi-Fi", "Enterprise-grade wireless network setup, monitoring and optimization."),
            ("Data Pool", "Shared data allocation pooled across multiple business lines."),
        ],
    },
    {
        "slug": "fixed-solutions",
        "name": "Fixed Solutions",
        "tagline": "Dedicated, wired infrastructure for offices, branches and campuses.",
        "products": [
            ("Dedicated Internet Access (DIA)", "High-speed, secure and reliable dedicated internet for mission-critical operations."),
            ("Business Branch Connectivity", "Link multiple business locations into one unified, reliable network."),
            ("MPLS", "Multi-Protocol Label Switching for connecting your business worldwide."),
            ("Dark Fiber Cores", "Dedicated fiber infrastructure leasing for high-capacity, private networks."),
            ("SD-Connect", "Software-defined connectivity platform for flexible, centrally managed networks."),
        ],
    },
    {
        "slug": "international-carrier",
        "name": "International Carrier Business",
        "tagline": "Global network and datacenter infrastructure for carriers and large enterprises.",
        "products": [
            ("IEPL", "International Ethernet Private Line services for point-to-point global connectivity."),
            ("IP Transit", "Direct internet backbone connectivity for carriers and content providers."),
            ("Global MPLS", "Worldwide managed network services across international locations."),
            ("Smart Hand Datacenter", "On-site datacenter infrastructure management and support services."),
            ("Datacenter Colocation", "Secure hosting and physical rack space for your infrastructure."),
            ("CDN Colocation", "Content delivery network colocation for faster regional content delivery."),
        ],
    },
    {
        "slug": "iot",
        "name": "Internet of Things (IoT)",
        "tagline": "Connected monitoring for logistics, fleets and industrial operations.",
        "products": [
            ("Cold Chain Monitoring", "Real-time temperature tracking for sensitive goods in transit and storage."),
            ("Smart Fleet Management", "Vehicle tracking, route optimization and fleet visibility in one platform."),
            ("Fuel Monitoring", "Track fuel consumption and detect leakage or theft across your fleet."),
            ("Genset Monitoring", "Remote monitoring of backup generators for uptime and maintenance alerts."),
            ("Machine-to-Machine (M2M)", "Connectivity solutions for automated device-to-device communication."),
        ],
    },
    {
        "slug": "voice",
        "name": "Voice Solutions",
        "tagline": "Reliable business calling infrastructure at any scale.",
        "products": [
            ("Business Postpaid", "Dedicated postpaid voice plans designed for corporate accounts."),
            ("PRI Lines", "Primary Rate Interface lines for high-volume business call handling."),
            ("SIP Trunking", "SIP-based voice lines for scalable, IP-based telephony."),
            ("Coverage Enhancement", "Improve indoor and site-specific signal coverage for your premises."),
            ("Push-to-Talk", "Instant team communication for field and operations staff."),
        ],
    },
    {
        "slug": "software",
        "name": "Software Solutions",
        "tagline": "Business applications to run day-to-day operations.",
        "products": [
            ("Workforce Management", "Scheduling, attendance and productivity tools for distributed teams."),
            ("Fleet & Task Tracking", "Assign, track and manage field tasks and deliveries in real time."),
            ("Service Desk", "Ticketing and support desk software for internal or customer support teams."),
            ("Billing Systems", "Automated invoicing and billing management for recurring revenue."),
            ("ERP", "Enterprise resource planning for finance, inventory and operations."),
            ("Cloud File Storage", "Secure, centralized document storage and sharing for teams."),
            ("Building Management", "Systems for managing facilities, access and building operations."),
            ("HR Systems", "Payroll, attendance and employee record management."),
            ("Custom Development", "Bespoke software built around your specific business processes."),
        ],
    },
    {
        "slug": "communication",
        "name": "Communication Solutions",
        "tagline": "Reach customers at scale through messaging and voice broadcast.",
        "products": [
            ("Bulk SMS", "Send promotional or transactional SMS to large customer lists."),
            ("Voice Messaging / Broadcast", "Automated voice broadcasts for announcements and alerts."),
            ("Messaging Platform", "A unified platform to manage customer messaging campaigns."),
            ("Customer Acquisition Tools", "Tools to help identify, reach and convert new business customers."),
        ],
    },
    {
        "slug": "digital-transformation",
        "name": "Digital Transformation (DICT)",
        "tagline": "Consulting and cloud services to modernize enterprise operations.",
        "products": [
            ("Digital Transformation Consulting", "Strategic consulting to guide your enterprise's digital roadmap."),
            ("Z-SIAS Cloud", "Zong's cloud infrastructure and application services offering."),
        ],
    },
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — Zong Business</title>
<meta name="description" content="{tagline} Explore {name} from Zong Business and add products to your interest form.">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<header>
  <div class="container nav">
    <a href="index.html" class="logo">zong<span>.</span><small>business</small></a>
    <nav class="nav-links">
      <a href="index.html">Home</a>
      <a href="index.html#solutions" class="active">Solutions</a>
      <a href="index.html#why-us">Why Zong</a>
      <a href="contact.html">Contact</a>
    </nav>
    <div class="nav-cta">
      <span class="interest-pill" id="interestPill" style="display:none;">Interest list <span class="count">0</span></span>
      <a href="contact.html" class="btn btn-outline btn-sm">Get in touch</a>
    </div>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</header>

<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> / <a href="index.html#solutions">Solutions</a> / <span>{name}</span>
    </div>
  </div>
</section>

<section style="padding-top:10px;">
  <div class="container">
    <div class="category-header">
      <div class="cat-icon-lg"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{icon}</svg></div>
      <div>
        <h1>{name}</h1>
        <p>{tagline}</p>
      </div>
    </div>

    <div class="product-grid">
{product_cards}
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h3>Not sure which product fits?</h3>
        <p>Add a few options above and our corporate sales team will help you narrow it down.</p>
      </div>
      <a href="contact.html" class="btn btn-primary">Go to interest form →</a>
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-logo">zong<span>.</span>business</div>
      <div class="footer-links">
        <a href="index.html#solutions">Solutions</a>
        <a href="index.html#why-us">Why Zong</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year"></span> Zong Business. All rights reserved.</span>
      <span>Corporate &amp; Enterprise Solutions Portfolio</span>
    </div>
    <p class="disclaimer">This is an informational corporate lead-generation page listing Zong Business (CMPak Ltd) product categories. Product names, availability, pricing and features are subject to change — final terms are confirmed directly by the Zong corporate sales team.</p>
  </div>
</footer>

<div class="floating-bar" id="floatingBar">
  <span class="fb-text"><span class="fb-count">0</span> product<span>s</span> selected</span>
  <a href="contact.html" class="btn btn-primary">View &amp; submit →</a>
  <span class="fb-clear">Clear</span>
</div>

<script src="script.js"></script>
</body>
</html>
"""

CARD_TEMPLATE = """      <div class="product-card">
        <h4>{pname}
          <label class="add-toggle">
            <input type="checkbox" value="{pname}"> ADD
          </label>
        </h4>
        <p>{pdesc}</p>
      </div>"""

out_dir = os.path.dirname(os.path.abspath(__file__))

for cat in CATEGORIES:
    cards = "\n".join(
        CARD_TEMPLATE.format(pname=p[0], pdesc=p[1]) for p in cat["products"]
    )
    html = PAGE_TEMPLATE.format(
        name=cat["name"],
        tagline=cat["tagline"],
        icon=ICONS[cat["slug"]],
        product_cards=cards,
    )
    path = os.path.join(out_dir, f"{cat['slug']}.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"wrote {path}")
