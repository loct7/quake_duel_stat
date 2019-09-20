from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from typing import Dict, List





@dataclass
class DamageStatusList:
    hits: int
    shots: int
    kills: int
    headshots: int
    damage: int

    def __init__(self, weapon_data):
        self.hits = weapon_data["hits"]
        self.shots = weapon_data["shots"]
        self.kills = weapon_data["kills"]
        self.headshots = weapon_data["headshots"]
        self.damage = weapon_data["damage"]


@dataclass
class DuelStat:
    won: int
    lost: int
    life_time: int
    time_played: int
    kills: int
    deaths: int
    mega_health_pickups: int
    heavy_armor_pickups: int
    healed: int
    small_armor_pickups: int
    ranked_won: int
    ranked_lost: int
    ranked_time_played: int

    def __init__(self, duel_stat_data):
        self.won = duel_stat_data["won"]
        self.lost = duel_stat_data["lost"]
        self.life_time = duel_stat_data["lifeTime"]
        self.time_played = duel_stat_data["timePlayed"]
        self.kills = duel_stat_data["kills"]
        self.deaths = duel_stat_data["deaths"]
        self.mega_health_pickups = duel_stat_data["megaHealthPickups"]
        self.heavy_armor_pickups = duel_stat_data["heavyArmorPickups"]
        self.healed = duel_stat_data["healed"]
        self.small_armor_pickups = duel_stat_data["smallArmorPickups"]
        self.ranked_won = duel_stat_data["rankedWon"]
        self.ranked_lost = duel_stat_data["rankedLost"]
        self.ranked_time_played = duel_stat_data["rankedTimePlayed"]

@dataclass
class Champion:
    duel_stat: DuelStat
    GAUNTLET_stat: DamageStatusList
    MACHINEGUN_stat: DamageStatusList
    MACHINEGUN_GRADE1_stat: DamageStatusList
    SHOTGUN_stat: DamageStatusList
    SHOTGUN_GRADE1_stat: DamageStatusList
    NAILGUN_stat: DamageStatusList
    NAILGUN_GRADE1_stat: DamageStatusList
    ROCKET_LAUNCHER_stat: DamageStatusList
    LIGHTNING_GUN_stat: DamageStatusList
    RAILGUN_stat: DamageStatusList
    LAGBOLT_stat: DamageStatusList

    def __init__(self, player_data):
        self.duel_stat = DuelStat(player_data["gameModes"]["GameModeDuel"])
        self.GAUNTLET_stat = DamageStatusList(player_data["damageStatusList"]["GAUNTLET"])
        self.MACHINEGUN_stat = DamageStatusList(player_data["damageStatusList"]["MACHINEGUN"])
        self.MACHINEGUN_GRADE1_stat = DamageStatusList(player_data["damageStatusList"]["MACHINEGUN_GRADE1"])
        self.SHOTGUN_stat = DamageStatusList(player_data["damageStatusList"]["SHOTGUN"])
        self.SHOTGUN_GRADE1_stat = DamageStatusList(player_data["damageStatusList"]["SHOTGUN_GRADE1"])
        self.NAILGUN_stat = DamageStatusList(player_data["damageStatusList"]["NAILGUN"])
        self.NAILGUN_GRADE1_stat = DamageStatusList(player_data["damageStatusList"]["NAILGUN_GRADE1"])
        self.ROCKET_LAUNCHER_stat = DamageStatusList(player_data["damageStatusList"]["ROCKET_LAUNCHER"])
        self.LIGHTNING_GUN_stat = DamageStatusList(player_data["damageStatusList"]["LIGHTNING_GUN"])
        self.RAILGUN_stat = DamageStatusList(player_data["damageStatusList"]["RAILGUN"])
        self.LAGBOLT_stat = DamageStatusList(player_data["damageStatusList"]["LAGBOLT"])


@dataclass
class PlayerStats:
    name: str
    player_level: int
    player_exp: int
    duel_rating: int
    duel_rating_games_count: int
    RANGER_stat: Champion
    SCALEBEARER_stat: Champion
    VISOR_stat: Champion
    ANARKI_stat: Champion
    NYX_stat: Champion
    SORLAG_stat: Champion
    CLUTCH_stat: Champion
    GALENA_stat: Champion
    SLASH_stat: Champion
    DOOM_SLAYER_stat: Champion
    BJ_BLAZKOWICZ_stat: Champion
    KEEL_stat: Champion
    STROGG_stat: Champion
    DEATH_KNIGHT_stat: Champion
    ATHENA_stat: Champion
    EISEN_stat: Champion

    def __init__(self, player_data):
        self.name = player_data["name"]
        self.player_level = player_data["playerLevelState"]["level"]
        self.player_exp = player_data["playerLevelState"]["exp"]
        self.duel_rating = player_data["playerRatings"]["duel"]["rating"]
        self.duel_rating_games_count = player_data["playerRatings"]["duel"]["gamesCount"]

        self.RANGER_stat = Champion(player_data["playerProfileStats"]["champions"]["RANGER"])
        self.SCALEBEARER_stat = Champion(player_data["playerProfileStats"]["champions"]["SCALEBEARER"])
        self.VISOR_stat = Champion(player_data["playerProfileStats"]["champions"]["VISOR"])
        self.ANARKI_stat = Champion(player_data["playerProfileStats"]["champions"]["ANARKI"])
        self.NYX_stat = Champion(player_data["playerProfileStats"]["champions"]["NYX"])
        self.SORLAG_stat = Champion(player_data["playerProfileStats"]["champions"]["SORLAG"])
        self.CLUTCH_stat = Champion(player_data["playerProfileStats"]["champions"]["CLUTCH"])
        self.GALENA_stat = Champion(player_data["playerProfileStats"]["champions"]["GALENA"])
        self.SLASH_stat = Champion(player_data["playerProfileStats"]["champions"]["SLASH"])
        self.DOOM_SLAYER_stat = Champion(player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"])
        self.BJ_BLAZKOWICZ_stat = Champion(player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"])
        self.KEEL_stat = Champion(player_data["playerProfileStats"]["champions"]["KEEL"])
        self.STROGG_stat = Champion(player_data["playerProfileStats"]["champions"]["STROGG"])
        self.DEATH_KNIGHT_stat = Champion(player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"])
        self.ATHENA_stat = Champion(player_data["playerProfileStats"]["champions"]["ATHENA"])
        self.EISEN_stat = Champion(player_data["playerProfileStats"]["champions"]["EISEN"])

'''
    def to_obj(self, player_data):
        #self = PlayerStats()
        #self.player_data = player_data
        self.name = player_data["name"]
        self.player_level= player_data["playerLevelState"]["level"]
        self.player_exp= player_data["playerLevelState"]["exp"]
        self.duel_rating = player_data["playerRatings"]["duel"]["rating"]
        self.duel_rating_games_count = player_data["playerRatings"]["duel"]["gamesCount"]


        self.RANGER_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["won"]
        self.RANGER_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["lost"]
        self.RANGER_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.RANGER_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.RANGER_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["kills"]
        self.RANGER_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["deaths"]
        self.RANGER_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.RANGER_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.RANGER_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["healed"]
        self.RANGER_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.RANGER_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.RANGER_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.RANGER_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["RANGER"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.RANGER_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.RANGER_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.RANGER_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.RANGER_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.RANGER_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.RANGER_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.RANGER_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.RANGER_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.RANGER_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.RANGER_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.RANGER_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.RANGER_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.RANGER_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.RANGER_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.RANGER_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.RANGER_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.RANGER_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.RANGER_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.RANGER_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.RANGER_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.RANGER_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.RANGER_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.RANGER_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.RANGER_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.RANGER_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.RANGER_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN"]["hits"]
        self.RANGER_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN"]["shots"]
        self.RANGER_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN"]["kills"]
        self.RANGER_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.RANGER_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN"]["damage"]

        self.RANGER_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.RANGER_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.RANGER_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.RANGER_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.RANGER_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.RANGER_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.RANGER_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.RANGER_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.RANGER_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.RANGER_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.RANGER_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.RANGER_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.RANGER_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.RANGER_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.RANGER_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.RANGER_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["RAILGUN"]["hits"]
        self.RANGER_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["RAILGUN"]["shots"]
        self.RANGER_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["RAILGUN"]["kills"]
        self.RANGER_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.RANGER_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["RAILGUN"]["damage"]

        self.RANGER_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.RANGER_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.RANGER_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.RANGER_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.RANGER_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["RANGER"]["damageStatusList"]["LAGBOLT"]["damage"]

    ################################################################################################################################################

        self.SCALEBEARER_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["won"]
        self.SCALEBEARER_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["lost"]
        self.SCALEBEARER_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.SCALEBEARER_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.SCALEBEARER_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["kills"]
        self.SCALEBEARER_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["deaths"]
        self.SCALEBEARER_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.SCALEBEARER_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.SCALEBEARER_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["healed"]
        self.SCALEBEARER_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.SCALEBEARER_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.SCALEBEARER_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.SCALEBEARER_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.SCALEBEARER_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.SCALEBEARER_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.SCALEBEARER_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.SCALEBEARER_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.SCALEBEARER_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.SCALEBEARER_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.SCALEBEARER_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.SCALEBEARER_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.SCALEBEARER_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.SCALEBEARER_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.SCALEBEARER_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.SCALEBEARER_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.SCALEBEARER_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.SCALEBEARER_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.SCALEBEARER_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.SCALEBEARER_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.SCALEBEARER_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.SCALEBEARER_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.SCALEBEARER_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.SCALEBEARER_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.SCALEBEARER_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.SCALEBEARER_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.SCALEBEARER_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.SCALEBEARER_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.SCALEBEARER_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.SCALEBEARER_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN"]["hits"]
        self.SCALEBEARER_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN"]["shots"]
        self.SCALEBEARER_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN"]["kills"]
        self.SCALEBEARER_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.SCALEBEARER_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN"]["damage"]

        self.SCALEBEARER_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.SCALEBEARER_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.SCALEBEARER_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.SCALEBEARER_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.SCALEBEARER_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.SCALEBEARER_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.SCALEBEARER_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.SCALEBEARER_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.SCALEBEARER_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.SCALEBEARER_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.SCALEBEARER_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.SCALEBEARER_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.SCALEBEARER_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.SCALEBEARER_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.SCALEBEARER_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.SCALEBEARER_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["RAILGUN"]["hits"]
        self.SCALEBEARER_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["RAILGUN"]["shots"]
        self.SCALEBEARER_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["RAILGUN"]["kills"]
        self.SCALEBEARER_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.SCALEBEARER_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["RAILGUN"]["damage"]

        self.SCALEBEARER_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.SCALEBEARER_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.SCALEBEARER_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.SCALEBEARER_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.SCALEBEARER_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["SCALEBEARER"]["damageStatusList"]["LAGBOLT"]["damage"]


        #######################################################################################################################################################

        self.VISOR_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["won"]
        self.VISOR_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["lost"]
        self.VISOR_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.VISOR_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.VISOR_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["kills"]
        self.VISOR_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["deaths"]
        self.VISOR_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.VISOR_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.VISOR_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["healed"]
        self.VISOR_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.VISOR_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.VISOR_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.VISOR_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["VISOR"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.VISOR_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.VISOR_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.VISOR_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.VISOR_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.VISOR_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.VISOR_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.VISOR_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.VISOR_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.VISOR_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.VISOR_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.VISOR_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.VISOR_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.VISOR_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.VISOR_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.VISOR_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.VISOR_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.VISOR_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.VISOR_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.VISOR_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.VISOR_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.VISOR_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.VISOR_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.VISOR_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.VISOR_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.VISOR_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.VISOR_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN"]["hits"]
        self.VISOR_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN"]["shots"]
        self.VISOR_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN"]["kills"]
        self.VISOR_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.VISOR_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN"]["damage"]

        self.VISOR_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.VISOR_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.VISOR_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.VISOR_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.VISOR_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.VISOR_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.VISOR_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.VISOR_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.VISOR_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.VISOR_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.VISOR_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.VISOR_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.VISOR_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.VISOR_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.VISOR_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.VISOR_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["RAILGUN"]["hits"]
        self.VISOR_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["RAILGUN"]["shots"]
        self.VISOR_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["RAILGUN"]["kills"]
        self.VISOR_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.VISOR_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["RAILGUN"]["damage"]

        self.VISOR_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.VISOR_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.VISOR_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.VISOR_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.VISOR_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["VISOR"]["damageStatusList"]["LAGBOLT"]["damage"]


        ##################################################################################################################################

        self.ANARKI_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["won"]
        self.ANARKI_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["lost"]
        self.ANARKI_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.ANARKI_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.ANARKI_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["kills"]
        self.ANARKI_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["deaths"]
        self.ANARKI_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.ANARKI_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.ANARKI_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["healed"]
        self.ANARKI_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.ANARKI_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.ANARKI_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.ANARKI_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["ANARKI"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.ANARKI_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.ANARKI_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.ANARKI_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.ANARKI_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.ANARKI_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.ANARKI_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.ANARKI_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.ANARKI_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.ANARKI_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.ANARKI_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.ANARKI_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.ANARKI_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.ANARKI_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.ANARKI_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.ANARKI_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.ANARKI_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.ANARKI_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.ANARKI_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.ANARKI_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.ANARKI_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.ANARKI_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.ANARKI_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.ANARKI_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.ANARKI_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.ANARKI_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.ANARKI_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN"]["hits"]
        self.ANARKI_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN"]["shots"]
        self.ANARKI_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN"]["kills"]
        self.ANARKI_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.ANARKI_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN"]["damage"]

        self.ANARKI_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.ANARKI_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.ANARKI_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.ANARKI_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.ANARKI_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.ANARKI_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.ANARKI_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.ANARKI_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.ANARKI_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.ANARKI_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.ANARKI_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.ANARKI_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.ANARKI_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.ANARKI_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.ANARKI_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.ANARKI_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["RAILGUN"]["hits"]
        self.ANARKI_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["RAILGUN"]["shots"]
        self.ANARKI_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["RAILGUN"]["kills"]
        self.ANARKI_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.ANARKI_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["RAILGUN"]["damage"]

        self.ANARKI_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.ANARKI_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.ANARKI_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.ANARKI_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.ANARKI_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["ANARKI"]["damageStatusList"]["LAGBOLT"]["damage"]


        ##############################################################################################################################


        self.NYX_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["won"]
        self.NYX_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["lost"]
        self.NYX_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.NYX_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.NYX_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["kills"]
        self.NYX_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["deaths"]
        self.NYX_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.NYX_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.NYX_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["healed"]
        self.NYX_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.NYX_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.NYX_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.NYX_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["NYX"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.NYX_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.NYX_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.NYX_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.NYX_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.NYX_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.NYX_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.NYX_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.NYX_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.NYX_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.NYX_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.NYX_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.NYX_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.NYX_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.NYX_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.NYX_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.NYX_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.NYX_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.NYX_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.NYX_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.NYX_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.NYX_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.NYX_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.NYX_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.NYX_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.NYX_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.NYX_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN"]["hits"]
        self.NYX_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN"]["shots"]
        self.NYX_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN"]["kills"]
        self.NYX_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.NYX_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN"]["damage"]

        self.NYX_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.NYX_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.NYX_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.NYX_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.NYX_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.NYX_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.NYX_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.NYX_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.NYX_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.NYX_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.NYX_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.NYX_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.NYX_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.NYX_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.NYX_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.NYX_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["RAILGUN"]["hits"]
        self.NYX_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["RAILGUN"]["shots"]
        self.NYX_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["RAILGUN"]["kills"]
        self.NYX_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.NYX_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["RAILGUN"]["damage"]

        self.NYX_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.NYX_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.NYX_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.NYX_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.NYX_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["NYX"]["damageStatusList"]["LAGBOLT"]["damage"]


        ############################################################################################################################

        self.SORLAG_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["won"]
        self.SORLAG_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["lost"]
        self.SORLAG_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.SORLAG_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.SORLAG_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["kills"]
        self.SORLAG_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["deaths"]
        self.SORLAG_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.SORLAG_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.SORLAG_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["healed"]
        self.SORLAG_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.SORLAG_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.SORLAG_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.SORLAG_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["SORLAG"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.SORLAG_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.SORLAG_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.SORLAG_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.SORLAG_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.SORLAG_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.SORLAG_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.SORLAG_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.SORLAG_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.SORLAG_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.SORLAG_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.SORLAG_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.SORLAG_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.SORLAG_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.SORLAG_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.SORLAG_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.SORLAG_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.SORLAG_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.SORLAG_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.SORLAG_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.SORLAG_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.SORLAG_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.SORLAG_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.SORLAG_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.SORLAG_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.SORLAG_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.SORLAG_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN"]["hits"]
        self.SORLAG_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN"]["shots"]
        self.SORLAG_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN"]["kills"]
        self.SORLAG_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.SORLAG_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN"]["damage"]

        self.SORLAG_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.SORLAG_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.SORLAG_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.SORLAG_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.SORLAG_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.SORLAG_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.SORLAG_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.SORLAG_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.SORLAG_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.SORLAG_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.SORLAG_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.SORLAG_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.SORLAG_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.SORLAG_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.SORLAG_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.SORLAG_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["RAILGUN"]["hits"]
        self.SORLAG_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["RAILGUN"]["shots"]
        self.SORLAG_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["RAILGUN"]["kills"]
        self.SORLAG_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.SORLAG_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["RAILGUN"]["damage"]

        self.SORLAG_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.SORLAG_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.SORLAG_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.SORLAG_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.SORLAG_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["SORLAG"]["damageStatusList"]["LAGBOLT"]["damage"]


        ###############################################################################################################################

        self.CLUTCH_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["won"]
        self.CLUTCH_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["lost"]
        self.CLUTCH_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.CLUTCH_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.CLUTCH_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["kills"]
        self.CLUTCH_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["deaths"]
        self.CLUTCH_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.CLUTCH_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.CLUTCH_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["healed"]
        self.CLUTCH_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.CLUTCH_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.CLUTCH_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.CLUTCH_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["CLUTCH"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.CLUTCH_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.CLUTCH_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.CLUTCH_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.CLUTCH_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.CLUTCH_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.CLUTCH_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.CLUTCH_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.CLUTCH_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.CLUTCH_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.CLUTCH_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.CLUTCH_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.CLUTCH_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.CLUTCH_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.CLUTCH_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.CLUTCH_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.CLUTCH_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.CLUTCH_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.CLUTCH_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.CLUTCH_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.CLUTCH_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.CLUTCH_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.CLUTCH_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.CLUTCH_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.CLUTCH_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.CLUTCH_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.CLUTCH_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN"]["hits"]
        self.CLUTCH_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN"]["shots"]
        self.CLUTCH_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN"]["kills"]
        self.CLUTCH_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.CLUTCH_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN"]["damage"]

        self.CLUTCH_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.CLUTCH_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.CLUTCH_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.CLUTCH_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.CLUTCH_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.CLUTCH_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.CLUTCH_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.CLUTCH_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.CLUTCH_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.CLUTCH_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.CLUTCH_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.CLUTCH_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.CLUTCH_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.CLUTCH_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.CLUTCH_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.CLUTCH_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["RAILGUN"]["hits"]
        self.CLUTCH_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["RAILGUN"]["shots"]
        self.CLUTCH_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["RAILGUN"]["kills"]
        self.CLUTCH_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.CLUTCH_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["RAILGUN"]["damage"]

        self.CLUTCH_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.CLUTCH_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.CLUTCH_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.CLUTCH_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.CLUTCH_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["CLUTCH"]["damageStatusList"]["LAGBOLT"]["damage"]


        #########################################################################################################################

        self.GALENA_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["won"]
        self.GALENA_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["lost"]
        self.GALENA_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.GALENA_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.GALENA_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["kills"]
        self.GALENA_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["deaths"]
        self.GALENA_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.GALENA_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.GALENA_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["healed"]
        self.GALENA_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.GALENA_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.GALENA_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.GALENA_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["GALENA"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.GALENA_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.GALENA_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.GALENA_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.GALENA_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.GALENA_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.GALENA_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.GALENA_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.GALENA_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.GALENA_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.GALENA_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.GALENA_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.GALENA_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.GALENA_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.GALENA_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.GALENA_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.GALENA_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.GALENA_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.GALENA_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.GALENA_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.GALENA_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.GALENA_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.GALENA_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.GALENA_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.GALENA_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.GALENA_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.GALENA_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN"]["hits"]
        self.GALENA_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN"]["shots"]
        self.GALENA_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN"]["kills"]
        self.GALENA_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.GALENA_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN"]["damage"]

        self.GALENA_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.GALENA_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.GALENA_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.GALENA_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.GALENA_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.GALENA_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.GALENA_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.GALENA_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.GALENA_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.GALENA_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.GALENA_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.GALENA_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.GALENA_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.GALENA_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.GALENA_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.GALENA_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["RAILGUN"]["hits"]
        self.GALENA_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["RAILGUN"]["shots"]
        self.GALENA_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["RAILGUN"]["kills"]
        self.GALENA_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.GALENA_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["RAILGUN"]["damage"]

        self.GALENA_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.GALENA_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.GALENA_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.GALENA_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.GALENA_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["GALENA"]["damageStatusList"]["LAGBOLT"]["damage"]

        #######################################################################################################################################

        self.SLASH_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["won"]
        self.SLASH_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["lost"]
        self.SLASH_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.SLASH_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.SLASH_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["kills"]
        self.SLASH_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["deaths"]
        self.SLASH_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.SLASH_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.SLASH_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["healed"]
        self.SLASH_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.SLASH_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.SLASH_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.SLASH_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["SLASH"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.SLASH_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.SLASH_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.SLASH_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.SLASH_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.SLASH_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.SLASH_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.SLASH_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.SLASH_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.SLASH_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.SLASH_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.SLASH_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.SLASH_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.SLASH_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.SLASH_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.SLASH_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.SLASH_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.SLASH_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.SLASH_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.SLASH_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.SLASH_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.SLASH_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.SLASH_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.SLASH_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.SLASH_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.SLASH_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.SLASH_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN"]["hits"]
        self.SLASH_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN"]["shots"]
        self.SLASH_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN"]["kills"]
        self.SLASH_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.SLASH_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN"]["damage"]

        self.SLASH_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.SLASH_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.SLASH_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.SLASH_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.SLASH_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.SLASH_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.SLASH_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.SLASH_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.SLASH_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.SLASH_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.SLASH_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.SLASH_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.SLASH_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.SLASH_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.SLASH_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.SLASH_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["RAILGUN"]["hits"]
        self.SLASH_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["RAILGUN"]["shots"]
        self.SLASH_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["RAILGUN"]["kills"]
        self.SLASH_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.SLASH_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["RAILGUN"]["damage"]

        self.SLASH_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.SLASH_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.SLASH_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.SLASH_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.SLASH_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["SLASH"]["damageStatusList"]["LAGBOLT"]["damage"]


        ########################################################################################################################################

        self.DOOM_SLAYER_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["won"]
        self.DOOM_SLAYER_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["lost"]
        self.DOOM_SLAYER_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.DOOM_SLAYER_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.DOOM_SLAYER_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["kills"]
        self.DOOM_SLAYER_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["deaths"]
        self.DOOM_SLAYER_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.DOOM_SLAYER_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.DOOM_SLAYER_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["healed"]
        self.DOOM_SLAYER_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.DOOM_SLAYER_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.DOOM_SLAYER_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.DOOM_SLAYER_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.DOOM_SLAYER_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.DOOM_SLAYER_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.DOOM_SLAYER_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.DOOM_SLAYER_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.DOOM_SLAYER_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.DOOM_SLAYER_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.DOOM_SLAYER_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.DOOM_SLAYER_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.DOOM_SLAYER_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.DOOM_SLAYER_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.DOOM_SLAYER_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.DOOM_SLAYER_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.DOOM_SLAYER_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.DOOM_SLAYER_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.DOOM_SLAYER_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.DOOM_SLAYER_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.DOOM_SLAYER_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.DOOM_SLAYER_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.DOOM_SLAYER_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.DOOM_SLAYER_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.DOOM_SLAYER_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.DOOM_SLAYER_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.DOOM_SLAYER_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.DOOM_SLAYER_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.DOOM_SLAYER_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.DOOM_SLAYER_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN"]["hits"]
        self.DOOM_SLAYER_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN"]["shots"]
        self.DOOM_SLAYER_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN"]["kills"]
        self.DOOM_SLAYER_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.DOOM_SLAYER_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN"]["damage"]

        self.DOOM_SLAYER_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.DOOM_SLAYER_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.DOOM_SLAYER_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.DOOM_SLAYER_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.DOOM_SLAYER_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.DOOM_SLAYER_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.DOOM_SLAYER_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.DOOM_SLAYER_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.DOOM_SLAYER_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.DOOM_SLAYER_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.DOOM_SLAYER_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.DOOM_SLAYER_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.DOOM_SLAYER_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.DOOM_SLAYER_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.DOOM_SLAYER_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.DOOM_SLAYER_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["RAILGUN"]["hits"]
        self.DOOM_SLAYER_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["RAILGUN"]["shots"]
        self.DOOM_SLAYER_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["RAILGUN"]["kills"]
        self.DOOM_SLAYER_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.DOOM_SLAYER_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["RAILGUN"]["damage"]

        self.DOOM_SLAYER_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.DOOM_SLAYER_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.DOOM_SLAYER_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.DOOM_SLAYER_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.DOOM_SLAYER_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["DOOM_SLAYER"]["damageStatusList"]["LAGBOLT"]["damage"]



        ##############################################################################################################################################

        self.BJ_BLAZKOWICZ_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["won"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["lost"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["kills"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["deaths"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["healed"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.BJ_BLAZKOWICZ_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.BJ_BLAZKOWICZ_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.BJ_BLAZKOWICZ_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.BJ_BLAZKOWICZ_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.BJ_BLAZKOWICZ_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.BJ_BLAZKOWICZ_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.BJ_BLAZKOWICZ_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.BJ_BLAZKOWICZ_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN"]["hits"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN"]["shots"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN"]["kills"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN"]["damage"]

        self.BJ_BLAZKOWICZ_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.BJ_BLAZKOWICZ_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.BJ_BLAZKOWICZ_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.BJ_BLAZKOWICZ_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.BJ_BLAZKOWICZ_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.BJ_BLAZKOWICZ_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.BJ_BLAZKOWICZ_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.BJ_BLAZKOWICZ_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.BJ_BLAZKOWICZ_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.BJ_BLAZKOWICZ_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["RAILGUN"]["hits"]
        self.BJ_BLAZKOWICZ_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["RAILGUN"]["shots"]
        self.BJ_BLAZKOWICZ_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["RAILGUN"]["kills"]
        self.BJ_BLAZKOWICZ_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["RAILGUN"]["damage"]

        self.BJ_BLAZKOWICZ_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.BJ_BLAZKOWICZ_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.BJ_BLAZKOWICZ_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.BJ_BLAZKOWICZ_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.BJ_BLAZKOWICZ_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["BJ_BLAZKOWICZ"]["damageStatusList"]["LAGBOLT"]["damage"]


        #######################################################################################################################################

        self.KEEL_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["won"]
        self.KEEL_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["lost"]
        self.KEEL_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.KEEL_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.KEEL_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["kills"]
        self.KEEL_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["deaths"]
        self.KEEL_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.KEEL_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.KEEL_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["healed"]
        self.KEEL_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.KEEL_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.KEEL_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.KEEL_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["KEEL"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.KEEL_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.KEEL_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.KEEL_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.KEEL_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.KEEL_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.KEEL_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.KEEL_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.KEEL_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.KEEL_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.KEEL_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.KEEL_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.KEEL_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.KEEL_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.KEEL_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.KEEL_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.KEEL_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.KEEL_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.KEEL_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.KEEL_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.KEEL_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.KEEL_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.KEEL_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.KEEL_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.KEEL_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.KEEL_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.KEEL_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN"]["hits"]
        self.KEEL_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN"]["shots"]
        self.KEEL_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN"]["kills"]
        self.KEEL_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.KEEL_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN"]["damage"]

        self.KEEL_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.KEEL_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.KEEL_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.KEEL_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.KEEL_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.KEEL_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.KEEL_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.KEEL_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.KEEL_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.KEEL_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.KEEL_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.KEEL_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.KEEL_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.KEEL_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.KEEL_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.KEEL_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["RAILGUN"]["hits"]
        self.KEEL_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["RAILGUN"]["shots"]
        self.KEEL_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["RAILGUN"]["kills"]
        self.KEEL_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.KEEL_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["RAILGUN"]["damage"]

        self.KEEL_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.KEEL_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.KEEL_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.KEEL_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.KEEL_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["KEEL"]["damageStatusList"]["LAGBOLT"]["damage"]

        ##############################################################################################################################

        self.STROGG_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["won"]
        self.STROGG_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["lost"]
        self.STROGG_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.STROGG_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.STROGG_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["kills"]
        self.STROGG_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["deaths"]
        self.STROGG_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.STROGG_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.STROGG_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["healed"]
        self.STROGG_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.STROGG_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.STROGG_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.STROGG_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["STROGG"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.STROGG_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.STROGG_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.STROGG_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.STROGG_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.STROGG_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.STROGG_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.STROGG_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.STROGG_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.STROGG_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.STROGG_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.STROGG_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.STROGG_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.STROGG_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.STROGG_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.STROGG_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.STROGG_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.STROGG_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.STROGG_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.STROGG_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.STROGG_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.STROGG_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.STROGG_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.STROGG_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.STROGG_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.STROGG_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.STROGG_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN"]["hits"]
        self.STROGG_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN"]["shots"]
        self.STROGG_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN"]["kills"]
        self.STROGG_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.STROGG_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN"]["damage"]

        self.STROGG_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.STROGG_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.STROGG_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.STROGG_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.STROGG_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.STROGG_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.STROGG_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.STROGG_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.STROGG_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.STROGG_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.STROGG_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.STROGG_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.STROGG_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.STROGG_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.STROGG_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.STROGG_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["RAILGUN"]["hits"]
        self.STROGG_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["RAILGUN"]["shots"]
        self.STROGG_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["RAILGUN"]["kills"]
        self.STROGG_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.STROGG_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["RAILGUN"]["damage"]

        self.STROGG_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.STROGG_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.STROGG_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.STROGG_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.STROGG_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["STROGG"]["damageStatusList"]["LAGBOLT"]["damage"]

        ################################################################################################################################

        self.DEATH_KNIGHT_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["won"]
        self.DEATH_KNIGHT_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["lost"]
        self.DEATH_KNIGHT_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.DEATH_KNIGHT_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.DEATH_KNIGHT_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["kills"]
        self.DEATH_KNIGHT_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["deaths"]
        self.DEATH_KNIGHT_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.DEATH_KNIGHT_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.DEATH_KNIGHT_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["healed"]
        self.DEATH_KNIGHT_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.DEATH_KNIGHT_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.DEATH_KNIGHT_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.DEATH_KNIGHT_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.DEATH_KNIGHT_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.DEATH_KNIGHT_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.DEATH_KNIGHT_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.DEATH_KNIGHT_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.DEATH_KNIGHT_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.DEATH_KNIGHT_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.DEATH_KNIGHT_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.DEATH_KNIGHT_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.DEATH_KNIGHT_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.DEATH_KNIGHT_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.DEATH_KNIGHT_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.DEATH_KNIGHT_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.DEATH_KNIGHT_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.DEATH_KNIGHT_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.DEATH_KNIGHT_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.DEATH_KNIGHT_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.DEATH_KNIGHT_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.DEATH_KNIGHT_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.DEATH_KNIGHT_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN"]["hits"]
        self.DEATH_KNIGHT_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN"]["shots"]
        self.DEATH_KNIGHT_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN"]["kills"]
        self.DEATH_KNIGHT_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.DEATH_KNIGHT_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN"]["damage"]

        self.DEATH_KNIGHT_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.DEATH_KNIGHT_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.DEATH_KNIGHT_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.DEATH_KNIGHT_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.DEATH_KNIGHT_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.DEATH_KNIGHT_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.DEATH_KNIGHT_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.DEATH_KNIGHT_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.DEATH_KNIGHT_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.DEATH_KNIGHT_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.DEATH_KNIGHT_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.DEATH_KNIGHT_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.DEATH_KNIGHT_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.DEATH_KNIGHT_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.DEATH_KNIGHT_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.DEATH_KNIGHT_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["RAILGUN"]["hits"]
        self.DEATH_KNIGHT_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["RAILGUN"]["shots"]
        self.DEATH_KNIGHT_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["RAILGUN"]["kills"]
        self.DEATH_KNIGHT_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.DEATH_KNIGHT_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["RAILGUN"]["damage"]

        self.DEATH_KNIGHT_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.DEATH_KNIGHT_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.DEATH_KNIGHT_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.DEATH_KNIGHT_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.DEATH_KNIGHT_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["DEATH_KNIGHT"]["damageStatusList"]["LAGBOLT"]["damage"]


        ######################################################################################################################################################

        self.ATHENA_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["won"]
        self.ATHENA_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["lost"]
        self.ATHENA_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.ATHENA_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.ATHENA_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["kills"]
        self.ATHENA_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["deaths"]
        self.ATHENA_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.ATHENA_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.ATHENA_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["healed"]
        self.ATHENA_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.ATHENA_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.ATHENA_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.ATHENA_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["ATHENA"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.ATHENA_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.ATHENA_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.ATHENA_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.ATHENA_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.ATHENA_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.ATHENA_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.ATHENA_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.ATHENA_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.ATHENA_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.ATHENA_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.ATHENA_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.ATHENA_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.ATHENA_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.ATHENA_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.ATHENA_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.ATHENA_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.ATHENA_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.ATHENA_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.ATHENA_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.ATHENA_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.ATHENA_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.ATHENA_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.ATHENA_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.ATHENA_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.ATHENA_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.ATHENA_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN"]["hits"]
        self.ATHENA_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN"]["shots"]
        self.ATHENA_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN"]["kills"]
        self.ATHENA_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.ATHENA_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN"]["damage"]

        self.ATHENA_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.ATHENA_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.ATHENA_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.ATHENA_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.ATHENA_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.ATHENA_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.ATHENA_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.ATHENA_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.ATHENA_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.ATHENA_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.ATHENA_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.ATHENA_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.ATHENA_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.ATHENA_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.ATHENA_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.ATHENA_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["RAILGUN"]["hits"]
        self.ATHENA_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["RAILGUN"]["shots"]
        self.ATHENA_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["RAILGUN"]["kills"]
        self.ATHENA_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.ATHENA_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["RAILGUN"]["damage"]

        self.ATHENA_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.ATHENA_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.ATHENA_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.ATHENA_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.ATHENA_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["ATHENA"]["damageStatusList"]["LAGBOLT"]["damage"]



        ########################################################################################################################################
        self.EISEN_stat.duel_stat.won = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["won"]
        self.EISEN_stat.duel_stat.lost = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["lost"]
        self.EISEN_stat.duel_stat.life_time = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["lifeTime"]
        self.EISEN_stat.duel_stat.time_played = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["timePlayed"]
        self.EISEN_stat.duel_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["kills"]
        self.EISEN_stat.duel_stat.deaths = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["deaths"]
        self.EISEN_stat.duel_stat.mega_health_pickups = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["megaHealthPickups"]
        self.EISEN_stat.duel_stat.heavy_armor_pickups = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["heavyArmorPickups"]
        self.EISEN_stat.duel_stat.healed = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["healed"]
        self.EISEN_stat.duel_stat.small_armor_pickups = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["smallArmorPickups"]
        self.EISEN_stat.duel_stat.ranked_won = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["rankedWon"]
        self.EISEN_stat.duel_stat.ranked_lost = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["rankedLost"]
        self.EISEN_stat.duel_stat.ranked_time_played = player_data["playerProfileStats"]["champions"]["EISEN"]["gameModes"]["GameModeDuel"]["rankedTimePlayed"]

        self.EISEN_stat.GAUNTLET_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["GAUNTLET"]["hits"]
        self.EISEN_stat.GAUNTLET_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["GAUNTLET"]["shots"]
        self.EISEN_stat.GAUNTLET_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["GAUNTLET"]["kills"]
        self.EISEN_stat.GAUNTLET_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["GAUNTLET"]["headshots"]
        self.EISEN_stat.GAUNTLET_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["GAUNTLET"]["damage"]

        self.EISEN_stat.MACHINEGUN_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN"]["hits"]
        self.EISEN_stat.MACHINEGUN_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN"]["shots"]
        self.EISEN_stat.MACHINEGUN_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN"]["kills"]
        self.EISEN_stat.MACHINEGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN"]["headshots"]
        self.EISEN_stat.MACHINEGUN_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN"]["damage"]

        self.EISEN_stat.MACHINEGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN_GRADE1"]["hits"]
        self.EISEN_stat.MACHINEGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN_GRADE1"]["shots"]
        self.EISEN_stat.MACHINEGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN_GRADE1"]["kills"]
        self.EISEN_stat.MACHINEGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN_GRADE1"]["headshots"]
        self.EISEN_stat.MACHINEGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["MACHINEGUN_GRADE1"]["damage"]

        self.EISEN_stat.SHOTGUN_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN"]["hits"]
        self.EISEN_stat.SHOTGUN_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN"]["shots"]
        self.EISEN_stat.SHOTGUN_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN"]["kills"]
        self.EISEN_stat.SHOTGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN"]["headshots"]
        self.EISEN_stat.SHOTGUN_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN"]["damage"]

        self.EISEN_stat.SHOTGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN_GRADE1"]["hits"]
        self.EISEN_stat.SHOTGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN_GRADE1"]["shots"]
        self.EISEN_stat.SHOTGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN_GRADE1"]["kills"]
        self.EISEN_stat.SHOTGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN_GRADE1"]["headshots"]
        self.EISEN_stat.SHOTGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["SHOTGUN_GRADE1"]["damage"]

        self.EISEN_stat.NAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN"]["hits"]
        self.EISEN_stat.NAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN"]["shots"]
        self.EISEN_stat.NAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN"]["kills"]
        self.EISEN_stat.NAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN"]["headshots"]
        self.EISEN_stat.NAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN"]["damage"]

        self.EISEN_stat.NAILGUN_GRADE1_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN_GRADE1"]["hits"]
        self.EISEN_stat.NAILGUN_GRADE1_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN_GRADE1"]["shots"]
        self.EISEN_stat.NAILGUN_GRADE1_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN_GRADE1"]["kills"]
        self.EISEN_stat.NAILGUN_GRADE1_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN_GRADE1"]["headshots"]
        self.EISEN_stat.NAILGUN_GRADE1_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["NAILGUN_GRADE1"]["damage"]

        self.EISEN_stat.ROCKET_LAUNCHER_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["ROCKET_LAUNCHER"]["hits"]
        self.EISEN_stat.ROCKET_LAUNCHER_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["ROCKET_LAUNCHER"]["shots"]
        self.EISEN_stat.ROCKET_LAUNCHER_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["ROCKET_LAUNCHER"]["kills"]
        self.EISEN_stat.ROCKET_LAUNCHER_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["ROCKET_LAUNCHER"]["headshots"]
        self.EISEN_stat.ROCKET_LAUNCHER_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["ROCKET_LAUNCHER"]["damage"]

        self.EISEN_stat.LIGHTNING_GUN_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LIGHTNING_GUN"]["hits"]
        self.EISEN_stat.LIGHTNING_GUN_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LIGHTNING_GUN"]["shots"]
        self.EISEN_stat.LIGHTNING_GUN_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LIGHTNING_GUN"]["kills"]
        self.EISEN_stat.LIGHTNING_GUN_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LIGHTNING_GUN"]["headshots"]
        self.EISEN_stat.LIGHTNING_GUN_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LIGHTNING_GUN"]["damage"]

        self.EISEN_stat.RAILGUN_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["RAILGUN"]["hits"]
        self.EISEN_stat.RAILGUN_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["RAILGUN"]["shots"]
        self.EISEN_stat.RAILGUN_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["RAILGUN"]["kills"]
        self.EISEN_stat.RAILGUN_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["RAILGUN"]["headshots"]
        self.EISEN_stat.RAILGUN_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["RAILGUN"]["damage"]

        self.EISEN_stat.LAGBOLT_stat.hits = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LAGBOLT"]["hits"]
        self.EISEN_stat.LAGBOLT_stat.shots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LAGBOLT"]["shots"]
        self.EISEN_stat.LAGBOLT_stat.kills = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LAGBOLT"]["kills"]
        self.EISEN_stat.LAGBOLT_stat.headshots = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LAGBOLT"]["headshots"]
        self.EISEN_stat.LAGBOLT_stat.damage = player_data["playerProfileStats"]["champions"]["EISEN"]["damageStatusList"]["LAGBOLT"]["damage"]

        return self
'''