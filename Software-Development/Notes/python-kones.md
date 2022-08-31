# Python Kones - Interesting Problems, and Observations
This will serve as a collection of the experiences I have had so far with Python Koans. As of so far, I have found them to be engaging, thought-provoking, interesting, and rather challenging.

## Strings
### Automatically Concatenated Strings
    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)
This was not something I knew -- multiple strings placed next to each other will automatically concatenate. Could potentially prevent a lot of "a+b" shenanigans.
