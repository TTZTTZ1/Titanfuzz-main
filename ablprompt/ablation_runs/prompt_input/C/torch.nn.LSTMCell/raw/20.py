import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_tensor = torch.randn(5, input_size)  # Sequence length of 5
hidden_state = torch.zeros(5, hidden_size)
cell_state = torch.zeros(5, hidden_size)

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print(next_hidden_state.shape)  # Should be (5, 20)
print(next_cell_state.shape)    # Should be (5, 20)