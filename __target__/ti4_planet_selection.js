// Transcrypt'ed from Python, 2019-03-01 16:35:38
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var num_iterations = 100;
export var tiles = [tuple (['Mecatol Rex', 1, 6, false, false, false]), tuple (['Bereg, Lirta IV', 5, 4, false, false, false]), tuple (['Abyz, Fria', 5, 0, false, false, false]), tuple (['New Albion, Starpoint', 4, 2, false, false, false]), tuple (['Arnor, Lor', 3, 3, false, false, false]), tuple (['Mellon, Zohbat', 3, 3, false, false, false]), tuple (['Corneeq, Resculon', 3, 2, false, false, false]), tuple (['Lodor', 3, 1, true, false, false]), tuple (['Lazar, Sakulag', 3, 1, false, false, false]), tuple (['Centauri, Gral', 2, 4, false, false, false]), tuple (["Tequ'ran, Torkan", 2, 3, false, false, false]), tuple (['Vefut II', 2, 2, false, false, false]), tuple (['Saudor', 2, 2, false, false, false]), tuple (['Quann', 2, 1, true, false, false]), tuple (['Arinam, Meer', 1, 6, false, false, false]), tuple (["Qucen'n, Rarron", 1, 5, false, false, false]), tuple (['Mehar Xull', 1, 3, false, false, false]), tuple (['Dal Bootha, Xxehan', 1, 3, false, false, false]), tuple (['Wellon', 1, 2, false, false, false]), tuple (["Tar'mann", 1, 1, false, false, false]), tuple (['Thibah', 1, 1, false, false, false]), tuple (['A Wormhole', 0, 0, true, false, false]), tuple (['B Wormhole', 0, 0, true, false, false]), tuple (['Asteroid Field', 0, 0, false, true, false]), tuple (['Asteroid Field', 0, 0, false, true, false]), tuple (['Supernova', 0, 0, false, true, false]), tuple (['Nebula', 0, 0, false, true, false]), tuple (['Gravity Rift', 0, 0, false, true, false]), tuple (['Blank', 0, 0, false, false, true]), tuple (['Blank', 0, 0, false, false, true]), tuple (['Blank', 0, 0, false, false, true]), tuple (['Blank', 0, 0, false, false, true]), tuple (['Blank', 0, 0, false, false, true])];
export var names = (function () {
	var __accu0__ = [];
	for (var tile of tiles) {
		__accu0__.append (tile [0]);
	}
	return __accu0__;
}) ();
export var resource = (function () {
	var __accu0__ = [];
	for (var tile of tiles) {
		__accu0__.append (tile [1]);
	}
	return __accu0__;
}) ();
export var influence = (function () {
	var __accu0__ = [];
	for (var tile of tiles) {
		__accu0__.append (tile [2]);
	}
	return __accu0__;
}) ();
export var wormhole = (function () {
	var __accu0__ = [];
	for (var ii = 0; ii < len (tiles); ii++) {
		if (tiles [ii] [3]) {
			__accu0__.append (ii);
		}
	}
	return __accu0__;
}) ();
export var anomaly = (function () {
	var __accu0__ = [];
	for (var ii = 0; ii < len (tiles); ii++) {
		if (tiles [ii] [4]) {
			__accu0__.append (ii);
		}
	}
	return __accu0__;
}) ();
export var blank = (function () {
	var __accu0__ = [];
	for (var ii = 0; ii < len (tiles); ii++) {
		if (tiles [ii] [5]) {
			__accu0__.append (ii);
		}
	}
	return __accu0__;
}) ();
export var lowest = (function () {
	var __accu0__ = [];
	for (var ii = 0; ii < len (tiles); ii++) {
		if (tiles [ii] [1] == 1 && tiles [ii] [2] == 1) {
			__accu0__.append (ii);
		}
	}
	return __accu0__;
}) ();
export var Results =  __class__ ('Results', [object], {
	__module__: __name__,
	player_resource: null,
	player_influence: null,
	player_planets: null,
	num_tiles: 0,
	shared_planets: null,
	used: null,
	get __init__ () {return __get__ (this, function (self, num_players) {
		self.player_resource = null;
		self.player_influence = null;
		self.player_planets = null;
		self.shared_planets = [];
		self.used = (function () {
			var __accu0__ = [];
			for (var ii = 0; ii < len (tiles); ii++) {
				__accu0__.append (0);
			}
			return __accu0__;
		}) ();
		self._allocate_planet (0, -(1));
		self._configure (num_players);
	});},
	get _allocate_planet () {return __get__ (this, function (self, planet_num, player_num) {
		if (self.used [planet_num] == 1) {
			var __except0__ = RuntimeError ('Attempt to allocate already used tile: {}'.format (planet_num));
			__except0__.__cause__ = null;
			throw __except0__;
		}
		self.used [planet_num] = 1;
		if (player_num >= 0) {
			if (len (self.player_planets [player_num]) >= self.num_tiles) {
				var __except0__ = RuntimeError ('Too many tiles allocated to player: {}'.format (player_num));
				__except0__.__cause__ = null;
				throw __except0__;
			}
			self.player_planets [player_num].append (planet_num);
			self.player_resource [player_num] = self.player_resource [player_num] - resource [planet_num];
			self.player_influence [player_num] = self.player_influence [player_num] - influence [planet_num];
		}
		else {
			self.shared_planets.append (planet_num);
		}
	});},
	get allocate () {return __get__ (this, function (self, num_players) {
		for (var player = 0; player < num_players; player++) {
			if (!(self._fill_player (player, self._get_unused_vector (), self.player_resource [player], self.player_influence [player], self.num_tiles - len (self.player_planets [player]), []))) {
				return false;
			}
		}
		return true;
	});},
	get check_all_used () {return __get__ (this, function (self) {
		for (var uu of self.used) {
			if (!(uu)) {
				var __except0__ = RuntimeError ('Unused tiles');
				__except0__.__cause__ = null;
				throw __except0__;
			}
		}
	});},
	get _get_unused_vector () {return __get__ (this, function (self) {
		var unused_tiles = [];
		var unused_tiles = (function () {
			var __accu0__ = [];
			for (var ii = 0; ii < len (self.used); ii++) {
				if (self.used [ii] == 0) {
					__accu0__.append (ii);
				}
			}
			return __accu0__;
		}) ();
		random.shuffle (unused_tiles);
		return unused_tiles;
	});},
	get _fill_player () {return __get__ (this, function (self, player_num, unused_tiles, resources_required, influence_required, num_planets, player_planets) {
		if (num_planets < 0) {
			return false;
		}
		if (num_planets == 0 && resources_required == 0 && influence_required == 0) {
			for (var planet of player_planets) {
				self._allocate_planet (planet, player_num);
			}
			return true;
		}
		var new_unused_tiles = (function () {
			var __accu0__ = [];
			for (var tile of unused_tiles) {
				if (resources_required >= resource [tile] && influence_required >= influence [tile]) {
					__accu0__.append (tile);
				}
			}
			return __accu0__;
		}) ();
		while (true) {
			if (len (new_unused_tiles) == 0) {
				return false;
			}
			var candidate_tile = new_unused_tiles [0];
			var new_unused_tiles = new_unused_tiles.__getslice__ (1, null, 1);
			var new_player_planets = list (player_planets);
			new_player_planets.append (candidate_tile);
			if (self._fill_player (player_num, new_unused_tiles, resources_required - resource [candidate_tile], influence_required - influence [candidate_tile], num_planets - 1, new_player_planets)) {
				return true;
			}
		}
	});},
	get _configure () {return __get__ (this, function (self, num_players) {
		if (num_players == 4) {
			self._configure_4_players ();
		}
		else if (num_players == 5) {
			self._configure_5_players ();
		}
		else if (num_players == 6) {
			self._configure_6_players ();
		}
		else {
			var __except0__ = RuntimeError ('Invalid number of players: {}'.format (num_players));
			__except0__.__cause__ = null;
			throw __except0__;
		}
	});},
	get _configure_rip () {return __get__ (this, function (self, res_infls) {
		random.shuffle (res_infls);
		self.player_resource = (function () {
			var __accu0__ = [];
			for (var res_infl of res_infls) {
				__accu0__.append (res_infl [0]);
			}
			return __accu0__;
		}) ();
		self.player_influence = (function () {
			var __accu0__ = [];
			for (var res_infl of res_infls) {
				__accu0__.append (res_infl [1]);
			}
			return __accu0__;
		}) ();
		self.player_planets = (function () {
			var __accu0__ = [];
			for (var res_infl of res_infls) {
				__accu0__.append ([]);
			}
			return __accu0__;
		}) ();
	});},
	get _configure_w () {return __get__ (this, function (self) {
		for (var ii = 0; ii < 4; ii++) {
			self._allocate_planet (wormhole [ii], ii);
		}
	});},
	get _configure_ab () {return __get__ (this, function (self, abs) {
		var num_total = (function () {
			var __accu0__ = [];
			for (var ab of abs) {
				__accu0__.append (ab [0]);
			}
			return __accu0__;
		}) ();
		var num_anoms = (function () {
			var __accu0__ = [];
			for (var ab of abs) {
				__accu0__.append (ab [1]);
			}
			return __accu0__;
		}) ();
		var num_blank = (function () {
			var __accu0__ = [];
			for (var ab of abs) {
				__accu0__.append (ab [2]);
			}
			return __accu0__;
		}) ();
		var reds = list (anomaly);
		random.shuffle (reds);
		for (var ii = 0; ii < len (num_anoms); ii++) {
			for (var jj = 0; jj < num_anoms [ii]; jj++) {
				self._allocate_planet (reds [0], ii);
				var reds = reds.__getslice__ (1, null, 1);
				num_total [ii] = num_total [ii] - 1;
			}
		}
		var blanks = list (blank);
		for (var ii = 0; ii < len (abs); ii++) {
			for (var jj = 0; jj < num_blank [ii]; jj++) {
				self._allocate_planet (blanks [0], ii);
				var blanks = blanks.__getslice__ (1, null, 1);
				num_total [ii] = num_total [ii] - 1;
			}
		}
		var remain = list (reds);
		remain.append (blanks);
		random.shuffle (remain);
		for (var ii = 0; ii < len (num_total); ii++) {
			for (var jj = 0; jj < num_total [ii]; jj++) {
				self._allocate_planet (remain [0], ii);
				var remain = remain.__getslice__ (1, null, 1);
			}
		}
		for (var rem of remain) {
			self._allocate_planet (rem, -(1));
		}
	});},
	get _configure_4_players () {return __get__ (this, function (self) {
		self.num_tiles = 8;
		var res_infls = [tuple ([11, 13]), tuple ([11, 12]), tuple ([12, 12]), tuple ([12, 12])];
		self._configure_rip (res_infls);
		self._configure_w ();
		var abs = [tuple ([3, 1, 1]), tuple ([3, 1, 1]), tuple ([2, 1, 1]), tuple ([2, 1, 1])];
		random.shuffle (abs);
		self._configure_ab (abs);
	});},
	get _configure_5_players () {return __get__ (this, function (self) {
		self.num_tiles = 6;
		self._allocate_planet (lowest [random.randint (0, 1)], -(1));
		var res_infls = [tuple ([9, 10]), tuple ([9, 10]), tuple ([9, 10]), tuple ([9, 9]), tuple ([9, 9])];
		self._configure_rip (res_infls);
		self._configure_w ();
		var abs = [tuple ([2, 1, 1]), tuple ([2, 1, 1]), tuple ([2, 1, 1]), tuple ([1, 1, 0]), tuple ([1, 1, 0])];
		random.shuffle (abs);
		abs [4] = tuple ([abs [4] [0] + 1, abs [4] [1], abs [4] [2] + 1]);
		self._configure_ab (abs);
	});},
	get _configure_6_players () {return __get__ (this, function (self) {
		self.num_tiles = 5;
		var res_infls = [tuple ([8, 8]), tuple ([8, 8]), tuple ([8, 8]), tuple ([8, 8]), tuple ([7, 8]), tuple ([7, 9])];
		self._configure_rip (res_infls);
		self._configure_w ();
		var abs = [tuple ([1, 1, 0]), tuple ([1, 1, 0]), tuple ([1, 1, 0]), tuple ([1, 0, 1]), tuple ([1, 0, 1]), tuple ([1, 0, 1])];
		random.shuffle (abs);
		abs [4] = tuple ([abs [4] [0] + 1, abs [4] [1] + 1, abs [4] [2]]);
		abs [5] = tuple ([abs [5] [0] + 1, abs [5] [1] + 1, abs [5] [2]]);
		self._configure_ab (abs);
	});}
});
export var print_planets = function (py_name, planets) {
	var output = '<h2>{0}</h2>'.format (py_name);
	var total_resource = 0;
	var total_influence = 0;
	var num_planets = len (planets);
	for (var ii of planets) {
		var worm = ' ';
		var anom = ' ';
		var blnk = ' ';
		if (__in__ (ii, wormhole)) {
			var worm = 'W';
		}
		if (__in__ (ii, anomaly)) {
			var anom = 'A';
		}
		if (__in__ (ii, blank)) {
			var blnk = 'B';
		}
		var total_resource = total_resource + resource [ii];
		var total_influence = total_influence + influence [ii];
		var output = output + '<p>Name: {}; Resource: {}; Influence: {}; {}{}{}</p>'.format (names [ii], resource [ii], influence [ii], worm, anom, blnk);
	}
	var output = output + '<p/><i>Number of systems {}, total resource: {}, total influence {}</i></p>'.format (num_planets, total_resource, total_influence);
	return output;
};
export var ti4_planet_selection = function (num_players) {
	var results = null;
	var success = false;
	for (var num_attempts = 0; num_attempts < num_iterations; num_attempts++) {
		var results = Results (num_players);
		if (results.allocate (num_players)) {
			var success = true;
			break;
		}
	}
	if (!(success)) {
		var __except0__ = RuntimeError ('Unable to converge in {} iterations');
		__except0__.__cause__ = null;
		throw __except0__;
	}
	results.check_all_used ();
	var output = print_planets ('Shared planets:', results.shared_planets);
	for (var nn = 0; nn < num_players; nn++) {
		var output = output + print_planets ('Player {}'.format (nn + 1), results.player_planets [nn]);
	}
	return output;
};

//# sourceMappingURL=ti4_planet_selection.map