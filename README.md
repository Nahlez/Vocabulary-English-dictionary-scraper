This was an old script that I used to create a csv to import into Anki.

# Vocab Dictionary Scrap to csv.

This repository should be used after obtaining the file "***vocab.csv***" from [this another script.](https://github.com/Nahlez/Add-new-vocabulary-to-a-csv "this another script.")

**Requeriments:**

- Python 3.
- The python module: [Selenium.](https://selenium-python.readthedocs.io/installation.html "Selenium.")

The script was only tested in Windows. Please feel free to clone/fork the repo and use it in your own S.O.

**How to use the script:**

- Once you have generated the "Vocab.csv" file with the vocabulary you want to learn, paste it in the root of this folder.
- Then open "Dictionary Scrap to csv". As a result (after selenium has obtained the data). You will have a file called csv-vocab-anki.csv" with the next four fields:

1) The english word with the spanish translation inside parentheses.
2) only the English word (This is because maybe you need to use it to generate audios with some TTS extension).
3) The meaning of the word.
4) the example of how to use the word.



Note: If you want to test this repository without using my other script, you can rename "input used for output.csv" to "vocab.csv".

