import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create dummy input and initial hidden/cell states
input_tensor = torch.randn(1, input_size)
hx = torch.zeros(1, hidden_size)
cx = torch.zeros(1, hidden_size)

# Forward pass through LSTMCell
hx_new, cx_new = lstm_cell(input_tensor, (hx, cx))

print("New Hidden State:", hx_new)
print("New Cell State:", cx_new)