import os
import time

import docker
from docker.client import DockerClient
from fastapi.testclient import TestClient
from app.index import app

from ..utils import (
    CONTAINER_NAME,
    get_logs,
    get_response_text1,
    remove_previous_container,
)
client = TestClient(app)

docker_client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    response = client.get("http://127.0.0.1:2376")
    data = response.json()
    assert data == response_text
    logs = get_logs(container)
    assert "Application startup complete." in logs
    assert "Started reloader process" in logs


def test_defaults() -> None:
    image = "ghcr.io/ismael-su/python-ci:latest"
    response_text = get_response_text1()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(docker_client)
    container = docker_client.containers.run(
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
