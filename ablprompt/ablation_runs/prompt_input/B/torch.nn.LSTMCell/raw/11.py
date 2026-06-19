import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_data = torch.randn(5, input_size)  # Sequence length of 5
h0 = torch.zeros(5, hidden_size)
c0 = torch.zeros(5, hidden_size)

# Forward pass through LSTMCell
h1, c1 = lstm_cell(input_data, (h0, c0))

print(h1.shape)  # Should print: torch.Size([5, 20])
print(c1.shape)  # Should print: torch.Size([5, 20])