import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Sample input and hidden state initialization
input_data = torch.randn(3, input_size)  # Batch size of 3, sequence length of 3
hx = torch.zeros(3, hidden_size)
cx = torch.zeros(3, hidden_size)

# Forward pass through the LSTMCell
hx, cx = lstm_cell(input_data, (hx, cx))

print("Updated Hidden State:", hx)
print("Updated Cell State:", cx)