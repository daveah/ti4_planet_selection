#pragma once

#include <functional>
#include <string>

class Config {
public:
  Config(int num_players_, std::string style_);
  Config();
  Config(const Config &) = default;
  Config(Config &&) = default;
  Config &operator=(const Config &) = default;
  Config &operator=(Config &&) = default;

  int num_players() const;
  std::string style() const;

  friend bool operator==(const Config &lhs, const Config &rhs) {
    return (lhs.num_players() == rhs.num_players() &&
            lhs.style() == rhs.style());
  }
  friend bool operator!=(const Config &lhs, const Config &rhs) {
    return !operator==(lhs, rhs);
  }

private:
  int _num_players;
  std::string _style;
};

namespace std {
template <>
struct hash<Config> {
  using argument_type = Config;
  using result_type = std::size_t;
  std::size_t operator()(const Config &config_) const noexcept {
    auto h1 = std::hash<int>()(config_.num_players());
    auto h2 = std::hash<std::string>()(config_.style());
    return h1 ^ (h2 << 1);
  }
};
} // namespace std