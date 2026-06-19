import torch
part_transform = torch.nn.Identity()
compose_transform = torch.distributions.transforms.ComposeTransform([part_transform])
result = compose_transform(torch.tensor([0.5]))