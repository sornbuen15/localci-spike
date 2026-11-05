import os
import socket


def test_no_docker_socket():
    assert not os.path.exists("/var/run/docker.sock")


def test_no_secret_like_env():
    bad = [k for k in os.environ if any(w in k.upper() for w in ("TOKEN", "SECRET", "PASSWORD", "NETRC"))]
    assert bad == [], bad


def test_no_windows_or_home_mounts():
    mounts = open("/proc/mounts").read()
    for needle in ("/mnt/c", "/mnt/wsl", "C:\\\\", "/Users", "/home/"):
        assert needle not in mounts, needle


def test_no_docker_api_on_host_ports():
    for host in ("host.docker.internal", "172.17.0.1"):
        for port in (2375, 2376):
            s = socket.socket(); s.settimeout(1)
            try:
                assert s.connect_ex((host, port)) != 0, f"{host}:{port} open"
            except socket.gaierror:
                pass
            finally:
                s.close()


def test_not_privileged():
    caps = [l for l in open("/proc/self/status") if l.startswith("CapEff")][0].split()[1]
    assert caps != "000001ffffffffff" and caps != "0000003fffffffff", caps
