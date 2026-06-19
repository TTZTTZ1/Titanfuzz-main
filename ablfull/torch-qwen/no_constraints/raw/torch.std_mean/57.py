import torch

# Prepare valid input data
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Call the API
result = torch.std_mean(x)

print(result)