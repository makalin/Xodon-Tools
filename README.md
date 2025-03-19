# Xodon Tools

**Xodon Tools - A bridging utility for seamless transmission between X and Mastodon**

Xodon Tools is a Python-based utility that bridges your X (Twitter) and Mastodon accounts. It automatically mirrors your X posts to Mastodon and syncs your X following list by searching for and following those users on Mastodon. Designed for users who want to maintain a presence across both platforms without manual effort, Xodon Tools simplifies cross-platform engagement.

## Features

- **Post Syncing**: Automatically posts your X tweets to Mastodon in real-time (or near real-time via polling).
- **Following Sync**: Finds and follows your X friends on Mastodon, bridging your social networks.
- **Customizable Polling**: Adjust how often the app checks for new X posts.
- **Lightweight**: Built with Python, leveraging `tweepy` and `requests` for simplicity and efficiency.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/makalin/Xodon-Tools.git
   cd Xodon-Tools
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed, then run:
   ```bash
   pip install tweepy requests
   ```

3. **Set Up API Credentials**:
   - **X (Twitter)**: Obtain API Key, API Secret, Access Token, and Access Token Secret from the [X Developer Portal](https://developer.twitter.com/).
   - **Mastodon**: Generate an Access Token from your Mastodon instance (e.g., via Settings > Development).

## Configuration

Create a `.env` file in the project root and add your credentials:

```env
X_API_KEY=your-api-key
X_API_SECRET=your-api-secret
X_ACCESS_TOKEN=your-access-token
X_ACCESS_SECRET=your-access-token-secret
MASTODON_INSTANCE=https://mastodon.social  # Replace with your instance URL
MASTODON_TOKEN=your-mastodon-access-token
```

Update the script to load these from the `.env` file (requires `python-dotenv`):
```bash
pip install python-dotenv
```

Modify the script’s top section like this:
```python
from dotenv import load_dotenv
import os

load_dotenv()
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
MASTODON_INSTANCE = os.getenv("MASTODON_INSTANCE")
MASTODON_TOKEN = os.getenv("MASTODON_TOKEN")
```

## Usage

1. **Run the App**:
   ```bash
   python xodon.py
   ```
2. **Enter Details**:
   - Your X username (without @).
   - Polling interval in seconds (e.g., 60).

3. **What Happens**:
   - The app syncs your X following list to Mastodon on startup.
   - It then monitors your X account for new posts and mirrors them to Mastodon.

### Example Output
```
Enter your X username (without @): myxuser
Enter polling interval in seconds (e.g., 60): 60
Xodon Tools - A bridging utility for seamless transmission between X and Mastodon
Starting app for myxuser...
Syncing following list for myxuser...
Found 50 users on X.
Followed user1 on Mastodon as @user1@mastodon.social
Monitoring X posts every 60 seconds...
New tweet detected: Hello world!...
Posted to Mastodon: Hello world!...
```

## Limitations

- **API Rate Limits**: X’s free tier limits reads and posts; Mastodon limits vary by instance. Adjust polling intervals accordingly.
- **User Matching**: Matches X usernames to Mastodon, which may not always be accurate. Bio or name matching could improve this (future feature).
- **Single Instance**: Currently supports one Mastodon instance. Multi-instance support is planned.

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

### Ideas for Improvement
- Webhook support for real-time X updates (requires premium X API access).
- Multi-instance Mastodon support.
- GUI interface for easier configuration.
- Enhanced user matching logic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Tweepy](https://github.com/tweepy/tweepy) for X API integration.
- Uses [Mastodon API](https://docs.joinmastodon.org/api/) for Mastodon interactions.

- Add a `LICENSE` file to your repo (e.g., MIT License text) if you choose to include licensing.
- The `.env` setup is recommended for security; the README assumes you’ll update the code accordingly.
- This README is structured for clarity and appeal on GitHub, with Markdown formatting.

Let me know if you’d like to adjust any section or add more details!
