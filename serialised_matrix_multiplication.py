import random
import time

# Generate random matrices
def generate_matrix(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

def matrix_multiply_sequential(A, B):
    size = len(A)
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    import cProfile

    size = 500  # Size of the matrix
    A = generate_matrix(size)
    B = generate_matrix(size)

    profiler = cProfile.Profile()
    profiler.enable()

    start_time = time.time()
    C = matrix_multiply_sequential(A, B)
    end_time = time.time()

    profiler.disable()
    profiler.print_stats(sort="time")

    print(f"Sequential execution time: {end_time - start_time:.2f} seconds")
