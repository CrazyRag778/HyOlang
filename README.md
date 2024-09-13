HyOlang: A Custom Scripting Language Interpreter
=====================================

This project is a custom interpreter for a simple scripting language. The interpreter reads commands from a file, parses them, and executes various operations such as printing, variable handling, and file operations.

Features
--------

*   **Printing Commands:**
    *   `rawPRINT`: Prints text without a newline at the end.
    *   `PRINT`: Prints text with a newline.
    *   `fPRINT`: Evaluates and prints the result of an expression without a newline.
    *   `LOOpRINT`: Prints multiple pieces of text on the same line.
*   **Variable Handling:**
    *   `TYPE`: Prints the type of an evaluated object.
    *   `INPUT`: Prompts for user input and stores the result in a variable.
    *   `showVAR`: Prints the value of a variable.
    *   `takeVAR`: Assigns a value to a variable.
*   **File Operations (Requires `@ALLOW FILE`):**
    *   `FILE.ACCESS`: Opens a file with a given mode.
    *   `FILE.CLOSE`: Closes an open file.
    *   `FILE.CREATE`: Creates a new file.
    *   `FILE.DELETE`: Deletes a file.
    *   `FILE.WRITE`: Writes to a file.
*   **Module Management:**
    *   `@ALLOW`: Enables the use of specific modules, such as the `FILE` module.
*   **End Command:**
    *   `END`: Exits the interpreter.

Usage
-----

To run the interpreter, use the following command:

    hyolang <script-file>

Where `<script-file>` is the file containing the commands to be executed by the interpreter.

### Example Script

Here is a sample script that demonstrates the functionality:

    @ALLOW - FILE
    PRINT - "Hello, World!"
    INPUT - "Enter your name: " - name
    fPRINT - "Hello, {name}!"
    FILE.CREATE - test.txt - file
    FILE.WRITE - file - "This is a test."
    FILE.CLOSE - file
    END
    

Security Considerations
-----------------------

This is not a real and working programming language, and was built for educational purpose. Do not use it for professional use!

Contributions
-------------

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

License
-------

This project is licensed under the Creative Commons Zero v1.0 Universal. See the [LICENSE](LICENSE) file for more details.
