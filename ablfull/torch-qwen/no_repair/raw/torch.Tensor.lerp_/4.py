import torch

# Generate input data
start = torch.tensor([0.0, 1.0, 2.0])
end = torch.tensor([4.0, 5.0, 6.0])
weight = 0.5

# Call the API
result = start.lerp_(end, weight)
print(result)