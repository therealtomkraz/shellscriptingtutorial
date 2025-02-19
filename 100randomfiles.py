import os
import random
from random_word import RandomWords

# Configuration
OUTPUT_DIR = "random_files"
EXTENSIONS = ['jpg', 'png', 'gif', 'pdf', 'docx', 'txt', 'zip', 'tar.gz', 'rar']
MIN_SIZE = 1024  # 1KB
MAX_SIZE = 5120  # 5KB

# Initialize generators
r = RandomWords()
os.makedirs(OUTPUT_DIR, exist_ok=True)

for _ in range(100):
    # Generate filename
    noun = r.get_random_word().replace(" ", "_").lower()
    filename = f"{noun}_{random.randint(1000,9999)}"
    ext = random.choice(EXTENSIONS)
    path = os.path.join(OUTPUT_DIR, f"{filename}.{ext}")

    # Generate random content
    file_size = random.randint(MIN_SIZE, MAX_SIZE)
    random_content = os.urandom(file_size)  # Cryptographically secure random bytes

    # Write to file
    with open(path, 'wb') as f:
        f.write(random_content)

print(f"Created 100 random files in '{OUTPUT_DIR}' with sizes between {MIN_SIZE//1024}KB-{MAX_SIZE//1024}KB")
