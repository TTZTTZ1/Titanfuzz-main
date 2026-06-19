import torch

# Generate input data
x = torch.tensor([-0.5, 0.0, 0.5])

# Call the API
result = x.asin_()
print(result)