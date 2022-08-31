# Python Kones - Interesting Problems, and Observations
This will serve as a collection of the experiences I have had so far with Python Koans. As of so far, I have found them to be engaging, thought-provoking, interesting, and rather challenging.

## Strings
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
