import torch

# Example input tensor (batch_size=1, channels=1, height=4, width=4)
input_tensor = torch.tensor([[[[1, 2, 3, 4],
                               [5, 6, 7, 8],
                               [9, 10, 11, 12],
                               [13, 14, 15, 16]]]])

# Using Unfold with specific parameters
unfold = torch.nn.Unfold(kernel_size=(2, 2), stride=(1, 1), padding=(0, 0))
output = unfold(input_tensor)

print(output)