Phishing Email Analyzer

A Python-based defensive cybersecurity tool that analyzes email text for common phishing indicators and assigns a basic risk level.

Features

- Analyzes email text for suspicious phrases
- Detects urgency-related language
- Detects password-related language
- Identifies HTTP/HTTPS links
- Records detected phishing indicators
- Assigns LOW, MEDIUM, or HIGH risk levels
- Does not open detected links or attachments

Indicators Checked

The analyzer looks for phrases such as:

- "urgent"
- "immediately"
- "verify your account"
- "account suspended"
- "click here"
- "confirm your password"

It also checks for:

- HTTP/HTTPS links
- Password-related language

Risk Classification

- LOW — fewer than 2 indicators
- MEDIUM — 2–3 indicators
- HIGH — 4 or more indicators

Example — Suspicious Email

Input:

"URGENT: Your account has been suspended. Click here to verify your account immediately: https://example.com"

Detected indicators include:

- Urgent language
- Immediate-action language
- Account verification request
- Click-here language
- Link detected

Result:

Risk Level: HIGH

Example — Normal Email

Input:

"Hello John, the project meeting is scheduled for Monday at 10 AM. Please bring your latest notes."

Result:

Risk Level: LOW

Technologies

- Python
- Regular expressions ("re")
- Text analysis
- Google Colab
- GitHub

SOC Use Cases

This project demonstrates basic concepts relevant to:

- Phishing investigation
- Email security analysis
- Security alert triage
- Indicator identification
- SOC analyst workflows

Limitations

This is a basic educational analyzer. A HIGH risk result does not prove that an email is malicious, and a LOW result does not guarantee that an email is safe. Real phishing investigations may also require sender/domain analysis, email-header inspection, attachment analysis, URL reputation checks, and threat intelligence.

Future Improvements

- Analyze sender domains
- Parse email headers
- Extract URLs for offline inspection
- Detect suspicious attachment names
- Export findings to CSV
- Integrate trusted threat-intelligence services

Ethical Use

This project is intended for cybersecurity education and defensive security analysis. Suspicious links and attachments should not be opened during analysis.

Author

Jawad Hussain

Computer Science Graduate | Aspiring Cybersecurity Analyst
