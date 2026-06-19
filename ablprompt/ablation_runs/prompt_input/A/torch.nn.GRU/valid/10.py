import torch
import torch.nn as nn

# Define a simple GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)

    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.gru(x, h0)  # out: tensor of shape (batch_size, seq_length, hidden_size)
        return out

# Example usage
if __name__ == "__main__":
    # Parameters
    input_size = 10
    hidden_size = 20
    num_layers = 2
    sequence_length = 5
    batch_size = 3

    # Create an instance of the GRU model
    gru_model = SimpleGRU(input_size, hidden_size, num_layers)

    # Dummy input data
    input_data = torch.randn(batch_size, sequence_length, input_size)

    # Forward pass
    output = gru_model(input_data)
    print(output.shape)  # Should print: torch.Size([3, 5, 20])