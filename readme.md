### The problem was solved assuming that:
    1. Rectangles will not be angled or skewed
    2. The numbers entered for rectangle coordinates and lengths are real numbers and not imaginary
    3. If a large rectangle contains a smaller rectangle, they are contained
    4. If a smaller rectangle is inside a larger rectangle, they are contained
    5. If a two rectangles have the same coordinates/properties, they are contained
    6. Two rectangles are not adjacent if only a vertex is shared

# How to run main program in the terminal (IMPORTANT!):
        1. Makes sure you are using the virtual environment by doing "source venv/bin/activate"
        2. To execute, please cd to the directory of the python programs and run using (excluding quotes) "python3 RectanglesProblem.py"
        3. The program will not output anything by default without entering your own rectangles into the class constructors located in the main method at the bottom
            3a. You can run the unit test file and it already has lots of test cases in it
        3. If the program does not run, try using "python RectanglesProblem.py"
        4. If none of these work this probably means you do not have python installed correctly
        
# How to run unit tests in the terminal (IMPORTANT!):
        1. Makes sure you are using the virtual environment by doing "source venv/bin/activate"
        2. CD to the directory of the test_RectanglesProblem.py and run using "python -m unittest discover" excluding quotes

# How to run the program with your own rectangle values:
    ## OPTION 1 (recommended and default)
        In the main method of RectangleProblem.py make sure the OVERRIDE variable is set equal to True
            1. Change the parameters of the two Rectangle classes to whatever you would like
            2. Run the program in the command line
            3. It will output to the console once all the appropriate lines have been commented out
            
    ## OPTION 2 (finniky, most likely will not work)
        There is a folder named Input Folder and in there is where you can place create a text file to test you specific case. 
            1. Use the Example Input.txt for help
            2. You can name the file anything as long as it ends with .txt and is also not called Example Input.txt
            3. Each line represents a new rectangle as longs as it has the X1= within the line'
            5. Each keyword must be seperated by a comma
            4. the X1 and Y1 value for each rectangle represents the top left corner of the rectangle
            5. The LENGTH and WIDTH keyword represent the distance from (X1, Y1)

# Other notes:
    -   Lines meant to not be run are commented out, uncomment at your own risk!!!
