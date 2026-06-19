
import torch
input_data = torch.randn(1, 3, 4, 4)
p = 0.3
inplace = False
dropout_layer = torch.nn.Dropout2d(p=p, inplace=inplace)
output = dropout_layer(input_data)
