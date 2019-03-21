#include "num_players.hpp"
#include <boost/lexical_cast.hpp>

namespace TI4 {

num_players::num_players() : _num_players(6) {
}

num_players::num_players(const std::string &num_players_) {
  if (num_players_ == "3" || num_players_ == "4" || num_players_ == "5" ||
      num_players_ == "6") {
    _num_players = std::atoi(num_players_.c_str());
  } else {
    namespace po = boost::program_options;
    throw po::validation_error(po::validation_error::invalid_option_value);
  }
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
