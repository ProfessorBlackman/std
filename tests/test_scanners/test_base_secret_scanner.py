# tests/test_cli.py
import os
import pytest

from src.std.scanners.base_secret_scanner import BaseSecretScanner

scanner = BaseSecretScanner()


@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample_file.txt"
    file_content = """
    # This is a sample Python script containing various types of secrets

    # API Keys
    API_KEY = "12345-ABCDE-67890-FGHIJ"
    api_key = "AKIAIOSFODNN7EXAMPLE"

    # Passwords
    DB_PASSWORD = "supersecretpassword123"
    password = "anotherpassword456"

    # Private Keys
    PRIVATE_KEY = \"""
    -----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEA0A1spxQ7DPghlzJz9D7uAfhxT1SKy3V4Yl5y7O2+U6sm6iMB
    ...
    XJO/YIbT+E4c9uLvZ3P0J5/yZd3A==
    -----END RSA PRIVATE KEY-----
    \"""

    # Misc Secrets
    SECRET_TOKEN = "this_is_a_very_secret_token"
    client_secret = "shhh_dont_tell_anyone"
    """
    file_path.write_text(file_content)
    return file_path


@pytest.fixture
def another_sample_file(tmp_path):
    file_path = tmp_path / "another_sample_file.txt"
    file_content = """
    import os

    # API Keys in environment variables
    os.environ["API_KEY"] = "AbCdEfGhIjKlMnOpQrStUvWxYz123456"
    os.environ["api_key"] = "zyxwvutsrqponmlkjihgfedcba654321"

    # Passwords in environment variables
    os.environ["DB_PASSWORD"] = "env_supersecretpassword"
    os.environ["password"] = "env_anotherpassword"

    # Embedded private key in environment variable
    os.environ["PRIVATE_KEY"] = \"""
    -----BEGIN DSA PRIVATE KEY-----
    MIIBugIBAAKBgQCxG9F7DxC8x2P3MeQc6P9s5J9Vb0Qz9W8jFbT1K7vLs8d1nMPp
    ...
    tY5B7+aX5+ptvewFkDQ==
    -----END DSA PRIVATE KEY-----
    \"""

    # Misc Secrets
    os.environ["SECRET_TOKEN"] = "super_secret_token_env"
    os.environ["client_secret"] = "keep_this_secret_too"
    """
    file_path.write_text(file_content)
    return file_path


def test_scan_file(sample_file):
    secrets = scanner.scan_file(file_path=str(sample_file))
    assert get_length(secrets) == 5
    assert secrets[0][0] == 'API Key'
    assert secrets[1][0] == 'Password'
    assert secrets[2][0] == 'Private Key'


def test_scan_directory(tmp_path, sample_file):
    sample_dir = tmp_path / "sample_directory"
    os.makedirs(sample_dir)
    sample_file_path = sample_dir / "sample_file.txt"
    sample_file_path.write_text(sample_file.read_text())

    results = scanner.scan_directory(path=str(sample_dir))
    assert get_length(results) == 2

    for secrets in results.values():
        assert get_length(secrets) == 5
        assert secrets[0][0] == 'API Key'
        assert secrets[1][0] == 'Password'
        assert secrets[2][0] == 'Private Key'


def get_length(data: list | dict) -> int:
    length = 0
    if type(data) is dict:
        for entry in data.values():
            if type(entry) is tuple:
                length += len(entry[1])
            else:
                length += 1
    for entry in data:
        if type(entry) is tuple:
            length += len(entry[1])
        else:
            length += 1
    return length
