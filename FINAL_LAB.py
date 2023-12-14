class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traversed(root):
    if not root:
        return []

    vertical_order = {}
    queue = [(root, 0)]

    while queue:
        node, distance = queue.pop(0)

        if distance in vertical_order:
            vertical_order[distance].append(node.val)
        else:
            vertical_order[distance] = [node.val]

        if node.left:
            queue.append((node.left, distance - 1))

        if node.right:
            queue.append((node.right, distance + 1))

    sorted_distance = sorted(vertical_order.keys())

    result = []
    for distance in sorted_distance:
        result.extend(vertical_order[distance])

    return result

def reverse(output_list):
    for val in output_list:
        print(f"{val:^3}", end=" ")
    print()

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    result = traversed(root)
    reversed_result = result[::-1]  # Reversing the result
    print("Output:")
    reverse(reversed_result)

main()
