import os
import re
import csv
import io
import time
import psutil

while True:
    try:
        spider_list = [_ for _ in os.listdir(os.path.dirname(os.path.abspath(__file__))) if
                       "os_try.py" not in _ and _.endswith('.py')]

        result = [_ for _ in os.popen('tasklist /V /fo csv|findstr cmd.exe').read().splitlines() if 'ANOMALY' not in _][:-1]

        program_set = set()
        file = csv.reader(io.StringIO('\n'.join(result)))
        for i in file:
            # print('#' * 100)
            if 'cmd.exe' in i[-1] and 'python' in i[-1]:
                program_name = re.search('python\s+(.*)', i[-1]).group(1)
                program_set.add(program_name)
            else:
                if len(psutil.Process(int(i[1])).children()) == 1:
                    os.popen(f'taskkill /pid {i[1]} /f')

        # print("当前已启动的程序：",program_set)
        print("需要启动的程序：",set(spider_list)-program_set)

        for i, spider_name in enumerate(set(spider_list)-program_set):
            print(f'{spider_name}当前程序需要启动，正在启动')
            os.system('start cmd /k python ' + spider_name)
            time.sleep(3)
            print(f'已启动程序：{spider_name}'.center(100,'#'))

        program_set.clear()
        time.sleep(60)
    except Exception as e:
        print(e)


# taskkill /IM python.exe /F
# taskkill /IM chrome.exe /F
# taskkill /IM cmd.exe /F