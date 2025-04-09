from requests import get, request, status_codes

websites = (
  "google.com", "airbnb.com", "https://twitter.com", "facebook.com"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if 200 <= response.status_code <=300:
    print(f"Success: {website}")
    results[website] = "OK"
  else:
    print(f"Fail: {website}")
    results[website] = "Failed"

print(results)
  


  