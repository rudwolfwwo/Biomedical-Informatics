import argparse
import urllib.request
import re

parser = argparse.ArgumentParser()

parser.add_argument("-i","--url",action="store",dest="url",type=str,required=True)
parser.add_argument("--summary",action="store_true",default=False,dest="bool")

args = parser.parse_args()

#regex_links = r"<a href(.*?)www(.*?)>(.*?)<\/a>"
regex = r"<a href(.*)>(.*)<\/a>"

list = []
try:
    with urllib.request.urlopen(args.url) as website:
        input = website.read().decode("utf-8")
        matches = re.findall(regex, str(input))
        list = [m[1] for m in matches]
        if len(list) == 0:
            print("Error: Shutting down")
            quit()
        if args.bool == False:
            for element in list:
                print(element)
except:
    print("Error: Shutting down")
    quit()
def summary(list):

    set = {element for element in list}
    l_without_dublicates = [s for s in set]
    words = 0
    chars = 0
    for s in set:
        words += s.count(" ") + 1
        chars += len(s)
    print("Number of links: ",len(set))
    print("Average number of words per link: ",words/len(set))
    print("Average number of characters per link: ",chars/len(set))
    return len(set),words/len(set),chars/len(set)


if args.bool == True:
    summary(list)


