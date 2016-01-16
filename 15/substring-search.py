input_string = 'mmmm mama'
search_string = 'mama'

result = -1
for index in range(0, len(input_string)):
    for search_string_index in range(0, len(search_string)):
        letter_in_search_string = search_string[search_string_index]

        # Cey poshuk vihodit za meji stroky -> stop it
        if (index + search_string_index >= len(input_string)):
            break;

        letter_in_input_string = input_string[index + search_string_index]
        if (letter_in_search_string != letter_in_input_string):
            # znaishly nespivpadinna --> stop it
            break;
        elif (len(search_string) - 1 == search_string_index):
            # diyshly do kincja malenkoi stroky --> ce vono
            result = index
    # yaksho vje znaishly rezultat -> dali nicho ne robymo, my vzhe tam
    if (result != -1):
        print result
        break
