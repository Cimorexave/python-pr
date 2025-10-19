def top5(i_str):
    out = {}
    for i,c in enumerate(i_str.lower()):
        print(c)
        if (c in out):  
            out[c] += out[c]
        else:
            out[c] = 1

    # keep only top 5
        max_nums = []
    for value in out.values():
        if (len(max_nums) < 5):
            max_nums.append(value)
        else:
            
    # sort alphabetically 
    return out

top5("Hello Parallel Computing!") 

# assert top5("Hello Parallel Computing!") == {'l': 5, 'a': 2, 'e': 2, 'o': 2, 'p': 2}, top5("Hello Parallel Computing!")
assert top5("Wait... What?! Letters, lots of letters!!!") == {'t': 7, 'e': 4, 'l': 3, 's': 3, 'a': 2}, top5("Wait... What?! Letters, lots of letters!!!")
assert top5("The course 191.125 Scientific Programming with Python (VU 2,0) 2025W is awesome") == {'i': 6, 'e': 5, 'o': 4, 's': 4, 't': 4}, top5("The course 191.125 Scientific Programming with Python (VU 2,0) 2025W is awesome")