# -*- coding: utf-8 -*-

import enum
from types import DynamicClassAttribute

__all__ = ["Species"]

_special_names = None
_special_names_rev = None

def special_names():
	global _special_names

	if _special_names is None:
		_special_names = {
			"Nidoran♀": Species.Nidoran_f,
			"Nidoran♂": Species.Nidoran_m,
			"Farfetch'd": Species.Farfetchd,
			"Mr. Mime": Species.Mr_Mime
		}
	return _special_names

def special_names_rev():
	global _special_names_rev
	if _special_names_rev is None:
		_special_names_rev = {v: k for k, v in special_names().items()}
	return _special_names_rev

class SpeciesMeta(type(enum.Enum)):
	
	def __getitem__(cls, name):
		try:
			return special_names()[name]
		except KeyError:
			return super().__getitem__(name)

class Species(enum.Enum, metaclass=SpeciesMeta):
	MissingNo_00, \
	Rhydon, \
	Kangaskhan, \
	Nidoran_m, \
	Clefairy, \
	Spearow, \
	Voltorb, \
	Nidoking, \
	Slowbro, \
	Ivysaur, \
	Exeggutor, \
	Lickitung, \
	Exeggcute, \
	Grimer, \
	Gengar, \
	Nidoran_f, \
	Nidoqueen, \
	Cubone, \
	Rhyhorn, \
	Lapras, \
	Arcanine, \
	Mew, \
	Gyarados, \
	Shellder, \
	Tentacool, \
	Gastly, \
	Scyther, \
	Staryu, \
	Blastoise, \
	Pinsir, \
	Tangela, \
	MissingNo_1F, \
	MissingNo_20, \
	Growlithe, \
	Onix, \
	Fearow, \
	Pidgey, \
	Slowpoke, \
	Kadabra, \
	Graveler, \
	Chansey, \
	Machoke, \
	Mr_Mime, \
	Hitmonlee, \
	Hitmonchan, \
	Arbok, \
	Parasect, \
	Psyduck, \
	Drowzee, \
	Golem, \
	MissingNo_32, \
	Magmar, \
	MissingNo_34, \
	Electabuzz, \
	Magneton, \
	Koffing, \
	MissingNo_38, \
	Mankey, \
	Seel, \
	Diglett, \
	Tauros, \
	MissingNo_3D, \
	MissingNo_3E, \
	MissingNo_3F, \
	Farfetchd, \
	Venonat, \
	Dragonite, \
	MissingNo_43, \
	MissingNo_44, \
	MissingNo_45, \
	Doduo, \
	Poliwag, \
	Jynx, \
	Moltres, \
	Articuno, \
	Zapdos, \
	Ditto, \
	Meowth, \
	Krabby, \
	MissingNo_4F, \
	MissingNo_50, \
	MissingNo_51, \
	Vulpix, \
	Ninetales, \
	Pikachu, \
	Raichu, \
	MissingNo_56, \
	MissingNo_57, \
	Dratini, \
	Dragonair, \
	Kabuto, \
	Kabutops, \
	Horsea, \
	Seadra, \
	MissingNo_5E, \
	MissingNo_5F, \
	Sandshrew, \
	Sandslash, \
	Omanyte, \
	Omastar, \
	Jigglypuff, \
	Wigglytuff, \
	Eevee, \
	Flareon, \
	Jolteon, \
	Vaporeon, \
	Machop, \
	Zubat, \
	Ekans, \
	Paras, \
	Poliwhirl, \
	Poliwrath, \
	Weedle, \
	Kakuna, \
	Beedrill, \
	MissingNo_73, \
	Dodrio, \
	Primeape, \
	Dugtrio, \
	Venomoth, \
	Dewgong, \
	MissingNo_79, \
	MissingNo_7A, \
	Caterpie, \
	Metapod, \
	Butterfree, \
	Machamp, \
	MissingNo_7F, \
	Golduck, \
	Hypno, \
	Golbat, \
	Mewtwo, \
	Snorlax, \
	Magikarp, \
	MissingNo_86, \
	MissingNo_87, \
	Muk, \
	MissingNo_89, \
	Kingler, \
	Cloyster, \
	MissingNo_8C, \
	Electrode, \
	Clefable, \
	Weezing, \
	Persian, \
	Marowak, \
	MissingNo_92, \
	Haunter, \
	Abra, \
	Alakazam, \
	Pidgeotto, \
	Pidgeot, \
	Starmie, \
	Bulbasaur, \
	Venusaur, \
	Tentacruel, \
	MissingNo_9C, \
	Goldeen, \
	Seaking, \
	MissingNo_9F, \
	MissingNo_A0, \
	MissingNo_A1, \
	MissingNo_A2, \
	Ponyta, \
	Rapidash, \
	Rattata, \
	Raticate, \
	Nidorino, \
	Nidorina, \
	Geodude, \
	Porygon, \
	Aerodactyl, \
	MissingNo_AC, \
	Magnemite, \
	MissingNo_AE, \
	MissingNo_AF, \
	Charmander, \
	Squirtle, \
	Charmeleon, \
	Wartortle, \
	Charizard, \
	MissingNo_B5, \
	MissingNo_B6, \
	MissingNo_B7, \
	MissingNo_B8, \
	Oddish, \
	Gloom, \
	Vileplume, \
	Bellsprout, \
	Weepinbell, \
	Victreebel = range(191)

	@DynamicClassAttribute
	def name(self):
		try:
			return special_names_rev()[self]
		except KeyError:
			return super().name
