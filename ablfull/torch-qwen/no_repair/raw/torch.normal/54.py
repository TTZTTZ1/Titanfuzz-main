import torch

# Generate input data
mean = torch.tensor([0.5])
std = torch.tensor([1.0])

# Call the API
result = torch.normal(mean=mean, std=std)
print(result)