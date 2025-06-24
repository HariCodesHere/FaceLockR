# FaceLockR User Guide 🛠️

## Table of Contents
1. [Hardware Setup](#-hardware-setup)
2. [Software Installation](#-software-installation)
3. [Face Enrollment](#-face-enrollment)
4. [System Operation](#-system-operation)
5. [Troubleshooting](#-troubleshooting)
6. [Safety Precautions](#⚠️-safety-precautions)

---

## 🔌 Hardware Setup

### Components Needed
- Arduino Uno + USB cable
- 5V Relay Module
- 12V Solenoid Lock
- Webcam (Logitech C270 recommended)
- 12V Power Supply
- Jumper Wires

### Wiring Diagram
~~~
Arduino       Relay       Lock       Power Supply
~~~~~
5V     →     VCC
GND    →     GND
D8     →     IN1
                   COM → Lock Positive
                   NO  → 12V+
GND    → Lock Negative
~~~

> 📌 Note: Refer to [circuit_diagram.pdf](docs/circuit_diagram.pdf) for visual reference

---

## 💾 Software Installation

### Python Setup
1. Install Python 3.10+
   ~~~bash
   sudo apt install python3.10
   ~~~
2. Install required packages:
   ~~~bash
   pip install opencv-python numpy pyserial
   ~~~

### Arduino IDE
1. Download from [arduino.cc](https://www.arduino.cc/en/software)
2. Upload the sketch:
   ~~~arduino
   void setup() {
     pinMode(8, OUTPUT);
     Serial.begin(9600);
   }

   void loop() {
     if (Serial.available()) {
       char cmd = Serial.read();
       if (cmd == 'U') digitalWrite(8, HIGH); // Unlock
       if (cmd == 'L') digitalWrite(8, LOW);  // Lock
     }
   }
   ~~~

---

## 📸 Face Enrollment

1. Run the enrollment script:
   ~~~bash
   python software/face_enrollment.py
   ~~~
2. Follow on-screen instructions:
   - Enter user ID (e.g., 1 for first user)
   - Look straight at camera
   - Move head slightly for 5 captures
3. Database saves to `software/faces.yml`

> 💡 Tip: For best results:
> - Use consistent lighting
> - Remove glasses/hats initially
> - Capture different angles

---

## 🖥️ System Operation

### Starting the System
~~~bash
python software/face_detection.py
~~~

### Normal Workflow
1. Green box appears around recognized faces
2. System beeps and unlocks for authorized users
3. Red box appears for unknown faces
4. Auto-relocks after 5 seconds

### Admin Commands
| Key | Action |
|-----|--------|
| `q` | Quit system |
| `a` | Add new face (admin mode) |
| `d` | Delete face (admin mode) |

---

## 🐞 Troubleshooting

### Common Issues
1. **Camera not detected**:
   - Check USB connection
   - Verify camera works with other apps

2. **Arduino not responding**:
   - Check COM port in `serial_comm.py`
   - Re-upload Arduino sketch

3. **False recognitions**:
   - Retrain with better samples
   - Adjust threshold in `face_detection.py`

---

## ⚠️ Safety Precautions
1. Always disconnect power when wiring
2. Use insulated tools
3. Keep liquids away from components
4. Secure loose wires with tape
5. Don't touch relay contacts when powered

---

## 📞 Support
For additional help:
- GitHub: [Issues Page](https://github.com/HariCodesHere/FaceLockR/issues)

