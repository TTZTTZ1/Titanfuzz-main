import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
transform = torch.distributions.transforms.SoftmaxTransform()
result = transform(input_data)
print(result)