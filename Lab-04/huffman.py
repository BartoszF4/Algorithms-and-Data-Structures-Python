from heap import Node, PriorityQueue


def get_frequencies(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq


def build_huffman_tree(text):
    if not text:
        return None

    frequencies = get_frequencies(text)
    pq = PriorityQueue()
    for char, freq in frequencies.items():
        pq.push(Node(char, freq))

    if len(pq) == 1:
        single_node = pq.pop()
        dummy_root = Node(None, single_node.freq)
        dummy_root.left = single_node
        pq.push(dummy_root)

    while len(pq) > 1:
        left = pq.pop()
        right = pq.pop()
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        pq.push(merged)

    return pq.pop()


def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def encode_huffman(text):
    if not text:
        return "", {}, 0.0

    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)
    encoded_text = "".join(codes[char] for char in text)

    original_size = len(text) * 8
    encoded_size = len(encoded_text)
    compression_ratio = original_size / encoded_size if encoded_size > 0 else 0

    return encoded_text, codes, compression_ratio