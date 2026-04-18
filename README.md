<div align="center">

# <img src="https://img.icons8.com/fluency/48/snake.png" width="40"/> Snake Game

### Grid-Based Arcade Game • Real-Time Movement • Score Tracking

<p>
A classic Snake Game built with real-time movement mechanics where players control a growing snake, collect food, and avoid collisions to achieve the highest score.
</p>

<br/>

<a href="YOUR_LIVE_LINK_HERE" target="_blank">
  <img src="https://img.shields.io/badge/Play%20Game-Open-1E88E5?style=for-the-badge&logo=google-chrome&logoColor=white" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Python-Game%20Logic-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pygame-Rendering-1E88E5?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Grid-System-Game%20Mechanics-6A1B9A?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-2E7D32?style=for-the-badge"/>

</div>

---

## Overview

**Snake Game** is a grid-based arcade game where the player controls a snake that moves continuously across the screen.

The objective is simple:
- Eat food to grow  
- Avoid collisions  
- Achieve the highest score  

---

## Screenshot & Explanation

<div align="center">

<img src="assets/output.png" width="700"/>

</div>

### What You See in the Game

- 🟩 **Green Blocks** → Snake body  
- 🟥 **Red Block** → Food  
- 🔵 **Grid Background** → Movement system  
- 📊 **Score (Top-Left)** → Current score  

---

## Game Rules

1. The snake moves continuously in one direction  
2. Player can change direction using arrow keys  
3. Eating food:
   - Increases snake length  
   - Increases score  
4. Game ends if:
   - Snake hits the wall  
   - Snake collides with itself  

---

## Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |

---

## Game Mechanics

- Grid-based movement system  
- Snake grows dynamically after eating food  
- Random food spawning  
- Collision detection system  
- Continuous game loop  

---

## Key Features

- Real-time gameplay  
- Smooth directional controls  
- Score tracking  
- Dynamic difficulty (longer snake = harder game)  
- Minimal and clean UI  

---

## Technology Stack

<div align="center">

| Category | Technology |
|----------|-----------|
| Language | <img src="https://img.icons8.com/color/20/python.png"/> Python |
| Game Engine | <img src="https://img.icons8.com/ios-filled/20/game-controller.png"/> Pygame |
| Rendering | Grid-Based Rendering |

</div>

---

## Project Structure

```
05_snake_game/
├── main.py
├── game_logic.py
├── assets/
│   └── output.png
├── requirements.txt
└── README.md
```

---

## How It Works

1. Game initializes snake position and direction  
2. Game loop runs continuously  
3. Player input updates direction  
4. Each frame:
   - Snake moves forward  
   - Collision is checked  
   - Food is generated if eaten  
5. Score updates dynamically  

---

## Installation

```bash
git clone https://github.com/priyanildz/Snake-Game.git
cd Snake-Game
```

```bash
pip install pygame
```

---

## Run Game

```bash
python main.py
```

---

## Use Cases

- Learning game development basics  
- Understanding real-time systems  
- Practicing Python and Pygame  
- Beginner-friendly project  

---

## Future Improvements

- Add sound effects  
- Add pause/resume  
- High score system  
- Difficulty levels  
- Mobile/GUI enhancements  

---

## License

This project is licensed under the MIT License.

---

<div align="center">

Developed by  
<strong>priyanildz</strong>

</div>