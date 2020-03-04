## The text files have typos: code has been written to accomodate them
## tags should be normalized for capitlization and spelling

import numpy as np


def round_to_nearest_frac(number,frac):
    '''
    Round to the nearest fraction i.e. when frac = 2, rounds to the nearest half, when frac = 3 rounds to the nearest 3
    '''
    number = round(number * frac)
    return number / frac


def import_data(file_input,interval):
    '''
    takes a file input and the interval for the timestaps to be seperated into
    '''
    Behavioral_Engagement, Attention_Engagement, Emotional_Engagement = [], [], []
    f = open(file_input)
    for line in f:
        line = line.split("\t")
        del line[1]
        line[-1] = line[-1].strip("\n")
        if line[0] == "default":
            continue
        start = round_to_nearest_frac(float(line[1]),interval)
        stop = round_to_nearest_frac(float(line[2]),interval)
        if line[4] == "off-tsak" or line[4] == "distarcted" or line[4] == "Bored":
            tag = 0
        if line[4] == "on-task" or line[4] == "idle" or line[4] == "Confused":
            tag = 1
        if line[4] == "Satisfied" or line[4] == "focused":
            tag = 2
        if start == stop:
            print(
                "interval from "
                + str(line[1])
                + " to"
                + str(line[2])
                + " too small, discarded"
            )
        if line[0] == "Behavioral_Engagement":
            for n in range(int(start * interval), int(stop * interval) + 1):
                Behavioral_Engagement.append(tag)
        elif line[0] == "Attention_Engagement":
            for n in range(int(start * interval), int(stop * interval) + 1):
                Attention_Engagement.append(tag)
        elif line[0] == "Emotional_Engagement":
            for n in range(int(start * interval), int(stop * interval) + 1):
                Emotional_Engagement.append(tag)
    f.close()
    return Behavioral_Engagement, Attention_Engagement, Emotional_Engagement


def equalizer(file1, file2,interval):
    '''
    equalizes length of the lists so that they can be converted.  currently only chops off the end of the longer list 
    '''
    b1, a1, e1 = import_data(file1,interval)
    b2, a2, e2 = import_data(file2,interval)
    if len(b1) != len(b2):
        if len(b1) > len(b2):
            diff = len(b1) - len(b2)
            b1 = b1[: len(b1) - diff]
        else:
            diff = len(b2) - len(b1)
            b2 = b2[: len(b2) - diff]

    if len(a1) != len(a2):
        if len(a1) > len(a2):
            diff = len(a1) - len(a2)
            a1 = a1[: len(a1) - diff]
        else:
            diff = len(a2) - len(a1)
            a2 = a2[: len(a2) - diff]

    if len(e1) != len(e2):
        if len(e1) > len(e2):
            diff = len(e1) - len(e2)
            e1 = e1[: len(e1) - diff]
        else:
            diff = len(e2) - len(e1)
            e2 = e2[: len(e2) - diff]
    return (b1, a1, e1, b2, a2, e2)


def find_cronbachs(file1, file2,interval):
    b1, a1, e1, b2, a2, e2 = equalizer(file1, file2,interval)
    b = cronbachs(b1, b2)
    a = cronbachs(a1, a2)
    d = cronbachs(e1, e2)
    return (
        "\nBehavioral: "
        + str(b)
        + "\nAttentional: "
        + str(a)
        + "\nEmotional: "
        + str(d)
        + "\n"
    )


def cronbachs(list1, list2):
    '''
    implementation of cronbachs alpha 
    '''
    N = len(list1)
    var = (np.var(list1) + np.var(list2)) / 2
    covar = np.cov(list1, list2)[0][1]
    return (N * covar) / (var + (N - 1) * covar)


if __name__ == "__main__":
    print(find_cronbachs("p01_s02.txt", "P01_S02_wellness_Emily.txt",2))
