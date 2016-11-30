import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html')
soup = BeautifulSoup(r.content, "html.parser")

content = soup.find_all("pre")
bee_script = content[0].text

with open("bee_movie_script.txt", "w") as text_file:
    text_file.write(bee_script)
