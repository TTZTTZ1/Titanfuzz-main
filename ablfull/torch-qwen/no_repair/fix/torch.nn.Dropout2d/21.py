
import torch
input_tensor = torch.randn(3, 32, 32)
dropout_layer = torch.nn.Dropout2d(p=0.3)
output_tensor = dropout_layer(input_tensor)
