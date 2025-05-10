import os
import pandas as pd

EXCEL_FILE = "local_seo_pages.xlsx"
OUTPUT_DIR = "generated_sites"

cities_df = pd.read_excel(EXCEL_FILE, sheet_name="Cities")
settings = pd.read_excel(EXCEL_FILE, sheet_name="Settings").iloc[0].to_dict()

sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.html")
sitemap_links = []

# Add all city pages
for _, row in cities_df.iterrows():
    slug = f"{row['city'].lower().replace(' ', '-')}-{row['state'].lower()}"
    url = f"https://{slug}.{settings['domain']}/"
    sitemap_links.append(f"<li><a href='{url}' target='_blank'>{row['city']}, {row['state']}</a></li>")

# Add all state pages
for state in sorted(cities_df['state'].unique()):
    url = f"https://{state.lower()}.{settings['domain']}/"
    sitemap_links.append(f"<li><a href='{url}' target='_blank'>{state} State Page</a></li>")

# Final HTML
sitemap_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HTML Sitemap</title>
    <meta name="robots" content="index, follow">
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        ul {{ columns: 3; column-gap: 30px; list-style: none; padding-left: 0; }}
        li {{ margin-bottom: 10px; }}
    </style>
</head>
<body>
    <h1>All Pages Sitemap</h1>
    <ul>
        {''.join(sitemap_links)}
    </ul>
</body>
</html>
"""

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_html)

print("✅ sitemap.html created successfully.")
