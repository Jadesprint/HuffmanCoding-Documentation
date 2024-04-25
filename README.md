# HuffmanCoding-Documentation
Huffman Coding in Python + Extended documentation + FrontEnd


# Info
Here is a Python script for Huffman Coding adding some user-friendly documentation and a basic front end aswell

# Usage
- Download the Huffman.py, useHuffman.py, sample.txt and optionally the Monocraft font for I added it as the default font in the front end.
- Run useHuffman.py and it should be good to go
- You can use any txt file or any bin file to compress and decompress respectively, for I added a file explorer in the front end

# Feats
- File compression and decompression
- Use any txt or bin file
- Easy usage
- File preview for txt compression
- Character count in compression function
- Documentation for any user to understand and/or modify

# Disclaimer
This Huffman Coding script isn't of my fully authory, I'll link the original repo below, I only addded a very basic front end, additional documentation in code and some misc. functions from the original script for 
this code to be as user friendly as it gets and to get a good grade in my Algorithm Analysis class :) I took the time to read and appreciate the code myself and I'm thankful that this guy helped me understand 
greedy algorithms via Huffman Coding.

# Original repo:
https://github.com/bhrigu123/huffman-coding

# Monocraft font repo:
https://github.com/IdreesInc/Monocraft/releases/tag/v3.0

# Additional notes
Code is a bit messy in regards of separating compress() and decompress() functions, so I did a little dirty trick for giving the illusion of separating them.
As the og author said: The decompress() function uses the object created from the compress() function as input since the info for decompress is stored in this object (i.e. the huffman tree)
What I did is declaring the object (in this case the file) as a global variable and then using the compress() func as a literal input in the decompress() func and it doesn't seems to be any
notable problem such as file dupe or text getting messy, so I just left it that way, a bit lazy I know, but it works.
