#include "config.hpp"

namespace TI4 {

Config::Config(int num_players_, std::string style_)
    : _num_players(num_players_), _style(style_) {
}

Config::Config() : _num_players(6), _style("default") {
}

int Config::num_players() const {
  return _num_players;
}
std::string Config::style() const {
  return _style;
}

} // namespace TI4
