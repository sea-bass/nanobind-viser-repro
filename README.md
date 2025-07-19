# nanobind-viser-repro

NOTE: You may want to do this all in a virtual environment.

To reproduce this example, you should first [install nanobind](https://nanobind.readthedocs.io/en/latest/installing.html).
Easiest way is:

```bash
pip install nanobind
```

Then, build this extension

```bash
pip install --break-system-packages -ve .
```

Finally, run the example!

```bash
python3 repro_example.py
```

You should then see an error like this:

```
nanobind: leaked 1 instances!
nanobind: leaked 1 types!
 - leaked type "nanobind_viser_repro.nanobind_viser_repro.DummyClass"
nanobind: leaked 1 functions!
 - leaked function "__init__"
nanobind: this is likely caused by a reference counting issue in the binding code.
```
