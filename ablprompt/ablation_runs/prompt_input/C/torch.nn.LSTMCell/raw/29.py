import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden/cell states
input_tensor = torch.randn(5, 10)  # Sequence length of 5, input size of 10
hx = torch.zeros(5, 20)            # Hidden state size of 20
cx = torch.zeros(5, 20)            # Cell state size of 20

# Process each time step
for i in range(input_tensor.size(0)):
    hx, cx = lstm_cell(input_tensor[i], (hx, cx))

print("Final hidden state:", hx)
print("Final cell state:", cx)