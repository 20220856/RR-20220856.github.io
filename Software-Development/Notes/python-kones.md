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
A useful way to reference multiple items in a list; and something I did not know. Relatively self explanatory, and good to know that lists cannot be recursively referenced (using example above, noms[4:100] does not cause the program to expect a recursion until 100 items are presented.
