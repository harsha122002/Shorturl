from pyshorteners import Shortener
url="https://internship.codeclause.com/"
url_shortener = Shortener()
print("Short URL {}",format(url_shortener.tinyurl.short(url)))



