import torch
input_data = torch.randn(5)
transform = torch.distributions.transforms.SoftmaxTransform()
output = transform(input_data)