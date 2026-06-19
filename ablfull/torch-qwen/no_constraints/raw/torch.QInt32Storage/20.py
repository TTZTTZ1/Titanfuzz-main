import torch

# Task 2: Generate input data
data = torch.randint(0, 256, (10,), dtype=torch.uint8)

# Task 3: Call the API
storage = torch.QInt32Storage(wrap_storage=data.storage())