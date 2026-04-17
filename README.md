<div align="center">

# <img src="https://img.icons8.com/fluency/48/snake.png" width="40"/> Snake Game

### Classic Arcade • Real-Time Interaction • Browser-Based Game

<p>
A classic Snake Game implemented in the browser, where players control a snake to collect food, grow in length, and avoid collisions.
</p>

<br/>

<a href="YOUR_LIVE_LINK_HERE" target="_blank">
  <img src="https://img.shields.io/badge/Play%20Game-Open-1E88E5?style=for-the-badge&logo=google-chrome&logoColor=white" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/HTML-Structure-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-Game%20Logic-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Canvas-Rendering-000000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-2E7D32?style=for-the-badge"/>

</div>

---

## Overview

**Snake Game** is a browser-based implementation of the classic arcade game where the player controls a snake that moves around the screen, eats food, and grows in size.

The objective is to survive as long as possible without colliding with the walls or the snake’s own body.

---

## Screenshots

<div align="center">

| Gameplay | 
|----------|
| <img src="assets/output.png" width="1000"/> | 

</div>

---

## Explanation of Gameplay

- The snake moves continuously on the grid  
- Player controls direction using keyboard keys  
- Food appears randomly on the screen  
- Eating food increases snake length and score  
- Game ends if:
  - Snake hits the wall  
  - Snake collides with itself  

---

## Key Features

- Real-time snake movement  
- Keyboard controls for direction  
- Random food generation  
- Score tracking system  
- Collision detection (walls and self)  
- Game over state handling  
- Smooth gameplay using browser rendering  

---

## Technology Stack

<div align="center">

| Category | Technology |
|----------|-----------|
| Structure | <img src="https://img.icons8.com/color/20/html-5.png"/> HTML |
| Styling | <img src="https://img.icons8.com/color/20/css3.png"/> CSS |
| Logic | <img src="https://img.icons8.com/color/20/javascript.png"/> JavaScript |
| Rendering | <img src="https://img.icons8.com/ios-filled/20/game-controller.png"/> Canvas API |

</div>

---

## Project Structure

```
05_snake_game/
├── index.html
├── style.css
├── script.js
├── assets/
│   ├── gameplay.png
│   └── gameover.png
└── README.md
```

---

## How It Works

1. Game initializes with snake position  
2. Game loop runs continuously  
3. Player input changes snake direction  
4. Snake moves and checks for:
   - Food collision → grow  
   - Wall/self collision → game over  
5. Score updates dynamically  

---

## Controls

| Key | Action |
|-----|--------|
| Arrow Up | Move Up |
| Arrow Down | Move Down |
| Arrow Left | Move Left |
| Arrow Right | Move Right |

---

## Getting Started

### Prerequisites

- Web browser  

---

### Installation

```bash
git clone https://github.com/priyanildz/Snake-Game.git
cd Snake-Game
```

---

## Run Game

Open:

```
index.html
```

in your browser

---

## Use Cases

- Learning JavaScript game logic  
- Understanding real-time rendering  
- Practicing event handling  
- Building interactive browser games  

---

## Future Improvements

- Add difficulty levels  
- Add sound effects  
- Mobile touch controls  
- Leaderboard system  
- Pause and resume functionality  

---

## License

This project is licensed under the MIT License.

---

<div align="center">

Developed by  
<strong>priyanildz</strong>

</div>