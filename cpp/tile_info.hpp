#pragma once

#include <string>

namespace TI4 {

class TileInfo {
public:
  TileInfo();
  TileInfo(const std::string &name_, int resource_, int influence_,
           bool is_wormhole_, bool is_anomaly_, bool is_blank_);
  TileInfo(const TileInfo &) = default;
  TileInfo(TileInfo &&) = default;
  TileInfo &operator=(const TileInfo &) = default;
  TileInfo &operator=(TileInfo &&) = default;

  const std::string &name() const;
  int resource() const;
  int influence() const;
  bool is_wormhole() const;
  bool is_anomaly() const;
  bool is_blank() const;

  std::string print() const;

private:
  std::string _name;
  int _resource;
  int _influence;
  bool _is_wormhole;
  bool _is_anomaly;
  bool _is_blank;
};

} // namespace TI4
