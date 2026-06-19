import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_tensor = torch.tensor([1.5, 2.5], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.nextafter_(input_tensor, other_tensor)
print(result)