import timeit
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

start = timeit.default_timer()
lookup("collated.txt","query.txt")
taken = timeit.default_timer()-start
print("Time taken:",taken/60,"mins")