import torch

# Prepare valid input data
input_tensor = torch.randn(1, 64, 32, 32)

# Call the target API
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_tensor = dropout_layer(input_tensor)