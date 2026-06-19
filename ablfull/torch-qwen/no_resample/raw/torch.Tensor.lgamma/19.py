import torch

# Task 2: Generate input data
input_tensor = torch.tensor([0.5, 1.0, 2.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.lgamma(input_tensor)
print(result)