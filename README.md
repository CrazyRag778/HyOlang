Custom Scripting Language Interpreter
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

    python interpreter.py <script-file>

Where `<script-file>` is the file containing the commands to be executed by the interpreter.

### Example Script

Here is a sample script that demonstrates the functionality:

    PRINT "Hello, World!"
    takeVAR -name-INPUT 'Enter your name: ' -name-
    fPRINT "Hello, {name}!"
    @ALLOW FILE
    FILE.CREATE 'test.txt' -file-
    FILE.WRITE -file- "This is a test."
    FILE.CLOSE -file-
    END
    

Security Considerations
-----------------------

This interpreter uses `eval` and `exec` for certain operations, which can be a security risk if the input is not properly sanitized. It is recommended to use this interpreter only with trusted scripts.

Contributions
-------------

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
