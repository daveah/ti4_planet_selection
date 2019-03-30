#pragma once

#include <boost/lexical_cast.hpp>
#include <exception>
#include <string>

namespace TI4 {

class InternalError : public std::exception {
public:
  InternalError() : _what("Error") {
  }
  InternalError(const std::string &what_) : _what(what_) {
  }
  InternalError(const InternalError &) = default;
  InternalError(InternalError &&) = default;
  InternalError &operator=(const InternalError &) = default;
  InternalError &operator=(InternalError &&) = default;

  virtual const char *what() const noexcept override {
    return _what.c_str();
  }

  const InternalError &append(const std::string &ee_) const {
    _what += ee_;
    return *this;
  }

private:
  mutable std::string _what;
};

} // namespace TI4

template <typename TT>
const TI4::InternalError &operator<<(const TI4::InternalError &ee_,
                                     const TT &tt_) {
  return ee_.append(boost::lexical_cast<std::string>(tt_));
}