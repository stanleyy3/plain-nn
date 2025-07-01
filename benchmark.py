import time
import subprocess
import sys

NUM_RUNS = 5
SCRIPTS = ['main.py', 'cuda_main.py']

def benchmark_script(script):
    """Run a script multiple times and return the average duration."""
    times = []
    for i in range(NUM_RUNS):
        print(f"Running {script}, iteration {i+1}/{NUM_RUNS}...")
        start = time.time()
        subprocess.run([sys.executable, script], check=True)
        duration = time.time() - start
        print(f"Duration: {duration:.2f} seconds")
        times.append(duration)
    avg = sum(times) / len(times)
    return avg


def main():
    results = {}
    for script in SCRIPTS:
        avg_time = benchmark_script(script)
        results[script] = avg_time

    print("\nAverage training times over {} runs:".format(NUM_RUNS))
    for script, avg in results.items():
        print(f"{script}: {avg:.2f} seconds")


if __name__ == '__main__':
    main()
