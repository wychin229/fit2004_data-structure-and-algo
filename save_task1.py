def process(filename):
    my_file = open(filename, "r")
    my_list = []
    """
    puts the words corresponding to the id into tuple and append into a list
    """
    # lyrics = []
    # for lines in my_file:
    #     lines = lines.split(":")
    #     lyrics.append(lines)
    # print(lyrics)
    # for i in range(len(lyrics)):
    #     counting_sort_stable(lyrics,lyrics[i][0])

    for lines in my_file:
        lines = lines.strip("\n")
        lines = lines.replace(":", " ")
        words = lines.split(" ")
        for i in range(1, len(words)):
            my_list.append((words[i], words[0]))

    """
    find the longest word and sort them by length
    index of the max element (longest word)
    """

    # sort by the id first

    my_max = 0
    # find the maximum element
    for k in range(1, len(my_list)):
        (lyric, id) = my_list[k]
        if len(lyric) > len(my_list[my_max][0]):
            my_max = k
    max_length = len(my_list[my_max][0])

    counting = []
    # the length of the longest word + 1
    for _ in range(max_length + 1):
        counting.append([])
    for k in range(len(my_list)):
        counting[len(my_list[k][0])].append(my_list[k])
    # new_list = []
    # # try to no make a new list , but to "plus" up the ones that wanna pass into counting sort
    # for i in range(len(counting)-1,0,-1): # start from index 25 , minus until 0
    #     for k in range(len(counting[i])):
    #         new_list.append(counting[i][k])
    #     my_list = counting_sort_stable(new_list,i-1)
    # return my_list

    i = len(counting) - 1  # index 25
    while len(counting) > 1:  # loop thru from 0 - longest word length
        # start sorting from the longest word length etc. 25, and character 24 (length-1 for word indexing)
        counting[i] = counting_sort_stable(counting[i], i - 1)
        last = counting.pop(i)
        counting[len(counting) - 1] += last
        i -= 1
    my_list = counting[0]

    for i in range(len(my_list)):
        my_list[i] = ":".join(my_list[i]) + "\n"

    # write to new file
    new_file = open("sorted_words.txt", "w")
    new_file.writelines(my_list)
    new_file.close()


def counting_sort_stable(my_list, target=None):
    """
    Assume my_list is alist of numbers
    its similar to a linked array
    """
    my_max = my_list[0]  # a tuple (lyric, id)
    # find the maximum element
    if len(my_list) > 1:
        for k in range(1, len(my_list)):
            if my_list[k][0][target] > my_max[0][target]:
                my_max = my_list[k]

    counting = []
    for _ in range(26):
        counting.append([])

    # uses ord() to get the corresponding number to the characters
    for k in range(len(my_list)):
        counting[ord(my_list[k][0][target]) - 97].append(my_list[k])
    index = 0
    """
    the complexity is also O(n) even though there is a while loop,
    this is because there is still N items that is terminated.
    """
    for i in range(len(counting)):
        item = counting[i]
        while len(item) > 0:
            my_list[index] = item.pop(0)
            index += 1
    return my_list


process("example_songs.txt")