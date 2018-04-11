**Project Name**

`PatternClipsExperiments`

**Description**

This module conducts experiments on [pattern](https://github.com/clips/pattern) from the CLiPS (Computational Linguistics & Psycholinguistics) research centre. Two experiments are currently completed:
* Checking the output of the Porter stemmer implemented in pattern against the output of the [original implementation](https://tartarus.org/martin/PorterStemmer/) by Martin Porter. Performed by the `check` function of the `StemmerChecker` class.
* Comparing the list of stop words currently used by pattern's [vector module](https://github.com/clips/pattern/blob/master/pattern/vector/stopwords-en.txt) against other popular stop word lists to check whether an update is required. Performed by the `find_important` and `compare` function of the `StemmerChecker` class.

**Results**

* Porter stemmer output check: There were a total of 1043 errors (pattern Porter stemmer output does not match the output of the original implementation) found which are stored in the file `Check/errors.txt`. Sample errors are provided in the table below.

|word_input     | original_output| pattern_output  |
|:-------------:|:--------------:|:---------------:|
| admiringly    | admiringli  | admir           |
| crying        | cry            |   cri           |
| spy           | spy            |    spi          |

* List of stopwords comparison: A total of 11 sources of stop words were used to compare with as linked in the appendix. For each source, the set of words present in the source but not in pattern's list of stop words and vice versa were reported in the corresponding file. Comparison output was stored in the directory `Results`.

**Dependencies**
* pattern 2.6
* Python 2.7

**Usage**

Run `python stemmer_checker.py` to obtain experiment statistics.

**Appendix: List of Sources of Stopwords**

1. unine.txt (formation retrieval multilingual resources from Universite de Neuchatel, Switzerland) [link](http://members.unine.ch/jacques.savoy/clef/englishST.txt)

2. princeton.txt (Algorithms book by Robert Sedgewick and Kevin Wayne, Princeton) [link](https://algs4.cs.princeton.edu/35applications/stopwords.txt)

3. nltk.txt (Natural Language Toolkit 3.2.5)

4. yoast.txt (YoastSEO is a text analysis and assessment library in JavaScript for SEO feedback) [link](https://github.com/Yoast/YoastSEO.js/blob/develop/src/config/stopwords.js)

5. mysql.txt (MySQL Stopword list) [link](https://www.ranks.nl/stopwords)

6. ranksnl_short.txt (Default stopword list used by ranks.nl) [link](https://www.ranks.nl/stopwords)

7. ranksnl_long.txt (Longer version of stopword list used by ranks.nl) [link](https://www.ranks.nl/stopwords)

8. corenlp.txt (Stanford CoreNLP - natural language software) [link](https://github.com/stanfordnlp/CoreNLP/blob/master/data/edu/stanford/nlp/patterns/surface/stopwords.txt)

9. mallet.txt (MALLET (MAchine Learning for LanguagE Toolkit) from UMass Amherst) [link](https://github.com/mimno/Mallet/blob/master/stoplists/en.txt)

10. glasgow.txt (Information retrieval resources from University of Glasgow) [link](http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words)

11. onix.txt (Onix Text Retrieval Toolkit) [link](http://www.lextek.com/manuals/onix/stopwords1.html)
