
import torch
input_tensor = torch.randn(1, 3, 28, 28)
dropout_layer = torch.nn.Dropout2d(p=0.2, inplace=False)
output_tensor = dropout_layer(input_tensor)
