# AQ3D API Wrapper for Python

---
This is a package for Python which aims to
have complete practical coverage of the AQ3D API.
Developed with OOP principles in mind for easy extensibility.

_This package is under development which means it's not in a usable state.
Technically you can use it, but without future implementation of async processes,
it's not going to be ideal._

### API Coverage

- **Servers**
  - GET server statistics such as player counts.
  - Capture timestamped server snapshots for logging or charting graphs.

- **Items (Supports Ranges)**
  - Create a container of Item objects and view their data.
  - Filter items by multiple types:
    - Item Type
    - Item Equip Type
    - Item Attribute Key
    - Item Rarity

- **Maps (Supports Ranges)**
  - Create a container of Map objects and view their data.
  - Filter maps by map attribute keys.

- **Dialogs (Supports Ranges)**
  - Create a container of Dialog objects and view their data.
  - View individual frames and actors of each Dialog.


Save data CSV and JSON files with a single method either
`to_csv(Path)` or `to_json_file(Path)` on the container objects.

---

### TODOs

- Refactor all HTTP requests to use async for non-blocking operations.
- API for more types
  - **NPCs**
  - **Dialog Image Generator**
  - **Class Skills**
  - **Spells & Skills**
  - **Loot Box Items**
  - **Character Info (Name, Level, Class, Badges)** 
  - **Daily Map**
- Filter Items by category.
- Create a wiki on here to explain how to use the package.

---

### How To Use

- **Coming Soon**

---

_This project was intended for learning purposes, and for
a way to easily interface with AQ3D's API endpoints. Please use fairly, 
and within the terms and conditions by Artix Entertainment themselves._