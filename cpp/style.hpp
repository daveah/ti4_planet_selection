#pragma once

#include <boost/program_options.hpp>
#include <string>

namespace TI4 {

class style {
public:
  enum class style_store { DEFAULT, ORIGINAL, WARP };

  style();
  style(const std::string &style_);
  style(const style &) = default;
  style(style &&) = default;
  style &operator=(const style &) = default;
  style &operator=(style &&) = default;

  style::style_store value() const;
  bool is_default() const;
  bool is_original() const;
  bool is_warp() const;

  std::string str() const;

  static std::string str(style_store style_);
  static const char *help();

  friend std::istream &operator>>(std::istream &in, style &st) {
    std::string style_string;
    auto &retval = in >> style_string;
    st = style(style_string);
    return retval;
  }

private:
  style_store _style;
};

} // namespace TI4
