import torch

# Generate input data
data = torch.randint(0, 256, (10,), dtype=torch.uint8)

# Call the API
storage = torch.QInt32Storage.from_buffer(data.numpy())