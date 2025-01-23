.. _qa_utils:

===========================
`utils.py` - Utility Methods
===========================

This module provides utility functions for text matching and phrase extraction within a given context. These functions are particularly useful for text-based QA systems that need to find and validate excerpts within larger documents or contexts.

Functions
=========

`find_text`
-----------

**Description:**
Identifies matching spans of text from a search span within a larger context. This function uses the `SequenceMatcher` from Python's `difflib` to compute matching blocks and returns merged spans for the matches.

**Parameters:**
- `search_span` (str): The text span to be searched within the context.
- `context` (str): The larger context in which to search for the `search_span`.
- `min_length` (int): The minimum length for a match to be considered valid (default: 5).

**Returns:**
- A list of tuples representing the start and end indices of matching spans within the context.

**Key Details:**
- If the search span's length is less than `min_length`, no search is performed.
- Merges overlapping matches into a single span.

---

`find_start_end_phrase`
-----------------------

**Description:**
Finds the start and end positions of a phrase pair (`start_phrase` and `end_phrase`) in a given context. This function is optimized to ensure that excerpts are not excessively long.

**Parameters:**
- `start_phrase` (str): The phrase marking the start of the target span.
- `end_phrase` (str): The phrase marking the end of the target span.
- `context` (str): The larger context in which to locate the phrases.
- `min_length` (int): The minimum length for a match to be considered valid (default: 5).
- `max_excerpt_length` (int): The maximum permissible length for an excerpt (default: 300).

**Returns:**
- `final_match` (tuple): A tuple with start and end indices of the matched span, or `None` if no match is found.
- `matched_length` (int): Total length of the matched phrases.

**Key Details:**
- Avoids cases where the `end_phrase` appears before the `start_phrase`.
- Ensures the matched excerpt does not exceed the specified maximum length.

Source Code
===========

.. code-block:: python

    from difflib import SequenceMatcher

    def find_text(search_span, context, min_length=5):
        sentence_list = search_span.split("\n")
        context = context.replace("\n", " ")

        matches_span = []
        # don't search for small text
        if len(search_span) > min_length:
            for sentence in sentence_list:
                match_results = SequenceMatcher(
                    None,
                    sentence,
                    context,
                    autojunk=False,
                ).get_matching_blocks()

                matched_blocks = []
                for _, start, length in match_results:
                    if length > max(len(sentence) * 0.2, min_length):
                        matched_blocks.append((start, start + length))

                if matched_blocks:
                    start_index = min(start for start, _ in matched_blocks)
                    end_index = max(end for _, end in matched_blocks)
                    length = end_index - start_index

                    if length > max(len(sentence) * 0.35, min_length):
                        matches_span.append((start_index, end_index))

        if matches_span:
            # merge all matches into one span
            final_span = min(start for start, _ in matches_span), max(
                end for _, end in matches_span
            )
            matches_span = [final_span]

        return matches_span

    def find_start_end_phrase(
        start_phrase, end_phrase, context, min_length=5, max_excerpt_length=300
    ):
        context = context.replace("\n", " ")

        matches = []
        matched_length = 0
        for sentence in [start_phrase, end_phrase]:
            if sentence is None:
                continue

            match = SequenceMatcher(
                None, sentence, context, autojunk=False
            ).find_longest_match()
            if match.size > max(len(sentence) * 0.35, min_length):
                matches.append((match.b, match.b + match.size))
                matched_length += match.size

        # check if second match is before the first match
        if len(matches) == 2 and matches[1][0] < matches[0][0]:
            # if so, keep only the first match
            matches = [matches[0]]

        if matches:
            start_idx = min(start for start, _ in matches)
            end_idx = max(end for _, end in matches)

            # check if the excerpt is too long
            if end_idx - start_idx > max_excerpt_length:
                end_idx = start_idx + max_excerpt_length

            final_match = (start_idx, end_idx)
        else:
            final_match = None

        return final_match, matched_length
