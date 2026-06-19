import torch

# Generate input data
input_tensor = torch.randn(10)

# Call the API
result = torch.std_mean(input_tensor, unbiased=False)
print(result)