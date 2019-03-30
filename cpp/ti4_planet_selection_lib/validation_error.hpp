#pragma once

#include <boost/lexical_cast.hpp>
#include <exception>
#include <string>

namespace TI4 {

class ValidationError : public std::exception {
public:
  ValidationError() {
  }
  ValidationError(const std::string &what_) : _what(what_) {
  }
  ValidationError(const ValidationError &) = default;
  ValidationError(ValidationError &&) = default;
  ValidationError &operator=(const ValidationError &) = default;
  ValidationError &operator=(ValidationError &&) = default;

  virtual const char *what() const noexcept override {
    return _what.c_str();
  }

  const ValidationError &append(const std::string &ee_) const {
    _what += ee_;
    return *this;
  }

private:
  mutable std::string _what;
};

} // namespace TI4

template <typename TT>
const TI4::ValidationError &operator<<(const TI4::ValidationError &ee_,
                                       const TT &tt_) {
  return ee_.append(boost::lexical_cast<std::string>(tt_));
}
