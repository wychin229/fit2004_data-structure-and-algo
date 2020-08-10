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

    # sort the individual words by length
    for _ in range(len(lyrics)):
        lyrics[0] = " ".join(lyrics[0])
        words = lyrics.pop(0)
        words = words.split(" ")
        for j in range(1,len(words)):
            if len(words[j])>0:
                words[j] = (words[j],words[0])
                lyrics.append(words[j])
    lyrics = counting_sort_stable(lyrics,"length")

    i = len(lyrics)-1
    while len(lyrics) > 1: # loop through from 0 - longest word length
        # start sorting from the longest word length etc. 25,
        # and character 24 (length-1 for word indexing)
        lyrics[i] = counting_sort_stable(lyrics[i],i-1)
        last = lyrics.pop(i)
        lyrics[len(lyrics)-1] += last # concat the pop item to the last item in list
        i -= 1
    my_list = lyrics[0]

    for i in range(len(my_list)):
        my_list[i] = ":".join(my_list[i])+"\n"

    # write to new file
    new_file = open("sorted", "w")
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
    for i in range(len(counting)):
        item = counting[i]
        while len(item) > 0:
            a_list[index] = item.pop(0)
            index += 1
    return a_list

def collate(filename):
    my_file = open(filename, "r")
    my_list = []
    for lines in my_file:
        lines = lines.strip("\n")
        lines = lines.split(":")
        if len(my_list) < 1: # append in the first item
            my_list.append(lines)
        else:
            if lines[0] == my_list[len(my_list)-1][0]: # if word is already in list

                if int(lines[1]) > int(my_list[len(my_list)-1][len(my_list[len(my_list)-1])-1]): # if id not in list
                    my_list[len(my_list)-1].append(lines[1])
            else:
                my_list.append(lines)

    for i in range(len(my_list)):
        if len(my_list[i])<3:
            my_list[i] = ":".join(my_list[i])+"\n"
        else:
            ids = " ".join(my_list[i][1:])
            my_list[i] = my_list[i][0]+":"+ids+"\n"
    new_file = open("collated.txt", "w")
    new_file.writelines(my_list)
    new_file.close()

def lookup(collated_file,query_file):
    queries = open(query_file, "r")
    collated = open(collated_file,"r")
    a_list = []
    for lines in collated:
        lines = lines.strip("\n")
        lines = lines.replace(":"," ")
        lines = lines.split(" ")
        a_list.append(lines)

    result = []
    for query in queries:
        query = query.strip("\n")
        result.append(binarySearch(a_list,query))

    new_file = open("songs_ids.txt", "w")
    for i in range(len(result)):
        if result[i]>=0:
            new_file.writelines(" ".join(a_list[result[i]][1:])+"\n")
        else:
            new_file.writelines("Not found"+"\n")
    new_file.close()

def binarySearch(arr, x):
    left = 0
    right = len(arr)
    while (left <= right):
        middle = left + ((right - left) // 2)

        # Check if x is present at mid
        if arr[middle][0] == x:
            return middle

        # If x greater, ignore left half
        if arr[middle][0] < x:
            left = middle + 1

        # If x is smaller, ignore right half
        else:
            right = middle - 1
    return -1

if __name__ == "__main__":
    song_file = "new_file1.txt"
    sorted_file = "sorted_new_file1.txt"
    collated_file = "collated_new_ids1.txt"
    query_file = "query.txt"
    start = timeit.default_timer()
    process(song_file)
    taken1 = timeit.default_timer()-start
    collate(sorted_file)
    taken2 = timeit.default_timer()-taken1
    lookup(collated_file, query_file)
    taken3 = timeit.default_timer()-taken2
    taken4 = timeit.default_timer()-start
    print("task1 time taken -->",taken1)
    print("task2 time taken -->", taken2)
    print("task3 time taken -->", taken3)
    print("all task time taken -->", taken4)
    """
    task1 time taken --> 87.365329057
    task2 time taken --> 4.115126520000004
    task3 time taken --> 87.778085468
    all task time taken --> 91.863225539
    """
