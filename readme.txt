Instructions for running the twitter stream parse application:

1) Inside the extweetwordcount directory, run the storm streamparse:

    $ sparse run
    
2) Enter Control + C to end the stream. 

3) Run the finalresult.py script. 

    To return the count for a specific word, enter it as an argument after the script.
    
        ex:  $ python finalresults.py Berkeley
        
    To return a list of all counts (limited to 1,000 results), you can omit this argument. 
    
        ex: $ python finalresults.py 
        
3) Run the histogram.py script. To find all words with a count between two specific values, enter the lower and upper bounds of the ranges as a second and third argument after the script, respectively. Use spaces to separate the limits. 

        ex: $ python histogram.py 10 12 (this returns all words with a count between 10 and 12 and specifies their count)