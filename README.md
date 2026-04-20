# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`ODT-2026-Siya_Pramiti`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Pramiti Goel]` | `[Electronics & Coding]` | `[Fabrication]` | `[Worked on coding and electronics, concept mechanism, physical build]` |
| `[Siya Ghorpade]` | `[ Mechanics & Connections]` | `[Fabrication]` | `[Worked on the circuit setup and connections, concept mechanism, physical build]` |

## 1.3 Project Title
`[Smash or Panic: TT Ball Launcher]`

## 1.4 One-Line Pitch
`[ Smash or panic-
 An Arduino-powered rhythmic table tennis launcher that turns ball shooting into a fast-paced reaction game.]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This project is an interactive table tennis ball launcher designed as a playful human–machine experience. The system uses a motorized mechanism to shoot ping pong balls toward a player, who must react using a racket. Instead of continuous random firing, the launcher is paired with a programmed countdown system using an OLED display and buzzer, creating a structured and timed gameplay experience.

The experience is engaging because it combines anticipation and reaction. The countdown builds tension, and the sudden launch creates moments of surprise, making the interaction feel both controlled and unpredictable. This balance keeps the player alert and encourages repeated play.

The project integrates mechanical design and embedded systems. It uses an ESP32 microcontroller to control timing, an OLED screen for visual feedback, a buzzer for auditory cues, and a servo-based mechanism for ball release. Together, these elements transform a simple launcher into an interactive, game-like system.'

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`What is the experience?
The project creates a fast-paced, physical game where a user plays table tennis against a machine that launches balls in a timed sequence. It feels like a mix between a game and a training partner, where the user must constantly react and adapt. The interaction is immediate — the user steps in, picks up a racket, and starts responding to incoming shots.

What do you want the player or participant to feel?
The user should feel excitement, urgency, and a sense of challenge. The countdown builds anticipation, and the sudden launch of balls creates moments of surprise. At higher speeds, the experience becomes slightly chaotic, pushing the player to react quickly and stay focused. Successfully returning shots feels satisfying and rewarding.

Why would someone want to try it again?
The experience encourages repetition because it is skill-based and dynamic. Players can try to improve their reaction time, maintain longer rallies, or challenge themselves at different speeds. The combination of rhythm, unpredictability, and physical engagement makes each attempt feel slightly different, motivating users to play again.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[ We are designing this project as if we are a small creative studio making a **[fast-paced interactive game]** for **[classmates and exhibition visitors]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Website]` | `[(https://www.pcbway.com/project/shareproject/Ping_Pong_Robot_V1_DIY_0c6b7731.html)]` | `[Helped understand how ping pong launchers are built using motors and how angle affects the ball direction.]` |
| `[Website]` | `[(https://www.instructables.com/Ping-Pong-Ball-Launcher-2/)]` | `[Gave a simple idea of how to build a ball launcher using basic materials and components.]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[What makes this project original is the shift from building a functional machine to designing an interactive experience. Instead of focusing on precision or automation, the project emphasizes human reaction, timing, and engagement.

The addition of a countdown system using an OLED display and buzzer introduces rhythm and anticipation, transforming the launcher from a continuous device into a structured game. This creates moments of tension followed by sudden action, making the experience feel dynamic and slightly unpredictable.

Rather than acting as a tool, the machine behaves more like an opponent, encouraging users to react, adapt, and improve. This shift in focus—from control to interaction—defines the uniqueness of the project.]`

---

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`press start → countdown (OLED + buzzer) → launch ball → player reacts → repeat until balls finish`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Table tennis enthusiasts and casual players` |
| Age range | `10+` |
| Solo or multiplayer | `solo(with optional score comparison between players)` |
| Expected duration of one round | `30 sec` |
| What should the player feel? | `Engaged, alert, and challenged` |
| Is explanation required before use? | `Minimal (basic instructions for gameplay)` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The player approaches the setup and loads a fixed number of balls into the machine.    `
2. **Start:** `The player presses the start button.`
3. **First Action:** `A countdown (3, 2, 1, GO) is displayed using the OLED screen with buzzer cues.  `
4. **Main Interaction:** `The machine launches balls at timed intervals, and the player responds using a racket.`
5. **System Response:** `The launcher continues to shoot balls at a fixed delay, independent of whether the player successfully returns them.  `
6. **Win / Lose / End Condition:** `The round ends after all balls are launched. Points are counted based on successful returns.  `
7. **Reset:** `Balls are collected, reloaded into the machine, and the system is ready for the next player. `

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Each player gets a fixed number of serves (balls). `
- `A valid return must bounce on both sides of the table.  `
- `If the player fails to return the ball correctly, no point is awarded.  `
- `Each successful return earns +1 point. `
- `The player with the highest score wins (in case of multiple players).   `
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `[The machine successfully launches all balls loaded into it  ]`
- [ ] `[Balls are launched toward the player consistently  ]`
- [ ] `[The system runs with a timed countdown before starting  ]`
- [ ] `[The launcher operates at high speed with short time interval between shots]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The minimum viable version is a working ball launcher that shoots balls at intervals after a countdown. The system should allow a player to react and engage with the incoming shots.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Adjustable speed of ball launching ]`
- `[Variation in launch angle ] `
- `[Side-to-side movement of the launcher  ]`
- `[Different game modes (easy / medium / fast)  ]`
- `[Score display on OLED screen  ]`
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [yes] Electronics-based
- [yes] Mechanical
- [yes] Sensor-based
- [no] App-connected
- [yes] Motorized
- [yes] Sound-based
- [no] Light-based
- [yes] Screen/UI-based
- [no] Fabricated structure
- [yes] Game logic based
- [no] Installation / tabletop experience
- [ ] Other: `[Write here]`


## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[The system is an interactive ball launching setup controlled by an ESP32 microcontroller. The user loads ping pong balls into the machine, the system then begins with a countdown displayed on an OLED screen, supported by buzzer sounds to create anticipation.

After the countdown, the launcher activates and releases balls at fixed time intervals toward the player. The player interacts physically using a racket, responding to each incoming ball. The system operates independently once triggered, completing a full round based on the number of balls loaded.

The setup consists of a mechanical launcher structure, an ESP32 for control, a servo/motor mechanism for ball release, an OLED display for visual feedback, and a buzzer for sound cues. Together, these elements create a structured, timed interaction between the user and the machine.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| Push Button | Input | Starts the game sequence |
| ESP32 | Processing | Controls timing, countdown, and actuation logic |
| OLED Display | Output | Shows countdown (3, 2, 1, GO) |
| Buzzer | Output | Provides audio cues for countdown and start |
| Servo / Motor | Output | Controls the release or launching of balls |
| Mechanical Launcher | Physical Action | Moves and shoots balls toward the player |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[https://github.com/pramiti07/ODT-2026-Siya_Pramiti/blob/e4703b0f2677695b200d00a381e08191467a8505/images/Concept_Sketch.jpg]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[https://github.com/pramiti07/ODT-2026-Siya_Pramiti/blob/8404ccd82d4602a309c61160d488bdebb3d90c3f/images/Labeled%20Build%20Sketch.jpg]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[~20 cm]` |
| Width | `[~20 cm]` |
| Height | `[~25 cm]` |
| Estimated weight | `[~1–1.5 kg]` |

---
# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [yes] Gears
- [no] Pulleys
- [no] Belt drives
- [no] Linkages
- [no] Hinges
- [yes] Shafts
- [no] Springs
- [no] Bearings
- [yes] Wheels
- [no] Sliders
- [no] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The mechanical system consists of a rotating launcher mechanism that feeds and shoots ping pong balls. Balls are stored in a chamber and guided toward the launching section through rotation. The motion is driven by a motor, which enables continuous feeding and shooting of balls.

The structure is designed to hold multiple balls and release them one at a time, creating a steady flow of shots toward the player.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[The main motion in the system is the rotation of the launcher mechanism, which feeds balls into the shooting path. This motion is driven by a DC motor.

The servo controls a small movement that helps regulate ball release timing. The system is designed to move quickly enough to maintain a rhythm, but not too fast to overwhelm the player.

Potential issues include balls getting stuck, inconsistent feeding, or variation in launch direction due to alignment problems.]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Rhino/Illustrator]` | `[https://github.com/pramiti07/ODT-2026-Siya_Pramiti/blob/cb9184ac112fa12a54e61f11de2e3f12b367996c/cad/Lasercut_file.ai]` | `[Correct dimensions for the project]` |


## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[the mechanism was developed through physical prototyping and iterative testing rather than digital simulation. During testing, adjustments were made to improve ball flow and consistency. The spacing and alignment of the mechanism were modified to prevent jamming. The timing of ball release was also refined to create a more playable experience.

The system evolved from a continuous launcher to a more timed and structured interaction with the addition of the countdown system.]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller for timing and logic]` |
| `[OLED Display (SSD1306)]` | `1 `| `[Displays countdown (3, 2, 1, GO) ]`|
| `[Buzzer]` |`1` | `[Provides audio cues for countdown ]`|
| `[Servo Motor ]`| `1 `|`[ Controls ball release mechanism]` |
| `[Jumper Wires]` | `Multiple` |`[ Electrical connections]` |
| `[Power Supply (USB) ]`| `1 `| `[Powers the system]` |
| `[DC Motor ]`| `3 `|`[ Controls ball release mechanism]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[The ESP32 acts as the central controller. The OLED display is connected using I2C communication (SDA to GPIO 21 and SCL to GPIO 22). The buzzer is connected to a digital output pin (GPIO 25) and is used to provide sound feedback.

The servo motor is connected to a PWM-capable pin (GPIO 12) and powered separately to ensure stable operation. 
All components share a common ground, and power is supplied through a USB connection to the ESP32.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[[(https://github.com/pramiti07/ODT-2026-Siya_Pramiti/blob/74b01e766d523556132741915d1bd843cf8e4067/images/CircuitDiagram.jpg)]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[adapter and esp32]` |
| Voltage required | `[3.3V (logic), 5V (servo). 12V Dc Motors]` |
| Current concerns | `[Servo requires higher current during movement; unstable supply can cause jitter]` |
| Safety concerns | `[Avoid overvoltage to components and ensure proper grounding to prevent erratic behavior ]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython (Thonny )]` | `[Writing and uploading code to ESP32]` |
| `[SSD1306 Library]` | `[Controlling OLED display]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[The system starts by initializing all components, including the OLED display, buzzer, and servo motor. When powered, the system sets the servo to its default position.

Once triggered, the system displays a countdown (3, 2, 1, GO) on the OLED screen, accompanied by buzzer sounds to create anticipation. After the countdown, the servo activates to release the ball.

The system follows a timed sequence where outputs are triggered in order: display updates, buzzer signals, and servo movement. After completing the sequence, the system stops and can be reset for the next round.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[(https://github.com/pramiti07/ODT-2026-Siya_Pramiti/blob/f4df1efb069b93a8996de403667caabed45ad80e/images/flowchart.png)]`

## 10.4 Pseudocode

```text
[START
Initialize OLED, buzzer, servo

Set servo to rest position

Display "3"
Beep
Wait

Display "2"
Beep
Wait

Display "1"
Beep
Wait

Display "GO"
Beep twice
Wait

Move servo to release position
Wait 5 seconds

Return servo to rest position

END]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [x] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Microcontroller]` | `[Easy to program and supports multiple outputs ]` |
| `[OLED Display]` | `[1]` | `[No]` | `[Yes]` | `[200]` | `[SSD1306]` | `[Compact visual feedback]` |
| `[Servo Motor]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[SG90]` | `[Simple control for movement]` |
| `[Buzzer]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[Active buzzer]` | `[Simple sound output]` |
| `[DC Motor]` | `[3]` | `[Yes]` | `[No]` | `[0]` | `[12V]` | `[ control for movement]` |
| `[Ping pong Ball]` | `[6]` | `[no]` | `[yes]` | `[200]` | `[Plastic]` | `[To play the game]` |
| `[Skewers]` | `[12]` | `[no]` | `[yes]` | `[200]` | `[wood]` | `[For outer structure]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Materials were chosen based on ease of fabrication and availability. Cardboard and simple structural materials allowed quick iteration and modification during testing. For final version we used Laser cut MDF and Acrylic sheet for better finish. 

DC motor was chosen for the rotating the wheels as it required higher power for speed, whereas The servo motor was chosen over a DC motor for precise control of movement. The OLED display was selected for compact and clear feedback, while the buzzer provided simple auditory cues without complex setup.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[OLED screen]` | `[To indicate Game starting]` | `[https://robu.in/product/0-96-inch-yellow-yellow-blue-oled-lcd-led-display-module]` | `[9th April]` | `[Ordered]` |
| `[Ping Pong balls]` | `[To play the game]` | `[https://www.zepto.com/pn/decathlon-pongori-table-tennis-balls-size-40/pvid/bbe161b5-8d31-4e81-8371-8b3506caf228?marketplaceType=SUPER_SAVER]` | `[9th April]` | `[Ordered]` |
| `[Wooden Skewers]` | `[Outer structure of the machine]` | `[https://amzn.in/d/0gfdTNE3]` | `[9th April]` | `[Ordered]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[150]` |
| Mechanical parts | `[200]` |
| Fabrication materials | `[200]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[550]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Oled screen can be removed, it adds to the game interaction but is not a necessary element ]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Tasks were divided based on strengths, Pramiti focusing more on coding and electronics, and Siya focusing more on mechanical build and connections. However, both members contributed to ideation, testing, and decision-making.

Progress was reviewed at the end of each working session, and issues were discussed together before deciding on changes. If a task was delayed, responsibilities were adjusted to ensure progress continued.

Documentation was updated regularly alongside the build process.]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Pramiti and Siya]` | `2` | `[4th April]` | `None` | `Done` |
| T2 | `[Complete BOM]` | `[Pramiti and Siya]` | `1` | `[8th April]` | `T1` | `Done` |
| T3 | `[Test electronics]` | `[Siya]` | `2` | `[10th April]` | `T1` | `Done` |
| T4 | `[Build structure]` | `[Pramiti]` | `4` | `[17th April]` | `T1` | `Done` |
| T5 | `[Write control code]` | `[Pramiti]` | `4` | `[15th April]` | `T3` | `Done` |
| T6 | `[Integrate system]` | `[Siya]` | `4` | `[16th April]` | `T4, T5` | `Done` |
| T7 | `[Playtest]` | `[Siya]` | `2` | `[16th April]` | `T6` | `Done` |
| T8 | `[Refine and document]` | `[Pramiti]` | `3` | `[19th April]` | `T7` | `Done` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Pramiti and SIya]` | `[Pramiti and SIya]` |
| Electronics | `[Siya]` | `[Pramiti]` |
| Coding | `[Pramiti]` | `[Siya]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Siya]` | `[Pramiti]` |
| Testing | `[Pramiti]` | `[Siya]` |
| Documentation | `[Pramiti]` | `[Siya]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | Finalize idea, sketches, and concept | Explored multiple ideas like interactive wall, Kaliedoscope, robot car before finalizing the ping pong launcher. Created initial sketches and discussed gameplay and interaction. | Shifted from abstract interactive ideas to a more buildable mechanical + electronics system. | Begin prototyping using simple materials. |
| Week 2 | Build initial mechanism and test electronics | Built an early prototype using cardboard to test the ball feeding and launching concept. Tested basic electronics (servo, buzzer, OLED). Faced issues with power supply and unstable servo behavior. | Decided to first validate the mechanical concept before refining electronics. Simplified interaction logic. | Improve mechanism and fix power stability issues. |
| Week 3 | Integrate system (mechanics + electronics + code) | Transitioned from cardboard prototype to more stable materials. Used the material lab to fabricate parts using laser-cut MDF and acrylic. Integrated OLED, buzzer, and servo into the system. | Improved structural stability and reduced jamming. Introduced countdown system to enhance interaction. | Test full system and refine timing + ball flow. |
| Week 4 | Refine system, test gameplay, complete documentation | Final system assembled using MDF and acrylic components. Spent most time in the material lab refining the build. Conducted testing and small adjustments for smoother operation. Completed documentation. | Focus shifted from adding features to improving reliability and user experience. | Final testing and preparation for demo. |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| Balls getting jammed in mechanism | Mechanical | High | High | Adjust spacing, refine alignment, test multiple iterations | Siya |
| Servo not behaving consistently | Technical | Medium | High | Stabilize power supply, test angles, reduce load | Pramiti |
| Power supply instability | Technical | Medium | High | Use proper 5V supply and common grounding | Pramiti |
| Structure breaking during play | Mechanical | Medium | Medium | Shift from cardboard to MDF and acrylic | Siya |


## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[The biggest uncertainty was achieving consistent and reliable ball launching without jamming or irregular motion. Ensuring smooth mechanical flow was a key challenge.]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| Servo movement | Run repeated cycles | Moves smoothly without jitter |
| OLED display | Run countdown code | Text displays clearly every time |
| Buzzer | Trigger beep during countdown | Sound is audible and synced |
| Ball launching | Test with multiple balls | Balls launch consistently without jamming |


## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | Observe if they can start and play without instructions |
| Is the interaction satisfying? | Ask for feedback after one round |
| Do players want another turn? | Check if they voluntarily replay |
| Is the challenge balanced? | Observe if it feels too easy or too hard |
| Is the response clear and immediate? | Observe timing between countdown and launch |


## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| Week 2 | Servo twitching and not moving | Technical | Changed power supply and wiring | Worked | Stabilize connections |
| Week 2 | OLED not displaying anything | Technical | Rechecked wiring, changed library | Worked | Integrate into main code |
| Week 3 | Balls getting stuck | Mechanical | Adjusted spacing and alignment | Partly worked | Refine structure |
| Week 3 | Inconsistent launching | Mechanical | Modified angle and positioning | Worked | Final testing |


## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| Classmate 1 | Played one full round | Didn’t understand start immediately | Found it fun and fast-paced | Add clearer start cue |
| Classmate 2 | Tried multiple rounds | Timing felt slightly unpredictable | Enjoyed challenge and reaction | Improve consistency |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[The project began with a quick cardboard prototype to test the ball feeding and launching concept. This helped us understand spacing, movement, and flow without investing time in final materials.

After validating the idea, we used the material lab to fabricate the final structure using laser-cut MDF and acrylic. These materials provided better strength, stability, and precision.

The build involved iterative testing, where parts were adjusted to reduce jamming and improve consistency. Electronics were integrated alongside the structure, and wiring was refined for stability.

Most of the time was spent in the material lab focusing on fabrication, assembly, and improving reliability.]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| v1 | Week 2 | Cardboard prototype built | Test basic concept quickly |
| v2 | Week 3 | MDF + acrylic structure | Improve strength and reliability |
| v3 | Week 4 | Integrated electronics + countdown | Enhance interaction |
---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[The initial idea was to create a trainer that will serve from one side what changed was, we decide to make it a interactive ]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[We were effective in our iteration process due to a strong balance within the team—one of us focused on practicality while the other contributed ambitious, forward-thinking ideas. This combination allowed us to develop concepts that were both innovative and feasible. As a result, we were able to continuously refine our approach and resolve challenges throughout the process.

We worked consistently and maintained a clear vision, which helped us stay aligned and productive. The only point at which our progress slowed was during the material approval stage, which temporarily delayed execution.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Designing this game showed me that play comes from giving players freedom within structure, where choices feel meaningful rather than forced. Delight emerged through small surprises and responsive feedback, making even mistakes enjoyable. I learned that clarity is crucial—players rely on quick, intuitive signifiers like speed and timing to make decisions.

The physical nature of the game highlighted how movement and reaction are part of the experience, not just thinking. Players understand the system through interaction and patterns, not instructions. 
Throughout the process we realised how consistancy playes a role and sometimes all we need to do is start insted of thinking. action gives clarity to our thoughts.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[if we had more time we would have made a angle changing mechanism that adds to the unpridictablity and the mechanism becomes we would also want to incourporate a mechanism which would allow the balls to shoot one at a time rather than a continious series of one after the other]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [Yes] Team details are complete
- [Yes] Project description is complete
- [Yes] Inspiration sources are included
- [Yes] Player journey is written
- [Yes] Sketches are added
- [Yes] BOM is complete
- [Yes] Purchase list is complete
- [Yes] Budget summary is complete
- [Yes] Mechanical planning is documented if applicable
- [Yes] App planning is documented if applicable
- [Yes] Code flowchart is added
- [Yes] Task breakdown is complete
- [Yes] Weekly logs are updated
- [Yes] Risk register is complete
- [Yes] Testing log is updated
- [Yes] Playtesting notes are included
- [Yes] Build photos are included
- [Yes] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
