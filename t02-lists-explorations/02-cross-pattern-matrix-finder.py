import random


class MatrixScanner:

    def __init__(self, matrix):
        self.matrix = matrix

    def scan_pattern_on_position(self):
        print("\n")
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                row_flag = self.check_row(element, i)
                col_flag = self.check_column(element, j)
                print(f"{i}x{j}: {row_flag} x {col_flag}")
                if row_flag and col_flag:
                    print(f"\nFound pattern in cell {i}x{j} with number: {element}\n")

    def check_row(self, num, row_num):

        if num == 1:
            return all(self.matrix[row_num])
        else:
            return not any(self.matrix[row_num])

    def check_column(self, num, col_num):
        if num == 1:
            return all([row[col_num] for row in self.matrix])
        else:
            return not any([row[col_num] for row in self.matrix])

    def print_matrix(self):
        print('\n', self.matrix, '\n')
        for row in self.matrix:
            print(row)
        print('\n')

    def cross_pattern_finder(self, row, col, total=1000):
        counter = 0
        temp_matrix = []
        for i in range(total):
            round_matrix = [[random.randint(0, 1) for i in range(3)] for j in range(3)]
            all_row = all(round_matrix[row])
            all_col = all([row[col] for row in round_matrix])
            if all([all_row, all_col]):
                temp_matrix = round_matrix
                counter += 1

        print(f"Total matrix scanned: {total}")
        print(f"Patterns encounter: {counter}")
        self.print_matrix(temp_matrix)


if __name__ == '__main__':
    matrix = [[random.randint(0, 1) for i in range(3)] for j in range(3)]
    # matrix2 = [[1, 1, 1], [1, 0, 1], [1, 1, 0]]
    scanner = MatrixScanner(matrix)
    scanner.scan_pattern_on_position()
    scanner.print_matrix()
