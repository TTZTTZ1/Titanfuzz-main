import torch

# Task 2: Generate input data
data = torch.randint(0, 128, (5,), dtype=torch.int32)

# Task 3: Call the API
storage = torch.QInt32Storage(data.numpy())