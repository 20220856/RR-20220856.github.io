# Python Kones - Interesting Problems, and Observations
This will serve as a collection of the experiences I have had so far with Python Koans. As of so far, I have found them to be engaging, thought-provoking, interesting, and rather challenging.

## Strings
### Backslashes for quotation
    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, \"Go Away.\"'
        self.assertEqual("He said, \"Go Away.\"", string)
I cannot describe the degree to which this problem initially had me confused. I must have pondered it for about an hour before I could figure out what the Kone was asking of me. The objective of the exercise is to prove that double-quotes can be used inside a double-quoted string, as long as they are preceeded by a backslash. In retrospect, the answer is obvious, but my journey there was rather frustrating -- imagine my relief when I figured it out.

### Automatically Concatenated Strings
    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)
This was not something I knew -- multiple strings placed next to each other will automatically concatenate. Could potentially prevent a lot of "a+b" shenanigans.

### "Plus Equals" String Appending
    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)
Rather than overwriting a variable (such as in the case of "a=b" - the original value of a is lost), += conserves the original value of the variable, appending the second variable to the end rather than overwriting it. This is very good to know, and may have in fact been beneficial during some of our coding exercises.

## Lists
### Accessing List Elements
    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual("peanut", noms[0])
        self.assertEqual("jelly", noms[3])
        self.assertEqual("jelly", noms[-1])
        self.assertEqual("butter", noms[-3])
This took more time for me to understand than I would care to admit. Referencing list elements can be done from the right side through the use of negative numbers. Useful in smaller lists where "for i in list" might not be applicable, but then I fail to see why one would not just right the list reference as a positive integer. I'm sure it has applications either way.

### Slicing parts of Lists
    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(["peanut"], noms[0:1])
        self.assertEqual(["peanut","butter"], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(["and","jelly"], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])
A useful way to reference multiple items in a list; and something I did not know. Relatively self explanatory, and good to know that lists cannot be recursively referenced (using example above, noms[4:100] does not cause the program to expect a recursion until 100 items are presented).

### Inserting into lists
    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(["you", "shall", "not", "pass"],knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(["Arthur","you","shall","not","pass"], knight)
I did not know that you can insert into lists in such a fashion - a handy piece of information, and one that I'm sure is invaluable when trying to manage larger datasets.

## List Assignments
### Parallel Assignments
    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky","Bobby"], first_names)
        self.assertEqual("Worthington", last_name)

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual("Mr", title)
        self.assertEqual([], first_names)
        self.assertEqual("Bond", last_name)
It was interesting to learn that parts of a list can be referenced and assigned to variables in this manner. I was - and I cannot stress this enough - *extremely* confused initially by the fact that - especially in the case of the second example, first_names was unassigned. However, I do understand now - progress!

## Dictionaries 
### Dictionary Literals
    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish))
Only the keys in a dictionary - and NOT all of the individual values are considered in the dictionary. It took me a while to understand that fact.
## Equality of Keys and Values
    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual("uno", babel_fish['one'])
        self.assertEqual("dos", babel_fish['two'])
Values in a dictionary are always equal to the Key from which they stem - a mildly difficult concept to get my head around - never before have I seen a scenario in which (True=("uno"="one")), but it turns out that, using the example above, it is certainly a possibility within a dictionary. *(also yes, I know that is not quite what is going on, but that was my initial thought process while trying to solve the Koan - hence my confusion*

## Disorganised Dictionaries
    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2)
It, apparently, does not matter if a dictionary is out of order. The more you know.

## Keys and Values
    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys()))
        self.assertEqual(2, len(babel_fish.values()))
        self.assertEqual(True, 'one' in babel_fish.keys())
        self.assertEqual(False, 'two' in babel_fish.values())
        self.assertEqual(False, 'uno' in babel_fish.keys())
        self.assertEqual(True, 'dos' in babel_fish.values())
This was the exercise that really helped me understand the difference between a Key and a Value. I had a hard time understanding, but then once I did, the material is extremely simple. I'm glad I persevered.
