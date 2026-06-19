import torch

# Generate input data
p = 0.7  # Scalar value within the range [0, 1]
input_tensor = torch.zeros(3, 4)  # Example tensor of any shape

# Call the API
result = input_tensor.bernoulli_(p)