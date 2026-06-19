import torch

# Prepare input data with NaN values to test nanmean functionality
input_data = torch.tensor([1.0, 2.0, float('nan'), 4.0])

# Call the target API
result = torch.Tensor.nanmean(input_data)

print(result)