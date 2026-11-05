import multiprocessing as mp
import time


def _burn(seconds):
    end = time.time() + seconds
    while time.time() < end:
        pass


def test_tries_to_use_four_cpus_for_40s():
    ps = [mp.Process(target=_burn, args=(40,)) for _ in range(4)]
    [p.start() for p in ps]
    [p.join() for p in ps]
