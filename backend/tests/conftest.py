"""Pytest Configuration and Fixtures for Insurix Backend Test Suite."""

import sys
from pathlib import Path
import pytest
from starlette.testclient import TestClient

# Ensure repository root is on PYTHONPATH
repo_root = Path(__file__).resolve().parent.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from backend.main import create_app
from backend.api.policy import load_sample_policies
from backend.services.cost_service import load_treatments


@pytest.fixture(scope="session", autouse=True)
def init_test_environment():
    """Seeds sample data and in-memory caches before tests run."""
    load_sample_policies()
    load_treatments()


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    with TestClient(app) as tc:
        yield tc
