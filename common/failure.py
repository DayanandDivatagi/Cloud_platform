import os
import time
import threading

FAIL_MODE = os.getenv("FAIL_MODE", "normal")

def apply_failure():
    if FAIL_MODE == "cpu_spike":
        def burn():
            while True:
                pass
        threading.Thread(target=burn).start()

    elif FAIL_MODE == "latency":
        time.sleep(5)

    elif FAIL_MODE == "crash":
        os._exit(1)
