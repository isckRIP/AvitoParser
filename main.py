from Browser.HTMLGetter import HtmlGetter

source = HtmlGetter("https://pskov.gorodrabot.ru/resumes?s=%D0%B4%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%BD%D0%B0%D1%8F")
source.html_getting()
print(source.source)
