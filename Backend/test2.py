from bs4 import BeautifulSoup

# The description content from the RSS item
description_html = '''
<ol>
<li><a href="https://news.google.com/rss/articles/CBMiamh0dHBzOi8vYXBuZXdzLmNvbS9hcnRpY2xlL2luZGlhLWVsZWN0aW9uLXJlc3VsdHMtMjAyNC1sb2stc2FiaGEtbW9kaS1ianAtNzg5M2VmZWNjODNmYTgyMjVhNjExZjE3NGU2NDIwZWXSAQA?oc=5" target="_blank">India election results 2024: Modi's BJP ahead but opposition makes inroads</a>&nbsp;&nbsp;<font color="#6f6f6f">The Associated Press</font></li>
<li><a href="https://news.google.com/rss/articles/CBMiuQFodHRwczovL3d3dy5uZHR2LmNvbS9pbmRpYS1uZXdzL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1saXZlLXVwZGF0ZXMtbG9rLXNhYmhhLWVsZWN0aW9ucy1yZXN1bHRzLTIwMjQtYmpwLWNvbmdyZXNzLWluZGlhLWFsbGlhbmNlLW5hcmVuZHJhLW1vZGktcmFodWwtZ2FuZGhpLXdpbnMtd2F5YW5hZC1yYWViYXJlbGktNTgxMTA2N9IBAA?oc=5" target="_blank">Election Results 2024 Highlights: Lok Sabha Elections 2024, Lok Sabha Election Results, BJP, Congress, INDIA Alliance, Narendra Modi, Rahul Gandhi</a>&nbsp;&nbsp;<font color="#6f6f6f">NDTV</font></li>
<li><a href="https://news.google.com/rss/articles/CBMifWh0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9lbGVjdGlvbnMvbG9rLXNhYmhhL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1ianAtZmFsbHMtc2hvcnQtbmVlZHMtYWxsaWVzLXRvLWdvdmVybi9hcnRpY2xlNjgyNTIxOTIuZWNl0gGCAWh0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9lbGVjdGlvbnMvbG9rLXNhYmhhL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1ianAtZmFsbHMtc2hvcnQtbmVlZHMtYWxsaWVzLXRvLWdvdmVybi9hcnRpY2xlNjgyNTIxOTIuZWNlL2FtcC8?oc=5" target="_blank">BJP’s ‘400-paar’ hits INDIA wall, needs allies to govern</a>&nbsp;&nbsp;<font color="#6f6f6f">The Hindu</font></li>
<li><a href="https://news.google.com/rss/articles/CBMiamh0dHBzOi8vaW5kaWFuZXhwcmVzcy5jb20vYXJ0aWNsZS9leHBsYWluZWQvZXhwbGFpbmVkLXBvbGl0aWNzL2xvay1zYWJoYS1yZXN1bHRzLWJqcC1uZGEtcGFydG5lcnMtOTM3MjA3MC_SAQA?oc=5" target="_blank">Lok Sabha Results 2024: Why BJP's top NDA partners may stay with the alliance – and why they might leave</a>&nbsp;&nbsp;<font color="#6f6f6f">The Indian Express</font></li>
<li><a href="https://news.google.com/rss/articles/CBMiNmh0dHBzOi8vYXBuZXdzLmNvbS9saXZlL2luZGlhLWVsZWN0aW9uLXJlc3VsdHMtdXBkYXRlc9IBAA?oc=5" target="_blank">India election results: Modi claims victory for alliance</a>&nbsp;&nbsp;<font color="#6f6f6f">The Associated Press</font></li>
</ol>
'''

# Parse the HTML content
soup = BeautifulSoup(description_html, 'html.parser')

# Extracting data from the parsed HTML
news_items = []

for li in soup.find_all('li'):
    link = li.find('a', href=True)
    font = li.find('font')
    news_item = {
        'title': link.get_text(),
        'link': link['href'],
        'source': font.get_text() if font else ''
    }
    news_items.append(news_item)

# Print extracted data
for item in news_items:
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print(f"Source: {item['source']}")
    print("-" * 40)
