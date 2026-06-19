import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_tensor = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5
hx = torch.zeros(5, hidden_size)          # Initial hidden state
cx = torch.zeros(5, hidden_size)          # Initial cell state

# Forward pass through LSTMCell
for i in range(input_tensor.size(0)):
    hx, cx = lstm_cell(input_tensor[i], (hx, cx))

print(hx.shape, cx.shape)  # Output should be (5, 20) for both hidden and cell states