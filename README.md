# trello_export

Tool for exporting archived Trello cards, categorized by label to help track activity for liaison reports and annual reviews. _Andrew Weymouth, Fall 2024_.

## Step 1: Building Virtual Environment for Python Dependencies

```bash
python3 -m venv .venv
```

## Step 2: Activate the Virtual Environment

On Mac

```bash
source .venv/bin/activate
```

On Windows
```bash
.venv\Scripts\activate
```

## Step 3: Install Required Packages

```bash
pip install requests
```

## Step 4: Locating Trello API Key, API Token, and Board ID

To use the script, you will need to locate your Trello **API Key**, **API Token**, and the **Board ID** for the board you wish to export archived cards from.

### A. Get Your Trello API Key and API Token
   - Visit the [Trello Developer API Key Page](https://trello.com/app-key).
   - Log in with your Trello account credentials.
   - Go to the [Power-Up Admin Portal](https://trello.com/power-ups/admin/)
   - Select **New** Power-Up and Integration
   - On the sidebar, select **API Key**
   - Copy your **API Key** from the page save into a safe document
   - To the right of the API field, select [manually generate a token](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&key=1f28d3b35afb7ee011095b37a887e0f3)
   - Approve the requested permissions and copy your **API Token**

### B. Find Your Board ID
   - Open the Trello board in your web browser
   - Look at the URL. It should look something like this:
     ```
     https://trello.com/b/abcdef123456/my-board-name
     ```
   - The **Board ID** is the string of characters after `/b/` and before the next `/`. In this example, the Board ID is `abcdef123456`.

### C. Add API Credentials and Board ID to the Script
   - Open the `script.py` file in a text editor
   - Replace the placeholders for `API_KEY`, `API_TOKEN`, and `BOARD_ID` with your actual values:

     ```python
     API_KEY = 'your_api_key_here'
     API_TOKEN = 'your_api_token_here'
     BOARD_ID = 'your_board_id_here'
     ```

## Step 5: Run the Script

Once everything is set up, run the script:

```bash
python script.py
```

## Step 6: Remove API information from script.py and add to .gitignore

To keep API information secure, remove this data before saving your script.py file and save it to the .gitignore file, which will preserve this information for future reference but only be accessible to you (as long as your repository is set to private).
