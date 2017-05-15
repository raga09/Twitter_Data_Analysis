#!/usr/bin/python
import sys
import subprocess
import StringIO
import csv
import re
import string


class textanalysis(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def analyse(self):

        regex = re.compile('[%s]' % re.escape(string.punctuation))

        with open(self.filepath, "rb") as f_obj:
            reader = csv.reader(f_obj)
            with open("test.csv", "wb") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for row in reader:
                    # print[row]
                    review = row[1]
                    review = re.sub('br]', '<br />', review)
                    review = re.sub("(RT|via)((?:\\b\\W*@\\w+)+)", "", review)
                    review = re.sub("@\\w+", "", review)
                    review = re.sub("#\\w+", "", review)
                    review = regex.sub('', review)
                    review = re.sub(" \d+", " ", review)
                    review = re.sub("http\\w+", "", review)
                    review = re.sub(" \t]{2,}", "", review)
                    review = re.sub("^\\s+|\\s+$", "", review)
                    review = re.sub("amp", "", review)
                    review = review.lower()
                    if review != '':
                        writer.writerow([review])


def main():
    script, filepath = sys.argv
    textanalysisobj = textanalysis(filepath)
    textanalysisobj.analyse()


if __name__ == "__main__":
    main()


