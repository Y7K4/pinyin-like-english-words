# Pinyin-Like English Words

A text file containing 12209 English words that look like pinyin, i.e., can be segmented into Chinese syllables. See `pinyin_like_english_words.txt`.

## Motivation

Certain English words can be segmented into Chinese syllables and interpreted as pinyin, for example

* cache as "ca che",
* siren as "si ren",
* genre as "gen re",
* Chihuahua as "chi hua hua",

and sometimes the dramatic differences in the resulted pronunciations are funny to me.

Out of curiosity, I wrote a simple Python script `main.py` to find these pinyin-like English words.

## Input files

`words_alpha.txt` is obtained from [english-words](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) and contains about 370k English words.

`pinyin.txt` is obtained from [ISO 7098:2015](https://www.iso.org/standard/61420.html) (Annex A: Table of Chinese syllable forms) and contains 410 Chinese syllables.

## Fun facts

1. The longest pinyin-like word is [humuhumunukunukuapuaa](https://en.wikipedia.org/wiki/Reef_triggerfish). The pronounciations in English and pinyin are quite similar.
2. About 3% (12209/370103) of words are pinyin-like.

I'll write more in [my blog post](https://y7k4.github.io/2021/07/11/pinyin-like-english-words.html). It'll be in Chinese though.
