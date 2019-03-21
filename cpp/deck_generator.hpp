#pragma once

#include "num_players.hpp"
#include "style.hpp"
#include <cstddef>
#include <string>
#include <unordered_map>
#include <vector>

namespace TI4 {

class DeckGenerator {
public:
  DeckGenerator(const num_players &num_players_, const style &style_);
  DeckGenerator(const DeckGenerator &) = delete;
  DeckGenerator(DeckGenerator &&) = delete;
  DeckGenerator &operator=(const DeckGenerator &) = delete;
  DeckGenerator &operator=(DeckGenerator &&) = delete;

  using Data = std::vector<int>;
  using ConfigSet = std::unordered_map<std::string, Data>;
  using UData = std::vector<std::size_t>;
  using UDataVector = std::vector<UData>;

private:
  // Reset data structures followed a failed convergence
  void reset();
  // Allocate anomalies and blanks to players using heuristic
  void allocate_ab(Data total_, const Data &anoms_, const Data &blanks_);
  // Allocate planet tiles to players using backtracking algorithm
  bool allocate();
  // Sweep any left-over tiles into the shared pool
  void sweep_to_shared();
  // Print all tile stacks
  void print_planets() const;

  // Allocate a single tile to a given player
  void allocate_planet(std::size_t planet_num_, std::size_t player_num_);
  // Allocate a single tile to the shared pool
  void allocate_planet_shared(std::size_t planet_num_);

  // Configure the maximum number of iterations before failing
  const static std::size_t _num_iterations = 100;

  // Configuration
  ConfigSet _config;

  // Number of players
  const std::size_t _num_players;
  // Number of tiles to allocate to each player
  const std::size_t _num_tiles;
  // Vector of resource allocations per player
  // Reduced as tiles are allocated
  Data _player_resource;
  // Vector of influence allocations per player
  // Reduced as tiles are allocated
  Data _player_influence;
  // Vector of vectors of tile numbers, one per player
  UDataVector _player_planets;
  // Vector of tile numbers allocated to shared
  UData _shared_planets;
  // Vector denoting whether a tile has been used - 0 = no, 1 = yes
  Data _used;
};

} // namespace TI4
