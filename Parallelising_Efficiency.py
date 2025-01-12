from multiprocessing import Pool
import random
import time

# Define row_multiply globally
def row_multiply(args):
    row, B = args
    return [sum(a * b for a, b in zip(row, col)) for col in zip(*B)]

def matrix_multiply_sequential(A, B):
    """Sequential matrix multiplication"""
    result = []
    for row in A:
        result.append([sum(a * b for a, b in zip(row, col)) for col in zip(*B)])
    return result

def matrix_multiply_parallel(A, B, num_processes):
    """Parallel matrix multiplication"""
    with Pool(num_processes) as pool:
        return pool.map(row_multiply, [(row, B) for row in A])

def run_experiment(matrix_size, processes_list):
    """Run experiments and measure execution time"""
    A = [[random.randint(1, 100) for _ in range(matrix_size)] for _ in range(matrix_size)]
    B = [[random.randint(1, 100) for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    # Measure serial time
    start_time = time.time()
    matrix_multiply_sequential(A, B)
    serial_time = time.time() - start_time
    print(f"Serial Time for {matrix_size}x{matrix_size}: {serial_time:.2f} seconds")

    # Measure parallel time for each process count
    results = []
    for processes in processes_list:
        start_time = time.time()
        matrix_multiply_parallel(A, B, processes)
        parallel_time = time.time() - start_time
        speedup = serial_time / parallel_time
        efficiency = (speedup / processes) * 100
        results.append((processes, serial_time, parallel_time, speedup, efficiency))
        print(f"Processes: {processes}, Parallel Time: {parallel_time:.2f}, "
              f"Speedup: {speedup:.2f}, Efficiency: {efficiency:.2f}%")

    return results

# Run the experiment
if __name__ == "__main__":
    matrix_size = 500
    processes_list = [1, 2, 4]
    results = run_experiment(matrix_size, processes_list)

    # Print results in tabular format
    print("\n| Matrix Size | Processes | Serial Time (s) | Parallel Time (s) | Speedup | Efficiency (%) |")
    print("| --- | --- | --- | --- | --- | --- |")
    for processes, serial_time, parallel_time, speedup, efficiency in results:
        print(f"| {matrix_size}x{matrix_size} | {processes} | {serial_time:.2f} | "
              f"{parallel_time:.2f} | {speedup:.2f} | {efficiency:.2f} |")
