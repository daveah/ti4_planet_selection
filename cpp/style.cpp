#include <style.hpp>

style::style() : _style(style_store::DEFAULT) {
}

style::style(const std::string &style_) {
  if (style_ == "default") {
    _style = style_store::DEFAULT;
  } else if (style_ == "original") {
    _style = style_store::ORIGINAL;
  } else if (style_ == "warp") {
    _style = style_store::WARP;
  } else {
    namespace po = boost::program_options;
    throw po::validation_error(po::validation_error::invalid_option_value);
  }
}

style::style_store style::value() const {
  return _style;
}

bool style::is_default() const {
  return _style == style_store::DEFAULT;
}

bool style::is_original() const {
  return _style == style_store::ORIGINAL;
}

bool style::is_warp() const {
  return _style == style_store::WARP;
}

std::string style::str() const {
  return str(_style);
}

std::string style::str(style_store style_) {
  switch (style_) {
  case style_store::DEFAULT:
    return "default";
  case style_store::ORIGINAL:
    return "original";
  case style_store::WARP:
    return "warp";
  default:
    throw 0;
  }
}

const char *style::help() {
  return "Galaxy Style {default, original, warp}";
}
