import torch

# Prepare valid input data
start = torch.tensor([1.0, 2.0])
end = torch.tensor([4.0, 5.0])
weight = 0.5

# Call the API
result = start.lerp_(end, weight)
print(result)