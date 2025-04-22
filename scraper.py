import requests
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()  # returns a requests.Session object

# 경고 무시
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

for page in range(1, 3):  # 1~2페이지 반복
    if page == 1:
        url = "https://berlinstartupjobs.com/engineering/"
    else:
        url = f"https://berlinstartupjobs.com/engineering/page/{page}/"

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")

    print(f"\n🔹 Page {page} 🔹")
    for job in jobs:
        title = job.find("h4").text.strip()
        company = job.find("a", class_="bjs-jlid__b").text.strip()
        link = job.find("a")["href"]

        print("제목:", title)
        print("회사:", company)
        print("링크:", link)
        print("-" * 40)

#https://berlinstartupjobs.com/skill-areas/python/
# 1. URL 설정
url_python = "https://berlinstartupjobs.com/skill-areas/python/"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
# 2. 웹페이지 요청
response_python = requests.get(url_python, headers=headers)

# 3. BeautifulSoup으로 HTML 파싱
soup_python = BeautifulSoup(response_python.text, "html.parser")

# 4. 채용 공고 가져오기
jobs_python = soup_python.find_all("li", class_="bjs-jlid")

# 5. 출력
print("\n🔹 Python Jobs 🔹")
for job_python in jobs_python:
    title = job_python.find("h4").text
    company = job_python.find("a", class_="bjs-jlid__b").text.strip()
    link = job_python.find("a")["href"]

    print("제목:", title)
    print("회사:", company)
    print("링크:", link)
    print("-" * 40)

#https://berlinstartupjobs.com/skill-areas/typescript/
# 1. URL 설정
url_typescript = "https://berlinstartupjobs.com/skill-areas/typescript/"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
# 2. 웹페이지 요청
response_typescript = requests.get(url_typescript, headers=headers)

# 3. BeautifulSoup으로 HTML 파싱
soup_typescript = BeautifulSoup(response_typescript.text, "html.parser")

# 4. 채용 공고 가져오기
jobs_typescript = soup_typescript.find_all("li", class_="bjs-jlid")

# 5. 출력
print("\n🔹 TypeScript Jobs 🔹")
for job_typescript in jobs_typescript:
    title = job_typescript.find("h4").text
    company = job_typescript.find("a", class_="bjs-jlid__b").text.strip()
    link = job_typescript.find("a")["href"]

    print("제목:", title)
    print("회사:", company)
    print("링크:", link)
    print("-" * 40)

#https://berlinstartupjobs.com/skill-areas/javascript/
# 1. URL 설정
url_javascript = "https://berlinstartupjobs.com/skill-areas/javascript/"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
# 2. 웹페이지 요청
response_javascript = requests.get(url_javascript, headers=headers)

# 3. BeautifulSoup으로 HTML 파싱
soup_javascript = BeautifulSoup(response_javascript.text, "html.parser")

# 4. 채용 공고 가져오기
jobs_javascript = soup_javascript.find_all("li", class_="bjs-jlid")

# 5. 출력
print("\n🔹 JavaScript Jobs 🔹")
for job_javascript in jobs_javascript:
    title = job_javascript.find("h4").text
    company = job_javascript.find("a", class_="bjs-jlid__b").text.strip()
    link = job_javascript.find("a")["href"]

    print("제목:", title)
    print("회사:", company)
    print("링크:", link)
    print("-" * 40)
