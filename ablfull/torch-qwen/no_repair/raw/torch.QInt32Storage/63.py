import torch

# Generate input data
input_data = torch.randint(0, 256, (5,), dtype=torch.uint8)

# Call the API
storage = torch.QInt32Storage(input_data)