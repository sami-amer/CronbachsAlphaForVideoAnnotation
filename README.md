# Cronbachs Alpha For Video Annotation

Takes two outputs from video annotation software and tests their reliability against each other using Cronbach's Alpha Formula
for inter-reliability

## Inputs

The inputs are tab-delimitted .txt files that are organized [type,start time, stop time, duration, tag]
Examples can be seen in the resources folder\
\
Libraries Used: `numpy, csv`

## Functions

#### `round_to_nearest_frac(number,fraction)`

This allows for variable seperation of times by rounding to the nearest fraction.  
The fraction argument tells it what to round to i.e. if the operater is 5, it will round to the nearest fifth

#### `import_data(file_input, interval)`

This function goes through the input and seperates it into 3 distinct lists to be used for later calculations: `Behavioral_Engagment`,`Attention_Engagement`,`Emotional_Engagement`\
The interval argument is passed to the rounding fucnton, and works simlilary i.e. if the interval is 2, cuts in halves.\
If an interval is too small (in other words, if the rounded start == rounded stop, making rounded duration == 0), the interval is skipped and a message is printed\

#### `save_default(files)` and `write_default(list)`

Simple functions that take a list of files in `save_default` which can be passed into `write_defualt` to create a csv of all entries tagged 'default'

#### ~~`equalizer(file1,file2, interval)`~~

~~Essentially the first step in the `find_cronbach` function, parses the input data, then makes the lists equal\
Currently chops off data from the ends, but can be updated to take the least signifcant data instead~~\
this is defunct now; everything is broken down to the smallest portion, which is milliseconds.

#### `cronbachs(list1,list2)`

Given two lists of tagged time intervals (output of `import_data` and by extension `equalizer`), runs [Cronbach's Alpha Formula](https://en.wikipedia.org/wiki/Cronbach%27s_alpha "Wikipedia Entry for Cronbach's")

#### `find_cronbachs(file1,file2,interval)`

Takes two files as inputs and an interval, and then runs `equalizer` twice to get 6 lists, and then computes `cronbachs` on the matching pairs of these lists.\
returns three values, an inter-reliability rating for each category (Behavior, Attention, Emotion)
