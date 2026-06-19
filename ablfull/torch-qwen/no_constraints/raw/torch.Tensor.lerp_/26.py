import torch

# Task 2: Generate input data
start_tensor = torch.tensor([0.0, 1.0])
end_tensor = torch.tensor([4.0, 5.0])
weight = 0.5

# Task 3: Call the API
result_tensor = start_tensor.lerp_(end_tensor, weight)
print(result_tensor)