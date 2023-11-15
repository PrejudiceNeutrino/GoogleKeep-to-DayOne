# What does this do?

This code converts Google Keep notes into a .csv that can be imported into DayOne via iOS.

# How?

There are 2 versions of this code available.

The first will just iterate through the folder of .json files, convert the UNIX timestamps into readible times/dates based off when the note was created, and then combine this into a .csv that you can then import into DayOne.

The second method will do the same as the first, but will search for duplicate texts relative to another .csv file. I used this one since I switched from Apple to a Google Pixel and had some duplicate notes.

All you need to do to use this code is input the JSON folder path and define the .csv file paths.

If you get any errors, just feed them back into ChatGPT.
