import torch

# Prepare valid input data
input_tensor = torch.randn(2, 3, 4, 4)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_tensor = dropout_layer(input_tensor)