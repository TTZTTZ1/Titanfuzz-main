import torch

# Task 2: Generate input data
data = torch.tensor([100, 200, 300], dtype=torch.uint8)

# Task 3: Call the API
storage = torch.QUInt8Storage(wrap_storage=data.storage())