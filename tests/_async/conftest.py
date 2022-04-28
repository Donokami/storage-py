from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from storage3 import AsyncStorageClient


def pytest_configure(config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture(scope="session")
def storage() -> AsyncStorageClient:
    url = os.environ.get("SUPABASE_TEST_URL")
    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    key = os.environ.get("SUPABASE_TEST_KEY")
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    return AsyncStorageClient(url, key)
