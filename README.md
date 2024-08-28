# Rummy Game - Python Application

## Overview

This is a simplified version of the classic card game **Rummy** developed in Python. The game is designed to be played by two players, without jokers and wild cards, making it an easy introduction to both Rummy and Python programming concepts. Players can draw cards, create melds (sets or sequences), and lay off cards onto existing melds, with the goal of being the first to "go out" by using all the cards in their hand.

## Features

- **Card Class:** Represents individual cards, with methods to return a card's abbreviation and compare two cards.
- **Deck Class:** Manages a deck of 52 cards, shuffling and dealing them to players.
- **Player Class:** Represents each player, managing their hand of cards and allowing them to draw, discard, and sort their hand.
- **RummyGame Class:** Manages the gameplay, including dealing cards, handling turns, checking melds, and determining the winner.

## How to Play

1. **Setup:** The game starts by initializing a deck and two players. Each player is dealt 10 cards, and one card is placed in the discard pile to begin.

2. **Turns:** Players take turns performing the following actions:
   - **Draw:** A player can draw a card from either the top of the deck or the top of the discard pile.
   - **Meld:** A player can place a set or sequence on the table. 
     - **Set:** Three or four cards of the same rank (e.g., 7♥, 7♠, 7♣).
     - **Sequence:** Three or more consecutive cards of the same suit (e.g., 4♠, 5♠, 6♠).
   - **Lay Off:** A player can add cards to their own or other player's existing melds on the table.
   - **Discard:** A player must discard one card from their hand onto the discard pile at the end of their turn.

3. **Winning the Game:** The game continues until one player uses all their cards by creating valid melds and laying off cards. When this happens, the player "goes out" and wins the game.

## Classes and Methods

### 1. `Card` Class

- **Attributes:** `suit`, `rank`, `abbr` (abbreviation of the card).
- **Methods:** 
  - `get_abbreviation()`: Returns a short string representation of the card (e.g., '7♥').
  - `__str__()`: Returns a string representation of the card (e.g., '7 of Hearts').
  - `__lt__()`: Comparison method for sorting cards.

### 2. `Deck` Class

- **Attributes:** `cards` (list of Card objects).
- **Methods:** 
  - `__init__()`: Initializes and shuffles the deck.
  - `draw()`: Draws a card from the deck.

### 3. `Player` Class

- **Attributes:** `name`, `hand` (list of Card objects).
- **Methods:**
  - `draw(card)`: Adds a card to the player's hand.
  - `discard(card)`: Removes a card from the player's hand.
  - `sort_hand()`: Sorts the player's hand.

### 4. `RummyGame` Class

- **Attributes:** `deck`, `players`, `discard_pile`, `table`.
- **Methods:**
  - `deal_initial_hands()`: Deals initial hands to players.
  - `is_valid_meld(cards)`: Checks if a set of cards forms a valid meld.
  - `handle_melds_and_layoffs(player)`: Allows players to create melds and lay off cards.
  - `put_down_meld(player)`: Handles creating and placing down a new meld.
  - `lay_off_card(player)`: Handles laying off a card to existing melds.
  - `get_input(prompt)`: Gets user input and handles game exit.
  - `play_turn(player)`: Manages a single player's turn.
  - `reshuffle_discard_pile()`: Reshuffles the discard pile into the deck.
  - `check_winner(player)`: Checks if a player has won.
  - `play_game()`: Starts and controls the flow of the game.

## How to Run the Game on Your Own Machine

To get the game running on your local machine, follow these steps:

### Prerequisites

- Ensure you have [Python](https://www.python.org/downloads/) installed (version 3.x is recommended).
- You should have [Git](https://git-scm.com/downloads) installed to clone the repository.

### Installation Steps

1. **Clone the Repository:**

   Open a terminal and clone the repository using Git:

   ```bash
   git clone https://github.com/Sebdababo/Python-Rummy.git
   ```

2. **Navigate to the Project Directory:**

   Change to the directory where the repository was cloned:

   ```bash
   cd Python-Rummy
   ```

3. **Run the Game:**

   Execute the `rummy.py` script to start the game:

   ```bash
   python rummy.py
   ```

   Follow the on-screen instructions to play the game.

## Future Improvements

- Adding support for more than two players.
- Implementing a graphical user interface (GUI) for better user experience.
- Introducing jokers and wild cards to enhance gameplay options.
- Adding AI opponents for single-player mode.

## Example gameplay:
![rummy output](https://github.com/user-attachments/assets/536a0588-f15e-498c-be4a-7354fef74592)


Enjoy playing Rummy and exploring Python development!
