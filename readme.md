# KiCad Assets

A curated collection of custom **KiCad assets** to enhance your PCB design experience. Includes symbols, footprints, and 3D models, all ready to integrate into your projects.


## KiCad Library Convention (KLC)

This repository adheres to the **KiCad Library Conventions (KLC)** to ensure quality, consistency, and ease of contribution. Understanding KLC will help you submit or update library files effectively. 

- **Overview**: [KiCad Library Conventions (KLC)](https://klc.kicad.org/)
- **Helper Tools**: [KiCad Library Utils - GitLab](https://gitlab.com/kicad/libraries/kicad-library-utils)

While KLC provides guidelines, exceptions are allowed at the discretion of the library maintainers.


## Project Structure

```bash
📁 kicad/
├── 📦 3dmodels/          # 3D models in .step format
│   └── 🗂️ *.3dshapes/
│       └── 📂 *.step
│
├── 📦 symbols/           # Component symbols
│   └── 📂 *.kicad_sym
│
├── 📦 footprints/        # Footprints for PCB layouts
│   └── 🗂️ *.pretty/
│       └── 📂 *.kicad_mod
│
└── 🛠️ scripts/           # Utility scripts for automation
    ├── 📂 *.py
    └── 📂 *.csv
```

## 🚀 Getting Started

1. Add User Library Path  
   Under `Preferences → Configure Paths`, add the following:  
   - Name: `KICAD_USER_LIB`  
   - Path: `<path-to-repo>\kicad-lib`

2. Set Up Symbol and Footprint Libraries  
   - Place the `sym-lib-table` and `fp-lib-table` files in your project directory.  
   - These files link your project to the custom library assets.


## License

This repository is licensed under [Insert License Name Here]. Refer to the [LICENSE](license) file for more details.

## 💡 Contributing

We welcome contributions! Follow the KLC guidelines and open an issue or pull request for any updates or suggestions.  
For any questions or suggestions, feel free to open an issue or contact me directly. Happy designing! ✨