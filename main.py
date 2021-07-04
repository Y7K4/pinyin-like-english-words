PINYIN = 'pinyin.txt'
WORDS = 'words_alpha.txt'
OUT = 'pinyin_like_english_words.txt'

with open(PINYIN) as file:
    pinyin_set = {line.rstrip() for line in file}

words_like_pinyin = []
with open(WORDS) as file:
    for line in file:
        word = line.rstrip()
        L = len(word)
        dp = [False] * (L + 1)  # dp[i]: if first i letters is like pinyin
        dp[0] = True
        for i in range(1, L + 1):
            for j in range(i):
                if dp[j] and word[j:i] in pinyin_set:
                    dp[i] = True
                    break
        if dp[-1]:
            words_like_pinyin.append(word)

words_like_pinyin.sort(key=len, reverse=True)  # sort by word length

with open(OUT, 'w') as file:
    for word in words_like_pinyin:
        file.write(word + '\n')
    file.truncate(file.tell() - 1)  # remove the last new line
