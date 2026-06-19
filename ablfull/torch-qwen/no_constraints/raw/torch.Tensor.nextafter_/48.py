import torch

# Prepare valid input data
x = torch.tensor(0.0)
y = torch.tensor(0.1)

# Call the API
result = torch.Tensor.nextafter_(x, y)

print(result)