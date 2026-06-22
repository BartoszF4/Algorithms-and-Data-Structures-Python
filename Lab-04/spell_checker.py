from distances import custom_levenshtein_distance


class SpellChecker:
    def __init__(self, dictionary_path):
        self.dictionary = {}
        self.word_frequencies = {}
        self.load_dictionary(dictionary_path)

    def get_freq_profile(self, word):
        profile = [0] * 26
        for char in word:
            if 'a' <= char <= 'z':
                profile[ord(char) - ord('a')] += 1
        return profile

    def load_dictionary(self, path):
        with open(path, 'r') as f:
            for line in f:
                word = line.strip().lower()
                length = len(word)
                if length not in self.dictionary:
                    self.dictionary[length] = []
                self.dictionary[length].append(word)
                self.word_frequencies[word] = self.get_freq_profile(word)

    def freq_distance(self, p1, p2):
        return sum(abs(a - b) for a, b in zip(p1, p2))

    def suggest_word(self, incorrect_word):
        length = len(incorrect_word)
        candidates = []

        for l in range(max(1, length - 2), length + 3):
            if l in self.dictionary:
                candidates.extend(self.dictionary[l])

        incorrect_profile = self.get_freq_profile(incorrect_word)
        filtered_candidates = []

        for word in candidates:
            if self.freq_distance(incorrect_profile, self.word_frequencies[word]) <= 3:
                filtered_candidates.append(word)

        if not filtered_candidates:
            filtered_candidates = candidates

        best_word = incorrect_word
        min_dist = float('inf')

        for word in filtered_candidates:
            dist = custom_levenshtein_distance(incorrect_word, word)
            if dist < min_dist:
                min_dist = dist
                best_word = word

        return best_word

    def correct_file(self, input_path, output_path):
        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            for line in infile:
                words = line.strip().lower().split()
                corrected_words = []
                for word in words:
                    clean_word = "".join(c for c in word if c.isalpha())
                    if not clean_word:
                        continue
                    if any(clean_word in self.dictionary[l] for l in self.dictionary if l == len(clean_word)):
                        corrected_words.append(clean_word)
                    else:
                        corrected_words.append(self.suggest_word(clean_word))
                outfile.write(" ".join(corrected_words) + "\n")