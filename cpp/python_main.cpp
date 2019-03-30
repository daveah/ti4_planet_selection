#include "deck_generator.hpp"
#include "num_players.hpp"
#include "style.hpp"
#include "validation_error.hpp"
#include <iostream>
#include <pybind11/pybind11.h>
#include <string>

// TODO:

// Create wrappers around TileInfoVector, Config and DeckGenerator classes, call
// in from there
// Note, we also need to factor out the boost::program_options exceptions from
// things like num_players and style
// Finally, let's build the pure C++ version anyway - we just need to fiddle
// with CMakeLists.txt

namespace py = pybind11;

void ti4_planet_selection(int num_players_, std::string style_) {
  using namespace TI4;
  try {
    num_players np(num_players_);
    style st(style_);
    DeckGenerator df(np, st);
  } catch (ValidationError &ee) {
    std::cout << "Error: " << ee.what() << std::endl;
  }
}

PYBIND11_MODULE(ti4_planet_selection, m) {
  m.doc() = "TI4 Planet Selection"; // optional module docstring

  using namespace TI4;
  py::class_<num_players>(m, "NumPlayers")
      .def(py::init<const std ::string &>());
  py::class_<style>(m, "Style").def(py::init<const std::string &>());
  py::class_<DeckGenerator>(m, "DeckGenerator")
      .def(py::init<const num_players &, const style &>());
  m.def("ti4_planet_selection", &ti4_planet_selection, "Compute planet stacks");
}
