import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden states
input_data = torch.randn(5, 10)  # Batch size of 5, sequence length of 10, input size of 10
hx = torch.zeros(5, 20)           # Initial hidden state
cx = torch.zeros(5, 20)           # Initial cell state

# Process each time step
for i in range(input_data.size(0)):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

print(hx.shape)  # Should print torch.Size([5, 20])
print(cx.shape)  # Should print torch.Size([5, 20])