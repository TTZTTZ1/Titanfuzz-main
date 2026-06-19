import torch

# Prepare valid input data
input_data = 0  # Scalar value within the allowed range [0, 1]

# Call the target API
transform = torch.distributions.transforms.SoftmaxTransform(input_data)