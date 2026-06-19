import torch

# Generate input data
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Call the API
result = torch.std_mean(data)

print(result)