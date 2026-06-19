import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 4, 4)

# Call the API
dropout = torch.nn.Dropout2d(p=0.5)
output_tensor = dropout(input_tensor)