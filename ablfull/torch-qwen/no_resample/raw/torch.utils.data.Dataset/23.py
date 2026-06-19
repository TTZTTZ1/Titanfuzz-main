import torch

# Prepare valid input data
data = [torch.randn(3, 224, 224) for _ in range(10)]

# Call the API
dataset = torch.utils.data.Dataset(data)