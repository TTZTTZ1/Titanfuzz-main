import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_tensor = torch.randn(1, input_size)  # Batch size of 1
hx = torch.zeros(1, hidden_size)          # Initial hidden state
cx = torch.zeros(1, hidden_size)          # Initial cell state

# Forward pass through LSTMCell
hx, cx = lstm_cell(input_tensor, (hx, cx))

print("Updated Hidden State:", hx)
print("Updated Cell State:", cx)