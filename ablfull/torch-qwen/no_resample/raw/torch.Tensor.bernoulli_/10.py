import torch

# Prepare valid input data
p = 0.7  # Scalar value within [0, 1]
input_tensor = torch.tensor([[0.3, 0.8], [0.4, 0.6]])

# Call the API
result = input_tensor.bernoulli_(p)
print(result)