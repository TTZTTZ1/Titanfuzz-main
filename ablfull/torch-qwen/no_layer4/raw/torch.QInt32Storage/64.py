import torch

# Task 2: Generate input data
data = [torch.tensor([1, 2, 3], dtype=torch.int8)]

# Task 3: Call the API
storage = torch.QInt32Storage(data)