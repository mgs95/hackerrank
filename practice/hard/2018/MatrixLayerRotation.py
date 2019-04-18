"""
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

Score: 80/80
Submitted: 2018
"""


def ring_to_line(ring):
    """ Transforms a ring into a line """
    temp_ring = ring[:][:]
    temp_ring[0] = [temp_ring[0][0], temp_ring[0][-1]]
    temp_ring[-1] = [temp_ring[-1][0], temp_ring[-1][-1]]
    zipped_ring = list(zip(*temp_ring))
    line = ring[0] + list(zipped_ring[1][1:]) + list(reversed(ring[-1][:-1])) + list(
        reversed(zipped_ring[0][1:-1]))

    return line


def rotate_ring(ring):
    """ Rotate the ring passed through parameter """
    line = ring_to_line(ring)
    rotations = r % len(line)
    rotated_line = [0] * len(line)

    for idx in range(len(line)):
        new_idx = idx + rotations
        new_idx = new_idx if new_idx < len(line) else new_idx - len(line)
        rotated_line[idx] = [line[idx], line[new_idx]]

    return rotated_line


def matrix_rotation(matrix):
    # indexes_matrix is a matrix showing the indexes of matrix
    indexes_matrix = []
    for y in range(len(matrix)):
        new_row = []
        for x in range(len(matrix[0])):
            new_row.append([y, x])
        indexes_matrix.append(new_row)

    final_rings = []
    indexes_matrix_2 = indexes_matrix[:][:]

    # Extract rings from indexes matrix
    while indexes_matrix_2:
        ring = [indexes_matrix_2.pop(0)]
        for idx in range(len(indexes_matrix_2) - 1):
            el = [indexes_matrix_2[idx].pop(0), indexes_matrix_2[idx].pop(-1)]
            ring.append(el)
        ring.append(indexes_matrix_2.pop(-1))

        final_rings.append(ring)
        while [] in indexes_matrix_2:
            indexes_matrix_2.pop(indexes_matrix_2.index([]))

    # Build solution matrix
    result_matrix = [[0] * len(matrix[0]) for __ in range(len(matrix))]
    for ring in final_rings:
        ring = rotate_ring(ring)
        for origin, destination in ring:
            result_matrix[origin[0]][origin[1]] = matrix[destination[0]][destination[1]]

    # Print solution
    for line in result_matrix:
        line = map(str, line)
        print(' '.join(line))


if __name__ == "__main__":
    m, n, r = list(map(int, input().split()))
    matrix = []
    for __ in range(m):
        matrix_t = list(map(int, input().split()))
        matrix.append(matrix_t)
    matrix_rotation(matrix)
