import sys
import time
import runpy
import inspect
from collections import defaultdict

line_times = defaultdict(float)
last_time = None
last_line = None

def trace_lines(frame, event, arg):
    global last_time, last_line
    if event == "line":
        now = time.perf_counter()
        if last_line is not None:
            line_times[last_line] += now - last_time
        last_time = now
        last_line = (frame.f_code.co_filename, frame.f_lineno)
    elif event == "call":
        last_time = time.perf_counter()
        last_line = (frame.f_code.co_filename, frame.f_lineno)
    elif event == "return":
        now = time.perf_counter()
        if last_line is not None:
            line_times[last_line] += now - last_time
        last_line = None
    return trace_lines

def profile_script(target_script):
    sys.settrace(trace_lines)
    runpy.run_path(target_script, run_name="__main__")
    sys.settrace(None)

    # Pretty output
    print(f"\n{'File':<30} {'Line':<6} {'Time (ms)':>10}  Code")
    print("-" * 80)
    for (filename, lineno), total_time in sorted(line_times.items(), key=lambda x: x[1], reverse=True):
        try:
            code_line = inspect.getsourcefile(sys.modules['__main__'])
            with open(filename, 'r') as f:
                src = f.readlines()[lineno - 1].strip()
        except Exception:
            src = "<source unavailable>"
        print(f"{filename:<30} {lineno:<6} {total_time * 1000:>10.4f}  {src}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python profile_every_line.py your_script.py")
        sys.exit(1)
    target = sys.argv[1]
    profile_script(target)

#python .\trace_runtime.py .\FP2526P2.py 30 > results.txt