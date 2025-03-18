test_words = [
    "Big", "Small", "Fast", "Slow",
    "Happy", "Sad", "Angry", "Excited", "Tired",
    "Bright", "Dark", "Noisy", "Quiet", "Calm",
    "Soft", "Hard", "Hot", "Cold", "Warm",
    "Friendly", "Brave", "Shy", "Strong", "Weak"
]


def sort_words(words):

    sorted_words = sorted(words)
    sublists = make_sublists(sorted_words)
    return sublists


def make_sublists(words):

    sublists = []

    sublists.append(words[0:4])

    remaining_words = words[4:]

    for i in range(0, len(remaining_words), 5):
        sublists.append(remaining_words[i:i+5])

    return sublists