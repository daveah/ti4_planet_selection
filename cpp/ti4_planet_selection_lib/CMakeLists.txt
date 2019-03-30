file(GLOB ALL_SOURCES CONFIGURE_DEPENDS "*.cpp")
add_library(ti4_planet_selection_lib ${ALL_SOURCES})
target_link_libraries(ti4_planet_selection_lib
  Boost::boost)
target_include_directories(ti4_planet_selection_lib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}>)
