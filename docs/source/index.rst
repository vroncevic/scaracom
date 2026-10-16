.. image:: _static/scaracom_logo.png
   :align: right
   :width: 25%

SCARA Robot Python Communication Library
-----------------------------------------

**scaracom** is a dedicated Python communication library providing pure Layer 0 Hardware Transport, Layer 1 Protocol Bridge, and Layer 2 Flow Control components for the SCARA robotic manipulator ecosystem (`scaraemu`, `scarajectory`, and `scaralang`).

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|scaracom python checker| |scaracom python package| |scaracom interface checker| |scaracom isp checker| |scaracom srp checker| |gplv3 license| |apache license| |python version| |github issues| |documentation status| |github contributors|

.. |scaracom python checker| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python_checker.yml

.. |scaracom python package| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_package.yml

.. |scaracom interface checker| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_interface_checker.yml

.. |scaracom isp checker| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_isp_checker.yml

.. |scaracom srp checker| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_srp_checker.yml

.. |gplv3 license| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |apache license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

.. |python version| image:: https://img.shields.io/badge/python-3.12+-blue.svg
   :target: https://www.python.org/downloads/

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/scaracom.svg
   :target: https://github.com/vroncevic/scaracom/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/scaracom.svg
   :target: https://github.com/vroncevic/scaracom/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/scaracom/badge/?version=latest
   :target: https://scaracom.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
---------------

|scaracom python3 build|

.. |scaracom python3 build| image:: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/scaracom/actions/workflows/scaracom_python3_build.yml

Install using pip
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # python3
    pip3 install scaracom

Install using build
^^^^^^^^^^^^^^^^^^^^

Navigate to release `page <https://github.com/vroncevic/scaracom/releases/>`_ download and extract release archive.

To install **scaracom** type the following

.. code-block:: bash

    tar xvzf scaracom-x.y.z.tar.gz
    cd scaracom-x.y.z/
    # python3
    python3 -m pip install .

Install using py setup
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    python3 setup.py install --record files.txt

📦 Dependencies
---------------

**scaracom** is extremely lightweight and requires only:

* `pyserial <https://pypi.org/project/pyserial/>`_ (in addition to Python standard library built-ins)

📁 Framework structure
----------------------

**scaracom** is based on OOP and Clean Architecture.

Framework structure

.. code-block:: bash

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
         │       ├── icommand_sender.py
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

     16 directories, 72 files

🏗 Architecture & SOLID Principles
----------------------------------

SOLID Principles Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Single Responsibility Principle (SRP):** Subsystems and components contain strictly 2 to 4 cohesive public methods.
2. **Open/Closed Principle (OCP):** Protocol extensions hook into typed event delegates without modifying core transport loops.
3. **Liskov Substitution Principle (LSP):** Pure structural subtyping via ``typing.Protocol`` with zero multi-inheritance or ``@override`` decorators.
4. **Interface Segregation Principle (ISP):** Clients depend strictly on narrow role protocols (``ITransport``, ``ISerialDriver``, ``IPortScanner``, ``IConnectionCoordinator``).
5. **Dependency Inversion Principle (DIP):** Collaborators are injected as structural protocols with frozen dataclass bundles (``dependencies.py`` ➔ ``factory.py`` ➔ ``provides.py``).

Automated Quality Gates (``run_quality_gates.sh``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``interfaces_checker``: Verifies structural protocol adherence.
* ``isp_checker``: Enforces method count limits per role interface.
* ``limits_checker``: Enforces max file lengths and line character boundaries.
* ``srp_checker``: Enforces Single Responsibility constraints.

📊 Code coverage
----------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
-------

Port Scanning & Hardware Discovery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scaracom.transport.scanner.factory import PortScannerFactory

    # Discover available hardware serial ports with descriptions
    scanner = PortScannerFactory.create()
    ports = scanner.scan_ports()
    print("Detected serial ports:", ports)

Serial Transport Setup
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scaracom.transport.factory import SerialTransportFactory

    # Initialize physical serial connection (Layer 0)
    transport = SerialTransportFactory.create(port="/dev/ttyUSB0", baudrate=115200)

    if transport.connect():
        transport.write_bytes(b"\x01\x00\x00\x00")
        response = transport.read_bytes(size=64)
        transport.disconnect()

Protocol Bridge & Listener Dispatch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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

Flow Control & Frame Routing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scaracom.flow.router.factory import FrameRouterFactory
    from scaracom.flow.router.iframe import IRoutedFrame
    from scaracom.flow.barrier.factory import FlowBarrierFactory

    # Demultiplex incoming frames via structural protocol (Layer 2)
    router = FrameRouterFactory.create()
    barrier = FlowBarrierFactory.create()

    # Arm flow barrier for synchronized command execution
    barrier.arm()
    barrier.wait_until_unblocked(timeout=1.0)

📚 Docs
-------

More documentation and info at

* `scaracom.readthedocs.io <https://scaracom.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
---------------

Please read `CONTRIBUTING.md <https://github.com/vroncevic/scaracom/blob/dev/CONTRIBUTING.md>`_ and `CODE_OF_CONDUCT.md <https://github.com/vroncevic/scaracom/blob/dev/CODE_OF_CONDUCT.md>`_ for details on our code of conduct, and the process for submitting pull requests to us.

📄 Copyright and licence
-------------------------

|gplv3 license| |apache license|

Copyright (C) 2026 by `vroncevic.github.io/scaracom <https://vroncevic.github.io/scaracom>`_

**scaracom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Special thanks to **Google** and the Google developer ecosystem for their tremendous support and innovative tools from the Google bundle that empowered the development and realization of this project. *Google, you make this world a better place!* 🌍✨

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/scaracom/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
