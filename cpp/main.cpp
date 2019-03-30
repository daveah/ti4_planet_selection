#include "deck_generator.hpp"
#include "internal_error.hpp"
#include "num_players.hpp"
#include "style.hpp"
#include "validation_error.hpp"
#include <boost/program_options.hpp>
#include <iostream>

int main(int argc, char **argv) {
  namespace po = boost::program_options;
  TI4::num_players np_default, np;
  TI4::style st_default, st;
  po::options_description desc("Options");
  desc.add_options()("help,h", "Print help messages") // Help command
      ("style,s", po::value<TI4::style>(&st_default),
       TI4::style::help()) // Set the style
      ("num_players", po::value<TI4::num_players>(&np_default)->required(),
       TI4::num_players::help()) // Set the number of players
      ;
  po::positional_options_description positionalOptions;
  positionalOptions.add("num_players", 1);
  po::variables_map vm;
  try {
    po::store(po::command_line_parser(argc, argv)
                  .options(desc)
                  .positional(positionalOptions)
                  .run(),
              vm);
    if (vm.count("help")) {
      std::cout << "ti4_planet_selection <num_players> [--style <style>]"
                << std::endl;
      std::cout << "  Create balanced decks for a game of TI4." << desc
                << std::endl;
      return 1;
    }
    if (vm.count("num_players")) {
      np = vm["num_players"].as<TI4::num_players>();
    } else {
      throw po::validation_error(po::validation_error::invalid_option_value);
    }
    if (vm.count("style")) {
      st = vm["style"].as<TI4::style>();
      if (st.is_warp() && np.value() != 5) {
        throw po::validation_error(po::validation_error::invalid_option_value);
      }
    }
  } catch (TI4::ValidationError &ee) {
    std::cerr << "ERROR: " << ee.what() << std::endl;
    return -1;
  } catch (po::required_option &ee) {
    std::cerr << "ERROR: " << ee.what() << std::endl;
    return -1;
  } catch (po::too_many_positional_options_error &ee) {
    std::cerr << "ERROR: " << ee.what() << std::endl;
    return -1;
  } catch (po::validation_error &ee) {
    std::cerr << "ERROR: " << ee.what() << std::endl;
    return -1;
  }
  try {
    TI4::DeckGenerator dg(np, st);
  } catch (TI4::ValidationError &ee) {
    std::cout << ee.what() << std::endl;
  } catch (TI4::InternalError &ee) {
    std::cout << "Serious failure: " << ee.what() << std::endl;
  }
  return 0;
}
