"""Basic Security+ concept: demonstrate hashing for data integrity."""

import hashlib

def generate_sha256(message: str) -> str:
    """Return SHA-256 hash of given message."""
    return hashlib.sha256(message.encode()).hexdigest()


def main() -> None:
    """Run a simple hashing demonstration."""
    sample_data = "SecurityPlus"
    print(f"Message: {sample_data}")
    print(f"SHA-256: {generate_sha256(sample_data)}")


if __name__ == "__main__":
    main()
