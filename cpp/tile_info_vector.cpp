#include "tile_info_vector.hpp"
#include <pybind11/eval.h>

namespace TI4 {

TileInfoVector::TileInfoVector()
    : _tiles{{"Mecatol Rex", 1, 6, false, false, false},
             {"Bereg, Lirta IV", 5, 4, false, false, false},
             {"Abyz, Fria", 5, 0, false, false, false},
             {"New Albion, Starpoint", 4, 2, false, false, false},
             {"Arnor, Lor", 3, 3, false, false, false},
             {"Mellon, Zohbat", 3, 3, false, false, false},
             {"Corneeq, Resculon", 3, 2, false, false, false},
             {"Lodor", 3, 1, true, false, false},
             {"Lazar, Sakulag", 3, 1, false, false, false},
             {"Centauri, Gral", 2, 4, false, false, false},
             {"Tequ'ran, Torkan", 2, 3, false, false, false},
             {"Vefut II", 2, 2, false, false, false},
             {"Saudor", 2, 2, false, false, false},
             {"Quann", 2, 1, true, false, false},
             {"Arinam, Meer", 1, 6, false, false, false},
             {"Qucen'n, Rarron", 1, 5, false, false, false},
             {"Mehar Xull", 1, 3, false, false, false},
             {"Dal Bootha, Xxehan", 1, 3, false, false, false},
             {"Wellon", 1, 2, false, false, false},
             {"Tar'mann", 1, 1, false, false, false},
             {"Thibah", 1, 1, false, false, false},
             {"A Wormhole", 0, 0, true, false, false},
             {"B Wormhole", 0, 0, true, false, false},
             {"Asteroid Field", 0, 0, false, true, false},
             {"Asteroid Field", 0, 0, false, true, false},
             {"Supernova", 0, 0, false, true, false},
             {"Nebula", 0, 0, false, true, false},
             {"Gravity Rift", 0, 0, false, true, false},
             {"Blank", 0, 0, false, false, true},
             {"Blank", 0, 0, false, false, true},
             {"Blank", 0, 0, false, false, true},
             {"Blank", 0, 0, false, false, true},
             {"Blank", 0, 0, false, false, true}} {
}

std::size_t TileInfoVector::size() const {
  return _tiles.size();
}

const TileInfo &TileInfoVector::operator[](std::size_t idx) const {
  return _tiles[idx];
}

} // namespace TI4
