import torch

# Generate input data
data = torch.randint(0, 256, (3,), dtype=torch.uint8)

# Call the API
storage = torch.QInt32Storage(wrap_storage=None, dtype=torch.qint32, device='cpu', _internal=False)