#include <iostream>
#include <nanobind/nanobind.h>


/// Source code to bind
class DummyClass {
  public:
    DummyClass() {
        std::cout << "Instantiated a dummy class!" << std::endl;
    }
};

/// Nanobind module
NB_MODULE(nanobind_viser_repro, m) {

  nanobind::class_<DummyClass>(m, "DummyClass")
      .def(nanobind::init<>());

}