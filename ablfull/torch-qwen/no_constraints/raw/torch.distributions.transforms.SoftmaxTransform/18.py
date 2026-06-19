import torch

# Generate input data
input_data = torch.randn(5)

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform()
output = transform(input_data)