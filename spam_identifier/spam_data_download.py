# We’ll look at the files prefixed with 20021010 from https://spamassassin.apache.org/old/publiccorpus/
# Here is a script that will download and unpack them to the directory of your choice (or you can do it manually)

from io import BytesIO # So we can treat bytes as a file.
import requests # To download the files, which
import tarfile # are in .tar.bz format.
import glob, re
from typing import List

BASE_URL = "https://spamassassin.apache.org/old/publiccorpus"
FILES = ["20021010_easy_ham.tar.bz2",
"20021010_hard_ham.tar.bz2",
"20021010_spam.tar.bz2"]

# This is where the data will end up,
# in /spam, /easy_ham, and /hard_ham subdirectories.
# Change this to where you want the data.
OUTPUT_DIR = 'spam_data'

for filename in FILES:
    # Use requests to get the file contents at each URL.
    content = requests.get(f"{BASE_URL}/{filename}").content
    # Wrap the in-memory bytes so we can use them as a "file."
    fin = BytesIO(content)
    # And extract all the files to the specified output dir.
    with tarfile.open(fileobj=fin, mode='r:bz2') as tf:
        tf.extractall(OUTPUT_DIR)

# modify the path to wherever you've put the files
path = 'spam_data/*/*'

data: List[Message] = []
# glob.glob returns every filename that matches the wildcarded path
for filename in glob.glob(path):
    is_spam = "ham" not in filename
# There are some garbage characters in the emails; the errors='ignore'
# skips them instead of raising an exception.
    with open(filename, errors='ignore') as email_file:
        for line in email_file:
            if line.startswith("Subject:"):
                subject = line.lstrip("Subject: ")
                data.append(Message(subject, is_spam))
                break # done with this file
   
