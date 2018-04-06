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
    def check(self):
        '''
        Checks the output produced by pattern's porter stemmer with the original implementation.
        '''
        with open(self.infile_porter, "r") as f:
            inputs = f.read().split("\n")
        with open(self.outfile_porter, "r") as f:
            outputs = f.read().split("\n")
        errors = []
        for i in range(len(inputs)):
            pattern_output = stem(inputs[i], stemmer=PORTER)
            if (pattern_output != outputs[i]):
                errors.append((inputs[i], outputs[i], pattern_output))
        with open(self.error_file, "w") as f:
            f.write("{:<20}  {:<20}  {:<20}\n\n".format("word_input", "original_output", "pattern_output"))
            for error in errors:
                f.write("{:<20}  {:<20}  {:<20}\n".format(error[0], error[1], error[2]))
        if (len(errors) > 0):
            print ("\n\nErrors found in stemmer: {}".format(len(errors)))
        else:
            print ("\n\nNo errors found in stemmer")
    def compare(self):  
        '''
        Performs a comparison between the stop word list used by pattern and other sources.
        '''      
        for source in self.sources:          
            with open(source, "r") as f:
                stoplist = set(f.read().split("\n"))
            pattern_minus_x = self.curr_list.difference(stoplist)
            x_minus_pattern = stoplist.difference(self.curr_list)
            name = str(source.split(".")[0].split("/")[1])
            if (name == "pattern"):
                continue
            print ("X = {}".format(name))
            print ("In pattern but not in X = {}".format(len(pattern_minus_x)))
            print ("In X but not in pattern = {}\n".format(len(x_minus_pattern)))
            with open(self.write_folder + name + ".txt", "w") as f:
                f.write("X = {}\n\n".format(name))
                f.write("In pattern but not in X = {}\n\n".format(len(pattern_minus_x)))
                [f.write(str(item) + " ") for item in pattern_minus_x]
                f.write("\n\nIn X but not in pattern = {}\n\n".format(len(x_minus_pattern)))
                [f.write(str(item) + " ") for item in x_minus_pattern]            
    def find_missing(self):
        '''
        Find important stop words not included in the pattern list.
        An important stop word is defined by being present in all sources except pattern.
        Equals SetUnion(Sources) - Pattern
        '''
        imp_set = set()        
        flag_first = 1
        for source in self.sources:          
            with open(source, "r") as f:
                stoplist = set(f.read().split("\n"))   
                #if first file being read
                if(flag_first == 1):
                    imp_set = stoplist
                    flag_first = 0
                else:
                    imp_set = imp_set.intersection(stoplist)
        print ("\nNo of important stop words missing: {}".format(len(imp_set.difference(self.curr_list))))


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
