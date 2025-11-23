#!/bin/bash
# Perplexity MCP Setup Script
# Ensures dependencies are installed and environment is ready

set -e

echo "🔧 Setting up Perplexity MCP..."

# Find Python 3
PYTHON_CMD=""
for cmd in python3 /usr/bin/python3 /usr/local/bin/python3 /opt/homebrew/bin/python3; do
    if command -v "$cmd" &> /dev/null; then
        PYTHON_CMD="$cmd"
        echo "✓ Found Python: $PYTHON_CMD"
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Python 3 not found. Please install Python 3."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
echo "  Python version: $PYTHON_VERSION"

# Install dependencies
echo "📦 Installing dependencies..."
$PYTHON_CMD -m pip install --user --upgrade pip -q
$PYTHON_CMD -m pip install --user -r requirements.txt -q

echo "✓ Dependencies installed"

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found"
    echo "   Create .env with: PERPLEXITY_API_KEY=your_key_here"
else
    echo "✓ .env file found"
fi

# Update .mcp.json with correct Python path
echo "🔧 Updating .mcp.json with correct Python path..."
cat > .mcp.json << EOF
{
  "mcpServers": {
    "perplexity": {
      "command": "$PYTHON_CMD",
      "args": ["/Users/markus/perplexity/src/perplexity_mcp.py"],
      "env": {
        "PYTHONPATH": "/Users/markus/perplexity",
        "PYTHONDONTWRITEBYTECODE": "1"
      }
    }
  }
}
EOF

echo "✓ .mcp.json updated"

# Test the setup
echo "🧪 Testing setup..."
$PYTHON_CMD src/perplexity_mcp.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "To use Perplexity MCP in Claude Code:"
echo "  1. Make sure .env contains PERPLEXITY_API_KEY=your_key"
echo "  2. Restart Claude Code"
echo "  3. Ask Claude to search: 'Search for AI trends 2025'"
