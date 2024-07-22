# another_sample_file.txt

import os

# API Keys in environment variables
os.environ["API_KEY"] = "AbCdEfGhIjKlMnOpQrStUvWxYz123456"
os.environ["api_key"] = "zyxwvutsrqponmlkjihgfedcba654321"

# Passwords in environment variables
os.environ["DB_PASSWORD"] = "env_supersecretpassword"
os.environ["password"] = "env_anotherpassword"

# Embedded private key in environment variable
os.environ["PRIVATE_KEY"] = """
-----BEGIN DSA PRIVATE KEY-----
MIIBugIBAAKBgQCxG9F7DxC8x2P3MeQc6P9s5J9Vb0Qz9W8jFbT1K7vLs8d1nMPp
...
tY5B7+aX5+ptvewFkDQ==
-----END DSA PRIVATE KEY-----
"""

# Misc Secrets
os.environ["SECRET_TOKEN"] = "super_secret_token_env"
os.environ["client_secret"] = "keep_this_secret_too"
