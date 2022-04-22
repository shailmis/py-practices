import psutil

for process in psutil.process_iter():
    if 'firefox.exe' in process.name():
        cpu_times = process.cpu_times
        print(f'{cpu_times}')