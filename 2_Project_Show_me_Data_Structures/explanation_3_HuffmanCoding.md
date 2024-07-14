## Explanation_3: Huffman Coding

### Requirement:
The goal is to implement encoding and decoding algorithms using Huffman coding, a lossless data compression technique.

### Summary:
Huffman coding assigns shorter binary codes to more frequently occurring characters and longer codes to less frequent characters, optimizing the overall bit usage for a given set of characters.

#### huffman_encoding:
1. Calculate the frequency of each character in the input string and store it in a dictionary.
2. Construct a heap using the heapq module in Python.
3. Build a Huffman Tree by merging the two lowest frequency nodes until a root node is formed.
4. Assign '0' to left branches and '1' to right branches.
5. Encode the input text based on the generated Huffman codes and pass the encoded text along with the Huffman tree to the huffman_decoding function.

#### huffman_decoding:
Decode the encoded text using the provided Huffman tree to retrieve the original string.

### Time and Space Complexity:
#### Time Complexity:
- O(n): Iterate through the input string to calculate character frequencies and store them in a dictionary.
- O(n): List comprehension and heapify commands take O(n + logn) => O(n).
- O(n): Building the heap tree and encoding the text.
- O(n): The while loop inside the encoding function takes linear time.
- Total time complexity for encoding and decoding: O(n)

#### Space Complexity:
- O(distinct_characters): Space required for storing encoded/decoded data.

### Conclusion:
The Huffman coding algorithm efficiently encodes and decodes data by assigning variable-length codes to characters based on their frequencies, optimizing the overall bit usage for data compression. The implementation achieves a balance between time and space complexity for encoding and decoding operations.