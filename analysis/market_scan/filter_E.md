# Market scan filter – group E
Checked: 2026-11-18

## Summary
| Product | Q1 | Q2 | Q3 | Q4 | Result | Reason | Deployment | Starting price |
|---|---|---|---|---|---|---|---|---|
| Pylon | No | Yes | Yes | Yes | Fail | Q1 No: vendor scopes the product to B2B customer support; no employee/internal-request use case documented | SaaS (AWS, US or EU) | $89/seat on an annual contract (Professional); free trial via sales (usepylon.com/pricing) |
| Plain | No | Yes | Unknown | Yes | Fail | Q1 No: vendor scopes the product to B2B customer support; Q3 also Unknown (only a UK region documented) | SaaS (AWS) | $45/user/month billed annually (Foundation); 7-day free trial (plain.com/pricing) |
| Thena | No | Yes | Unknown | Yes | Fail | Q1 No: "purpose-built for B2B customer support and service"; Q3 also Unknown (no hosting location published) | SaaS (no self-hosting found) | $29/user/month billed annually (Starter, up to 5 seats); free plan mentioned (thena.ai/pricing) |
| Unthread | Yes | Yes | Partial | Yes | Pass | No "No" on Q1–Q3; EU data residency listed only in the Enterprise plan | SaaS; dedicated hosting on Enterprise | From $85/agent/month (Pro, min. 5 seats; page has Annual/Monthly toggle, period of shown price not confirmed); 14-day free trial (unthread.io/pricing) |
| ClearFeed | Partial | Yes | No | Yes | Fail | Q3 No: hosted in AWS us-east-1; "EU data residency: Coming soon". Q1 Partial: internal and external are separate product editions | SaaS (AWS us-east-1) | $24 USD/agent/month (Starter; page notes 15% off annual, period of shown price not confirmed); 14-day free trial (clearfeed.ai/pricing/helpdesk) |
| Suptask | Yes | Yes | Yes | Yes | Pass | No "No" on Q1–Q3 | SaaS (Slack app; AWS Ireland) | $15/agent/month, "Pay Annually" tab (Starter); 14-day free trial (suptask.com/pricing) |

## Pylon
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "Pylon is the first agentic support platform built for B2B. Track customer issues across any channel". Reviewer check: docs index and sitemap list no employee/internal-request use case; "internal" items are internal threads/channels on customer issues. | https://docs.usepylon.com/pylon-docs ; https://docs.usepylon.com/pylon-docs/llms.txt ; https://www.usepylon.com/sitemap.xml |
| Q2 | Yes | "Pylon holds SOC 2 Type II and ISO/IEC 27001:2022 certifications, audited every year, with both our US and EU deployments in scope." | https://www.usepylon.com/security |
| Q3 | Yes | "Choose US or EU hosting on AWS." / "EUROPEAN UNION AWS Frankfurt". Pricing table row "EU data residency" marked "Included" for Professional, Advanced and Enterprise. | https://www.usepylon.com/security ; https://www.usepylon.com/pricing |
| Q4 | Yes | "Pylon can track messages in public and private channels, as well as Slack Connect channels initiated by your customer." | https://www.usepylon.com/integrations/slack |

## Plain
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "The most collaborative AI-powered support platform for scaling B2B support teams." / "The fastest, most powerful support platform for modern B2B teams". Reviewer check: sitemap lists no employee/internal-request use case. | https://trust.plain.com/ ; https://www.plain.com/use-case/b2b-support-teams ; https://www.plain.com/sitemap.xml |
| Q2 | Yes | "Plain is SOC 2 Type II certified." | https://www.plain.com/docs/product/security |
| Q3 | Unknown | "Workspaces in Plain’s UK region are hosted in AWS eu-west-2 (London)." / subprocessor "Amazon Web Services • Cloud provider UK Hosting/Infrastructure". UK is not in the EU; no EU region found. | https://www.plain.com/docs/product/security ; https://trust.plain.com/ |
| Q4 | Yes | "Add the Plain bot to your Slack Connect channels and start tracking all your support requests in one place." | https://www.plain.com/channels/slack |

## Thena
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | No | "Thena is purpose-built for B2B customer support and service." | https://docs.thena.ai/guides/onboarding/introduction |
| Q2 | Yes | "We undergo annual independent third-party SOC 2 Type II audits" | https://www.thena.ai/policy/security |
| Q3 | Unknown | No hosting location on the security page. Privacy policy: "We transfer data internationally with appropriate safeguards." | https://www.thena.ai/policy/security ; https://www.thena.ai/policy/privacy |
| Q4 | Yes | "Slack-native customer support Detect and manage tickets directly in Slack" | https://www.thena.ai/ |

## Unthread
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | Internal: "For every internal team Automate internal support in Slack". External: "For Customer Support teams Support your customers right in Slack" with "Email-to-ticket with threading"; shared inbox: "Customers will see your response in an email thread on their end." | https://unthread.io/solutions/employee-support ; https://unthread.io/solutions/customer-support ; https://unthread.io/products/shared-email-inbox |
| Q2 | Yes | "We're SOC 2 Type II certified" | https://unthread.io/security |
| Q3 | Partial | "Unthread offers isolated, dedicated database instances in specific countries" with "EU European Union" listed. Pricing: "Enterprise … Everything in Business, plus: Dedicated hosting Data residency" (Enterprise plan only). | https://unthread.io/security ; https://unthread.io/pricing |
| Q4 | Yes | "Slack-native and Teams-native intake & responses" | https://unthread.io/ |

## ClearFeed
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Partial | "ClearFeed offers three products to cater to the following use cases." "External Helpdesk - For supporting customers via Slack Connect, MS Teams, Email, Web Chat…" "Internal Helpdesk - ClearFeed Service Desk for supporting employees on internal Slack & Email for teams like IT, Finance, Legal, HR…" "However Agents are counted separately across different Product Editions." Both uses need two editions: Internal Helpdesk + External Helpdesk. | https://clearfeed.ai/pricing/helpdesk |
| Q2 | Yes | "SOC 2 Type II compliant since 2023" | https://clearfeed.ai/security |
| Q3 | No | "Cloud provider & Region Amazon Web Services (AWS) us-east-1" / "EU data residency Coming soon" | https://clearfeed.ai/security |
| Q4 | Yes | "Slack-native Support Help customers & employees without leaving Slack" | https://clearfeed.ai/ |

## Suptask
| Q | Answer | Evidence (verbatim, short) | Source |
|---|---|---|---|
| Q1 | Yes | Professional plan: "Service desk for internal teams and customer support". Email: "Email tickets share the same queue as customer support tickets and internal requests." / "Can I support customers who aren't on Slack? Yes. Customer emails automatically become Slack tickets" | https://www.suptask.com/pricing ; https://www.suptask.com/ticketing/email ; https://www.suptask.com/products/customer-support-in-slack |
| Q2 | Yes | "SOC 2 & CSA Certified" | https://www.suptask.com/trust/security |
| Q3 | Yes | "Our technical solution is hosted within Amazon Web Services (AWS) Ireland (EU)". Also: "Tickets are stored within your Slack Workspace, with minimal amount of data managed by Suptask." | https://www.suptask.com/trust/privacy-policy ; https://www.suptask.com/trust/security |
| Q4 | Yes | "The AI Help Desk and Ticketing System Built Into Slack" | https://www.suptask.com/ |

## Reviewer check (2026-11-18)
1. Re-checked: Suptask pricing "Service desk for internal teams and customer support" (https://www.suptask.com/pricing; the page text read by the reviewer showed $24 per agent per month, the screen records $15 on the annual tab).
2. Re-checked: ClearFeed security page "EU data residency Coming soon" (https://clearfeed.ai/security), so Q3 = No and the Fail stands.
