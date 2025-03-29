import time
from datetime import datetime
import sys

for i in range(60):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # sys.stdout.flush()  # 👈 Force log output to appear immediately
    time.sleep(1)
