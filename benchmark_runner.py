# Creating a unified benchmark framework
import os ,subprocess, time

PYTHON_IMPLEMENTATIONS={
"CPython" : "python3"    
,"PyPy" : "pypy",
"Jython" : "jython"
}


BENCHMARK_SCRIPTS={

    # 4 PROGRAMS
    
    # NUMERICAL OPERATIONS  
    # --> fibonacci series
    "fibonacci" : "benchmarks/fibonacci.py",

    # STRING FUNCTIONS 
    # --> string reverse
    "string_reverse" : "benchmarks/string_reverse.py",

    # FILE OPERATIONS 
    # --> file write
    "file_write" : "benchmarks/file_write.py",

    # DATA PREPROCESSING
    # --> list_sorting 
    "list_sorting"  : "benchmarks/list_sorting.py"

}

RESULTS={}

# function definition for running a benchmark
def run_benchmark(implementation, script_path):
    start_time = time.time()
    try:
        subprocess.run([implementation, script_path],check=True)
    except Exception as e : 
        print(f"Error running {script_path} with {implementation} : {e}")
        # return float('inf')
    return time.time() - start_time

# remainig part of code
for implementation_name , implementation_command in PYTHON_IMPLEMENTATIONS.items():
    RESULTS[implementation_name] = {}
    print(f"Running benchmarks for {implementation_name}...")
    for benchmark_name, script_path in BENCHMARK_SCRIPTS.items():
        print(f"Executing {benchmark_name}...")
        exec_time = run_benchmark(implementation_command, script_path)
        RESULTS[implementation_name][benchmark_name] = exec_time

# print("Benchmark Results:")
with open("result.txt","w") as f:

    for implementation_name, benchmarks in RESULTS.items():
        # print(f"{implementation_name}:")
        f.write(f"{implementation_name}:\n")
        for benchmark_name, exec_time in benchmarks.items():
            # print(f"{benchmark_name}:{exec_time:.2f} seconds")
            f.write(f"{benchmark_name} : {exec_time:.2f} seconds\n")