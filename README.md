# SCARA Robot Communication Library

<img align="right" src="https://raw.githubusercontent.com/vroncevic/scaracom/dev/docs/scaracom_logo.png" width="25%">

**scaracom** is a dedicated Python communication library providing pure Layer 0 Hardware Transport, Layer 1 Protocol Bridge, and Layer 2 Flow Control components for the SCARA robotic manipulator ecosystem (`scaraemu`, `scarajectory`, and `scaralang`).

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
- [📁 Framework structure](#-framework-structure)
  - [🏗 Architecture & SOLID Principles](#-architecture--solid-principles)
    - [SOLID Principles Compliance](#solid-principles-compliance)
    - [Automated Quality Gates (`run_quality_gates.sh`)](#automated-quality-gates-run_quality_gatessh)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
    - [Port Scanning & Hardware Discovery](#port-scanning--hardware-discovery)
    - [Serial Transport Setup](#serial-transport-setup)
    - [Protocol Bridge & Listener Dispatch](#protocol-bridge--listener-dispatch)
    - [Flow Control & Frame Routing](#flow-control--frame-routing)
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

**scaracom** is extremely lightweight and requires only:
* `pyserial` (in addition to Python standard library built-ins)

### 📁 Framework structure

**scaracom** is based on OOP and Clean Architecture.

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    scaracom/
         ├── bridge/
         │   ├── coordinator/
         │   │   ├── coordinator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── icoordinator.py
         │   │   └── __init__.py
         │   ├── dependencies.py
         │   ├── factory.py
         │   ├── __init__.py
         │   ├── listener/
         │   │   ├── factory.py
         │   │   ├── holder.py
         │   │   ├── iholder.py
         │   │   ├── __init__.py
         │   │   └── itransport_listener.py
         │   ├── provides.py
         │   ├── receiver/
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── ireceiver.py
         │   │   └── receiver.py
         │   └── transceiver/
         │       ├── dependencies.py
         │       ├── factory.py
         │       ├── ibyte_sender.py
         │       ├── ichannel.py
         │       ├── __init__.py
         │       └── transceiver.py
         ├── flow/
         │   ├── barrier/
         │   │   ├── barrier.py
         │   │   ├── factory.py
         │   │   ├── ibarrier.py
         │   │   ├── __init__.py
         │   │   └── provides.py
         │   ├── __init__.py
         │   ├── pacing/
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── iwindow.py
         │   │   ├── provides.py
         │   │   └── window.py
         │   ├── queue/
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── iqueue.py
         │   │   ├── provides.py
         │   │   └── queue.py
         │   ├── router/
         │   │   ├── factory.py
         │   │   ├── iframe.py
         │   │   ├── ihandler.py
         │   │   ├── __init__.py
         │   │   ├── irouter.py
         │   │   ├── provides.py
         │   │   └── router.py
         │   └── sequence/
         │       ├── coordinator.py
         │       ├── factory.py
         │       ├── icoordinator.py
         │       ├── __init__.py
         │       └── provides.py
         ├── __init__.py
         ├── py.typed
         └── transport/
             ├── driver/
             │   ├── factory.py
             │   ├── idriver.py
             │   ├── __init__.py
             │   └── pyserial_driver.py
             ├── factory.py
             ├── __init__.py
             ├── itransport.py
             ├── preference/
             │   ├── __init__.py
             │   ├── irepository.py
             │   └── preference.py
             ├── scanner/
             │   ├── factory.py
             │   ├── __init__.py
             │   ├── iport_scanner.py
             │   └── port_scanner.py
             └── transport.py

     16 directories, 71 files
```
</details>

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

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `scaracom/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/coordinator/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/coordinator/coordinator.py` | 56 | 0 | 100%|
| `scaracom/bridge/coordinator/dependencies.py` | 20 | 0 | 100%|
| `scaracom/bridge/coordinator/factory.py` | 20 | 0 | 100%|
| `scaracom/bridge/coordinator/icoordinator.py` | 17 | 0 | 100%|
| `scaracom/bridge/dependencies.py` | 16 | 0 | 100%|
| `scaracom/bridge/factory.py` | 36 | 0 | 100%|
| `scaracom/bridge/listener/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/listener/factory.py` | 20 | 0 | 100%|
| `scaracom/bridge/listener/holder.py` | 29 | 0 | 100%|
| `scaracom/bridge/listener/iholder.py` | 16 | 0 | 100%|
| `scaracom/bridge/listener/itransport_listener.py` | 15 | 0 | 100%|
| `scaracom/bridge/provides.py` | 20 | 0 | 100%|
| `scaracom/bridge/receiver/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/receiver/dependencies.py` | 18 | 0 | 100%|
| `scaracom/bridge/receiver/factory.py` | 20 | 0 | 100%|
| `scaracom/bridge/receiver/ireceiver.py` | 15 | 0 | 100%|
| `scaracom/bridge/receiver/receiver.py` | 48 | 0 | 100%|
| `scaracom/bridge/transceiver/__init__.py` | 9 | 0 | 100%|
| `scaracom/bridge/transceiver/dependencies.py` | 16 | 0 | 100%|
| `scaracom/bridge/transceiver/factory.py` | 20 | 0 | 100%|
| `scaracom/bridge/transceiver/ibyte_sender.py` | 14 | 0 | 100%|
| `scaracom/bridge/transceiver/ichannel.py` | 15 | 0 | 100%|
| `scaracom/bridge/transceiver/transceiver.py` | 32 | 0 | 100%|
| `scaracom/flow/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/barrier/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/barrier/barrier.py` | 25 | 0 | 100%|
| `scaracom/flow/barrier/factory.py` | 18 | 0 | 100%|
| `scaracom/flow/barrier/ibarrier.py` | 17 | 0 | 100%|
| `scaracom/flow/barrier/provides.py` | 14 | 0 | 100%|
| `scaracom/flow/pacing/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/pacing/dependencies.py` | 13 | 0 | 100%|
| `scaracom/flow/pacing/factory.py` | 20 | 0 | 100%|
| `scaracom/flow/pacing/iwindow.py` | 16 | 0 | 100%|
| `scaracom/flow/pacing/provides.py` | 14 | 0 | 100%|
| `scaracom/flow/pacing/window.py` | 39 | 0 | 100%|
| `scaracom/flow/queue/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/queue/factory.py` | 18 | 0 | 100%|
| `scaracom/flow/queue/iqueue.py` | 17 | 0 | 100%|
| `scaracom/flow/queue/provides.py` | 14 | 0 | 100%|
| `scaracom/flow/queue/queue.py` | 36 | 0 | 100%|
| `scaracom/flow/router/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/router/factory.py` | 18 | 0 | 100%|
| `scaracom/flow/router/iframe.py` | 20 | 0 | 100%|
| `scaracom/flow/router/ihandler.py` | 15 | 0 | 100%|
| `scaracom/flow/router/irouter.py` | 18 | 0 | 100%|
| `scaracom/flow/router/provides.py` | 14 | 0 | 100%|
| `scaracom/flow/router/router.py` | 45 | 0 | 100%|
| `scaracom/flow/sequence/__init__.py` | 9 | 0 | 100%|
| `scaracom/flow/sequence/coordinator.py` | 29 | 0 | 100%|
| `scaracom/flow/sequence/factory.py` | 18 | 0 | 100%|
| `scaracom/flow/sequence/icoordinator.py` | 16 | 0 | 100%|
| `scaracom/flow/sequence/provides.py` | 14 | 0 | 100%|
| `scaracom/transport/__init__.py` | 9 | 0 | 100%|
| `scaracom/transport/driver/__init__.py` | 9 | 0 | 100%|
| `scaracom/transport/driver/factory.py` | 18 | 0 | 100%|
| `scaracom/transport/driver/idriver.py` | 17 | 0 | 100%|
| `scaracom/transport/driver/pyserial_driver.py` | 52 | 0 | 100%|
| `scaracom/transport/factory.py` | 21 | 0 | 100%|
| `scaracom/transport/itransport.py` | 17 | 0 | 100%|
| `scaracom/transport/preference/__init__.py` | 9 | 0 | 100%|
| `scaracom/transport/preference/irepository.py` | 17 | 0 | 100%|
| `scaracom/transport/preference/preference.py` | 14 | 0 | 100%|
| `scaracom/transport/scanner/__init__.py` | 9 | 0 | 100%|
| `scaracom/transport/scanner/factory.py` | 18 | 0 | 100%|
| `scaracom/transport/scanner/iport_scanner.py` | 14 | 0 | 100%|
| `scaracom/transport/scanner/port_scanner.py` | 39 | 0 | 100%|
| `scaracom/transport/transport.py` | 37 | 0 | 100%|
| **Total** | 1339 | 0 | 100% |

</details>

### 🛠 Usage

##### Port Scanning & Hardware Discovery

```python
from scaracom.transport.scanner.factory import PortScannerFactory

# Discover available hardware serial ports with descriptions
scanner = PortScannerFactory.create()
ports = scanner.scan_ports()
print("Detected serial ports:", ports)
```

##### Serial Transport Setup

```python
from scaracom.transport.factory import SerialTransportFactory

# Initialize physical serial connection (Layer 0)
transport = SerialTransportFactory.create(port="/dev/ttyUSB0", baudrate=115200)

if transport.connect():
    transport.write_bytes(b"\x01\x00\x00\x00")
    response = transport.read_bytes(size=64)
    transport.disconnect()
```

##### Protocol Bridge & Listener Dispatch

```python
from scaracom.bridge.factory import BridgeFactory
from scaracom.bridge.dependencies import BridgeDependencies
from scaracom.transport.factory import SerialTransportFactory

# Initialize transport and bridge (Layer 1)
transport = SerialTransportFactory.create(port="/dev/ttyUSB0", baudrate=115200)
bridge_provides = BridgeFactory.create(BridgeDependencies(transport=transport))

# Connect coordinator and dispatch byte streams
bridge_provides.coordinator.connect()
bridge_provides.transceiver.send_bytes(b"\x01\x02\x03\x04")
bridge_provides.coordinator.disconnect()
```

##### Flow Control & Frame Routing

```python
from scaracom.flow.router.factory import FrameRouterFactory
from scaracom.flow.router.iframe import IRoutedFrame
from scaracom.flow.barrier.factory import FlowBarrierFactory

# Demultiplex incoming frames via structural protocol (Layer 2)
router = FrameRouterFactory.create()
barrier = FlowBarrierFactory.create()

# Arm flow barrier for synchronized command execution
barrier.arm()
barrier.wait_until_unblocked(timeout=1.0)
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/scaracom/badge/?version=latest)](https://scaracom.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [scaracom.readthedocs.io](https://scaracom.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2026 by [vroncevic.github.io/scaracom](https://vroncevic.github.io/scaracom)

**scaracom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Special thanks to **Google** and the Google developer ecosystem for their tremendous support and innovative tools from the Google bundle that empowered the development and realization of this project. *Google, you make this world a better place!* 🌍✨

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/scaracom/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)