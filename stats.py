def get_num_words(text):
    text_splitted = text.split()
    num_words = len(text_splitted)
    return num_words

def get_enum_carac(text):
    enum_carac = {}
    for element in text.lower():
        if enum_carac.get(element):
            enum_carac[element] += 1
        else:
            enum_carac[element] = 1
    return enum_carac

def sort_dict(dict_carac):
    dict_list = []
    for key in dict_carac:
        dict_list.append({"char": key, "num": dict_carac[key]})
    sorted_dict_list = sorted(dict_list, key=lambda d:d["num"], reverse=True)
    return sorted_dict_list
