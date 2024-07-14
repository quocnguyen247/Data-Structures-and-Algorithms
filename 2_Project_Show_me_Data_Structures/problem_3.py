import sys
import heapq


def encoded_text(huffman_dict, data):
    huffcode = ''
    for c in data:
        huffcode += str(huffman_dict[c])

    return huffcode


def huffman_encoding(data):
    # Frequency dictionary
    huff = {char: data.count(char) for char in set(data)}
    
    # Create a priority queue (min-heap) from frequency dictionary
    heap = [[frequency, [symbol, '']] for symbol, frequency in huff.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        huffman_dict = {heap[0][1][0]: '0'}
        huffcode = encoded_text(huffman_dict, data)
        return huffcode, heap

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    # Create Huffman dictionary
    huffman_dict = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
    huffman_dict = {a[0]: a[1] for a in huffman_dict}
    
    huffcode = encoded_text(huffman_dict, data)
    return huffcode, heap


def huffman_decoding(encoded_data, tree):
    # Extract the Huffman tree from the heap
    root = tree[0]
    huffman_dict = {v: k for k, v in sorted(
        [pair for pair in root[1:]], key=lambda p: (len(p[-1]), p)
    )}
    
    decoded_text = ''
    current_code = ''

    for bit in encoded_data:
        current_code += bit
        if current_code in huffman_dict:
            decoded_text += huffman_dict[current_code]
            current_code = ''

    return decoded_text


if __name__ == "__main__":
    codes = {}

    print('***** Testcase 1 *****')
    a_great_sentence = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    print('\n***** Testcase 2 *****')
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEEEE"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    print('\n***** Testcase 3 *****')
    a_great_sentence = "XXXXXXXXYYYYYYYYYYYYYZZZZZZ"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))