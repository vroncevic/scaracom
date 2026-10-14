# SCARA Robot Communication Library

**scaracom** is a dedicated Python communication library providing pure Layer 0 Hardware Transport and Layer 1 Protocol Bridge components for the SCARA robotic manipulator ecosystem (`scaraemu`, `scarajectory`, and `scaralang`).

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![scaracom python checker](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python_checker.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python_checker.yml) [![scaracom python package](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_package_checker.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_package.yml) [![scaracom interface checker](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_interface_checker.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_interface_checker.yml) [![scaracom isp checker](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_isp_checker.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_isp_checker.yml) [![scaracom srp checker](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_srp_checker.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_srp_checker.yml) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/scaracom.svg)](https://github.com/vroncevic/scaracom/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/scaracom.svg)](https://github.com/vroncevic/scaracom/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [🏗 Architecture & SOLID Principles](#-architecture--solid-principles)
    - [SOLID Principles Compliance](#solid-principles-compliance)
    - [Automated Quality Gates (`run_quality_gates.sh`)](#automated-quality-gates-run_quality_gatessh)
    - [SCARA Ecosystem Role](#-scara-ecosystem-role)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

[![scaracom python3 build](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python3_build.yml/badge.svg)](https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python3_build.yml)

##### Install using pip

```bash
# python3
pip3 install scaracom
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/scaracom/releases/)** download and extract release archive.

To install **scaracom** type the following

```bash
tar xvzf scaracom-x.y.z.tar.gz
cd scaracom-x.y.z/
# python3
python3 -m pip install .
```

##### Install using py setup

```bash
python3 setup.py install --record files.txt
```

### 📦 Dependencies

**scaracom** requires the following external packages:
* `ats-utilities`
* `pyserial`

### 📁 Tool structure

```text
scaracom/
├── infrastructure/
│   ├── transport/       # Pure Layer 0 Hardware Transport
│   │   ├── connection/  # Serial port connection abstraction
│   │   ├── holder/      # Active session thread-safe holder
│   │   ├── scanner/     # Hardware serial port enumeration
│   │   ├── session/     # Physical serial stream session & Null Object
│   │   ├── stream/      # Raw byte stream read/write operations
│   │   ├── itransport.py
│   │   ├── transport.py
│   │   └── factory.py
│   └── connection/      # Layer 1 Protocol Bridge & Workers
│       ├── coordinator/ # Reader thread & transport event lifecycle
│       ├── listener/    # Protocol-agnostic event sinks (ASCII, Binary, Null)
│       ├── transceiver/ # Direct raw frame / byte transmission
│       ├── worker/      # Background polling worker thread
│       ├── dependencies.py
│       ├── factory.py
│       └── provides.py
```

#### 🏗 Architecture & SOLID Principles

##### SOLID Principles Compliance
1. **Single Responsibility Principle (SRP):** Subsystems and components contain strictly 2 to 4 cohesive public methods.
2. **Open/Closed Principle (OCP):** Protocol extensions hook into typed event delegates without modifying core transport loops.
3. **Liskov Substitution Principle (LSP):** Pure structural subtyping via `typing.Protocol` with zero multi-inheritance or `@override` decorators.
4. **Interface Segregation Principle (ISP):** Clients depend strictly on narrow role protocols (`ITransport`, `IConnection`, `IStream`, `IConnectionCoordinator`).
5. **Dependency Inversion Principle (DIP):** Collaborators are injected as structural protocols with frozen dataclass bundles (`dependencies.py` ➔ `factory.py` ➔ `provides.py`).

##### Automated Quality Gates (`run_quality_gates.sh`)
* `interfaces_checker`: Verifies structural protocol adherence.
* `isp_checker`: Enforces method count limits per role interface.
* `limits_checker`: Enforces max file lengths and line character boundaries.
* `srp_checker`: Enforces Single Responsibility constraints.

### 👥 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

### 📄 Copyright and licence

Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>

Licensed under the **[GNU General Public License v3.0](LICENSE)**.
