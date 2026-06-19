import torch
input_data = torch.tensor(0)
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data.item())