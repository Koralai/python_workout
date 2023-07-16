def format_word_count_data(list_name, num_rows=10):
    """
    Accepts word count data (in the form of a list of tuples: each tuple
    contains the word and its count). Print the data in a table, with the
    specified number of rows (or 10 rows by default).
    """
    
    output = ("--------------------------------------\n"
              "| WORD                      | # USES |\n"
              "--------------------------------------\n")
    
    i = 1
    for datum in list_name:
        if i <= num_rows:
            word = datum[0]
            count = datum[1]
            output += f"| {word:25} | {count:6} |\n"
            i += 1
    
    output += "--------------------------------------"
    
    return output
