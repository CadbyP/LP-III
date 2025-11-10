import threading
import random
import time

def generate_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def multiply_matrices(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def multiply_row(A, B, result, row):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[row][j] += A[row][k] * B[k][j]


def multiply_cell(A, B, result, i, j):
    for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]

def threaded_row_multiplication(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    threads = []

    for i in range(len(A)):
        t = threading.Thread(target=multiply_row, args=(A, B, result, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return result

def threaded_cell_multiplication(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    threads = []

    for i in range(len(A)):
        for j in range(len(B[0])):
            t = threading.Thread(target=multiply_cell, args=(A, B, result, i, j))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()
    return result

def main():
    n = 100  
    A = generate_matrix(n, n)
    B = generate_matrix(n, n)

    
    start = time.time()
    result_normal = multiply_matrices(A, B)
    normal_time = time.time() - start
    print(f"\nNormal multiplication time: {normal_time:.4f} seconds")

    
    start = time.time()
    result_row = threaded_row_multiplication(A, B)
    row_time = time.time() - start
    print(f"Thread-per-row multiplication time: {row_time:.4f} seconds")

    
    start = time.time()
    result_cell = threaded_cell_multiplication(A, B)
    cell_time = time.time() - start
    print(f"Thread-per-cell multiplication time: {cell_time:.4f} seconds")

    print("\nPerformance Summary:")
    print(f"Single-threaded: {normal_time:.4f}s")
    print(f"One thread per row: {row_time:.4f}s")
    print(f"One thread per cell: {cell_time:.4f}s")

if __name__ == "__main__":
    main()
