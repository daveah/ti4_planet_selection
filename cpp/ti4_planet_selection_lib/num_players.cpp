#include "num_players.hpp"
#include "validation_error.hpp"
#include <boost/lexical_cast.hpp>

namespace TI4 {

num_players::num_players() : _num_players(6) {
}

num_players::num_players(int num_players_) : _num_players(num_players_) {
  if (num_players_ < _min_players || num_players_ > _max_players) {
    throw ValidationError("Invalid number of players, ")
        << _min_players << "-" << _max_players
        << " allowed, you requested: " << num_players_;
  }
}

num_players::num_players(const std::string &num_players_)
    : num_players(std::atoi(num_players_.c_str())) {
}

int num_players::value() const {
  return _num_players;
}

std::string num_players::str() const {
  return boost::lexical_cast<std::string>(_num_players);
}

const char *num_players::help() {
  return "Number of players {3, 4, 5, 6}";
}

} // namespace TI4
