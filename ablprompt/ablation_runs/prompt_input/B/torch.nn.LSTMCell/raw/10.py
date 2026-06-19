import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden states
input_tensor = torch.randn(5, 10)  # Sequence length of 5, input size of 10
hx = torch.zeros(5, 20)            # Hidden state of size 20
cx = torch.zeros(5, 20)            # Cell state of size 20

# Process each time step
for i in range(input_tensor.size(0)):
    hx, cx = lstm_cell(input_tensor[i], (hx, cx))

print(hx.shape)  # Should print torch.Size([5, 20])
print(cx.shape)  # Should print torch.Size([5, 20])