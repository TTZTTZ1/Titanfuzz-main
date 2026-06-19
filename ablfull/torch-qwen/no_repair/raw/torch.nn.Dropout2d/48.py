import torch

# Prepare valid input data
input_tensor = torch.randn(1, 3, 4, 4)  # Example input tensor of shape (1, 3, 4, 4)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)
output_tensor = dropout_layer(input_tensor)