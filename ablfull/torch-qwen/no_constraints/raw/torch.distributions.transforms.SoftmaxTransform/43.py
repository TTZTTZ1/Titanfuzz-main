import torch

# Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform()
result = transform(input_data)
print(result)