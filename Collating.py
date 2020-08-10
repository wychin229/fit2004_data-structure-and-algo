import timeit
def collate(filename):
    my_file = open(filename, "r")
    my_list = []
    for lines in my_file:
        lines = lines.strip("\n")
        lines = lines.split(":")
        if len(my_list) < 1: # append in the first item
            my_list.append(lines)
        else:
            # counter = 0
            # while counter < len(my_list)+1:
            #     if counter == len(my_list): # when the word is not found in my_list
            #         my_list.append(lines)
            #         break
            #     elif lines[0] == my_list[counter][0]:
            #         if lines[1] not in my_list[counter]:
            #             my_list[counter].append(lines[1])
            #             break
            #         else:
            #             break
            #     counter += 1
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
    # return my_list

start = timeit.default_timer()
collate("sorted_new_file1.txt")
# collate("example_sorted_words.txt")
taken = timeit.default_timer()-start
print("Time taken:",taken/60,"mins")
# print(collate("example_sorted_words.txt"))
# Time taken: 401.58946374668335 mins