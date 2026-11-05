import os
import time


def test_writes_4gb_slowly():
    chunk = os.urandom(1024 * 1024)
    with open("/tmp/fill.bin", "wb") as f:
        for i in range(4096):            # 4 GB in 1 MB writes, ~100 MB/s
            f.write(chunk)
            if i % 100 == 0:
                f.flush(); os.fsync(f.fileno()); time.sleep(1)
