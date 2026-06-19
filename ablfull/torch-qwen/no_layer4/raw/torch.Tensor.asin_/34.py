import torch

# Generate input data: a tensor of values within the range [-1, 1]
input_tensor = torch.tensor([0.5], dtype=torch.float32)

# Call the API
result = input_tensor.asin_()
print(result)