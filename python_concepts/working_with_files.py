def break_down_poem(file):
    '''This function takes a text file that is  poem separated into lines
    and returns that poem as a list of lists, each list representing a line
    and containing all the words in that line, separated by commas'''
    poem = open(file).readlines()
    list_of_lines = []
    for line in poem:
        line = line.lower()
        list_of_lines.append(line.strip('.\n').split(" "))

    print(list_of_lines)


break_down_poem('the_hill_we_climb.txt')
