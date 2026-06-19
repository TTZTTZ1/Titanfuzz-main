import torch

# Define LSTMCell parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial states
batch_size = 5
input_tensor = torch.randn(batch_size, input_size)
hx = torch.zeros(batch_size, hidden_size)
cx = torch.zeros(batch_size, hidden_size)

# Forward pass through LSTMCell
hx, cx = lstm_cell(input_tensor, (hx, cx))

print("Updated Hidden State:", hx)
print("Updated Cell State:", cx)