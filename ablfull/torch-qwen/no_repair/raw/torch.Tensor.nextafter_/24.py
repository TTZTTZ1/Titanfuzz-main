import torch

# Task 2: Generate input data
self_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_tensor = torch.tensor([1.1, 2.2], dtype=torch.float32)

# Task 3: Call the API
result = self_tensor.nextafter_(other_tensor)