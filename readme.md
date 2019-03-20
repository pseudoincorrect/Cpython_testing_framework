Cpython Testing framework

Simple framework made to either test (integration) C code with python or to start a new Cpython project.

File Architecture:
    main.py: 
        python script that will:
        compile the C code in c_src/ folder
        import the compiled .so C library
        import data from data/ folder
        run the test (c function thanks to cpython)
        display with matplot lib
    c_src/:
        src/:
            .c and .h C files to be compiled
        makefile:
            gnu make build automation file
    data/:
        timeseries data to be inputed in python 

example chosen:
    the ./data/ folder contains the data of an optical heart rate sensor
    The C sources contains the algorith need to filter the above date and extrac the heart rate
    within the python code, we will input those data one by one to the .so library 
    for each data inputed, the .so library will output a filtered one
    we will display both.

debugging python is straight forward, no real need of explanaitions
however to debug the C code in ./src/ folder they are two ways:
    simpler one: 
        use printf with the c code and run the main.py to debug it
    more advanced one: 
        use vscode and GDB (or LLVM on mac) 
        go to ./c_src/ $> make executable
        use gdb with the binary file created in ./c_src/bin
        optional, setup VScode to debug with GDB:
            https://code.visualstudio.com/docs/languages/cpp  (debugging section)