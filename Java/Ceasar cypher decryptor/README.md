# Caesar Cipher Decryptor

Java application for decrypting Caesar cipher encrypted text.

## Files

- `src/Main.java` - Main application entry point
- `src/Decryptor.java` - Caesar cipher decryption implementation
- `Ceasar cypher decryptor.iml` - IntelliJ IDEA module configuration
- `out/` - Compiled class files directory

## Features

- Caesar cipher decryption algorithm
- Text processing and character shifting
- User-friendly interface for decryption
- Support for different shift values

## Prerequisites

- Java 11+
- IntelliJ IDEA (optional)

## Build & Run

### Command Line
```bash
cd src
javac *.java
java Main
```

### IntelliJ IDEA
1. Open the project by importing `Ceasar cypher decryptor.iml`
2. Run the Main class directly from the IDE

## Algorithm

The Caesar cipher decryptor implements:
- Character shift decryption
- Alphabet wrapping for proper character mapping
- Input validation and error handling
- Multiple shift value testing for unknown keys

## Usage

The application can decrypt Caesar cipher text by:
1. Accepting encrypted text input
2. Trying different shift values
3. Displaying potential decrypted results
4. Allowing user selection of correct decryption
