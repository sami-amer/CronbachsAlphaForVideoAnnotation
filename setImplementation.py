def round_to_nearest_half(number):
    number = round(number * 2)
    return (number / 2)

def import_data(file_input):
    Behavioral_Engagement, Attention_Engagement, Emotional_Engagement = set(),set(),set()
    f = open(file_input)
    for line in f:
        line = line.split('\t')
        del(line[1])
        line[-1] = line[-1].strip("\n")
        if line[0] == 'default':
            continue
        start = round_to_nearest_half(float(line[1]))
        stop = round_to_nearest_half(float(line[2]))
        tag = line[4]
        if start == stop:
            print('interval from ' + str(line[1]) +' to' + str(line[2])+' too small, discarded')
        if line[0] == 'Behavioral_Engagement':
            for n in range(int(start*2),int(stop*2)+1):
                Behavioral_Engagement.add((n*0.5,tag))
        elif line[0] == 'Attention_Engagement':
            for n in range(int(start*2),int(stop*2)+1):
                Attention_Engagement.add((n*0.5,tag))
        elif line[0] == 'Emotional_Engagement':
            for n in range(int(start*2),int(stop*2)+1):
                Emotional_Engagement.add((n*0.5,tag))             
    f.close()
    return Behavioral_Engagement, Attention_Engagement, Emotional_Engagement

def cronbachs(b1,a1,e1,b2,a2,e2):
   N = (len(b1)+len(b2)) / 2 + (len(a1)+len(a2)) / 2 + (len(e1)+len(e2)) / 2
   
if __name__ == "__main__":
    # print(round_to_nearest_half(10.74))
    a,b,c = (import_data('p01_s02.txt'))
    d,e,f = (import_data('P01_S02_wellness_Emily.txt'))
    print(len(a),len(d))
    print(len(b),len(e))
    print(len(c),len(f))

    