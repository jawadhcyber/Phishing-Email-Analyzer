import re

print("=== Phishing Email Analyzer ===")
print()

email_text = input("Paste email text: ")

score = 0
findings = []

urgent_words = [
    "urgent",
    "immediately",
    "verify your account",
    "account suspended",
    "click here",
    "confirm your password"
]

for phrase in urgent_words:
    if phrase.lower() in email_text.lower():
        score += 1
        findings.append(f"Suspicious phrase detected: {phrase}")

links = re.findall(r"https?://\S+", email_text)

if links:
    score += 1
    findings.append("One or more links detected")

if "password" in email_text.lower():
    score += 1
    findings.append("Password-related language detected")

print()
print("Analysis Results:")
print()

if findings:
    for finding in findings:
        print(f"- {finding}")
else:
    print("No basic phishing indicators detected.")

print()

if score >= 4:
    print("Risk Level: HIGH")
elif score >= 2:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")

print()
print("Analysis complete.")
