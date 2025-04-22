import requests
import cloudscraper
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
BASE_URL = "https://berlinstartupjobs.com"

scraper = cloudscraper.create_scraper()  # returns a requests.Session object

for page in range(1, 3):  # 1~2페이지 반복
    if page == 1:
        url = f"{BASE_URL}/engineering/"
    else:
        url = f"{BASE_URL}/engineering/page/{page}/"

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")

    print(f"\n🔹 Page {page} 🔹")
    for job in jobs:
        title = job.find("h4").text.strip()
        company = job.find("a", class_="bjs-jlid__b").text.strip()
        link = job.find("a")["href"]
        discription = job.find("div",
                               class_="bjs-jlid__description").text.strip()

        print("제목:", title)
        print("회사:", company)
        print("링크:", link)
        print("설명:", discription)
        print("-" * 40)


def scraper(word):
    # 1. URL 설정
    url_word = f"{BASE_URL}/skill-areas/{word}/"
    # 2. 웹페이지 요청
    response_word = requests.get(url_word, headers=HEADERS)

    # 3. BeautifulSoup으로 HTML 파싱
    soup_word = BeautifulSoup(response_word.text, "html.parser")

    # 4. 채용 공고 가져오기
    jobs_word = soup_word.find_all("li", class_="bjs-jlid")

    # 5. 출력
    upper_word = word.capitalize()
    print(f"\n🔹 {upper_word} Jobs 🔹")
    for job_word in jobs_word:
        title = job_word.find("h4").text
        company = job_word.find("a", class_="bjs-jlid__b").text.strip()
        link = job_word.find("a")["href"]
        discription = job_word.find(
            "div", class_="bjs-jlid__description").text.strip()

        print("제목:", title)
        print("회사:", company)
        print("링크:", link)
        print("설명:", discription)
        print("-" * 40)


#https://berlinstartupjobs.com/skill-areas/python/
scraper("python")

#https://berlinstartupjobs.com/skill-areas/typescript/
scraper("typescript")

#https://berlinstartupjobs.com/skill-areas/javascript/
scraper("javascript")
