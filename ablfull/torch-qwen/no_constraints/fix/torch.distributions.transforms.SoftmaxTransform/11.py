import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=0)
output = transform(input_data)
print(output)