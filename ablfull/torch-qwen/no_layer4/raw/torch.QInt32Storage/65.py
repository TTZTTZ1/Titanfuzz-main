import torch

# Generate input data
input_data = torch.tensor([1, 2, 3], dtype=torch.int8)

# Call the API
storage = torch.QInt32Storage(input_data, wrap_storage=None, dtype=torch.qint32, device='cpu', _internal=False)