import requests
from bs4 import BeautifulSoup

class PullURL:
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    # print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="ResultsContainer")
    # print(results.prettify())

    job_elements = results.find_all("div", class_="card-content")
    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
    )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs # List Comprehension: new_list = [expression for member in iterable], define the list and contents at the same time to be filled
    ]

    # print(len(python_job_elements))

    for job_element in python_job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        links = job_element.find_all("a")

        print(title_element.text)
        print(company_element.text)
        print(location_element.text)

        # looping would provide 2 links
        # for link in links:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")

        # print(job_element, end="\n" * 2)

