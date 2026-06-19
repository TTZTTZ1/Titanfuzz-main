import torch

# Prepare valid input data
start_tensor = torch.tensor([1.0, 2.0])
end_tensor = torch.tensor([4.0, 5.0])
weight = 0.5

# Call the API
start_tensor.lerp_(end_tensor, weight)
print(start_tensor)