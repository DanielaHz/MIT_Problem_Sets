# Problem Set 5 - RSS Feed Filter

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

# ======================
# Data structure design
# ======================

# Problem 1
# TODO: NewsStory


class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

# ======================
# Triggers
# ======================


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        text = text.lower()

        for char in string.punctuation:
            text = text.replace(char, ' ')

        text = ' '.join(text.split())

        words = text.split()
        phrase_words = self.phrase.split()

        words = text.split()
        phrase_words = self.phrase.split()

        for i in range(len(words) - len(phrase_words) + 1):
            if words[i:i + len(phrase_words)] == phrase_words:
                return True

        return False

    def evaluate(self, story):
        pass

# Problem 3
# TODO: TitleTrigger


class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):
        if isinstance(story, NewsStory):
            title = story.get_title()
            return self.is_phrase_in(title)
        else:
            raise TypeError('Title not relative story')

# Problem 4
# TODO: DescriptionTrigger


class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):
        if isinstance(story, NewsStory):
            description = story.get_description()
            return self.is_phrase_in(description)
        else:
            raise TypeError('Description not relative story')

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger


class TimeTrigger(Trigger):
    def __init__(self, time):
        est_tz = pytz.timezone('EST')
        time_obj = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        time_est = est_tz.localize(time_obj)
        self.time = time_est

    def evaluate(self, story):
        pass

# Problem 6
# TODO: BeforeTrigger


class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        super().__init__(time)

    def evaluate(self, story):
        if isinstance(story, NewsStory):
            est_tz = pytz.timezone('EST')
            pubdate_est = story.get_pubdate().astimezone(est_tz)
            return pubdate_est < self.time

# TODO: AfterTrigger


class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        super().__init__(time)

    def evaluate(self, story):
        if isinstance(story, NewsStory):
            est_tz = pytz.timezone('EST')
            pubdate_est = story.get_pubdate().astimezone(est_tz)
            return pubdate_est > self.time


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, x):
        return not self.trigger.evaluate(x)


# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, x):
        return self.trigger1.evaluate(x) and self.trigger2.evaluate(x)


# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, x):
        return self.trigger1.evaluate(x) or self.trigger2.evaluate(x)


# ======================
# Filtering
# ======================

# Problem 10
# TODO: Filter_stories ()

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        if any([T.evaluate(story) for T in triggerlist]):
            filtered_stories.append(story)

    return filtered_stories


# ======================
# User-Specified Triggers
# ======================

# Problem 11
# TODO: Complete the read_trigger_config()

FILENAME = 'problem_set_5/triggers.txt'


def read_trigger_config():
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!

    trigger_file = open(FILENAME, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
        # Initialize trigger mapping dictionary
    t_map = {"TITLE": TitleTrigger,
             "DESCRIPTION": DescriptionTrigger,
             "AFTER": AfterTrigger,
             "BEFORE": BeforeTrigger,
             "NOT": NotTrigger,
             "AND": AndTrigger,
             "OR": OrTrigger
             }

    # Initialize trigger dictionary, trigger list
    trigger_dict = {}
    trigger_list = []

    # Helper function to parse each line, create instances of Trigger objects,
    # and execute 'ADD'
    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]],
                                                       trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else:
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)

    return trigger_list


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("niños ")
        t2 = DescriptionTrigger("perdidos")
        t3 = DescriptionTrigger("selva")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config()

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14),
                    yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(
                    END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
