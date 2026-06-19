import torch

# Prepare valid input data
start_tensor = torch.tensor([0.0, 1.0], dtype=torch.float32)
end_tensor = torch.tensor([4.0, 5.0], dtype=torch.float32)
weight = 0.5

# Call the API
result = start_tensor.lerp_(end_tensor, weight)

print(result)