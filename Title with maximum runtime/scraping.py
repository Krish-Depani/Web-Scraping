import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# define function to scrape movie data from links
def get_movies():
    # set up Chrome driver
    ser = Service("C:\\Users\\Hp\\Downloads\\chromedriver_win32\\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

    # read links from file and loop through them
    with open("links.txt", "r") as f:
        links = f.readlines()

    for link in links:
        # navigate to link and find movie elements
        driver.get(link[:-1])
        movies = driver.find_elements(By.XPATH, '//div[@class="lister-item-content"]')

        # loop through movie elements and write movie data to file
        with open("movies.txt", "a", encoding="utf-8") as m:
            for movie in movies:
                try:
                    # try to find movie name and runtime
                    name = movie.find_element(By.XPATH, './h3/a')
                    runtime = movie.find_element(By.XPATH, './p/span[@class="runtime"]')
                    m.write(f'{name.text} - {runtime.text}\n')
                except selenium.common.exceptions.NoSuchElementException:
                    # if movie name or runtime not found, write 0 for runtime
                    name = movie.find_element(By.XPATH, './h3/a')
                    m.write(f'{name.text} - {0}\n')

    driver.quit()


# define function to find movie with highest runtime
def max_runtime():
    mx_runtime = 0
    movie_name = ''

    # read movie data from file and find movie with highest runtime
    with open('movies.txt', 'r', encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(' - ')
            if len(parts) != 2:
                continue
            movie = parts[0]
            try:
                runtime = int(parts[1][:-4])
            except ValueError:
                continue
            if runtime > mx_runtime:
                mx_runtime = runtime
                movie_name = movie
    # return movie name and runtime in required format
    return f'{movie_name} {mx_runtime}'

print(max_runtime())