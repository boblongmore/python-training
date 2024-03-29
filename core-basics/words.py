#!/usr/bin/env python

from urllib.request import urlopen
import sys


def fetch_words(url):
    """fetch a list of words from a url.
      Args:
        url: The URL of UTF-8 text doc
      Returns:
       A list of strings conatining the words from 
       the document.
      """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1])