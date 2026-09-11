from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Page content is deliberately kept in this data structure.  It lets an editor
# change page copy, card order, or Bootstrap icons without touching the shared
# layout in templates/marketing-page.html.
PAGES = {
    "services": {"eyebrow":"SERVICES & SOLUTIONS", "title":"Enterprise IAM Services", "accent":"Built for Scale and Security", "intro":"Atikes helps enterprises design, implement, and optimize identity and access management programs that protect critical resources and accelerate business outcomes.", "hero_icon":"shield-lock", "trust":["SailPoint Experts","Okta Specialists","Governance First","Cloud & SaaS Ready"], "section_title":"Our IAM Services & Solutions", "section_intro":"End-to-end services and practical solutions for a secure, compliant, and resilient identity ecosystem.", "cards":[("sailboat","SailPoint Services","Implement, integrate, and optimize SailPoint IdentityIQ and ISC for unified identities and automated governance at scale."),("circle","Okta Services","Design, deploy, and manage Okta solutions for secure access, SSO, MFA, lifecycle management, and app integrations."),("person-plus","Identity Lifecycle Automation","Automate joiner, mover, leaver processes across HR, applications, and infrastructure."),("shield-check","Access Governance & Certifications","Establish governance models, run access certifications, and enforce compliance."),("diagram-3","RBAC & Role Design","Design roles and permissions that align with business needs and least privilege."),("heart-pulse","IAM Health Check","Assess your IAM program, identify gaps, and receive actionable recommendations."),("headset","Managed IAM Support","Ongoing support, operations, and enhancements to keep your environment reliable."),("cloud","Cloud & SaaS Integrations","Integrate IAM with cloud platforms and SaaS applications for consistent provisioning."),("robot","Agentic AI & AI Identity Security","Design and govern enterprise AI agents with secure identities, least-privilege access, human ownership, scoped authorization, and auditable actions across cloud, SaaS, and internal systems.")], "method":["Assess","Design","Implement","Optimize"], "outcomes":[("shield-check","Stronger Security","Reduce identity risk and minimize unauthorized access."),("check-circle","Operational Efficiency","Automate processes and accelerate productivity."),("graph-up-arrow","Compliance Confidence","Simplify audits and meet regulatory requirements."),("cloud","Business Agility","Enable secure access at speed.")], "cta":"Ready to Strengthen Your Identity Security?"},
    "solutions": {"eyebrow":"SOLUTIONS", "title":"IAM Solutions for", "accent":"Modern Enterprises", "intro":"We deliver intelligent identity and access management solutions that secure every identity, everywhere. Automate identity lifecycles, enforce least privilege, and achieve continuous governance.", "hero_icon":"shield-lock", "trust":["Secure Every Identity","Automate with Intelligence","Govern with Confidence"], "section_title":"Our Identity & Access Management Solutions", "section_intro":"Practical identity solutions that are secure, scalable, and measurable.", "cards":[("person-plus","Joiner-Mover-Leaver Automation","Automate provisioning, updates, and deprovisioning across systems throughout the employee lifecycle."),("clipboard-check","Access Requests & Approvals","Streamline requests with intelligent workflows, approvals, and segregation of duties."),("shield-lock","Role-Based Access Control","Design roles based on business functions and enforce least privilege."),("shield-check","Access Governance & Certifications","Run periodic access reviews and attestation programs for audit readiness."),("lock","Zero Trust & Least Privilege","Adopt zero trust principles and enforce least privilege across users and applications."),("cloud","Cloud & SaaS Identity Governance","Govern identities across cloud and SaaS applications with visibility and control.")], "method":["Discover & Assess","Design & Blueprint","Implement & Integrate","Optimize & Evolve"], "outcomes":[("rocket-takeoff","Faster Provisioning","Automate access provisioning to improve productivity."),("clock","Reduced Manual Work","Streamline workflows and eliminate redundant tasks."),("shield-check","Audit-Ready Compliance","Maintain continuous compliance and complete audit trails."),("eye","Better Visibility","Gain real-time visibility into identities and access risk.")], "cta":"Ready to Transform Your Identity Security?"},
    "success": {"eyebrow":"SUCCESS STORIES", "title":"Proven IAM Outcomes for", "accent":"Complex Organizations", "intro":"See how enterprises across industries partner with Atikes to simplify identity, strengthen security, and achieve measurable business impact.", "hero_icon":"shield-check", "trust":["Real results from complex environments","Measurable impact and business value","Secure, scalable, future-ready"], "section_title":"Success Stories", "section_intro":"Explore how our IAM solutions drive security, efficiency, and business value.", "cards":[("cart","Retail IAM Automation","Automated user lifecycle management to reduce manual effort and improve compliance."),("building","OmniSuite SSO & Provisioning","Implemented SSO and automated provisioning across enterprise applications."),("clipboard-check","Access Review Optimization","Streamlined access reviews and certifications to improve compliance."),("cloud","Cloud Governance Modernization","Established scalable IAM governance and access controls across multi-cloud environments.")], "method":["Lifecycle Automation","Faster Onboarding","Reduced Manual Effort","Stronger Governance"], "outcomes":[("clock","70%","Reduction in provisioning time"),("shield-check","100%","Certification compliance achieved"),("people","20+","Enterprise applications integrated"),("check-circle","92%","Policy compliance")], "cta":"Ready to Achieve Similar Results?"},
    "health": {"eyebrow":"IAM HEALTH CHECK", "title":"Know Your IAM.", "accent":"Strengthen Your Security.", "intro":"Our IAM Health Check evaluates your identity architecture, access controls, provisioning processes, governance maturity, and opportunities for improvement.", "hero_icon":"shield-lock", "trust":["Expert-led assessment","Vendor & tool agnostic","Actionable insights","Improved security & efficiency"], "section_title":"What We Assess", "section_intro":"A focused assessment of the capabilities that make an IAM program effective.", "cards":[("layers","Architecture Assessment","Evaluate your IAM architecture for alignment with business goals, scalability, integration, and automation practices."),("shield-check","Access & Policy Review","Analyze access models, roles, permissions, segregation of duties, and policy effectiveness."),("gear","Process & Tool Evaluation","Review identity lifecycle processes, provisioning workflows, tool capability, and automation effectiveness."),("bullseye","Actionable Recommendations","Receive prioritized recommendations to strengthen security, improve efficiency, and reduce risk.")], "method":["Discover & Align","Assess & Analyze","Report & Prioritize","Advise & Enable"], "outcomes":[("file-earmark-text","Executive Summary","A clear view of your IAM program."),("shield-check","Risk Assessment","Detailed findings and priorities."),("gear","Maturity Scoring","Capabilities mapped to outcomes."),("signpost-split","Roadmap & Next Steps","A practical path forward.")], "cta":"Take the First Step Toward a Stronger IAM Program"},
    "partners": {"eyebrow":"TECHNOLOGY PARTNERS", "title":"Trusted Platforms and", "accent":"Technology Partners", "intro":"We partner with industry-leading identity, cloud, and enterprise technology providers to deliver secure, scalable, and interoperable IAM solutions.", "hero_icon":"shield-lock", "trust":["Best-in-class technologies","Seamless integrations","Stronger together"], "section_title":"Platform Partners Powering Secure Identity", "section_intro":"We collaborate with leading technology providers to deliver modern, interoperable IAM solutions.", "cards":[("people","Identity Platforms","Enterprise identity governance and automation: SailPoint, Okta, Evolveum, and Microsoft Entra."),("cloud","Cloud Platforms","Scalable, secure cloud infrastructure and services, including Microsoft Azure."),("pc-display","IT & Service Management","Service experience and IT operations management with Freshservice and Workday."),("bezier2","Ecosystem Integrations","Extended ecosystem of apps and technologies with 200+ supported integrations.")], "method":["Pre-built connectors","Certified integrations","API-first architecture","Lifecycle orchestration"], "outcomes":[("shield-check","Stronger Security","Enterprise-grade platforms protect critical capabilities."),("gear","Operational Efficiency","Automations reduce manual effort and errors."),("arrow-up-right","Scalability","Platforms grow with your business."),("lightbulb","Future-Ready","Access continuous innovation through our partner network.")], "cta":"Build on the best. Achieve more together."},
    "about": {"eyebrow":"ABOUT ATIKES", "title":"Identity Security Expertise with a", "accent":"Practical Delivery Mindset", "intro":"Atikes is an identity and access management consultancy built to solve complex challenges and deliver measurable outcomes. We combine expertise, automation, and proven methodologies.", "hero_icon":"shield-lock", "trust":["50,000+ identities supported","10+ years of IAM experience","Enterprise-ready delivery","Audit-focused outcomes"], "section_title":"Our Values & Principles", "section_intro":"The principles that guide every client engagement.", "cards":[("people","Client Success","We measure success by the outcomes and lasting impact we create for our clients."),("shield-check","Integrity","We operate with transparency, honesty, and accountability in every engagement."),("star","Excellence","We pursue excellence through expertise, quality, and continuous improvement."),("lightbulb","Innovation","We embrace automation and emerging technologies to solve today's challenges."),("handshake","Collaboration","We partner closely with clients and teams to achieve shared success.")], "method":["Assess","Design","Implement","Optimize"], "outcomes":[("check-circle","Deep IAM Expertise","Across SailPoint, Okta, Microsoft Entra, and more."),("check-circle","Automation First","For consistent and scalable results."),("check-circle","Security by Design","Compliance built into every solution."),("check-circle","Proven Delivery","Accelerators reduce time to value.")], "cta":"Let's Build a More Secure Future Together"},
    "sailpoint": {"eyebrow":"SAILPOINT SERVICES", "title":"SailPoint Services for", "accent":"Identity Security at Scale", "intro":"Atikes helps enterprises implement, optimize, and operate SailPoint solutions that secure identity, intelligence, and automated identity governance. From implementation and integration to managed support, we harness the power of SailPoint Identity Security Cloud and IdentityIQ.", "hero_icon":"sailboat", "trust":["SailPoint Specialists","Proven Frameworks","Measurable Outcomes"], "section_title":"End-to-End SailPoint Services", "section_intro":"Secure, scalable services across the SailPoint identity lifecycle.", "cards":[("puzzle","Implementation & Architecture","Strategy, design, and implementation of SailPoint Identity Security Cloud and IdentityIQ."),("wrench-adjustable","Connector Onboarding & Integrations","Rapid integration of applications, databases, SaaS platforms, and infrastructure."),("person-arms-up","Identity Lifecycle Automation","Automate joiner, mover, and leaver processes with policy-based workflows."),("shield-check","Access Certifications & Campaigns","Design and run intelligent certification campaigns that reduce risk."),("diagram-3","Role & Policy Design","Build least-privilege roles, entitlements, and access models aligned to business functions."),("arrow-up-circle","Upgrades & Optimization","Seamless upgrades, migrations, and platform optimizations."),("headset","Managed Support & Operations","24x7 monitoring, issue resolution, enhancements, and ongoing support.")], "method":["Assess & Discover","Design & Plan","Build & Integrate","Test & Validate","Deploy & Adopt","Operate & Optimize"], "outcomes":[("shield-check","70%","Faster access provisioning"),("clock","80%","Reduction in manual access reviews"),("people","90%","Certification compliance improvement"),("lock","60%","Reduction in access risk")], "cta":"Ready to Strengthen Your Identity Security with SailPoint?"},
    "okta": {"eyebrow":"OKTA SERVICES", "title":"Okta Services and", "accent":"Identity Governance Expertise", "intro":"Atikes helps enterprises design, implement, and optimize Okta solutions that strengthen security, simplify access, and accelerate digital transformation. From Workforce Identity to Okta Identity Governance and Workflows, we deliver secure, scalable, and future-ready experiences.", "hero_icon":"shield-lock", "trust":["Okta Certified Experts","Proven Implementations","Secure by Design"], "section_title":"End-to-End Okta Solutions for a Secure and Modern Workforce", "section_intro":"Purpose-built services for modern identity and access programs.", "cards":[("cloud-arrow-up","Okta Deployment & Implementation","Design and implement scalable Okta Workforce Identity solutions tailored to your needs."),("people","User Lifecycle Management","Automate joiner, mover, leaver, and role change processes."),("lock","SSO & MFA Enablement","Deliver seamless and secure access with single sign-on and adaptive MFA."),("grid-3x3-gap","Application Integrations","Integrate enterprise and custom applications for a unified user experience."),("shield-check","Identity Governance & Access Requests","Implement Okta Identity Governance, access reviews, policies, and role-based access."),("gear","Okta Workflows Automation","Automate identity processes and IT workflows to improve efficiency."),("graph-up-arrow","Okta Optimization & Support","Tune performance, enhance configurations, and provide ongoing support.")], "method":["Plan","Integrate","Automate","Optimize"], "outcomes":[("shield-check","Stronger Security","Reduce risk with adaptive access and governance."),("emoji-smile","Better User Experience","Seamless, secure access across apps and devices."),("graph-up-arrow","Improved Productivity","Simplify access and automate time-consuming tasks."),("clipboard-check","Audit & Compliance Ready","Prove access is appropriate, reviewed, and compliant.")], "cta":"Ready to Elevate Your Okta Program?"}
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services-and-solutions")
def services_and_solutions():
    return render_template("services.html", page=PAGES["services"], page_name="services", PAGES_SOLUTIONS=PAGES["solutions"])

@app.route('/success-stories/retail-rbac-automation')
def retail_rbac_automation():
    return render_template('retail-rbac-automation.html')


@app.route('/success-stories/omnisuite-sso-provisioning')
def omnisuite_sso_provisioning():
    return render_template('omnisuite-sso-provisioning.html')


@app.route('/access-review-optimization')
def access_review_optimization():
    return render_template('access-review-optimization.html')


@app.route('/success-stories/cloud-governance-modernization')
def cloud_governance_modernization():
    return render_template('cloud-governance-modernization.html')


@app.route("/services")
def services():
    return redirect(url_for("services_and_solutions"), code=301)

@app.route("/services/<service_key>")
def service_detail(service_key):
    if service_key not in {"sailpoint", "okta"}:
        return render_template("404.html"), 404
    return render_template("marketing-page.html", page=PAGES[service_key], page_name=service_key)


@app.route("/solutions")
def solutions():
    return redirect(url_for("services_and_solutions"), code=301)


@app.route("/success-stories")
def success_stories():
    return render_template("success-stories.html", page=PAGES["success"], page_name="success")


@app.route("/iam-health-check")
def iam_health_check():
    return render_template("iam-health-check.html", page=PAGES["health"], page_name="health")


@app.route("/partners")
def partners():
    return render_template("partners.html", page=PAGES["partners"], page_name="partners")


@app.route("/about")
def about():
    return render_template("about.html", page=PAGES["about"], page_name="about")


@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Add database/email logic here later.
        flash("Thank you. Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/consultation", methods=["GET", "POST"])
def consultation():
    if request.method == "POST":
        # Add calendar/database/email logic here later.
        flash("Thank you. We will contact you about the consultation.", "success")
        return redirect(url_for("consultation"))

    return render_template("consultation.html")


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("legal.html", legal_type="privacy")


@app.route("/terms-of-service")
def terms_of_service():
    return render_template("legal.html", legal_type="terms")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True ,port=5050,host ="0.0.0.0")
