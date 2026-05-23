import re

# Open and read the input text file
with open("sample.txt", "r") as file:
    content = file.read()

# Regular Expression pattern for email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all email addresses
emails = re.findall(pattern, content)

# Save emails into another file
with open("extracted mails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

# Print success message
print("Emails extracted successfully!")
print(f"Total Emails Found: {len(emails)}")