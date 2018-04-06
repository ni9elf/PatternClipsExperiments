import glob
from pattern.vector import stem, PORTER
    
    
class StemmerChecker(object):
    '''
    Checks the porter stemmer used by pattern and compares its stop word list with other sources.
    '''
    def __init__(self, curr_list_ctr, sources_ctr, write_folder_ctr, infile_porter_ctr,
                 outfile_porter_ctr, error_file_ctr):
        self.curr_list = curr_list_ctr
        self.sources = sources_ctr
        self.write_folder = write_folder_ctr
        self.infile_porter = infile_porter_ctr
        self.outfile_porter = outfile_porter_ctr    
        self.error_file = error_file_ctr


if __name__ == "__main__":
    READ_FOLDER = "Stoplists/"
    WRITE_FOLDER = "Results/"
    FILE_NAME = "pattern.txt"
    #input: https://tartarus.org/martin/PorterStemmer/voc.txt
    INFILE_PORTER = "Check/input.txt"
    #output: https://tartarus.org/martin/PorterStemmer/output.txt 
    OUTFILE_PORTER = "Check/output.txt"
    ERROR_FILE = "Check/errors.txt"
    sources = glob.glob("{}/*.txt".format(READ_FOLDER))
    #reading the current stop words list used by the vector module of pattern
    #found at: https://github.com/clips/pattern/blob/master/pattern/vector/stopwords-en.txt
    with open(READ_FOLDER + FILE_NAME, "r") as f:
        clips_stoplist = set(f.read().split("\n"))        
    checker = StemmerChecker(clips_stoplist, sources, WRITE_FOLDER, INFILE_PORTER, OUTFILE_PORTER, ERROR_FILE)        
    checker.compare()
    checker.find_missing()
    checker.check()
