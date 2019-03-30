#pragma once

#include "tile_info.hpp"
#include <cstddef>
#include <vector>

namespace TI4 {

class TileInfoVector {
public:
  TileInfoVector();
  TileInfoVector(const TileInfoVector &) = delete;
  TileInfoVector(TileInfoVector &&) = delete;
  TileInfoVector &operator=(const TileInfoVector &) = delete;
  TileInfoVector &operator=(TileInfoVector &) = delete;

  std::size_t size() const;
  const TileInfo &operator[](std::size_t idx) const;

private:
  std::vector<TileInfo> _tiles;
};

} // namespace TI4
