from multiprocessing import Pool
import random
import time

# Generate random matrices
def generate_matrix(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

def row_multiply(args):
    row, B = args
    return [sum(a * b for a, b in zip(row, col)) for col in zip(*B)]

def matrix_multiply_parallel(A, B):
    with Pool() as pool:
        return pool.map(row_multiply, [(row, B) for row in A])

if __name__ == "__main__":
    import cProfile

    size = 500  # Size of the matrix
    A = generate_matrix(size)
    B = generate_matrix(size)

    profiler = cProfile.Profile()
    profiler.enable()

    start_time = time.time()
    C = matrix_multiply_parallel(A, B)
    end_time = time.time()

    profiler.disable()
    profiler.print_stats(sort="time")

    print(f"Parallel execution time: {end_time - start_time:.2f} seconds")
