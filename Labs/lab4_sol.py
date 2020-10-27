# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        if self.my_dict:
            self.create_html(self.my_dict)
        else:
            print("Issue with input file, please check!")

    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}

        try:
            fo = open("gettisburg.txt", "r")
        except Exception as e:
            my_dict = False
            print("Caught this error: %s" % e.__class__.__name__)
        else:
            stop_words = ("the", "a", "that", "we", "to", "here", "and", "have", "of", "for",
                          "it", "in", "us", "this")
            stops_list = []
            try:
                stops = open("stops.txt", "r")
            except Exception as e:
                print (e)
            else: # no errors
                stops_list = list(stops.read().split("\n"))
                stops.close()
            finally: #with or without errors here, do this
                for line in fo:
                    line = line.lower()
                    line = line.split()
                    ##print(line)
                    for w in line:
                        if (stops_list and w in stops_list) or (not stops_list and w in stop_words):
                            continue
                        else:
                            self.add_to_dict(w, my_dict)
                fo.close()

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        for key in the_dict.keys():
            if key == word:
                the_dict[key] = the_dict[key] + 1
                return the_dict
        else:
            the_dict[word] = 1
            return the_dict

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        try:
            fo = open("output.html", "w")
        except Exception as e:
            print("Caught this error: %s" % e.__class__.__name__)
        else:
            fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

            ###fo.write('<span style="font-size: 10px"> WORD </span> </span>')

            for key in the_dict.keys():
                fo.write('<span style="font-size: ')
                fo.write(str(the_dict[key] * 10))
                fo.write('px"> ')
                fo.write(key)
                fo.write('</span>')

            fo.write('</div>\
        </body>\
        </html>')


wc = WordCloud()
