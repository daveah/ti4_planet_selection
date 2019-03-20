#pragma once

#include <boost/program_options.hpp>
#include <cstdlib>
#include <string>

class num_players {
public:
  num_players();
  num_players(const std::string &num_players_);
  num_players(const num_players &) = default;
  num_players(num_players &&) = default;
  num_players &operator=(const num_players &) = default;
  num_players &operator=(num_players &&) = default;

  int value() const;
  std::string str() const;

  static const char *help();

  friend std::istream &operator>>(std::istream &in, num_players &np) {
    std::string num_players_string;
    auto &retval = in >> num_players_string;
    np = num_players(num_players_string);
    return retval;
  }

private:
  int _num_players;
};
