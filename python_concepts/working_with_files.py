def break_down_poem(file):
    '''This function takes a text file that is  poem separated into lines
    and returns that poem as a list of lists, each list representing a line
    and containing all the words in that line, separated by commas'''
    poem = open(file)
    print(poem)
    # print(poem[0])
    # list_of_lines = []
    # for line in poem:
    #     line = line.lower()
    #     stripped_line = line.strip('.\n')
    #     split_line = stripped_line.split(" ")
    #     list_of_lines.append(split_line)

    # print(list_of_lines)


break_down_poem('the_hill_we_climb.txt')
