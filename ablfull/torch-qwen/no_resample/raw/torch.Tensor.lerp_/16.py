import torch

# Prepare valid input data
start_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
end_tensor = torch.tensor([4.0, 5.0], dtype=torch.float32)
weight = 0.5

# Call the API
result_tensor = start_tensor.clone()
result_tensor.lerp_(end_tensor, weight)

print(result_tensor)