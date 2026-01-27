<div align="center">

# ⚡ Fruit Slicer - Typing Game

<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="300"/>

### A Fast-Paced Typing Game Built with Python & Pygame

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-00ADD8?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [How to Play](#-how-to-play) • [Game Objects](#-game-objects) • [Team](#-team)

---

</div>

## 📖 About

**Fruit Slicer** is an exciting typing game where you must type letters to slice falling fruits before they hit the ground! Test your typing speed and accuracy while avoiding bombs and collecting ice power-ups that freeze time.

<div align="center">
  <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="500"/>
</div>

---

## ✨ Features

### 🎯 Gameplay Mechanics
- 🍎 **Falling Fruits** - Type the letter on each fruit to slice it
- 💣 **Bombs** - Avoid typing bomb letters or it's instant game over!
- ❄️ **Ice Power-ups** - Freeze time for 3-5 seconds
- 🔥 **Combo System** - Hit multiple fruits quickly for bonus points
- ❤️ **Three Lives** - Miss three fruits and it's game over
- 📈 **Progressive Difficulty** - Game speeds up as your score increases

### 🎨 Visual & Audio
- 🌈 **Colorful Graphics** - Vibrant fruits with distinct colors
- 📊 **Real-time HUD** - Score, lives, and combo indicators
- ⏱️ **Freeze Timer** - Visual countdown during ice power-up
- 🎮 **Smooth Animations** - 60 FPS gameplay

### 🏆 Scoring System
- **+1 point** per fruit sliced
- **Combo bonus** for rapid successive hits
- **Strike penalty** for missed fruits
- **High score tracking**

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/samba-gomis/fruit-slicer.git
cd fruit-slicer
```

2. **Install Pygame**
```bash
pip install pygame
```

3. **Run the game**
```bash
python main.py
```

That's it! Start slicing! 🎉

---

## 🎮 How to Play

<div align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="400"/>
</div>

### Controls

| Action | Key |
|--------|-----|
| **Slice Fruit** | Type the letter shown on the fruit (A-Z) |
| **Start Game** | `SPACE` (from menu) |
| **Restart** | `R` (after game over) |
| **Quit** | `Q` (from game over screen) |
| **Close Game** | `ESC` or close window |

### Game Rules

1. **Type quickly** - Fruits fall from the top of the screen with a letter on them
2. **Press the matching key** to slice the fruit and earn points
3. **Avoid bombs** (💣) - Typing their letter ends the game instantly
4. **Collect ice** (❄️) - Freezes all objects for 3-5 seconds
5. **Don't miss** - Let 3 fruits fall off screen = Game Over
6. **Build combos** - Hit multiple fruits rapidly for bonus points

### Difficulty Progression

As your score increases:
- ⚡ Objects fall faster
- 🎯 Spawn rate increases
- 💣 More bombs appear
- 🏆 Higher scores require better reflexes!

---

## 🎯 Game Objects

### 🍎 Fruits
- **Color**: Red, Green, or random colors
- **Effect**: +1 point when sliced
- **Spawn Rate**: 70%
- **Behavior**: Falls at increasing speed

### 💣 Bombs
- **Color**: Black or Yellow
- **Effect**: Instant Game Over if hit
- **Spawn Rate**: 20%
- **Warning**: Distinctive color to avoid accidentally hitting

### ❄️ Ice Cubes
- **Color**: Light Blue
- **Effect**: Freezes time for 3-5 seconds
- **Spawn Rate**: 10%
- **Power-up**: Gives you breathing room to plan your moves

---

## 📁 Project Structure

```
fruit-slicer/
│
├── 🎮 Core Game Files
│   ├── main.py                  # Entry point
│   ├── game.py                  # Main game loop & logic
│   └── constant.py              # Game constants & settings
│
├── 🎨 Models (Game Objects)
│   ├── models/
│   │   ├── fruit.py            # Fruit class
│   │   ├── bomb.py             # Bomb class
│   │   └── ice.py              # Ice power-up class
│
├── 🎯 Managers (Game Systems)
│   ├── managers/
│   │   ├── spawn_manager.py   # Object spawning logic
│   │   ├── score_manager.py   # Score & lives tracking
│   │   └── input_manager.py   # Keyboard input handling
│
├── 🖼️ UI Components
│   ├── ui/
│   │   ├── hud.py             # Heads-up display
│   │   ├── menu.py            # Main menu screen
│   │   └── game_over.py       # Game over screen
│
└── 📄 Documentation
    └── README.md
```

---

## 🛠️ Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

### Core Technologies
- **Python 3.7+** - Programming language
- **Pygame 2.0+** - Game development framework

### Programming Concepts
- ✅ Object-Oriented Programming (OOP)
- ✅ Game Loop Architecture
- ✅ Event-Driven Programming
- ✅ Sprite Management
- ✅ Collision Detection
- ✅ State Management
- ✅ Timer & Delay Systems

---

## 🎓 Learning Outcomes

This project helped us develop skills in:

### Technical Skills
- 🐍 Python game development
- 🎮 Pygame framework mastery
- 🏗️ Game architecture design (managers, models, UI separation)
- ⏱️ Timer and event systems
- 🎨 Graphics rendering and animation
- 🎯 Input handling and keyboard events

### Soft Skills
- 👥 Team collaboration (3-person team)
- 📋 Task distribution and specialization
- 🐛 Debugging complex interactions
- 📖 Code documentation
- ⏱️ Time management
- 🔄 Iterative development

---

## 🎨 Game Mechanics Breakdown

### Spawn System
```python
# Spawn probabilities
Fruits: 70%
Bombs: 20%
Ice: 10%

# Difficulty scaling
spawn_delay -= score * 10  # Faster spawning
object_speed += score * 0.1  # Faster falling
```

### Scoring System
```python
# Point calculation
Fruit sliced = +1 point
Combo multiplier = (fruits_in_combo - 1) bonus points
Missed fruit = +1 strike (3 strikes = game over)
Bomb hit = instant game over
```

### Freeze Mechanic
```python
# Ice power-up duration
freeze_time = random.randint(3, 5) seconds
All objects freeze in place
Resume normal speed after duration
```

### Combo Detection
```python
# Combo window
time_window = 500ms
If 2+ fruits hit within window → COMBO!
Display "COMBO x{count}!" on screen
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the project**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions
- 💡 Add more power-up types (slow motion, extra lives, shields)
- 🎵 Background music and sound effects
- 🏆 Persistent high score leaderboard
- 🌍 Multiple difficulty modes
- 🎨 Custom themes and skins
- 📊 Statistics tracking (accuracy, WPM, etc.)
- 🎯 Special fruit types with unique effects

---

## 👥 Team

<div align="center">

### 💻 Development Team

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/mahira-manico">
        <img src="https://github.com/mahira-manico.png" width="100px;" alt="Mahira Manico"/><br />
        <sub><b>Mahira Manico</b></sub>
      </a><br />
      <sub>💣 Bomb System | ❄️ Ice Power-ups<br/>📊 HUD | 🎯 Spawn Manager</sub>
    </td>
    <td align="center">
      <a href="https://github.com/samba-gomis">
        <img src="https://github.com/samba-gomis.png" width="100px;" alt="Samba Gomis"/><br />
        <sub><b>Samba Gomis</b></sub>
      </a><br />
      <sub>🎮 Game Loop | ⚙️ Core Logic<br/>🖼️ Menu | 💀 Game Over Screen</sub>
    </td>
    <td align="center">
      <a href="https://github.com/moinahalima-abdou">
        <img src="https://github.com/moinahalima-abdou.png" width="100px;" alt="Moina Halima Abdou"/><br />
        <sub><b>Moina Halima Abdou</b></sub>
      </a><br />
      <sub>🍎 Fruit System | 🏆 Score Manager<br/>⌨️ Input Handler</sub>
    </td>
  </tr>
</table>

### 🏫 Built at La Plateforme_

<img src="https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif" width="250"/>

*Project created as part of Python game development curriculum at [La Plateforme_](https://laplateforme.io/), Marseille*

</div>

---

## 📊 Game Statistics

### Difficulty Progression

| Score Range | Spawn Delay | Object Speed | Challenge Level |
|-------------|-------------|--------------|-----------------|
| 0-10 | 1000ms | 3 px/frame | 🟢 Easy |
| 11-25 | 800ms | 4 px/frame | 🟡 Medium |
| 26-50 | 600ms | 5 px/frame | 🟠 Hard |
| 51+ | 400ms | 6+ px/frame | 🔴 Expert |

---

## 🐛 Known Issues & Future Improvements

### Current Limitations
- ⚠️ No sound effects yet
- ⚠️ No background music
- ⚠️ Score doesn't persist between sessions
- ⚠️ No difficulty selection menu

### Planned Features
- [ ] 🎵 Add sound effects (slice, explosion, freeze)
- [ ] 🎶 Background music with volume control
- [ ] 💾 High score persistence with leaderboard
- [ ] 🎯 Difficulty selection (Easy/Medium/Hard)
- [ ] 🏆 Achievement system
- [ ] 📊 Statistics dashboard (accuracy, avg speed)
- [ ] 🎨 Multiple visual themes
- [ ] 🌟 Particle effects for slicing
- [ ] ⏸️ Pause menu
- [ ] 📱 Mobile/touch controls

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- 🎓 **La Plateforme_** for the project-based learning approach
- 🎮 **Pygame Community** for excellent documentation
- 🍎 **Fruit Ninja** for the original inspiration
- 🎨 Design inspiration from classic arcade typing games

---

## 📞 Support & Contact

Having issues or questions? Feel free to:

- 🐛 [Open an issue](https://github.com/samba-gomis/fruit-slicer/issues)
- 💬 Contact the team members directly
- ⭐ Star the repo if you like it!

---

## 🎯 Game Tips & Tricks

### For Beginners
1. **Focus on fruits first** - Ignore bombs and ice initially
2. **Use peripheral vision** - Don't stare at individual objects
3. **Stay calm** - Panic leads to mistakes
4. **Practice letter positions** - Know your keyboard layout

### For Advanced Players
1. **Hunt for combos** - Group similar letters together
2. **Strategic ice usage** - Save ice for high-pressure moments
3. **Bomb awareness** - Always track bomb positions
4. **Rhythm over speed** - Consistent typing beats frantic mashing

---

<div align="center">

### 🎮 Ready to test your typing skills?

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="300"/>

**[⬆ Back to Top](#-fruit-slicer---typing-game)**

[![GitHub](https://img.shields.io/badge/GitHub-samba--gomis%2Ffruit--slicer-181717?style=for-the-badge&logo=github)](https://github.com/samba-gomis/fruit-slicer)

*Type fast, slice faster! 🍎⚡*

</div>
