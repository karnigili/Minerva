import heapq
import urllib
import os
from collections import defaultdict
from bitarray import bitarray
import cPickle as pickle

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.l_child = left
        self.r_child = right
        self.data = data

    def __str__ (self):
        return str(self.data)

# Download the file if need be:
def download_file(url, filename):
    if not os.path.exists(filename):
        urllib.urlretrieve(url + filename, filename)


# build a frequency table:
def build_freq(filename):
    freq = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            for char in line.decode('utf-8-sig'):
                freq[char] += 1
    total = float(sum(freq.values()))
    return {char: count / total for (char, count) in freq.items()}


# Now build the Huffman encoding:
def encode(symb2freq):

    # tree #= {'value': 0, 'left':{}, 'rigth':{}}
    queue_of_sym = [(val, Node(data = key)) for key, val in symb2freq.items()]
    
    heapq.heapify(queue_of_sym)

    number_of_sym = len(symb2freq)

    for i in range(number_of_sym-1):

        k_left = heapq.heappop(queue_of_sym)
        k_right = heapq.heappop(queue_of_sym)

        k_freq = k_left[0] + k_right[0]

        heapq.heappush(queue_of_sym, (k_freq, Node(left = k_left[1], right = k_right[1])))

    root = queue_of_sym[0][1]
    huff_queue = [("", root)]
    encoding_dict = {}

    while huff_queue:
        prefix, node = huff_queue.pop()
        if node.data is not None:
            encoding_dict[node.data] = bitarray(prefix)

        else:
            if node.l_child is not None:
                huff_queue.append((prefix+"0", node.l_child))

            if node.r_child is not None:
                huff_queue.append((prefix+"1", node.r_child))

    return encoding_dict

# Now compress the file:
def compress(filename, encoding, compressed_name=None):
    if compressed_name is None:
        compressed_name = filename + ".huff"
    output = bitarray()
    with open(filename, 'r') as f:
        for line in f:
            for char in line.decode('utf-8-sig'):
                output.extend(encoding[char])
    N = len(output)
    with open(compressed_name, 'wb') as f:
        pickle.dump(N, f)
        pickle.dump(encoding, f)
        output.tofile(f)


# Now decompress the file:
def decompress(filename, decompressed_name=None):
    if decompressed_name is None:
        decompressed_name = filename + ".dehuff"
    with open(filename, 'rb') as f:
        N = pickle.load(f)
        encoding = pickle.load(f)
        bits = bitarray()
        bits.fromfile(f)
        bits = bits[:N]

    # Totally cheating here and using a builtin method:
    output = bits.decode(encoding)

    output = "".join(output).encode('utf-8-sig')
    with open(decompressed_name, 'wb') as f:
        f.write(output)


url = "https://www.gutenberg.org/ebooks/"
filename = "100.txt.utf-8"

download_file(url, filename)
freq = build_freq(filename)
encoding = encode(freq)
compress(filename, encoding)
decompress(filename + ".huff")
# Do you get identical files?