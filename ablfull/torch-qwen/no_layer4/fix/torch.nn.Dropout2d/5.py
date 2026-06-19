import torch
input_tensor = torch.randn(1, 3, 32, 32)
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_tensor = dropout_layer(input_tensor)