# KiCad Assets

Collection of custom KiCad assets to expand your design capabilities. Includes symbols, footprints, and 3D models ready for your projects.

## KiCad Library Convention (KLC)

This project follows the KiCad Library Conventions (KLC) to ensure consistency and facilitate contributions. Users wishing to submit or update library files should be familiar with these guidelines.

The KLC are a set of guidelines, rather than rules. Electronic component libraries are diverse and complex, and exceptions can be made at the discretion of the library team.

* Overview: [KLC - Library Conventions](https://klc.kicad.org/)
* KLC Helper Scripts: [KiCad Library Utils - GitLab](https://gitlab.com/kicad/libraries/kicad-library-utils)

## Project Structure

```bash
📁 kicad
├── 🗃️ 3dmodels
│   └── 🗂️ *.3dshapes
│       └── 📂 *.step
│
├── 🗃️ symbols
│   └── 🗂️ *.kicad_sym
│
└── 🗃️ footprints
    └── 🗂️ *.pretty
        └── 📂 *.kicad_mod
```

## Asset Database

```bash
📁 kicad
├─── 🗂️ Comms
│   ├─── 📂 LoRA_E5-mini       # Freq: 868/915MHz, 	3.7-5V (logic)
│   └─── 📂 TCA9548A           # 1-to-8 I2C mux, up to 400kHz
│
├─── 🗂️ Connectors
│   ├─── 📂 XT30PW-M           # 60V, 30A (cont.)
│   └─── 📂 XT60PW-M           # 60V, 60A (cont.)
│
├─── 🗂️ MCU
│   ├─── 📂 Arduino_Giga-R1    # STM32 dual-core, Digital: 75, PWM: 12, Analog: 12
│   └─── 📂 Raspberry_Pi-5     # BCM2712 quad-core, 8GB RAM, GPIO: 40
│
├─── 🗂️ Motors
│   ├─── 📂 DC_Motor
│   ├─── 📂 Orange_BLDC_Motor
│   ├─── 📂 Servo_Motor
│   ├─── 📂 Stepper_bipolar
│   └─── 📂 Stepper_unipolar
│
├─── 🗂️ Motor_Driver
│   ├─── 📂 DM542_Stepper      # Bipolar, 20-50V, 1-4.2A, 400-25600 Pulse/rev
│   ├─── 📂 SmartElex_15S_DC   # 6-30V, 15A (cont.), 30A (peak), PWM: 32kHz, 3.3/5V (logic)
│   ├─── 📂 SC08A_Servo        # 8-Ch, 4.8-9V, 8000 steps, UART 9600, Pulse 0.5-2.5ms
│   ├─── 📂 TB6612_DC          # 4.5-15V, 1.2A/Ch (3.2A peak), 2.7-5.5V (logic), PWM 100kHz
│   └─── 📂 TMC2209_Stepper    # Up to 256 microsteps, 4.75-29V, 2.8A peak, UART/SPI
│
└─── 🗂️ Sensors
    ├─── 📂 AS5600_Encoder       # 12-bit magnetic, I2C, analog/PWM out, 3.3/5V (logic)
    ├─── 📂 BMX160_IMU           # 16-bit, 3.3/5V, Acc: ±2-16g, Gyro: ±125-2000°/s, Mag: ±1150/2500uT(z)
    ├─── 📂 INA260_Power_Monitor # 0-36V, 15A±1.5mA cont., 16-bit I2C out, 2.7-5.5V (logic)
    ├─── 📂 Maker_Line_Sensor_05 # 5-Ch IR, 3.3/5V, 200Hz, Width:13-30mm, Height: 4-40mm
    └─── 📂 OE-28_Encoder        # 2-Ch Hall effect, 3-7 PPR, 4.5-24V, 20mA max

```

## License

This repository is licensed under [insert license here]. Please see the [LICENSE](license) for more details.

For any questions or suggestions, feel free to open an issue or contact us directly. Happy designing! ✨
