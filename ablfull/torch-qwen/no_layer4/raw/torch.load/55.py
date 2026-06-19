import torch
from pathlib import Path

# Generate input data
f = Path("example.pt")  # Assuming 'example.pt' is a file path to be loaded

# Call the API
result = torch.load(f)