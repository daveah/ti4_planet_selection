#include "tile_info_vector.hpp"
#include <pybind11/eval.h>

namespace TI4 {

TileInfoVector::TileInfoVector()
    : _tiles{{18, "Mecatol Rex", 1, 6, false, false, false},
             {35, "Bereg, Lirta IV", 5, 4, false, false, false},
             {38, "Abyz, Fria", 5, 0, false, false, false},
             {27, "New Albion, Starpoint", 4, 2, false, false, false},
             {36, "Arnor, Lor", 3, 3, false, false, false},
             {30, "Mellon, Zohbat", 3, 3, false, false, false},
             {33, "Corneeq, Resculon", 3, 2, false, false, false},
             {26, "Lodor", 3, 1, true, false, false},
             {31, "Lazar, Sakulag", 3, 1, false, false, false},
             {34, "Centauri, Gral", 2, 4, false, false, false},
             {28, "Tequ'ran, Torkan", 2, 3, false, false, false},
             {20, "Vefut II", 2, 2, false, false, false},
             {23, "Saudor", 2, 2, false, false, false},
             {25, "Quann", 2, 1, true, false, false},
             {37, "Arinam, Meer", 1, 6, false, false, false},
             {29, "Qucen'n, Rarron", 1, 5, false, false, false},
             {24, "Mehar Xull", 1, 3, false, false, false},
             {32, "Dal Bootha, Xxehan", 1, 3, false, false, false},
             {19, "Wellon", 1, 2, false, false, false},
             {22, "Tar'mann", 1, 1, false, false, false},
             {21, "Thibah", 1, 1, false, false, false},
             {39, "A Wormhole", 0, 0, true, false, false},
             {40, "B Wormhole", 0, 0, true, false, false},
             {44, "Asteroid Field", 0, 0, false, true, false},
             {45, "Asteroid Field", 0, 0, false, true, false},
             {43, "Supernova", 0, 0, false, true, false},
             {42, "Nebula", 0, 0, false, true, false},
             {41, "Gravity Rift", 0, 0, false, true, false},
             {46, "Blank", 0, 0, false, false, true},
             {47, "Blank", 0, 0, false, false, true},
             {48, "Blank", 0, 0, false, false, true},
             {49, "Blank", 0, 0, false, false, true},
             {50, "Blank", 0, 0, false, false, true}} {
}

std::size_t TileInfoVector::size() const {
  return _tiles.size();
}

const TileInfo &TileInfoVector::operator[](std::size_t idx) const {
  return _tiles[idx];
}

} // namespace TI4
