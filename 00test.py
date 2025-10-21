import string
from collections import Counter

def top5(i_str: str) -> dict:
    """
    Counts the occurrences of English alphabet letters in a string, 
    treating upper- and lowercase as identical. Returns a dictionary 
    containing the five letters with the highest frequencies, ordered 
    by frequency (descending) then lexicographically (ascending) for ties.
    """
    if not i_str:
        return {}

    filtered_chars = []
    for i , c in enumerate(i_str.lower()):
        if (c in string.ascii_lowercase): filtered_chars.append(c)
    
    counts = Counter(filtered_chars)
    
    sorted_items = sorted(
        counts.items(), 
        key=lambda item: (-item[1], item[0])
    )

    top_five_items = sorted_items[:5]
    return dict(top_five_items)


assert top5("Hello Parallel Computing!") == {'l': 5, 'a': 2, 'e': 2, 'o': 2, 'p': 2}, top5("Hello Parallel Computing!")
assert top5("Wait... What?! Letters, lots of letters!!!") == {'t': 7, 'e': 4, 'l': 3, 's': 3, 'a': 2}, top5("Wait... What?! Letters, lots of letters!!!")
assert top5("The course 191.125 Scientific Programming with Python (VU 2,0) 2025W is awesome") == {'i': 6, 'e': 5, 'o': 4, 's': 4, 't': 4}, top5("The course 191.125 Scientific Programming with Python (VU 2,0) 2025W is awesome")


def run_tests():
    print("Running top5 tests...")

    # 1. PROVIDED EXAMPLES (Demonstrates basic functionality and sorting)
    assert top5("Hello Parallel Computing!") == {'l': 5, 'a': 2, 'e': 2, 'o': 2, 'p': 2}, "Test 1 Failed: Example 1"
    assert top5("Wait... What?! Letters, lots of letters!!!") == {'t': 7, 'e': 4, 'l': 3, 's': 3, 'a': 2}, "Test 2 Failed: Example 2"
    assert top5("The course 191.125 Scientific Programming with Python (VU 2,0) 2025W is awesome") == {'i': 6, 'e': 5, 'o': 4, 's': 4, 't': 4}, "Test 3 Failed: Example 3"
    
    # 2. EDGE CASES - LENGTH AND EMPTY INPUT
    assert top5("") == {}, "Test 4 Failed: Empty String"
    assert top5("a") == {'a': 1}, "Test 5 Failed: Single Letter"
    assert top5("bbbbbaaaaa") == {'b': 5, 'a': 5}, "Test 6 Failed: Two Distinct Letters"
    assert top5("abc") == {'a': 1, 'b': 1, 'c': 1}, "Test 7 Failed: Fewer Than 5, Tied"
    
    # 3. FILTERING AND CASE INSENSITIVITY
    assert top5("123!@#$ ABC def") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}, "Test 8 Failed: Filtering Non-Alpha and Mixed Case"
    assert top5("ONLY NUMBERS 12345") == {'e': 1, 'm': 1, 'n': 1, 'o': 1, 'r': 1}, "Test 9 Failed: Ignore numbers/spaces"
    assert top5("áéíóú") == {}, "Test 10 Failed: Ignore non-ASCII/accented letters"
    
    # 4. DETAILED SORTING AND TIE-BREAKING
    
    # Case 4a: Top 5, varying counts, no ties
    assert top5("aaaaabbbbcccdd") == {'a': 5, 'b': 4, 'c': 3, 'd': 2}, "Test 11 Failed: No Ties"

    # Case 4b: Tie-breaker test 1 (a,b,c tied at 3, d,e tied at 2)
    # Correct order: (a,3), (b,3), (c,3), (d,2), (e,2) -> alphabetical tie-break
    assert top5("aaabbbcccddee") == {'a': 3, 'b': 3, 'c': 3, 'd': 2, 'e': 2}, "Test 12 Failed: Complex Tie-breaking 1"

    # Case 4c: Tie-breaker test 2 (All 6 letters tied at 2, only top 5 returned)
    # The letters b, c, d, e, f, g are tied at 2. Alphabetical selection of top 5: b, c, d, e, f.
    assert top5("bbccddeeffgg a") == {'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2}, "Test 13 Failed: Six letters tied, top 5 chosen alphabetically"

    # Case 4d: Tie-breaker test 3 (High count tie)
    # String: z=5, y=4, x=4, w=4. Top 4.
    # Sorted: (z,5), then (w,4), (x,4), (y,4) alphabetically.
    assert top5("zzzzzyyyyxxxxwwww") == {'z': 5, 'w': 4, 'x': 4, 'y': 4}, "Test 14 Failed: High Count Tie-breaker"
    
    # Case 4e: Exactly 5 distinct letters, all tied
    assert top5("abcdeABCDE") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}, "Test 15 Failed: Exactly 5 letters, all tied"
    
    # Case 4f: More than 5 letters, all tied, only top 5 returned
    # Letters a-z all appear once. Top 5 are a, b, c, d, e.
    assert top5("abcdefghijklmnopqrstuvwxyz") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}, "Test 16 Failed: All 26 letters, top 5 alphabetical"

    print("All 16 tests passed successfully!")

run_tests()