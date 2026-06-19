import torch

# Task 2: Generate input data
data = torch.tensor([0, 1, 2, 3], dtype=torch.uint8)

# Task 3: Call the API torch.QUInt8Storage
storage = torch.QUInt8Storage.from_tensor(data)