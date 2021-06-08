import os
import time

import docker
import requests
from docker.client import DockerClient

from ..utils import (
    CONTAINER_NAME,
    get_config,
    get_logs,
    get_response_text1,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    response = requests.get("http://127.0.0.1:8080")
    data = response.json()
    assert data == response_text
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 1
    assert config_data["use_max_workers"] is None
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "2376"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] >= 2
    assert config_data["bind"] == "0.0.0.0:2376"
    assert config_data["graceful_timeout"] == 120
    assert config_data["timeout"] == 120
    assert config_data["keepalive"] == 5
    assert config_data["errorlog"] == "-"
    assert config_data["accesslog"] == "-"
    logs = get_logs(container)
    assert '"GET / HTTP/1.1" 200' in logs
    assert "[INFO] Application startup complete." in logs


def test_defaults() -> None:
    image = "ismael-fastapi"
    response_text = get_response_text1()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    container = client.containers.run(
        image, name=CONTAINER_NAME, ports={"8080": "2376"}, detach=True
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    container.remove()
