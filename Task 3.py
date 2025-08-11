# task3_simple.py
# Task 3 - Simple Web Scraper for News Headlines (No external libraries)

import urllib.request

url = "https://www.bbc.com/news"  # Example news site
output_file = "headlines.txt"

# Fetch HTML content
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8", errors="ignore")

# Extract headlines from <h2> tags
headlines = []
start = 0
while True:
    start_h2 = html.find("<h2", start)
    if start_h2 == -1:
        break
    start_tag_end = html.find(">", start_h2) + 1
    end_h2 = html.find("</h2>", start_tag_end)
    headline = html[start_tag_end:end_h2].strip()
    if headline:
        headlines.append(headline)
    start = end_h2 + 5

# Save headlines to file
with open(output_file, "w", encoding="utf-8") as f:
    for h in headlines:
        f.write(h + "\n")

print("✅ Headlines saved to", output_file)
for i, h in enumerate(headlines, start=1):
    print(f"{i}. {h}")
