#include "deck_generator.hpp"
#include "config.hpp"
#include "tile_info.hpp"
#include "tile_info_vector.hpp"
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <random>
#include <unordered_map>
#include <vector>

std::random_device rd;
std::mt19937 mt(rd());

namespace TI4 {

using Data = DeckGenerator::Data;
using UData = DeckGenerator::UData;
using ConfigSet = DeckGenerator::ConfigSet;
using AllocationSet = std::unordered_map<Config, ConfigSet>;

const TileInfoVector tiles;

const std::size_t num_tiles = tiles.size();
const auto is_wormhole = [](const TileInfo &tile_) {
  return tile_.is_wormhole();
};
const auto is_anomaly = [](const TileInfo &tile_) {
  return tile_.is_anomaly();
};
const auto is_blank = [](const TileInfo &tile_) { return tile_.is_blank(); };
const auto extract_indices =
    [](const std::function<bool(const TileInfo &)> &predicate_) {
      UData indices = {};
      for (std::size_t ii = 0, iiend = tiles.size(); ii < iiend; ++ii) {
        if (predicate_(tiles[ii])) {
          indices.push_back(ii);
        }
      }
      return indices;
    };
const UData wormholes = extract_indices(is_wormhole);
const UData anomalies = extract_indices(is_anomaly);
const UData blanks = extract_indices(is_blank);

const AllocationSet
    allocations =     // Allocations of resources for each configuration
    {{{3, "default"}, // 3 Players, default
      {
          {"num_players", {3}},
          {"num_tiles", {8}},
          {"resource_allocations", {13, 13, 13}},
          {"influence_allocations", {14, 14, 14}},
          {"specials_shuffled_total", {2, 2, 2}},
          {"specials_shuffled_anomalies", {1, 1, 1}},
          {"specials_shuffled_blanks", {1, 1, 1}},
      }},
     {{3, "original"}, // 3 Players, original
      {
          {"num_players", {3}},
          {"num_tiles", {8}},
          {"resource_allocations", {14, 14, 14}},
          {"influence_allocations", {15, 15, 15}},
          {"specials_shuffled_total", {0, 0, 0}},
          {"specials_shuffled_anomalies", {0, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0}},
          {"specials_fixed_total", {1, 2, 1}},
          {"specials_fixed_anomalies", {0, 0, 0}},
          {"specials_fixed_blanks", {0, 0, 0}},
      }},
     {{4, "default"}, // 4 Player, default
      {
          {"num_players", {4}},
          {"num_tiles", {8}},
          {"resource_allocations", {11, 11, 12, 12}},
          {"influence_allocations", {13, 12, 12, 12}},
          {"specials_shuffled_total", {3, 3, 2, 2}},
          {"specials_shuffled_anomalies", {1, 1, 1, 1}},
          {"specials_shuffled_blanks", {1, 1, 1, 1}},
      }},
     {{4, "original"}, // 4 Player, original
      {
          {"num_players", {4}},
          {"num_tiles", {8}},
          {"resource_allocations", {11, 11, 12, 12}},
          {"influence_allocations", {13, 12, 12, 12}},
          {"specials_shuffled_total", {0, 0, 0, 0}},
          {"specials_shuffled_anomalies", {0, 0, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0, 0}},
          {"specials_fixed_total", {3, 3, 2, 2}},
          {"specials_fixed_anomalies", {0, 0, 0, 0}},
          {"specials_fixed_blanks", {0, 0, 0, 0}},
      }},
     {{5, "default"}, // 5 Player, default
      {
          {"num_players", {5}},
          {"num_tiles", {6}},
          {"resource_allocations", {9, 9, 9, 9, 9}},
          {"influence_allocations", {10, 10, 10, 9, 9}},
          {"specials_shuffled_total", {2, 2, 2, 1, 1}},
          {"specials_shuffled_anomalies", {1, 1, 1, 1, 1}},
          {"specials_shuffled_blanks", {1, 1, 1, 0, 0}},
          {"specials_fixed_total", {0, 0, 0, 0, 1}},
          {"specials_fixed_anomalies", {0, 0, 0, 0, 0}},
          {"specials_fixed_blanks", {0, 0, 0, 0, 1}},
      }},
     {{5, "original"}, // 5 Player, original
      {
          {"num_players", {5}},
          {"num_tiles", {6}},
          {"resource_allocations", {10, 9, 9, 9, 9}},
          {"influence_allocations", {9, 10, 10, 10, 10}},
          {"specials_shuffled_total", {0, 0, 0, 0, 0}},
          {"specials_shuffled_anomalies", {0, 0, 0, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0, 0, 0}},
          {"specials_fixed_total", {2, 2, 1, 1, 2}},
          {"specials_fixed_anomalies", {0, 0, 0, 0, 0}},
          {"specials_fixed_blanks", {0, 0, 0, 0, 0}},
      }},
     {{5, "warp"}, // 5 Players, warp
      {
          {"num_players", {5}},
          {"num_tiles", {5}},
          {"resource_allocations", {8, 8, 8, 8, 8}},
          {"influence_allocations", {9, 9, 9, 9, 9}},
          {"specials_shuffled_total", {1, 1, 1, 1, 1}},
          {"specials_shuffled_anomalies", {1, 1, 1, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0, 1, 1}},
          {"specials_fixed_total", {0, 0, 0, 0, 1}},
          {"specials_fixed_anomalies", {0, 0, 0, 0, 1}},
          {"specials_fixed_blanks", {0, 0, 0, 0, 0}},
      }},
     {{6, "default"}, // 6 Player, default
      {
          {"num_players", {6}},
          {"num_tiles", {5}},
          {"resource_allocations", {8, 8, 8, 8, 7, 7}},
          {"influence_allocations", {8, 8, 8, 8, 8, 9}},
          {"specials_shuffled_total", {1, 1, 1, 1, 1, 1}},
          {"specials_shuffled_anomalies", {1, 1, 1, 0, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0, 1, 1, 1}},
          {"specials_fixed_total", {0, 0, 0, 0, 1, 1}},
          {"specials_fixed_anomalies", {0, 0, 0, 0, 1, 1}},
          {"specials_fixed_blanks", {0, 0, 0, 0, 0, 0}},
      }},
     {{6, "original"}, // 6 Player, original
      {
          {"num_players", {6}},
          {"num_tiles", {5}},
          {"resource_allocations", {8, 8, 7, 7, 7, 7}},
          {"influence_allocations", {7, 8, 8, 8, 8, 8}},
          {"specials_shuffled_total", {0, 0, 0, 0, 0, 0}},
          {"specials_shuffled_anomalies", {0, 0, 0, 0, 0, 0}},
          {"specials_shuffled_blanks", {0, 0, 0, 0, 0, 0}},
          {"specials_fixed_total", {2, 2, 1, 1, 2, 2}},
          {"specials_fixed_anomalies", {0, 0, 0, 0, 0, 0}},
          {"specials_fixed_blanks", {0, 0, 0, 0, 0, 0}},
      }}};

const auto config_finder =
    [](const num_players &num_players_, const style &style_) -> const auto & {
  Config config(num_players_.value(), style_.str());
  if (auto found = allocations.find(config); found == allocations.end()) {
    throw std::string("Invalid Configuration");
  } else {
    return found->second;
  }
};

DeckGenerator::DeckGenerator(const num_players &num_players_,
                             const style &style_)
    : _config(config_finder(num_players_, style_)), _num_players(0),
      _num_tiles(0) {
  bool success = false;
  for (std::size_t ii = 0; ii < _num_iterations; ++ii) {
    reset();
    if (allocate()) {
      success = true;
      break;
    }
  }
  if (!success) {
    throw std::string("Unable to converge");
  }
  sweep_to_shared();
  print_planets();
}

void DeckGenerator::reset() {
  // Num_players and num_tiles are const to prevent accidental
  // changes, but must be configured during a reset - hence const_cast
  const_cast<std::size_t &>(_num_players) = _config["num_players"].front();
  const_cast<std::size_t &>(_num_tiles) = _config["num_tiles"].front();
  // Reset working vectors
  _player_resource = {};
  _player_influence = {};
  _player_planets = UDataVector(_num_players, UData());
  _shared_planets = {};
  _used = Data(num_tiles, 0);
  // Allocate Mecatol Rex to shared
  allocate_planet_shared(0);
  // Shuffle resource and influence
  {
    auto players = UData(_num_players);
    std::iota(players.begin(), players.end(), 0);
    std::shuffle(players.begin(), players.end(), mt);
    _player_resource = _player_influence = Data();
    _player_resource.reserve(_num_players);
    _player_influence.reserve(_num_players);
    const auto &resources = _config["resource_allocations"];
    const auto &influence = _config["influence_allocations"];
    for (auto player : players) {
      _player_resource.push_back(resources[player]);
      _player_influence.push_back(influence[player]);
    }
  }
  // Wormholes
  {
    std::size_t pn = 0;
    for (auto wormhole : wormholes) {
      allocate_planet(wormhole, pn);
      pn += 1;
      pn %= _num_players;
    }
  }
  // Anomalies and blanks
  {
    auto players = UData(_num_players);
    std::iota(players.begin(), players.end(), 0);
    std::shuffle(players.begin(), players.end(), mt);
    auto total = Data(_num_players, 0);
    auto anoms = Data(_num_players, 0);
    auto blnks = Data(_num_players, 0);
    for (std::size_t player = 0; player < _num_players; ++player) {
      total[player] += _config["specials_shuffled_total"][players[player]];
      anoms[player] += _config["specials_shuffled_anomalies"][players[player]];
      blnks[player] += _config["specials_shuffled_blanks"][players[player]];
      if (_config.find("specials_fixed_total") != _config.end()) {
        total[player] += _config["specials_fixed_total"][player];
        anoms[player] += _config["specials_fixed_anomalies"][player];
        blnks[player] += _config["specials_fixed_blanks"][player];
      }
    }
    allocate_ab(total, anoms, blnks);
  }
}

void DeckGenerator::allocate_ab(Data total_, const Data &anoms_,
                                const Data &blanks_) {
  auto reds = anomalies;
  std::shuffle(reds.begin(), reds.end(), mt);
  std::size_t red = 0, blnk = 0, tot = 0;
  // Anomalies
  {
    std::size_t player = 0;
    for (auto anom : anoms_) {
      for (std::size_t idx = 0; idx < static_cast<std::size_t>(anom); ++idx) {
        allocate_planet(reds[red++], player);
        --total_[player];
      }
      ++player;
    }
  }
  // Blanks
  {
    std::size_t player = 0;
    for (auto blank : blanks_) {
      for (std::size_t idx = 0; idx < static_cast<std::size_t>(blank); ++idx) {
        allocate_planet(blanks[blnk++], player);
        --total_[player];
      }
      ++player;
    }
  }
  // Remaining
  Data remain(reds.begin() + red, reds.end());
  remain.insert(remain.end(), blanks.begin() + blnk, blanks.end());
  std::shuffle(remain.begin(), remain.end(), mt);
  {
    std::size_t player = 0;
    for (auto total : total_) {
      for (std::size_t idx = 0; idx < static_cast<std::size_t>(total); ++idx) {
        allocate_planet(remain[tot++], player);
      }
      ++player;
    }
  }
  for (std::size_t idx = tot, idxend = remain.size(); idx < idxend; ++idx) {
    allocate_planet_shared(remain[tot++]);
  }
}

using FillPlayerRet = std::tuple<bool, UData>;
const std::function<FillPlayerRet(std::size_t, const UData &, int, int,
                                  std::size_t, const UData &)>
    fill_player = [](std::size_t player, const UData &unused, int resource,
                     int influence, std::size_t num_tiles,
                     const UData &player_planets) -> FillPlayerRet {
  // Terminate on fail if num_tiles is below zero
  if (num_tiles < 0) {
    return FillPlayerRet(false, {});
  }
  // Terminate on success if we have successfully allocated everything
  if (num_tiles == 0 && resource == 0 && influence == 0) {
    return FillPlayerRet(true, player_planets);
  }
  // Remove tiles that cannot be allocated
  UData new_unused;
  for (auto &tile : unused) {
    if (resource >= tiles[tile].resource() &&
        influence >= tiles[tile].influence()) {
      new_unused.push_back(tile);
    }
  }
  while (true) {
    // Terminate on fail if we've run out of valid tiles
    if (new_unused.empty()) {
      return FillPlayerRet(false, {});
    }
    // Select first tile and allocate
    std::size_t candidate_tile = new_unused.back();
    new_unused.pop_back();
    UData new_player_planets(player_planets);
    new_player_planets.push_back(candidate_tile);
    // Recurse, on false remove first tile
    if (auto found = fill_player(player, new_unused,
                                 resource - tiles[candidate_tile].resource(),
                                 influence - tiles[candidate_tile].influence(),
                                 num_tiles - 1, new_player_planets);
        std::get<0>(found)) {
      return FillPlayerRet(true, std::get<1>(found));
    }
  }
};

bool DeckGenerator::allocate() {
  UData empty_data;
  for (std::size_t player = 0; player < _num_players; ++player) {
    UData unused;
    for (std::size_t idx = 0, idxend = _used.size(); idx < idxend; ++idx) {
      if (_used[idx] == 0) {
        unused.push_back(idx);
      }
    }
    std::shuffle(unused.begin(), unused.end(), mt);
    if (auto found = fill_player(
            player, unused, _player_resource[player], _player_influence[player],
            _num_tiles - _player_planets[player].size(), empty_data);
        !std::get<0>(found)) {
      return false;
    } else {
      for (auto player_planet : std::get<1>(found)) {
        allocate_planet(player_planet, player);
      }
    }
  }
  return true;
}

void DeckGenerator::sweep_to_shared() {
  for (std::size_t idx = 0, idxend = _used.size(); idx < idxend; ++idx) {
    if (_used[idx] == 0) {
      allocate_planet_shared(idx);
    }
  }
}

const auto print_stack = [](const UData &planets) {
  int total_res = 0, total_inf = 0;
  for (auto planet : planets) {
    std::cout << "  " << tiles[planet].print() << std::endl;
    total_res += tiles[planet].resource();
    total_inf += tiles[planet].influence();
  }
  std::cout << "  Number of systems: " << planets.size()
            << ", total resource: " << total_res
            << ", total influence: " << total_inf << std::endl;
};

void DeckGenerator::print_planets() const {
  std::cout << "Shared planets:" << std::endl;
  print_stack(_shared_planets);
  for (std::size_t player = 0; player < _num_players; ++player) {
    std::cout << "Player " << player + 1 << std::endl;
    print_stack(_player_planets[player]);
  }
}

const auto allocate_planet_helper = [](std::size_t planet_num_, Data &used_,
                                       UData &planet_vector_) {
  if (used_[planet_num_] == 1) {
    throw std::string("Attempt to allocate already used tile");
  }
  used_[planet_num_] = 1;
  planet_vector_.push_back(planet_num_);
};

void DeckGenerator::allocate_planet(std::size_t planet_num_,
                                    std::size_t player_num_) {
  if (_player_planets[player_num_].size() > _num_tiles) {
    throw std::string("Too many tiles allocated to player");
  }
  allocate_planet_helper(planet_num_, _used, _player_planets[player_num_]);
  const auto &tile = tiles[planet_num_];
  _player_resource[player_num_] -= tile.resource();
  _player_influence[player_num_] -= tile.influence();
}

void DeckGenerator::allocate_planet_shared(std::size_t planet_num_) {
  allocate_planet_helper(planet_num_, _used, _shared_planets);
}

} // namespace TI4
