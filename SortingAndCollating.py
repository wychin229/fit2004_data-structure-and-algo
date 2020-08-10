import timeit
def process(filename):
    my_file = open(filename,"r")
    """
    puts the words corresponding to the id into tuple and append into a list
    """
    # pre-process the list so that the list is sorted according to the song ID,
    # so that the algorithm maintain the stability
    lyrics = []
    for lines in my_file:
        lines = lines.strip("\n")
        lines = lines.split(":")
        lyrics.append(lines)
    lyrics = counting_sort_stable(lyrics)
    # print(lyrics)
    # sort the individual words by length
    print(lyrics[0:2])
    for _ in range(len(lyrics)):
        lyrics[0] = " ".join(lyrics[0])
        words = lyrics.pop(0)
        words = words.split(" ")
        for j in range(1,len(words)):
            if len(words[j])>0:
                words[j] = (words[j],words[0])
                lyrics.append(words[j])
    lyrics = counting_sort_stable(lyrics,"length")
    print(lyrics[0:2])
    i = len(lyrics)-1
    while len(lyrics) > 1: # loop through from 0 - longest word length
        # start sorting from the longest word length etc. 25,
        # and character 24 (length-1 for word indexing)
        lyrics[i] = counting_sort_stable(lyrics[i],i-1)
        # print(lyrics[i])
        # print(lyrics)
        last = lyrics.pop(i)
        # print(lyrics)
        lyrics[len(lyrics)-1] += last # concat the pop item to the last item in list
        # print(lyrics)
        i -= 1
    my_list = lyrics[0]

    for i in range(len(my_list)):
        my_list[i] = ":".join(my_list[i])+"\n"

    # write to new file
    new_file = open("sorted_new_file1.txt", "w")
    new_file.writelines(my_list)
    new_file.close()

def counting_sort_stable(a_list, target=None):
    my_max = a_list[0]
    counting = []
    # sorting by ID
    if target is None and len(a_list) > 1:
        my_max = int(a_list[0][0])
        for k in range(1, len(a_list)):
            if int(a_list[k][0]) > my_max:
                my_max = int(a_list[k][0])

        for _ in range(my_max + 1):
            counting.append([])

        for k in range(len(a_list)):
            counting[int(a_list[k][0])].append(a_list[k])

    # sort using the length of the word
    elif target == "length":
        my_max = len(a_list[0][0])
        for k in range(1, len(a_list)):
            if len(a_list[k][0]) > my_max:
                my_max = len(a_list[k][0])

        for _ in range(my_max + 1):
            counting.append([])

        for k in range(len(a_list)):
            counting[len(a_list[k][0])].append(a_list[k])
        return counting

    # sort by alphabet
    else:
        for k in range(1, len(a_list)):
            if a_list[k][0][target] > my_max[0][target]:
                my_max = a_list[k]

        for _ in range(26): # 26 character , a=0, z=25
            counting.append([])

        # uses ord() to get the corresponding number to the characters
        for k in range(len(a_list)):
            counting[ord(a_list[k][0][target]) - 97].append(a_list[k])  # a starts from 0

    index = 0
    """
    the complexity is also O(n) even though there is a while loop,
    this is because there is still N items that is terminated.
    """
    for i in range(len(counting)):
        item = counting[i]
        while len(item) > 0:
            a_list[index] = item.pop(0)
            index += 1
    return a_list

start = timeit.default_timer()
process("new_file1.txt")
taken = timeit.default_timer()-start
print("Time taken:",taken/60,"mins")
# process("example_songs.txt")
# Time taken: 1.4497648792 mins