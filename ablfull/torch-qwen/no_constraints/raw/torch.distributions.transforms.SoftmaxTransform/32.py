import torch

# Generate valid input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform()
output_data = transform(input_data)