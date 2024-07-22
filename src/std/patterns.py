SECRET_PATTERNS = {
    'API Key': r'(?i)api[_-]?key\s*[:=]\s*["\']?[A-Za-z0-9-]{20,40}["\']?',
    'Password': r'(?i)password\s*[:=]\s*["\']?.{6,}["\']?',
    'Private Key': r'-----BEGIN (?:RSA|DSA|EC|OPENSSH) PRIVATE KEY-----'
}