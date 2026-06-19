import torch

# Task 2: Generate input data - a tensor of floats within the range [-π, π]
input_data = torch.tensor([-torch.pi, -0.5 * torch.pi, 0.0, 0.5 * torch.pi, torch.pi], dtype=torch.float32)

# Task 3: Call the API torch.Tensor.sin
result = torch.sin(input_data)
print(result)