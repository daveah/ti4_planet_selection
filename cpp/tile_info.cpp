#include "tile_info.hpp"
#include <iomanip>
#include <sstream>

namespace TI4 {

TileInfo::TileInfo()
    : _name("error"), _resource(0), _influence(0), _is_wormhole(false),
      _is_anomaly(false), _is_blank(false) {
}

TileInfo::TileInfo(const std::string &name_, int resource_, int influence_,
                   bool is_wormhole_, bool is_anomaly_, bool is_blank_)
    : _name(name_), _resource(resource_), _influence(influence_),
      _is_wormhole(is_wormhole_), _is_anomaly(is_anomaly_),
      _is_blank(is_blank_) {
}

const std::string &TileInfo::name() const {
  return _name;
}

int TileInfo::resource() const {
  return _resource;
}

int TileInfo::influence() const {
  return _influence;
}

bool TileInfo::is_wormhole() const {
  return _is_wormhole;
}

bool TileInfo::is_anomaly() const {
  return _is_anomaly;
}

bool TileInfo::is_blank() const {
  return _is_blank;
}

std::string TileInfo::print() const {
  std::ostringstream str;
  str << "Name: " << std::left << std::setw(22) << name() << "; ";
  str << "Resource: " << resource() << "; ";
  str << "Influence: " << influence() << "; ";
  str << (is_wormhole() ? "W" : " ");
  str << (is_anomaly() ? "A" : " ");
  str << (is_blank() ? "B" : " ");
  return str.str();
}

} // namespace TI4
