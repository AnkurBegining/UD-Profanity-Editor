import urllib.request as ur
import urllib.parse as parse


def read_text():
    quotes = open("/home/ankur/PycharmProjects/Profanity Editor/Profanity Editor/movie_quotes.txt")
    content_of_file = quotes.read()
    quotes.close()
    check_profanity(content_of_file)
    #print(content_of_file)

def check_profanity(text_to_be_checked):
    quote = parse.quote_plus(text_to_be_checked)
    connection = ur.urlopen("http://www.wdylike.appspot.com/?q="+quote)
    output = connection.read().decode('utf-8')
    connection.close()
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("No Profanity Word")
    else:
        print("could not scan the documented")


read_text()