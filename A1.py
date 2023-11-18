import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison methods for nodes
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

def build_huffman_tree(characters, frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        heapq.heappush(heap, internal_node)

    return heap[0]

def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_encoding(text):
    characters = list(set(text))
    frequencies = [text.count(char) for char in characters]

    root = build_huffman_tree(characters, frequencies)
    codes = generate_huffman_codes(root)

    encoded_text = ''.join([codes[char] for char in text])

    return encoded_text, codes

# Fixed inputs
input_text = "abracadabra"
encoded_text, huffman_codes = huffman_encoding(input_text)

print("Input Text:", input_text)
print("Huffman Codes:", huffman_codes)
print("Encoded Text:", encoded_text)
