def main():
    letter_count = {
    }
    with open("/home/crypticrecoil/workspace/github.com/Nick-Gen/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()
        for i in range(len(words)):
            word = words[i]
            for k in range(len(word)):
                letter = word[k]
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
    
    sorted_letter_count = dict(sorted(letter_count.items()))
    
    list_sorted = list(sorted_letter_count.items())
    list_cut = list_sorted[-26:]
    for i in range(len(list_cut)):
        alphabet = list_cut[i]
        print(f"The '{alphabet[0]}' character was found {alphabet[1]} times")
main()